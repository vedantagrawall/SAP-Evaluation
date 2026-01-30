## Analysis Populations Evaluation

**Section:** analysis_populations
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **populations found:** Intent-to-Treat (ITT) Population, Per-Protocol (PP) Population, Pharmacokinetic (PK) Population, Pharmacokinetic Population – Maintenance Period Subset, Safety Population
- **components per population:** Intent-to-Treat (ITT) Population: 1, Per-Protocol (PP) Population: 1, Pharmacokinetic (PK) Population: 1, Pharmacokinetic Population – Maintenance Period Subset: 1, Safety Population: 1
- **total components extracted:** 5
- **components in evaluation table:** 4
- **components in missing from generated SAP:** 1
- **counts match:** True

---

### Evaluation Table (4 items)

#### 1. Intent-to-Treat (ITT) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The ITT population will consist of all randomized patients who are randomly assigned to study drug regardless of whether or not any study treatment dosing is completed and successfully screened based on the ‘Screening Pass/Fail’ eCRF page. Patients will be assigned to treatment groups based on randomization. The primary population for the primary efficacy analysis will be the ITT population.
- **generated SAP text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed. Patients will be assigned to treatment groups based on randomization.
- **protocol text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed. Patients will be assigned to treatment groups based on randomization.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** and successfully screened based on the ‘Screening Pass/Fail’ eCRF page
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP includes specific criteria about successful screening based on a specific eCRF page. 2) Generated SAP omits this specific screening criterion. 3) Comparison: Less detailed. 4) Impact: Low, as randomization typically implies screening success in IWRS, but the specific data check is lost. 5) Conclusion: Acceptable as core definition is preserved.

#### 2. Per-Protocol (PP) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The PP population will consist of all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviations that may affect the interpretation of the primary endpoint. A patient will be considered as receiving full dose if the planned dose is recorded as ‘15mg/kg’ and the action taken is recorded as ‘Dose Not Changed’ on ‘Study Treatment Administration’ eCRF page. Final determination of the PP population was made at the Data Review Meeting (DRM) before unblinding. Patients will be assigned to treatment groups based on randomization. A supportive efficacy analysis will be repeated using the PP population.
- **generated SAP text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviation. A major protocol deviation is one that may affect the interpretation of the primary endpoint and it will be defined in the statistical analysis plan (SAP). Final determinations of the PP population will be made at the blinded data review meeting before unblinding. Patients will be assigned to treatment groups based on randomization.
- **protocol text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviation. A major protocol deviation is one that may affect the interpretation of the primary endpoint and it will be defined in the SAP.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific definition of 'full dose' (15mg/kg, Dose Not Changed on eCRF)
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction
- **severity:** minor
- **reasoning:** Chain-of-thought: 1) Original SAP defines 'full dose' explicitly with eCRF fields and values. 2) Generated SAP omits this definition entirely. 3) Generated SAP contains a circular reference ('defined in the SAP'). 4) Comparison: Less detailed and circular. 5) Impact: Potential ambiguity on what constitutes a full dose. 6) Conclusion: Problem due to circular reference and missing operational definition.

#### 3. Pharmacokinetic (PK) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The PK population will consist of all randomly assigned patients who receive at least one full dose (as defined in Section 4.4.2) of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result. Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population. If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not. Patients will be assigned to treatment groups based on treatment they actually received during the Induction Study Period.
- **generated SAP text:** The PK population is defined as all patients who receive at least one full dose of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result. If any patients are found to be non-compliant with respect to dosing, a decision will be made on a case-by-case basis at the blinded data review meeting before unblinding. Patients will be assigned to treatment groups based on treatment actually received.
- **protocol text:** The PK population is defined as all patients who receive at least one full dose of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result. If any patients are found to be non-compliant with respect to dosing, a decision will be made on a case-by-case basis at the blinded data review meeting before unblinding. Patients will be assigned to treatment groups based on treatment actually received.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Exclusion of patients who received incorrect treatment; specific reference to Induction Study Period for assignment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly excludes patients with incorrect treatment. 2) Generated SAP omits this specific exclusion. 3) Comparison: Less detailed. 4) Impact: Low, as 'treatment actually received' usually covers this, but the explicit exclusion is helpful. 5) Conclusion: Acceptable.

