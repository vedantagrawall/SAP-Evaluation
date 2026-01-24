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
        lines.append("| Issue Type | Severity | Component | Why They Conflict | Description |")
        lines.append("|------------|----------|-----------|-------------------|-------------|")
        for issue in issues:
            itype = issue.get('issue_type', '')
            sev = issue.get('severity', '')
            comp = issue.get('component', '')
            why_conflict = issue.get('why_they_conflict', '')[:40]
            desc = issue.get('description', '')[:40]
            lines.append(f"| {itype} | {sev} | {comp} | {why_conflict} | {desc} |")
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

    # Missing Required Content (in_protocol: "yes" OR classification: "missing_required")
    required = [m for m in missing if m.get('in_protocol') == 'yes' or m.get('classification') == 'missing_required']
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


def validate_contradictions(result: dict) -> dict:
    """
    Post-processing validation to enforce contradiction detection.
    If can_both_be_true == 'no', it's a contradiction.
    This guarantees consistency regardless of LLM judgment.
    """
    if 'evaluation_table' not in result:
        return result

    # Track existing issues by component
    existing_issues = {issue.get('component') for issue in result.get('issues', [])}

    for row in result['evaluation_table']:
        can_both_be_true = row.get('can_both_be_true', '').lower()

        # If statements conflict (can_both_be_true == 'no'), it's a contradiction
        if can_both_be_true == 'no':
            # Update the row if not already marked as problem
            if row.get('result') != 'problem':
                row['result'] = 'problem'
                row['issue_type'] = 'contradiction_original'
                if row.get('severity') == 'none':
                    row['severity'] = 'minor'

            # Add to issues array if not already there
            component = row.get('component', 'Unknown')
            if component not in existing_issues:
                issue = {
                    'issue_type': 'contradiction_original',
                    'severity': 'minor',
                    'component': component,
                    'original_sap_text': row.get('original_sap_text', ''),
                    'generated_sap_text': row.get('generated_sap_text', ''),
                    'why_they_conflict': row.get('reasoning', 'Statements cannot both be true'),
                    'description': 'Detected conflict between Original and Generated SAP',
                    'reasoning': 'Detected by post-processing validation'
                }
                if 'issues' not in result:
                    result['issues'] = []
                result['issues'].append(issue)
                existing_issues.add(component)

    return result


def load_documents():
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


def get_extraction_cache_path(nct_id: str, section: str) -> Path:
    """Get path for cached extraction results."""
    cache_dir = Path("cache")
    cache_dir.mkdir(exist_ok=True)
    return cache_dir / f"{nct_id}_{section}_extraction.json"


def extract_statements(nct_id: str, section: str, force: bool = False):
    """
    Extract statements from Original SAP (run ONCE, cache results).

    Args:
        nct_id: Trial ID (e.g., 'NCT03676192')
        section: Section name (e.g., 'general_methodology')
        force: If True, re-extract even if cache exists
    """
    from src.llm_client import create_document_cache, evaluate_with_cache, delete_cache

    cache_path = get_extraction_cache_path(nct_id, section)

    # Check if already cached
    if cache_path.exists() and not force:
        print(f"✓ Using cached extraction: {cache_path}")
        return json.loads(cache_path.read_text())

    print(f"Extracting statements from Original SAP (section: {section})...")

    # Load only Original SAP
    docs = load_documents()

    # Extraction prompt - only extracts, no comparison
    extraction_prompt = f"""
You are extracting statements from an Original SAP document for later comparison.

## YOUR TASK

Read the Original SAP document and extract ALL statements related to {section.replace('_', ' ')}.

For each statement:
1. Extract the EXACT TEXT (word-for-word quote)
2. Create one entry per statement
3. When a sentence contains "X and Y", split into SEPARATE entries

## OUTPUT FORMAT

Return a JSON array of extracted statements:

```json
{{
  "section": "{section}",
  "nct_id": "{nct_id}",
  "statements": [
    {{
      "id": 1,
      "component": "short description",
      "original_sap_text": "exact quote from Original SAP",
      "section_reference": "section number where found"
    }}
  ],
  "total_count": 0
}}
```

Extract ALL statements. Do not summarize or skip any.
"""

    # Create cache and run extraction
    cache_name = create_document_cache({"original_sap": docs["original_sap"]}, ttl_minutes=30)

    try:
        result = evaluate_with_cache(cache_name, extraction_prompt)

        # Save to cache
        cache_path.write_text(json.dumps(result, indent=2))
        print(f"✓ Extraction cached: {cache_path}")
        print(f"  Statements extracted: {result.get('total_count', len(result.get('statements', [])))}")

        return result
    finally:
        delete_cache(cache_name)


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

        # Post-processing validation to enforce contradiction rules
        result = validate_contradictions(result)

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

    if len(sys.argv) > 1 and sys.argv[1] == "extract":
        # Run extraction: python -m src.test_prompt extract general_methodology
        section = sys.argv[2] if len(sys.argv) > 2 else "general_methodology"
        force = "--force" in sys.argv
        extract_statements("NCT03676192", section, force=force)
    else:
        # Run evaluation: python -m src.test_prompt general_methodology
        prompt_name = sys.argv[1] if len(sys.argv) > 1 else "objectives_endpoints"
        test_prompt(prompt_name)
