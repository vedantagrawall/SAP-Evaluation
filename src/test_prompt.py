"""
Quick test script to validate a prompt against cached documents.

Run: python -m src.test_prompt
"""

import json
from pathlib import Path

# Prompts that return raw markdown instead of JSON
MARKDOWN_PROMPTS = {"objectives_endpoints_only"}


def json_to_markdown_analysis_populations(result: dict) -> str:
    """Convert analysis_populations JSON to markdown with 3-component focus."""
    lines = []

    # Header
    lines.append("## Analysis Populations Evaluation")
    lines.append("")
    lines.append(f"**Section:** {result.get('section', 'analysis_populations')}")
    lines.append(f"**Rating:** {result.get('rating', 'N/A')}")
    lines.append(f"**Status:** {result.get('status', 'N/A')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Get evaluation table
    eval_table = result.get('evaluation_table', [])

    # Extract populations and consolidate into 3 components each
    populations = {}
    granular_details = []

    for row in eval_table:
        comp = row.get('component', '')
        result_val = row.get('result', '')

        # Parse population name and component type
        if ' - ' in comp:
            pop_name, comp_type = comp.split(' - ', 1)
        else:
            pop_name = comp
            comp_type = 'Other'

        # Classify into 3 main components or granular
        comp_lower = comp_type.lower()

        # Name matching - exact "name" only
        if comp_lower == 'name':
            category = 'Name'
        # Treatment Assignment matching - flexible
        elif 'assignment' in comp_lower or (comp_lower == 'treatment assignment'):
            category = 'Treatment Assignment'
        # Definition matching - includes sub-components
        elif 'definition' in comp_lower:
            category = 'Definition'
            # Also add to granular if it's a sub-component
            if '(' in comp_type:
                granular_details.append(row)
        # Other known sub-components that belong to Definition
        elif any(keyword in comp_lower for keyword in ['base', 'dosing', 'randomization', 'response', 'deviations', 'results']):
            category = 'Definition'
            granular_details.append(row)
        # Other items (usage, timing, non-compliance, etc.) go to granular only
        else:
            granular_details.append(row)
            continue

        # Initialize population if not exists
        if pop_name not in populations:
            populations[pop_name] = {'Name': None, 'Definition': None, 'Treatment Assignment': None}

        # Store result (use first match or consolidate)
        if populations[pop_name][category] is None:
            populations[pop_name][category] = result_val
        elif populations[pop_name][category] == 'correct' and result_val == 'problem':
            populations[pop_name][category] = 'problem'  # Problem takes precedence

    # Main Section: 3 Critical Components
    lines.append("### Critical Components (3 per Population)")
    lines.append("")
    lines.append("These are the MUST match items for each population.")
    lines.append("")
    lines.append("| Population | Name | Definition | Treatment Assignment |")
    lines.append("|------------|------|------------|---------------------|")

    for pop_name, components in populations.items():
        name_result = components.get('Name', '-')
        def_result = components.get('Definition', '-')
        treat_result = components.get('Treatment Assignment', '-')

        # Format with checkmarks/crosses (both 'correct' and 'acceptable' are passing)
        name_display = '✓' if name_result in ('correct', 'acceptable') else ('✗' if name_result == 'problem' else '-')
        def_display = '✓' if def_result in ('correct', 'acceptable') else ('✗' if def_result == 'problem' else '-')
        treat_display = '✓' if treat_result in ('correct', 'acceptable') else ('✗' if treat_result == 'problem' else '-')

        lines.append(f"| {pop_name} | {name_display} | {def_display} | {treat_display} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed Evaluation - show omitted content for Definition and Assignment
    lines.append("### What Was Omitted (Definition & Treatment Assignment)")
    lines.append("")
    lines.append("Exact quotes of content in Original SAP that is missing from Generated SAP.")
    lines.append("")

    # Filter for Definition and Assignment rows with omitted content
    detail_rows = [row for row in eval_table
                   if row.get('omitted_content') and
                   ('definition' in row.get('component', '').lower() or
                    'assignment' in row.get('component', '').lower())]

    if detail_rows:
        lines.append("| Component | Omitted Content | Result |")
        lines.append("|-----------|-----------------|--------|")
        for row in detail_rows:
            comp = row.get('component', '')
            omitted = row.get('omitted_content', '-')
            result_val = row.get('result', '')
            lines.append(f"| {comp} | {omitted} | {result_val} |")
    else:
        lines.append("*No omissions in Definition or Treatment Assignment.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Issues Found
    lines.append("### Issues Found")
    lines.append("")
    issues = result.get('issues', [])
    if issues:
        lines.append("| Issue Type | Severity | Component | Description |")
        lines.append("|------------|----------|-----------|-------------|")
        for issue in issues:
            itype = issue.get('issue_type', '')
            sev = issue.get('severity', '')
            comp = issue.get('component', '')
            desc = issue.get('description', '')[:50]
            lines.append(f"| {itype} | {sev} | {comp} | {desc} |")
    else:
        lines.append("*No issues found.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Missing Required Content
    missing = result.get('missing_from_generated_sap', [])
    required = [m for m in missing if m.get('in_protocol') == 'yes' or m.get('classification') == 'missing_required']

    lines.append(f"### ❌ Missing Required Content ({len(required)} items)")
    lines.append("")
    lines.append("Content in both Original SAP AND Protocol - should be in Generated SAP.")
    lines.append("")
    if required:
        lines.append("| Component | Content Type | Description |")
        lines.append("|-----------|--------------|-------------|")
        for item in required:
            comp = item.get('component', '')
            ctype = item.get('content_type', '')
            desc = item.get('description', '')[:50]
            lines.append(f"| {comp} | {ctype} | {desc} |")
    else:
        lines.append("*None - all required content is present.*")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Secondary Section: Granular Details
    lines.append("### Granular Details (Definition Sub-components)")
    lines.append("")
    lines.append("<details>")
    lines.append("<summary>Click to expand detailed breakdown</summary>")
    lines.append("")

    if granular_details:
        lines.append("| Component | Result | Protocol Consulted |")
        lines.append("|-----------|--------|-------------------|")
        for row in granular_details:
            comp = row.get('component', '')
            res = row.get('result', '')
            proto = row.get('protocol_consulted', '')
            lines.append(f"| {comp} | {res} | {proto} |")
    else:
        lines.append("*No granular details.*")

    lines.append("")
    lines.append("</details>")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary
    lines.append("### Summary")
    lines.append("")
    lines.append(result.get('summary', '*No summary provided.*'))

    return "\n".join(lines)


def _format_key(key: str) -> str:
    """Convert snake_case JSON key to readable label."""
    return key.replace('_', ' ').replace('sap', 'SAP').strip()


def _render_dict_item(item: dict, lines: list):
    """Render all key-value pairs of a dict as markdown bullet points. No truncation."""
    for key, value in item.items():
        if value is None or value == '' or value == 'null':
            continue
        if key == 'component':
            continue  # already used as heading
        label = _format_key(key)
        lines.append(f"- **{label}:** {value}")


def _render_array_section(result: dict, key: str, heading: str, lines: list):
    """Render a JSON array as a numbered markdown section with all fields."""
    items = result.get(key, [])
    lines.append(f"### {heading} ({len(items)} items)")
    lines.append("")
    if items:
        for i, item in enumerate(items, 1):
            if isinstance(item, dict):
                title = item.get('component', item.get('content', f'Item {i}'))
                lines.append(f"#### {i}. {title}")
                lines.append("")
                _render_dict_item(item, lines)
                lines.append("")
            else:
                # Scalar item (string, number)
                lines.append(f"- {item}")
        lines.append("")
    else:
        lines.append(f"*No {heading.lower()}.*")
        lines.append("")
    lines.append("---")
    lines.append("")


def json_to_markdown(result: dict, section_name: str) -> str:
    """Convert JSON evaluation result to markdown format. All fields match JSON — no truncation.

    Renders every key in the JSON. Uses generic rendering so non-standard keys
    (e.g. missing_definitions, additions) are included automatically.
    """

    lines = []

    # Top-level scalar fields
    lines.append(f"## {section_name.replace('_', ' ').title()} Evaluation")
    lines.append("")
    lines.append(f"**Section:** {result.get('section', section_name)}")
    lines.append(f"**Rating:** {result.get('rating', 'N/A')}")
    lines.append(f"**Status:** {result.get('status', 'N/A')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Extraction Validation — render all keys generically
    extraction = result.get('extraction_validation', {})
    if extraction:
        lines.append("### Extraction Validation")
        lines.append("")
        for key, value in extraction.items():
            label = _format_key(key)
            if isinstance(value, list):
                lines.append(f"- **{label}:** {', '.join(str(v) for v in value)}")
            elif isinstance(value, dict):
                lines.append(f"- **{label}:** {', '.join(f'{k}: {v}' for k, v in value.items())}")
            else:
                lines.append(f"- **{label}:** {value}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Known array sections with preferred headings
    known_arrays = {
        'evaluation_table': 'Evaluation Table',
        'issues': 'Issues Found',
        'extra_information_flagged': 'Extra Information Flagged',
        'missing_from_generated_sap': 'Missing from Generated SAP',
        'internal_contradictions': 'Internal Contradictions',
        # Non-standard keys from key_definitions
        'missing_definitions': 'Missing Definitions',
        'additions': 'Additions',
    }

    # Render all array sections — both known and unknown
    rendered_keys = {'section', 'rating', 'status', 'extraction_validation', 'reasoning', 'summary'}

    # First render known arrays in order
    for key, heading in known_arrays.items():
        if key in result:
            _render_array_section(result, key, heading, lines)
            rendered_keys.add(key)

    # Then render any remaining arrays not in the known list
    for key, value in result.items():
        if key in rendered_keys:
            continue
        if isinstance(value, list):
            # Skip arrays of scalars (strings, numbers) — only render arrays of dicts
            if value and not isinstance(value[0], dict):
                # Render scalar arrays as a simple bullet list
                heading = _format_key(key).title()
                lines.append(f"### {heading}")
                lines.append("")
                for item in value:
                    lines.append(f"- {item}")
                lines.append("")
                lines.append("---")
                lines.append("")
                rendered_keys.add(key)
                continue
            heading = _format_key(key).title()
            _render_array_section(result, key, heading, lines)
            rendered_keys.add(key)

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
    """Load Generated SAP and Protocol only. Original SAP is in persistent cache."""
    data_dir = Path("data/processed_files")

    docs = {
        "protocol": (data_dir / "NCT03676192_protocol.md").read_text(),
        "generated_sap": (data_dir / "NCT03676192_generated_sap.md").read_text(),
    }

    print(f"Loaded documents:")
    for name, content in docs.items():
        print(f"  {name}: {len(content):,} chars")
    print(f"  original_sap: Using persistent LlamaParse cache")

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
You are extracting EVERY SINGLE STATEMENT from an Original SAP document.

## YOUR TASK

Extract EVERY statement, rule, definition, and specification from the ENTIRE Original SAP document.
This document has approximately 600 sentences - you must extract ALL of them.
Do NOT filter or skip anything. Extract EVERYTHING.

## SECTIONS TO EXTRACT (extract EVERYTHING from each):

### Section 1: INTRODUCTION
- Study background, data cut-off dates, analysis timing

### Section 2: STUDY OBJECTIVES
- Primary objective (efficacy similarity)
- Secondary objectives (ORR, PFS, OS, TTP, response duration, PK, safety, immunogenicity, QoL)

### Section 3: OVERALL STUDY DESIGN
- Study periods (Screening, Induction, Maintenance, Follow-up)
- Treatment regimens, dosing schedules
- Study flow

### Section 4: GENERAL STATISTICAL CONSIDERATIONS
- Descriptive statistics rules, decimal places, percentages
- Sample size calculation (305, 678, 80% power, 10% dropout)
- Randomization (IWRS, permuted blocks, 1:1 ratio)
- Stratification factors (country, sex, disease status, ECOG)
- Blinding (double-blind, database lock, 1st CSR unblinding)
- ALL population definitions (ITT, PP, PK, PK-Maintenance, Safety)
- Treatment assignment rules for EACH population
- Full dose definition (15mg/kg, Dose Not Changed)
- Baseline/post-baseline definitions
- Protocol deviations (FULL LIST: Mis-randomizations, Non-compliance, GCP, prohibited therapies, missing efficacy)
- Outliers handling
- Missing values handling (non-responder, tipping point, MNAR)

### Section 5: PATIENT DISPOSITION
- Screening failure definition
- Randomized definition
- Study period initiation definitions
- Completion/discontinuation definitions
- Time on study drug calculation

### Section 6: DEMOGRAPHICS AND BASELINE
- Age calculation
- Stratification factors from eCRF
- Medical history, disease characteristics
- Gene screening, viral testing

### Section 7: MEDICATIONS AND TREATMENTS
- Prior/concomitant medication definitions
- Medication date imputation rules (FULL DETAILS)
- Dose intensity calculations
- Carboplatin dose adjustments

### Section 8: EFFICACY ANALYSIS
- Primary endpoint (ORR, BOR, RECIST 1.1)
- ORR definition (responder = CR or PR confirmed)
- Similarity criterion (-12.5, 12.5)
- Primary analysis method (logistic regression, covariates)
- Delta method formulas
- Central vs local review
- Sensitivity analyses
- Time-to-event definitions (Response Duration, TTP, PFS, OS)
- Kaplan-Meier method
- Cox regression model
- Censoring rules (ALL scenarios)
- Censoring for incomplete new anticancer therapy dates (Section 8.2.2.5 - FULL DETAIL)
- Time conversion (30.4 days)
- Salvage treatment

### Section 9: PHARMACOKINETIC ANALYSIS
- PK populations
- Serum concentration handling (LLOQ)
- Ctrough definition (pre-dose concentration of next dose)
- PK parameter exclusions (post-dose, EOT <18 days, duplicates)

### Section 10: SAFETY ANALYSIS
- AE definition
- TEAE definition
- AE coding (MedDRA version)
- AE grading (CTCAE version)
- AE relationship (possible, probable, definite)
- AE counting rule (worst severity)
- AE date imputation (START and STOP - FULL DETAILS)
- SAE definition
- TEAEs leading to discontinuation
- TEAEs leading to death
- AESI FULL LIST (Hypersensitivity/IRR, GI perforations, wound healing, hypertension, PRES, proteinuria, ATE, VTE, hemorrhages, CHF, ovarian failure)
- Lab data (unit conversion, CTCAE grading, shift tables)
- Vital signs, weight, BSA
- ECG analysis
- Hypersensitivity monitoring
- Physical examination
- ECOG performance status
- Immunogenicity (ADA assay, tiered approach, transformations)

### Section 11: QUALITY OF LIFE
- QoL instruments (EORTC QLQ-C30, QLQ-LC13)
- Scoring formulas (Raw Score, Functional, Symptom)
- Missing items handling

### Section 14: APPENDICES
- Date imputation rules (Medication, AE, Death - FULL DETAILS)
- BOR confirmation rules (4 weeks CR/PR, 6 weeks SD)
- CTCAE terms and grades

## CRITICAL MISSING ITEMS - MUST EXTRACT:

### Section 4:
- General Comments eCRF page statement

### Section 6 Demographics:
- Demographics table content (sex, age, race, ethnicity will be summarized)
- Gene Screening (EGFR mutation, ALK rearrangement)
- Hepatitis B/C and HIV testing (HBsAg, HBsAb, HBcAb, HCV, HIV 1&2, HBV DNA)
- Viral serology summarization rules
- Disease Characteristic (disease status, pathological diagnosis, histologic grade, clinical stage, TNM stage)

### Section 7:
- ATC classification for medications
- Medication coding (WHO-DD)

### Section 8:
- Reason for Censoring tables (ALL censoring reasons and dates)
- Effusion drainage listing

### Section 10:
- Lab data shift tables rules
- Clinically notable vital sign criteria (systolic BP ≤90/≥160, diastolic ≤50/≥90, heart rate ≤50/≥100, etc.)
- ECG section (12-lead ECG, will be performed, will be listed)
- Physical Examination (Normal, Abnormal not clinically significant, Abnormal clinically significant, shift table)
- Pregnancy Test (urine and serum, Positive/Negative/Equivocal)
- ADA/NAb titer values and transformations

### Section 14:
- SMQ terms for each AESI category
- PT terms for AESI

### Other:
- Visit windows (days)
- ALL "will be listed" statements
- ALL "will be summarized" statements
- Point estimate statements
- ALL listings by treatment group statements

## EXTRACTION RULES:
1. Extract EXACT TEXT (word-for-word quotes)
2. One entry per distinct statement/rule/definition/specification
3. DO NOT skip or summarize ANYTHING
4. Include section reference for each statement
5. Target 500+ statements (document has ~600 sentences)
6. Extract EVERY "will be" statement
7. Extract EVERY "is defined as" statement
8. Extract EVERY table/listing/figure presentation rule
9. Extract EVERY population definition
10. Extract EVERY analysis method
11. Extract EVERY time point/schedule specification
12. Extract EVERY threshold/criteria
13. Extract EVERY eCRF reference
14. Extract EVERY coding/classification rule

DO NOT STOP until you have extracted the ENTIRE document.

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

Extract ALL statements from ALL sections. Do not summarize or skip any.
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
        pass  # Keep cache for reuse


def test_prompt(prompt_name: str = "objectives_endpoints", output_name: str = None):
    """Test a prompt against the NCT03676192 documents using persistent Original SAP cache."""
    from src.llm_client import evaluate_sap_with_persistent_cache

    output_name = output_name or prompt_name

    print("=" * 60)
    print(f"TESTING PROMPT: {prompt_name}")
    print(f"OUTPUT NAME: {output_name}")
    print("=" * 60)

    # Load documents (Generated SAP + Protocol only, Original SAP is in persistent cache)
    print("\n1. Loading documents...")
    docs = load_documents()

    # Load prompt
    print(f"\n2. Loading prompt: {prompt_name}.txt...")
    prompt = load_prompt(prompt_name)
    print(f"   Prompt length: {len(prompt):,} chars")

    # Determine output format based on prompt name
    is_markdown_prompt = prompt_name in MARKDOWN_PROMPTS
    output_format = "markdown" if is_markdown_prompt else "json"

    # Run evaluation using persistent Original SAP cache
    print(f"\n3. Running evaluation with persistent Original SAP cache (format: {output_format})...")
    try:
        result = evaluate_sap_with_persistent_cache(
            generated_sap=docs["generated_sap"],
            protocol=docs["protocol"],
            instruction=prompt,
            output_format=output_format
        )

        results_dir = Path("results/NCT03676192")
        results_dir.mkdir(parents=True, exist_ok=True)

        if is_markdown_prompt:
            # Markdown prompt: save raw markdown directly, no JSON
            print("\n4. RESULT (markdown):")
            print("=" * 60)
            print(result)

            md_output_path = results_dir / f"{output_name}.md"
            md_output_path.write_text(result)
            print(f"\n✓ Markdown saved to: {md_output_path}")
        else:
            # JSON prompt: existing behavior
            result = validate_contradictions(result)

            print("\n4. RESULT:")
            print("=" * 60)
            print(json.dumps(result, indent=2))

            output_path = results_dir / f"{output_name}.json"
            output_path.write_text(json.dumps(result, indent=2))
            print(f"\n✓ JSON saved to: {output_path}")

            markdown_content = json_to_markdown(result, output_name)
            md_output_path = results_dir / f"{output_name}.md"
            md_output_path.write_text(markdown_content)
            print(f"✓ Markdown saved to: {md_output_path}")

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        raise

    print("\n5. Done! Persistent cache preserved for future evaluations.")
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "extract":
        # Run extraction: python -m src.test_prompt extract general_methodology
        section = sys.argv[2] if len(sys.argv) > 2 else "general_methodology"
        force = "--force" in sys.argv
        extract_statements("NCT03676192", section, force=force)
    else:
        # Run evaluation: python -m src.test_prompt general_methodology [output_name]
        prompt_name = sys.argv[1] if len(sys.argv) > 1 else "objectives_endpoints"
        output_name = sys.argv[2] if len(sys.argv) > 2 else None
        test_prompt(prompt_name, output_name=output_name)
