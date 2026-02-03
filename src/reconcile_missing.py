"""
Post-processing reconciliation to remove false positives from missing lists.

After all section evaluations complete, this script:
1. Loads the full Generated SAP
2. For each section's missing_from_generated_sap items
3. Checks if the content exists elsewhere in the Generated SAP
4. Removes items that exist elsewhere
5. Regenerates ratings based on updated missing lists

Generic approach - works for any protocol, section, or content type.
"""

import json
import time
from pathlib import Path
from google import genai
from google.genai import types
from src.config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_CONFIG


def call_llm_simple(prompt: str) -> dict:
    """Make a simple LLM call without caching."""
    client = genai.Client(api_key=GEMINI_API_KEY)

    config = types.GenerateContentConfig(
        temperature=GEMINI_CONFIG["temperature"],
        max_output_tokens=8000,
        response_mime_type="application/json"
    )

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=config
            )
            return json.loads(response.text)
        except Exception as e:
            if attempt < 2:
                wait_time = 2 ** attempt
                print(f"      Retry {attempt + 1}/3 after {wait_time}s: {e}")
                time.sleep(wait_time)
            else:
                raise


def load_section_results(nct_id: str) -> dict:
    """Load all section evaluation results."""
    results_dir = Path(f"results/{nct_id}")
    sections = {}

    for json_file in results_dir.glob("*.json"):
        section_name = json_file.stem
        with open(json_file, 'r') as f:
            sections[section_name] = json.load(f)

    return sections


def load_generated_sap(nct_id: str) -> str:
    """Load the full Generated SAP document."""
    sap_path = Path(f"data/processed_files/{nct_id}_generated_sap.md")
    return sap_path.read_text()


def check_content_exists_elsewhere(missing_item: dict, generated_sap: str, section_name: str) -> dict:
    """
    Check if missing content exists elsewhere in Generated SAP.

    Returns dict with:
        - exists_elsewhere: bool
        - found_in_section: str or None
        - reasoning: str
    """
    original_text = missing_item.get('original_sap_text', '')
    component = missing_item.get('component', '')

    if not original_text:
        return {
            'exists_elsewhere': False,
            'found_in_section': None,
            'reasoning': 'No original text to search for'
        }

    # Use LLM to check if content exists elsewhere
    prompt = f"""You are checking if content from one section of a document exists in other sections.

**Component:** {component}

**Content from Original SAP (in {section_name} section):**
{original_text}

**Full Generated SAP:**
{generated_sap}

**Task:**
Does the Generated SAP contain equivalent content anywhere in the document?

**Key Principle:**
If the Original SAP content describes logic for organizing, assigning, or categorizing data using specific constructs, check if:
1. The Generated SAP uses those constructs anywhere
2. Those constructs are defined somewhere in the document

If BOTH conditions are met, the core requirement is satisfied even if the detailed assignment logic is structured differently or appears in a different section.

**What counts as "equivalent content":**
- Constructs are defined in another section
- Constructs are used for organizing or presenting data
- Definitions may be less detailed but cover the core concept
- Content may be in different sections with different organization
- Wording or structure may differ

**What does NOT count:**
- Construct mentioned but never defined
- Construct defined but never used
- Generated SAP actively contradicts the approach

**Output JSON:**
{{
    "exists_elsewhere": true/false,
    "found_in_section": "section name or heading where found, or null",
    "reasoning": "explain what you found and why it does/doesn't satisfy the requirement"
}}
"""

    try:
        result = call_llm_simple(prompt)
        return result
    except Exception as e:
        return {
            'exists_elsewhere': False,
            'found_in_section': None,
            'reasoning': f'Error checking: {str(e)}'
        }


def reconcile_evaluation_table(evaluation_table: list, generated_sap: str, section_name: str) -> dict:
    """
    Check evaluation_table items marked as 'problem' and fix if content exists elsewhere.

    Returns dict with counts and fixed items.
    """
    problem_items = [e for e in evaluation_table if e.get('result') == 'problem']

    if not problem_items:
        return {'items_checked': 0, 'items_fixed': 0, 'fixed_items': []}

    fixed_items = []
    print(f"\n  Checking {len(problem_items)} problem items in evaluation_table...")

    for item in problem_items:
        component = item.get('component', 'Unknown')
        omitted_content = item.get('omitted_content')

        # Only check items that have omitted_content (organizational differences)
        if not omitted_content:
            continue

        print(f"    - {component}...", end=' ')

        # Create a temporary item structure for checking
        check_item = {
            'component': component,
            'original_sap_text': item.get('original_sap_text', ''),
            'description': f"Omitted: {omitted_content}"
        }

        check_result = check_content_exists_elsewhere(check_item, generated_sap, section_name)

        if check_result['exists_elsewhere']:
            print(f"✓ Found in {check_result['found_in_section']}")
            # Change from problem to acceptable
            item['result'] = 'acceptable'
            item['severity'] = 'none'
            item['issue_type'] = 'none'
            item['matches_original_sap'] = 'yes'
            item['reconciliation_note'] = f"Found in {check_result['found_in_section']}"

            fixed_items.append({
                'component': component,
                'was': 'problem',
                'now': 'acceptable',
                'found_in_section': check_result['found_in_section'],
                'reasoning': check_result['reasoning']
            })
        else:
            print(f"✗ Not found elsewhere")

    return {
        'items_checked': len(problem_items),
        'items_fixed': len(fixed_items),
        'fixed_items': fixed_items
    }


