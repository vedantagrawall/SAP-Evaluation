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

# Processed files (LlamaParse extracted)
PROCESSED_FILES_DIR = "data/processed_files"
ORIGINAL_SAP_FILE = f"{PROCESSED_FILES_DIR}/NCT03676192_original_sap.md"
PROTOCOL_FILE = f"{PROCESSED_FILES_DIR}/NCT03676192_protocol.md"


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


def evaluate_with_cache(cache_name: str, instruction: str, schema: dict = None, max_retries: int = 3, output_format: str = "json") -> dict:
    """
    Call Gemini using cached documents + new instruction.

    Args:
        cache_name: The cache ID from create_document_cache()
        instruction: The evaluation instruction
        schema: Optional JSON schema for response
        max_retries: Number of retries on failure
        output_format: "json" (default) or "markdown"

    Returns:
        Parsed JSON response (dict) or raw markdown string
    """
    client = get_client()

    for attempt in range(max_retries):
        try:
            config_kwargs = dict(
                temperature=GEMINI_CONFIG["temperature"],
                max_output_tokens=GEMINI_CONFIG["max_output_tokens"],
                cached_content=cache_name,
            )
            if output_format == "json":
                config_kwargs["response_mime_type"] = "application/json"

            config = types.GenerateContentConfig(**config_kwargs)

            if schema and output_format == "json":
                config.response_schema = schema

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=f"## INSTRUCTION\n\n{instruction}",
                config=config,
            )

            if output_format == "markdown":
                return response.text

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


def get_or_create_static_docs_cache(ttl_minutes: int = 1440) -> str:
    """
    Get existing cache or create a new one for static documents (Original SAP + Protocol).
    These documents never change, so we cache them together to save tokens.

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

    # Read the processed files
    if not os.path.exists(ORIGINAL_SAP_FILE):
        raise FileNotFoundError(f"Original SAP not found: {ORIGINAL_SAP_FILE}")
    if not os.path.exists(PROTOCOL_FILE):
        raise FileNotFoundError(f"Protocol not found: {PROTOCOL_FILE}")

    with open(ORIGINAL_SAP_FILE, 'r') as f:
        original_sap_content = f.read()
    with open(PROTOCOL_FILE, 'r') as f:
        protocol_content = f.read()

    print(f"Creating new cache from processed files...")
    print(f"  Original SAP: {len(original_sap_content):,} characters")
    print(f"  Protocol: {len(protocol_content):,} characters")

    # Create the cache with both Original SAP and Protocol
    cached_content = f"""## ORIGINAL SAP DOCUMENT

{original_sap_content}

---

## PROTOCOL DOCUMENT

{protocol_content}"""

    cache = client.caches.create(
        model=GEMINI_MODEL,
        config=types.CreateCachedContentConfig(
            contents=[cached_content],
            ttl=f"{ttl_minutes * 60}s",
            display_name="original_sap_and_protocol_cache",
        ),
    )

    # Save cache info for reuse
    cache_info = {
        'cache_name': cache.name,
        'created_at': datetime.now(timezone.utc).isoformat(),
        'source_files': [ORIGINAL_SAP_FILE, PROTOCOL_FILE],
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
    protocol: str = None,  # No longer needed - Protocol is cached
    instruction: str = None,
    schema: dict = None,
    max_retries: int = 3,
    output_format: str = "json"
) -> dict:
    """
    Evaluate Generated SAP using the persistent cache (Original SAP + Protocol).

    Only Generated SAP is sent fresh each call. Original SAP and Protocol are cached.

    Args:
        generated_sap: The Generated SAP content
        protocol: DEPRECATED - Protocol is now cached. Kept for backwards compatibility.
        instruction: The evaluation instruction/prompt
        schema: Optional JSON schema for response
        max_retries: Number of retries on failure
        output_format: "json" (default) or "markdown"

    Returns:
        Parsed JSON response (dict) or raw markdown string
    """
    # Get or create the persistent cache (Original SAP + Protocol)
    static_docs_cache = get_or_create_static_docs_cache()

    # Build the evaluation prompt with only Generated SAP (Original SAP + Protocol are cached)
    full_prompt = f"""## GENERATED SAP DOCUMENT

{generated_sap}

---

## INSTRUCTION

{instruction}"""

    client = get_client()

    for attempt in range(max_retries):
        try:
            config_kwargs = dict(
                temperature=GEMINI_CONFIG["temperature"],
                max_output_tokens=GEMINI_CONFIG["max_output_tokens"],
                cached_content=static_docs_cache,
            )
            if output_format == "json":
                config_kwargs["response_mime_type"] = "application/json"

            config = types.GenerateContentConfig(**config_kwargs)

            if schema and output_format == "json":
                config.response_schema = schema

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=full_prompt,
                config=config,
            )

            if output_format == "markdown":
                return response.text

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
