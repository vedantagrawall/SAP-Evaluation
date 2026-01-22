import json
import time
from google import genai
from google.genai import types
from src.config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_CONFIG


# Initialize client
_client = None


def get_client() -> genai.Client:
    """Get or create the Gemini client."""
    global _client
    if _client is None:
        _client = genai.Client(api_key=GEMINI_API_KEY)
    return _client


def create_document_cache(documents: dict, ttl_minutes: int = 60) -> str:
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


# --- Legacy functions (without caching) ---

def build_cached_prompt(documents: dict, instruction: str) -> str:
    """Build a prompt with documents first and instruction after."""
    prompt_parts = []

    if "protocol" in documents:
        prompt_parts.append(f"## PROTOCOL DOCUMENT\n\n{documents['protocol']}")

    if "original_sap" in documents:
        prompt_parts.append(f"## ORIGINAL SAP DOCUMENT\n\n{documents['original_sap']}")

    if "generated_sap" in documents:
        prompt_parts.append(f"## GENERATED SAP DOCUMENT\n\n{documents['generated_sap']}")

    prompt_parts.append(f"## INSTRUCTION\n\n{instruction}")

    return "\n\n---\n\n".join(prompt_parts)


def call_llm(prompt: str, max_retries: int = 3) -> str:
    """Call Gemini and return text response."""
    client = get_client()

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=GEMINI_CONFIG["temperature"],
                    max_output_tokens=GEMINI_CONFIG["max_output_tokens"],
                ),
            )
            return response.text
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Retry {attempt + 1}/{max_retries} after {wait_time}s: {e}")
                time.sleep(wait_time)
            else:
                raise


def call_llm_json(prompt: str, schema: dict = None, max_retries: int = 3) -> dict:
    """Call Gemini and return structured JSON response."""
    client = get_client()

    for attempt in range(max_retries):
        try:
            config = types.GenerateContentConfig(
                temperature=GEMINI_CONFIG["temperature"],
                max_output_tokens=GEMINI_CONFIG["max_output_tokens"],
                response_mime_type="application/json",
            )

            if schema:
                config.response_schema = schema

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
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


def evaluate_with_docs(documents: dict, instruction: str, schema: dict = None) -> dict:
    """Convenience function: build prompt and get JSON response (no caching)."""
    prompt = build_cached_prompt(documents, instruction)
    return call_llm_json(prompt, schema)
