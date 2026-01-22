"""
Quick test script to validate a prompt against cached documents.

"""

import json
from pathlib import Path


def load_documents():
    """Load the processed markdown documents."""
    data_dir = Path("data/processed_files")

    docs = {
        "protocol": (data_dir / "NCT03676192_protocol.md").read_text(),
        "original_sap": (data_dir / "NCT03676192_original_sap.md").read_text(),
        "generated_sap": (data_dir / "NCT03676192_generated_sap.md").read_text(),
    }

    print(f"Loaded documents:")
    for name, content in docs.items():
        print(f"  {name}: {len(content):,} chars")

    return docs


def load_prompt(prompt_name: str) -> str:
    """Load a prompt file from prompts/"""
    prompt_path = Path("prompts") / f"{prompt_name}.txt"
    return prompt_path.read_text()


def test_prompt(prompt_name: str = "objectives_endpoints"):
    """Test a prompt against the NCT03676192 documents."""
    from src.llm_client import create_document_cache, evaluate_with_cache, delete_cache

    print("=" * 60)
    print(f"TESTING PROMPT: {prompt_name}")
    print("=" * 60)

    # Load documents
    print("\n1. Loading documents...")
    docs = load_documents()

    # Load prompt
    print(f"\n2. Loading prompt: {prompt_name}.txt...")
    prompt = load_prompt(prompt_name)
    print(f"   Prompt length: {len(prompt):,} chars")

    # Create cache
    print("\n3. Creating document cache...")
    cache_name = create_document_cache(docs, ttl_minutes=30)

    # Run evaluation
    print("\n4. Running evaluation (this may take 30-60 seconds)...")
    try:
        result = evaluate_with_cache(cache_name, prompt)

        print("\n5. RESULT:")
        print("=" * 60)
        print(json.dumps(result, indent=2))

        # Save result to file
        output_path = Path("output") / f"test_{prompt_name}_result.json"
        output_path.write_text(json.dumps(result, indent=2))
        print(f"\n✓ Result saved to: {output_path}")

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        raise
    finally:
        # Cleanup
        print("\n6. Cleaning up cache...")
        delete_cache(cache_name)

    return result


if __name__ == "__main__":
    test_prompt("objectives_endpoints")
