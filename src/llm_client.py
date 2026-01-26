import json
import time
import os
from datetime import datetime, timezone
from google import genai
from google.genai import types
from src.config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_CONFIG


# Initialize client
_client = None

# Path to store persistent cache info
CACHE_INFO_FILE = "cache/persistent_cache_info.json"
LLAMAPARSE_ORIGINAL_SAP = "cache/NCT03676192_original_sap_llamaparse.md"


def get_client() -> genai.Client:
    """Get or create the Gemini client."""
    global _client
    if _client is None:
        _client = genai.Client(api_key=GEMINI_API_KEY)
    return _client


def create_document_cache(documents: dict, ttl_minutes: int = 1440) -> str:
    """
    Create a cache for the SAP documents.

    Args:
        documents: Dict with keys 'protocol', 'original_sap', 'generated_sap'
        ttl_minutes: Cache time-to-live in minutes (default 60)

    Returns:
        Cache name/ID to use in subsequent calls
    """
    client = get_client()

    # Build content to cache
    content_parts = []

    if "protocol" in documents:
        content_parts.append(f"## PROTOCOL DOCUMENT\n\n{documents['protocol']}")

    if "original_sap" in documents:
        content_parts.append(f"## ORIGINAL SAP DOCUMENT\n\n{documents['original_sap']}")

    if "generated_sap" in documents:
        content_parts.append(f"## GENERATED SAP DOCUMENT\n\n{documents['generated_sap']}")

    cached_content = "\n\n---\n\n".join(content_parts)

    # Create the cache
    cache = client.caches.create(
        model=GEMINI_MODEL,
        config=types.CreateCachedContentConfig(
            contents=[cached_content],
            ttl=f"{ttl_minutes * 60}s",  # TTL as string in seconds
            display_name="sap_documents_cache",
        ),
    )

    print(f"Cache created: {cache.name}")
    print(f"Expires: {cache.expire_time}")

    return cache.name


def evaluate_with_cache(cache_name: str, instruction: str, schema: dict = None, max_retries: int = 3) -> dict:
    """
    Call Gemini using cached documents + new instruction.

    Args:
        cache_name: The cache ID from create_document_cache()
        instruction: The evaluation instruction
        schema: Optional JSON schema for response
        max_retries: Number of retries on failure

    Returns:
        Parsed JSON response
    """
    client = get_client()

    for attempt in range(max_retries):
        try:
            config = types.GenerateContentConfig(
                temperature=GEMINI_CONFIG["temperature"],
                max_output_tokens=GEMINI_CONFIG["max_output_tokens"],
                response_mime_type="application/json",
                cached_content=cache_name,
            )

            if schema:
                config.response_schema = schema

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=f"## INSTRUCTION\n\n{instruction}",
                config=config,
            )

            return json.loads(response.text)
        except json.JSONDecodeError as e:
            if attempt < max_retries - 1:
                print(f"JSON parse error, retrying: {e}")
                time.sleep(1)
            else:
                raise
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Retry {attempt + 1}/{max_retries} after {wait_time}s: {e}")
                time.sleep(wait_time)
            else:
                raise


def delete_cache(cache_name: str):
    """Delete a cache when done."""
    client = get_client()
    client.caches.delete(name=cache_name)
    print(f"Cache deleted: {cache_name}")


def list_caches():
    """List all active caches."""
    client = get_client()
    caches = list(client.caches.list())
    for cache in caches:
        print(f"  {cache.name} - expires {cache.expire_time}")
    return caches


def get_or_create_original_sap_cache(ttl_minutes: int = 1440) -> str:
    """
    Get existing Original SAP cache or create a new one.
    Uses the LlamaParse extracted document for consistency.

    Args:
        ttl_minutes: Cache TTL in minutes (default 24 hours)

    Returns:
        Cache name to use for evaluations
    """
    client = get_client()

    # Check if we have a saved cache that's still valid
    if os.path.exists(CACHE_INFO_FILE):
        with open(CACHE_INFO_FILE, 'r') as f:
            cache_info = json.load(f)

        # Check if cache is still valid
        try:
            cache = client.caches.get(name=cache_info['cache_name'])
            if cache.expire_time > datetime.now(timezone.utc):
                print(f"Using existing cache: {cache.name}")
                print(f"  Expires: {cache.expire_time}")
                return cache.name
        except Exception as e:
            print(f"Existing cache invalid or expired: {e}")

    # Read the LlamaParse extracted document
    if not os.path.exists(LLAMAPARSE_ORIGINAL_SAP):
        raise FileNotFoundError(f"LlamaParse document not found: {LLAMAPARSE_ORIGINAL_SAP}")

    with open(LLAMAPARSE_ORIGINAL_SAP, 'r') as f:
        original_sap_content = f.read()

    print(f"Creating new cache from LlamaParse document...")
    print(f"  Document size: {len(original_sap_content)} characters")

    # Create the cache with just the Original SAP
    cache = client.caches.create(
        model=GEMINI_MODEL,
        config=types.CreateCachedContentConfig(
            contents=[f"## ORIGINAL SAP DOCUMENT (LlamaParse Extracted)\n\n{original_sap_content}"],
            ttl=f"{ttl_minutes * 60}s",
            display_name="original_sap_llamaparse_cache",
        ),
    )

    # Save cache info for reuse
    cache_info = {
        'cache_name': cache.name,
        'created_at': datetime.now(timezone.utc).isoformat(),
        'source_file': LLAMAPARSE_ORIGINAL_SAP,
        'ttl_minutes': ttl_minutes
    }

    os.makedirs(os.path.dirname(CACHE_INFO_FILE), exist_ok=True)
    with open(CACHE_INFO_FILE, 'w') as f:
        json.dump(cache_info, f, indent=2)

    print(f"Cache created: {cache.name}")
    print(f"  Expires: {cache.expire_time}")
    print(f"  Cache info saved to: {CACHE_INFO_FILE}")

    return cache.name


def evaluate_sap_with_persistent_cache(
    generated_sap: str,
    protocol: str,
    instruction: str,
    schema: dict = None,
    max_retries: int = 3
) -> dict:
    """
    Evaluate Generated SAP using the persistent Original SAP cache.

    Args:
        generated_sap: The Generated SAP content
        protocol: The Protocol content
        instruction: The evaluation instruction/prompt
        schema: Optional JSON schema for response
        max_retries: Number of retries on failure

    Returns:
        Parsed JSON response
    """
    # Get or create the persistent Original SAP cache
    original_sap_cache = get_or_create_original_sap_cache()

    # Build the evaluation prompt with Generated SAP and Protocol
    full_prompt = f"""## GENERATED SAP DOCUMENT

{generated_sap}

---

## PROTOCOL DOCUMENT

{protocol}

---

## INSTRUCTION

{instruction}"""

    client = get_client()

    for attempt in range(max_retries):
        try:
            config = types.GenerateContentConfig(
                temperature=GEMINI_CONFIG["temperature"],
                max_output_tokens=GEMINI_CONFIG["max_output_tokens"],
                response_mime_type="application/json",
                cached_content=original_sap_cache,
            )

            if schema:
                config.response_schema = schema

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=full_prompt,
                config=config,
            )

            return json.loads(response.text)
        except json.JSONDecodeError as e:
            if attempt < max_retries - 1:
                print(f"JSON parse error, retrying: {e}")
                time.sleep(1)
            else:
                raise
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Retry {attempt + 1}/{max_retries} after {wait_time}s: {e}")
                time.sleep(wait_time)
            else:
                raise
