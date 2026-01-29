# Output Format Comparison: JSON vs Markdown

## Markdown Output Structure

```markdown
## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Evaluation Summary Table

| Component | Evaluation Type | Matches Original SAP | Protocol Consulted | Result | Issue Type | Severity |
|-----------|-----------------|---------------------|-------------------|--------|------------|----------|
| Continuous data summary stats | semantic | yes |  | correct | none | none |
| EOT visit handling | semantic | no |  | problem | contradiction_original | minor |
| ITT Definition | semantic | no |  | correct | none | none |
... (items where Generated SAP has content)

---

### Issues Found

| Issue Type | Component | Description |
|------------|-----------|-------------|
| contradiction_original | EOT visit handling | Original SAP explicitly excludes EOT... |
| contradiction_original | Unscheduled visit handling | Original SAP strictly excludes... |

---

### Extra Information Flagged

*No extra information flagged.*

---

### ✅ Acceptable Differences (N items)
Content in Original SAP only (not in Protocol) - acceptable to omit.

| Component | Category | Original SAP Text |
|-----------|----------|-------------------|
| Min/Max decimal precision | decimal_precision_minmax | same number of decimal places... |
| Mean decimal precision | decimal_precision_mean | one more decimal place... |
| COVID-19 PD analysis | protocol_deviation_definition | excluding patients with major... |
...

---

### ❌ Missing Required Content (N items)
Content in both Original SAP AND Protocol - should be in Generated SAP.

| Component | Category | Original SAP Text | Protocol Text |
|-----------|----------|-------------------|---------------|
| Sample size per group | sample_size_calculation | 305 patients per group | sample size of 305 patients... |
| Equivalence margin | sample_size_calculation | equivalence margin of -12.5... | equivalence margin of (±12.5) |
| Stratification factor 1 | stratification_factors | country | country |
...

---

### Reasoning
Step-by-step reasoning trace...

---

### Summary
2-3 sentence overall assessment...
```

---

## JSON vs Markdown Comparison

| Aspect | JSON | Markdown |
|--------|------|----------|
| **evaluation_table** | Full object with 15 fields per item (original_sap_text, generated_sap_text, protocol_text, core_meanings, reasoning, etc.) | Simplified table with 7 columns |
| **missing_information** | Single array with `in_protocol` field | **Split into 2 sections**: ✅ Acceptable (in_protocol: no) and ❌ Missing Required (in_protocol: yes) |
| **issues** | Detailed object with core_meanings, reasoning | Condensed to 3 columns |
| **extraction_validation** | Full counts, categories_found, sections_read | Not shown |
| **discovery_summary** | Sections identified in each document | Not shown |
| **internal_contradictions** | Full array | Not shown (empty in this case) |

---

## Missing Information Logic

The key feature is how `missing_information` is split based on Protocol check:

```
1. Model finds content in Original SAP that's missing from Generated SAP
2. Model checks: "Is this content ALSO in Protocol?"
3. Records in_protocol: "yes" or "no"
4. This determines classification:

   in_protocol: "no"  → ✅ Acceptable Differences
   └─ Content exists ONLY in Original SAP (not in Protocol)
   └─ Acceptable for Generated SAP to omit (Original had extra operational detail)

   in_protocol: "yes" → ❌ Missing Required Content
   └─ Content exists in BOTH Original SAP AND Protocol
   └─ Generated SAP should have included this (Protocol is source of truth)
```

**Important**: This classification is for INFORMATIONAL purposes only. Missing information NEVER affects the rating - only contradictions do.

---

## JSON Structure (Full)

```json
{
  "section": "general_methodology",
  "rating": "GREAT | DECENT | POOR",
  "status": "pass | pass_with_notes | fail",

  "extraction_validation": {
    "sections_read": ["4", "4.1", "4.2"],
    "elements_per_section": {"4": 24, "4.1": 0},
    "categories_found": {
      "software_version": true,
      "decimal_precision_mean": true
    },
    "paragraphs_processed": 65,
    "elements_extracted": 65,
    "elements_in_evaluation_table": 14,
    "elements_in_missing_information": 51,
    "missing_required_count": 16,
    "acceptable_difference_count": 31,
    "counts_match": true
  },

  "discovery_summary": {
    "original_sap": {
      "sections_identified": ["4. General Statistical Considerations"],
      "elements_extracted": 65
    },
    "generated_sap": {
      "sections_identified": ["3.3 Analysis Populations"],
      "elements_extracted": 14
    }
  },

  "evaluation_table": [
    {
      "component": "short description",
      "category": "category from checklist",
      "evaluation_type": "semantic | exact_match",
      "original_sap_text": "short quote max 50 chars...",
      "original_core_meaning": "INCLUDE | EXCLUDE | REQUIRED | etc.",
      "generated_sap_text": "short quote max 50 chars (MUST NOT BE NULL)",
      "generated_core_meaning": "INCLUDE | EXCLUDE | REQUIRED | etc.",
      "protocol_text": "quote if consulted, else null",
      "matches_original_sap": "yes | no",
      "matches_protocol": "yes | no | not_checked",
      "result": "correct | problem",
      "issue_type": "none | contradiction_original | contradiction_protocol",
      "severity": "none | minor | critical",
      "reasoning": "brief explanation"
    }
  ],

  "missing_information": [
    {
      "component": "short description (max 20 chars)",
      "category": "category from checklist",
      "original_sap_text": "short quote max 30 chars...",
      "protocol_text": "max 30 chars if found, null if not",
      "in_protocol": "yes | no",
      "classification": "missing_required | acceptable_difference"
    }
  ],

  "internal_contradictions": [],
  "extra_information_flagged": [],

  "issues": [
    {
      "issue_type": "contradiction_original | contradiction_protocol",
      "severity": "minor | critical",
      "component": "short description",
      "original_sap_text": "short quote...",
      "original_core_meaning": "the core instruction",
      "generated_sap_text": "short quote (MUST NOT BE NULL)...",
      "generated_core_meaning": "the core instruction",
      "protocol_text": "short quote if relevant...",
      "description": "explanation of the conflict",
      "reasoning": "why this is a true contradiction"
    }
  ],

  "reasoning": "Step-by-step reasoning trace",
  "summary": "2-3 sentence overall assessment"
}
```
