## Analysis Populations Evaluation

**Section:** analysis_populations
**Rating:** DECENT
**Status:** pass_with_notes

---

### Critical Components (3 per Population)

These are the MUST match items for each population.

| Population | Name | Definition | Treatment Assignment |
|------------|------|------------|---------------------|
| Intent-to-Treat (ITT) Population | ✓ | ✓ | ✓ |
| Per-Protocol (PP) Population | ✓ | ✓ | ✓ |
| Pharmacokinetic (PK) Population | ✓ | ✓ | ✓ |
| Safety Population | ✓ | ✓ | ✓ |

---

### What Was Omitted (Definition & Treatment Assignment)

Exact quotes of content in Original SAP that is missing from Generated SAP.

| Component | Omitted Content | Result |
|-----------|-----------------|--------|
| Intent-to-Treat (ITT) Population - Definition | and successfully screened based on the ‘Screening Pass/Fail’ eCRF page | acceptable |
| Per-Protocol (PP) Population - Definition | A patient will be considered as receiving full dose if the planned dose is recorded as ‘15mg/kg’ and the action taken is recorded as ‘Dose Not Changed’ on ‘Study Treatment Administration’ eCRF page. | acceptable |
| Pharmacokinetic (PK) Population - Definition | Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population. | acceptable |
| Pharmacokinetic (PK) Population - Treatment Assignment | during the Induction Study Period | acceptable |
| Safety Population - Treatment Assignment | Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group. All other patients will be analyzed under the EU-Approved Avastin treatment group. | acceptable |

---

### Issues Found

*No issues found.*

---

### ❌ Missing Required Content (0 items)

Content in both Original SAP AND Protocol - should be in Generated SAP.

*None - all required content is present.*

---

### Granular Details (Definition Sub-components)

<details>
<summary>Click to expand detailed breakdown</summary>

*No granular details.*

</details>

---

### Summary

The Generated SAP includes all Protocol-required analysis populations (ITT, PP, PK, Safety). It omits the 'PK Population – Maintenance Period Subset' found in the Original SAP, which is acceptable as it is not explicitly defined in the Protocol. The definitions in the Generated SAP are less detailed than the Original SAP, missing specific operational criteria such as the 'successfully screened' requirement for ITT and the hierarchy rule for mixed treatments in the Safety population.