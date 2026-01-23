"""
Quick test script to validate a prompt against cached documents.

Run: python -m src.test_prompt
"""

import json
from pathlib import Path


def json_to_markdown(result: dict, section_name: str) -> str:
    """Convert JSON evaluation result to markdown format."""
    lines = []

    # Header
    lines.append(f"## {section_name.replace('_', ' ').title()} Evaluation")
    lines.append("")
    lines.append(f"**Section:** {result.get('section', section_name)}")
    lines.append(f"**Rating:** {result.get('rating', 'N/A')}")
    lines.append(f"**Status:** {result.get('status', 'N/A')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Evaluation Summary Table
    lines.append("### Evaluation Summary Table")
    lines.append("")

    eval_table = result.get('evaluation_table', [])
    if eval_table:
        # Determine columns based on first item
        first_item = eval_table[0]
        if 'population' in first_item:
            # Analysis populations format
            lines.append("| Population | Component | Matches Original SAP | Matches Protocol | Result | Issue Type | Severity |")
            lines.append("|------------|-----------|---------------------|------------------|--------|------------|----------|")
            for row in eval_table:
                pop = row.get('population', '')
                comp = row.get('component', '')
                match_orig = row.get('matches_original_sap', '')
                match_proto = row.get('matches_protocol', '')
                res = row.get('result', '')
                issue = row.get('issue_type', '')
                sev = row.get('severity', '')
                lines.append(f"| {pop} | {comp} | {match_orig} | {match_proto} | {res} | {issue} | {sev} |")
        else:
            # Objectives/endpoints format
            lines.append("| Component | Evaluation Type | Matches Original SAP | Protocol Consulted | Result | Issue Type | Severity |")
            lines.append("|-----------|-----------------|---------------------|-------------------|--------|------------|----------|")
            for row in eval_table:
                comp = row.get('component', '')
                eval_type = row.get('evaluation_type', '')
                match_orig = row.get('matches_original_sap', '')
                proto_cons = row.get('protocol_consulted', '')
                res = row.get('result', '')
                issue = row.get('issue_type', '')
                sev = row.get('severity', '')
                lines.append(f"| {comp} | {eval_type} | {match_orig} | {proto_cons} | {res} | {issue} | {sev} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Issues Found
    lines.append("### Issues Found")
    lines.append("")
    issues = result.get('issues', [])
    if issues:
        lines.append("| Issue Type | Component | Description |")
        lines.append("|------------|-----------|-------------|")
        for issue in issues:
            itype = issue.get('issue_type', '')
            comp = issue.get('component', '')
            desc = issue.get('description', '')
            lines.append(f"| {itype} | {comp} | {desc} |")
    else:
        lines.append("*No issues found.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Extra Information Flagged
    lines.append("### Extra Information Flagged")
    lines.append("")
    extra = result.get('extra_information_flagged', [])
    if extra:
        lines.append("| Content | Contradicts | Detail |")
        lines.append("|---------|-------------|--------|")
        for item in extra:
            content = item.get('content', '')
            contradicts = item.get('contradicts', '')
            detail = item.get('detail', '')
            lines.append(f"| {content} | {contradicts} | {detail} |")
    else:
        lines.append("*No extra information flagged.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Missing from Generated SAP - split into two sections
    missing = result.get('missing_from_generated_sap', [])

    # Acceptable Differences (in_protocol: "no")
    acceptable = [m for m in missing if m.get('in_protocol') == 'no']
    lines.append(f"### ✅ Acceptable Differences ({len(acceptable)} items)")
    lines.append("")
    lines.append("Content in Original SAP only (not in Protocol) - acceptable to omit.")
    lines.append("")
    if acceptable:
        lines.append("| Component | Category | Original SAP Text |")
        lines.append("|-----------|----------|-------------------|")
        for item in acceptable:
            comp = item.get('component', '')
            cat = item.get('category', '')
            orig_text = item.get('original_sap_text', '')[:50]
            lines.append(f"| {comp} | {cat} | {orig_text} |")
    else:
        lines.append("*None*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Missing Required Content (in_protocol: "yes")
    required = [m for m in missing if m.get('in_protocol') == 'yes']
    lines.append(f"### ❌ Missing Required Content ({len(required)} items)")
    lines.append("")
    lines.append("Content in both Original SAP AND Protocol - should be in Generated SAP.")
    lines.append("")
    if required:
        lines.append("| Component | Category | Original SAP Text | Protocol Text |")
        lines.append("|-----------|----------|-------------------|---------------|")
        for item in required:
            comp = item.get('component', '')
            cat = item.get('category', '')
            orig_text = item.get('original_sap_text', '')[:40]
            proto_text = (item.get('protocol_text') or '')[:40]
            lines.append(f"| {comp} | {cat} | {orig_text} | {proto_text} |")
    else:
        lines.append("*None - all required content is present.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Reasoning
    lines.append("### Reasoning")
    lines.append("")
    lines.append(result.get('reasoning', '*No reasoning provided.*'))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary
    lines.append("### Summary")
    lines.append("")
    lines.append(result.get('summary', '*No summary provided.*'))

    return "\n".join(lines)


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

        # Save JSON result
        output_path = Path("output") / f"test_{prompt_name}_result.json"
        output_path.write_text(json.dumps(result, indent=2))
        print(f"\n✓ JSON saved to: {output_path}")

        # Save Markdown result
        markdown_content = json_to_markdown(result, prompt_name)
        md_output_path = Path("output") / f"test_{prompt_name}_result.md"
        md_output_path.write_text(markdown_content)
        print(f"✓ Markdown saved to: {md_output_path}")

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        raise
    finally:
        # Cleanup
        print("\n6. Cleaning up cache...")
        delete_cache(cache_name)

    return result


if __name__ == "__main__":
    import sys
    prompt_name = sys.argv[1] if len(sys.argv) > 1 else "objectives_endpoints"
    test_prompt(prompt_name)