def reconcile_section(section_name: str, section_data: dict, generated_sap: str) -> dict:
    """
    Reconcile missing items and evaluation_table problems for a single section.

    Returns updated section data with reconciliation metadata.
    """
    # Part 1: Reconcile missing_from_generated_sap
    missing_items = section_data.get('missing_from_generated_sap', [])
    kept_items = []
    removed_items = []

    if missing_items:
        print(f"\n  Checking {len(missing_items)} missing items...")

        for item in missing_items:
            component = item.get('component', 'Unknown')
            print(f"    - {component}...", end=' ')

            check_result = check_content_exists_elsewhere(item, generated_sap, section_name)

            if check_result['exists_elsewhere']:
                print(f"✓ Found in {check_result['found_in_section']}")
                removed_items.append({
                    **item,
                    'removed_by_reconciliation': True,
                    'found_in_section': check_result['found_in_section'],
                    'reconciliation_reasoning': check_result['reasoning']
                })
            else:
                print(f"✗ Not found elsewhere")
                kept_items.append(item)

        section_data['missing_from_generated_sap'] = kept_items

    # Part 2: Reconcile evaluation_table problem items
    evaluation_table = section_data.get('evaluation_table', [])
    eval_reconciliation = reconcile_evaluation_table(evaluation_table, generated_sap, section_name)

    # Update section data with reconciliation metadata
    section_data['reconciliation'] = {
        'performed': True,
        'missing_items_checked': len(missing_items),
        'missing_items_removed': len(removed_items),
        'removed_items': removed_items,
        'evaluation_problems_checked': eval_reconciliation['items_checked'],
        'evaluation_problems_fixed': eval_reconciliation['items_fixed'],
        'fixed_evaluation_items': eval_reconciliation['fixed_items']
    }

    return section_data


def reconcile_all_sections(nct_id: str, save: bool = True):
    """
    Run reconciliation for all sections.

    Args:
        nct_id: Trial ID (e.g., 'NCT03676192')
        save: If True, save updated results back to files
    """
    print(f"=" * 60)
    print(f"RECONCILIATION: {nct_id}")
    print(f"=" * 60)

    # Load full Generated SAP
    print("\n1. Loading Generated SAP...")
    generated_sap = load_generated_sap(nct_id)
    print(f"   Length: {len(generated_sap):,} chars")

    # Load all section results
    print("\n2. Loading section evaluations...")
    sections = load_section_results(nct_id)
    print(f"   Sections: {len(sections)}")

    # Reconcile each section
    print("\n3. Running reconciliation...")
    for section_name, section_data in sections.items():
        print(f"\n{section_name}:")
        sections[section_name] = reconcile_section(section_name, section_data, generated_sap)

    # Save updated results
    if save:
        print("\n4. Saving updated results...")
        # Import markdown converter
        from src.test_prompt import json_to_markdown

        results_dir = Path(f"results/{nct_id}")
        for section_name, section_data in sections.items():
            # Save JSON
            json_path = results_dir / f"{section_name}.json"
            with open(json_path, 'w') as f:
                json.dump(section_data, f, indent=2)

            # Regenerate markdown
            markdown_content = json_to_markdown(section_data, section_name)
            md_path = results_dir / f"{section_name}.md"
            with open(md_path, 'w') as f:
                f.write(markdown_content)

            print(f"   ✓ {section_name}.json + .md")

    # Summary
    print("\n5. Summary:")
    total_checked = sum(s['reconciliation']['items_checked'] for s in sections.values() if 'reconciliation' in s)
    total_removed = sum(s['reconciliation']['items_removed'] for s in sections.values() if 'reconciliation' in s)
    print(f"   Items checked: {total_checked}")
    print(f"   Items removed: {total_removed}")
    print(f"   Items kept: {total_checked - total_removed}")

    print("\n✓ Reconciliation complete!")
    return sections


if __name__ == "__main__":
    import sys

    nct_id = sys.argv[1] if len(sys.argv) > 1 else "NCT03676192"
    save = "--save" in sys.argv or "-s" in sys.argv

    reconcile_all_sections(nct_id, save=save)
