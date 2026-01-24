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
        if 'category' in first_item:
            # General methodology format (has category field)
            lines.append("| Component | Category | Matches Original SAP | Protocol Consulted | Result | Issue Type | Severity |")
            lines.append("|-----------|----------|---------------------|-------------------|--------|------------|----------|")
            for row in eval_table:
                comp = row.get('component', '')
                cat = row.get('category', '')
                match_orig = row.get('matches_original_sap', '')
                proto_cons = row.get('protocol_consulted', '')
                res = row.get('result', '')
                issue = row.get('issue_type', '')
                sev = row.get('severity', '')
                lines.append(f"| {comp} | {cat} | {match_orig} | {proto_cons} | {res} | {issue} | {sev} |")
        else:
            # Objectives/endpoints and analysis_populations format
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
        # Check if core meaning fields are present
        has_core_meaning = any(i.get('original_core_meaning') for i in issues)
        if has_core_meaning:
            lines.append("| Issue Type | Severity | Component | Original Core Meaning | Generated Core Meaning | Description |")
            lines.append("|------------|----------|-----------|----------------------|------------------------|-------------|")
            for issue in issues:
                itype = issue.get('issue_type', '')
                sev = issue.get('severity', '')
                comp = issue.get('component', '')
                orig_core = issue.get('original_core_meaning', '')
                gen_core = issue.get('generated_core_meaning', '')
                desc = issue.get('description', '')[:50]
                lines.append(f"| {itype} | {sev} | {comp} | {orig_core} | {gen_core} | {desc} |")
        else:
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

    # Missing from Generated SAP
    missing = result.get('missing_from_generated_sap', [])

    # Missing Required Content (in_protocol: "yes")
    required = [m for m in missing if m.get('in_protocol') == 'yes']
    lines.append(f"### ❌ Missing Required Content ({len(required)} items)")
    lines.append("")
    lines.append("Content in both Original SAP AND Protocol - should be in Generated SAP.")
    lines.append("")
    if required:
        # Use category if present, otherwise content_type
        has_category = any(m.get('category') for m in required)
        col_name = "Category" if has_category else "Content Type"
        lines.append(f"| Component | {col_name} | Original SAP Text | Protocol Text |")
        lines.append("|-----------|--------------|-------------------|---------------|")
        for item in required:
            comp = item.get('component', '')
            cat = item.get('category', '') or item.get('content_type', '')
            orig_text = item.get('original_sap_text', '')[:40]
            proto_text = (item.get('protocol_text') or '')[:40]
            lines.append(f"| {comp} | {cat} | {orig_text} | {proto_text} |")
    else:
        lines.append("*None - all required content is present.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Protocol Content Not In Generated SAP
    # Combine: protocol_content_not_in_generated_sap array + missing items where in_protocol="yes"
    protocol_missing_direct = result.get('protocol_content_not_in_generated_sap', [])
    protocol_missing_from_required = [m for m in missing if m.get('in_protocol') == 'yes']

    # Merge both lists (avoid duplicates by component name)
    seen_components = set()
    protocol_missing_combined = []
    for item in protocol_missing_direct + protocol_missing_from_required:
        comp = item.get('component', '')
        if comp not in seen_components:
            seen_components.add(comp)
            protocol_missing_combined.append(item)

    lines.append(f"### ⚠️ Protocol Content Not In Generated SAP ({len(protocol_missing_combined)} items)")
    lines.append("")
    lines.append("Content in Protocol but not in Generated SAP.")
    lines.append("")
    if protocol_missing_combined:
        # Use category if present, otherwise content_type
        has_category = any(m.get('category') for m in protocol_missing_combined)
        col_name = "Category" if has_category else "Content Type"
        lines.append(f"| Component | {col_name} | Protocol Text | Description |")
        lines.append("|-----------|--------------|---------------|-------------|")
        for item in protocol_missing_combined:
            comp = item.get('component', '')
            cat = item.get('category', '') or item.get('content_type', '')
            proto_text = (item.get('protocol_text') or '')[:40]
            desc = item.get('description', '')[:40]
            lines.append(f"| {comp} | {cat} | {proto_text} | {desc} |")
    else:
        lines.append("*No protocol content missing.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Internal Contradictions (for general_methodology)
    internal_contradictions = result.get('internal_contradictions', [])
    if internal_contradictions or section_name == 'general_methodology':
        lines.append(f"### Internal Contradictions ({len(internal_contradictions)} items)")
        lines.append("")
        if internal_contradictions:
            lines.append("| Component | Section A | Section A Text | Section B | Section B Text | Description |")
            lines.append("|-----------|-----------|----------------|-----------|----------------|-------------|")
            for item in internal_contradictions:
                comp = item.get('component', '')
                sec_a = item.get('section_a', '')
                sec_a_text = (item.get('section_a_text') or '')[:30]
                sec_b = item.get('section_b', '')
                sec_b_text = (item.get('section_b_text') or '')[:30]
                desc = item.get('description', '')[:40]
                lines.append(f"| {comp} | {sec_a} | {sec_a_text} | {sec_b} | {sec_b_text} | {desc} |")
        else:
            lines.append("*No internal contradictions found.*")

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