#### 4. Safety Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The safety population will consist of all randomly assigned patients who receive at least one dose (partial or full) of study drug (CT-P16 or EU-Approved Avastin). A patient will be considered to have received study drug if the patient is recorded as having study drug administered on the ‘Study Treatment Administration’ eCRF page. Patients will be assigned to treatment groups based on treatment they actually received. Treatment patients actually received will be based on the kit number recorded on the ‘Study Treatment Administration’ eCRF page. Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group. All other patients will be analyzed under the EU-Approved Avastin treatment group.
- **generated SAP text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug (CT-P16 or EU-Approved Avastin). Patients will be assigned to treatment groups based on treatment actually received.
- **protocol text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug (CT-P16 or EU-Approved Avastin). Patients will be assigned to treatment groups based on treatment actually received.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Operational details: eCRF page references, kit number usage, and specific rule for mixed treatments (at least one dose of CT-P16 -> CT-P16 group)
- **omission impact:** potential
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP provides detailed logic for handling mixed treatments (patients receiving both drugs). 2) Generated SAP omits this logic. 3) Comparison: Less detailed. 4) Impact: Potential ambiguity for patients who switch treatments, but the core definition matches. 5) Conclusion: Acceptable, though Original SAP is much more precise.

---

### Issues Found (1 items)

#### 1. Per-Protocol (PP) Population - Definition

- **issue type:** contradiction
- **severity:** minor
- **original SAP text:** A major protocol deviation is one that may affect the interpretation of primary endpoint or the patient’s rights, safety or welfare... Major protocol deviations include the following: [list]
- **generated SAP text:** A major protocol deviation is one that may affect the interpretation of the primary endpoint and it will be defined in the statistical analysis plan (SAP).
- **protocol text:** A major protocol deviation is one that may affect the interpretation of primary endpoint and it will be defined in the SAP.
- **why they conflict:** The Generated SAP IS the SAP, yet it defers the definition of major protocol deviations to 'the SAP', creating a circular reference.
- **description:** Circular reference: Generated SAP defers definition to itself.
- **reasoning:** Chain-of-thought: 1) The Generated SAP contains the text 'it will be defined in the statistical analysis plan (SAP)'. 2) Since this document IS the SAP, this statement provides no definition. 3) Original SAP provides the actual definition/list. 4) Severity: Minor, as it's a drafting error likely copied from Protocol, but it leaves the term undefined.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (1 items)

#### 1. Pharmacokinetic Population – Maintenance Period Subset

- **content type:** entire_population
- **original SAP text:** The PK population – Maintenance Period Subset will consist of all patients in PK population who received at least 1 dose (full) of either of the study drugs and have at least one post treatment PK result during the Maintenance Study Period. Patients who received incorrect treatment during the Maintenance Study Period will be excluded from the PK population – Maintenance Period Subset. If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not. Patients will be assigned to treatment groups based on treatment they actually received.
- **protocol text:** Searched Protocol Section 7.4 - not found. Protocol 7.6.3 mentions analysis of Ctrough during Maintenance, but no specific population subset is defined in 7.4.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Entire population subset defined in Original SAP is missing from Generated SAP.
- **reasoning:** Chain-of-thought: 1) Original SAP defines a specific subset for Maintenance PK analysis. 2) Protocol Section 7.4 does not list this subset, though analysis is required. 3) Classification: Acceptable difference as it's not explicitly required by Protocol Section 7.4, though it represents missing content from Original SAP.

---

### Reasoning

Step-by-step chain-of-thought reasoning trace: 1) Found ITT, PP, PK, Safety populations in Protocol. 2) Found ITT, PP, PK, PK Maintenance, Safety populations in Original SAP. 3) Found ITT, PP, PK, Safety populations in Generated SAP. 4) Compared content: Generated SAP definitions are largely verbatim copies of the Protocol text, whereas Original SAP contains significant operational details (eCRF references, specific dose definitions, mixed treatment handling). 5) Checked existence: PK Maintenance Subset is missing from Generated SAP; checked Protocol and it is not explicitly defined in Section 7.4, so this omission is acceptable. 6) Identified issue: PP definition in Generated SAP contains a circular reference ('defined in the SAP'), likely copied from Protocol. 7) Rating: DECENT because all required populations are present and definitions are consistent with Protocol, despite missing the operational precision of the Original SAP.

---

### Summary

The Generated SAP includes all Protocol-required analysis populations. However, it lacks the specific operational details found in the Original SAP (such as eCRF page references and specific dose definitions) and contains a circular reference in the Per-Protocol definition where it defers criteria to 'the SAP' instead of defining them.