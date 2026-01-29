## Analysis Populations Evaluation

**Section:** analysis_populations
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **populations found:** Intent-to-Treat (ITT) Population, Per-Protocol (PP) Population, Pharmacokinetic (PK) Population, Pharmacokinetic Population – Maintenance Period Subset, Safety Population
- **components per population:** Intent-to-Treat (ITT) Population: 3, Per-Protocol (PP) Population: 3, Pharmacokinetic (PK) Population: 3, Pharmacokinetic Population – Maintenance Period Subset: 3, Safety Population: 3, General: 1
- **total components extracted:** 16
- **components in evaluation table:** 12
- **components in missing from generated SAP:** 4
- **counts match:** True

---

### Evaluation Table (12 items)

#### 1. Intent-to-Treat (ITT) Population - Name

- **evaluation type:** exact_match
- **original SAP text:** Intent-to-Treat (ITT) Population
- **generated SAP text:** Intent-to-treat (ITT) Population
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP says 'Intent-to-Treat (ITT) Population', 2) Generated SAP says 'Intent-to-treat (ITT) Population', 3) Comparison: match (case difference only), 4) Conclusion: Correct

#### 2. Intent-to-Treat (ITT) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The ITT population will consist of all randomized patients who are randomly assigned to study drug regardless of whether or not any study treatment dosing is completed and successfully screened based on the ‘Screening Pass/Fail’ eCRF page. ... The primary population for the primary efficacy analysis will be the ITT population.
- **generated SAP text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** successfully screened based on the ‘Screening Pass/Fail’ eCRF page; The primary population for the primary efficacy analysis will be the ITT population
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP includes specific criteria 'successfully screened based on the ‘Screening Pass/Fail’ eCRF page' and usage statement. 2) Generated SAP omits these details. 3) Comparison: Less detailed. 4) Impact: Low, as randomized patients are typically screened successfully, but specificity is lost. 5) Conclusion: Acceptable

#### 3. Intent-to-Treat (ITT) Population - Treatment Assignment

- **evaluation type:** exact_match
- **original SAP text:** Patients will be assigned to treatment groups based on randomization.
- **generated SAP text:** Patients will be assigned to treatment groups based on randomization.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP says 'Patients will be assigned to treatment groups based on randomization.', 2) Generated SAP says 'Patients will be assigned to treatment groups based on randomization.', 3) Comparison: Match, 4) Conclusion: Correct

#### 4. Per-Protocol (PP) Population - Name

- **evaluation type:** exact_match
- **original SAP text:** Per-Protocol (PP) Population
- **generated SAP text:** Per-Protocol (PP) Population
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP says 'Per-Protocol (PP) Population', 2) Generated SAP says 'Per-Protocol (PP) Population', 3) Comparison: Match, 4) Conclusion: Correct

#### 5. Per-Protocol (PP) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The PP population will consist of all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviations that may affect the interpretation of the primary endpoint. A patient will be considered as receiving full dose if the planned dose is recorded as ‘15mg/kg’ and the action taken is recorded as ‘Dose Not Changed’ on ‘Study Treatment Administration’ eCRF page. Final determination of the PP population was made at the Data Review Meeting (DRM) before unblinding. ... A supportive efficacy analysis will be repeated using the PP population.
- **generated SAP text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviation. A major protocol deviation is one that may affect the interpretation of the primary endpoint and it will be defined in the statistical analysis plan (SAP). Final determinations of the PP population will be made at the blinded data review meeting before unblinding.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific definition of full dose (15mg/kg, Dose Not Changed on eCRF); Usage statement (supportive efficacy analysis)
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP defines 'full dose' with specific eCRF criteria. 2) Generated SAP omits this operational definition. 3) Generated SAP also includes a self-referential statement 'will be defined in the SAP' (copied from Protocol) instead of referencing the definition within the SAP. 4) Comparison: Less detailed. 5) Conclusion: Acceptable

#### 6. Per-Protocol (PP) Population - Treatment Assignment

- **evaluation type:** exact_match
- **original SAP text:** Patients will be assigned to treatment groups based on randomization.
- **generated SAP text:** Patients will be assigned to treatment groups based on randomization.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP says 'Patients will be assigned to treatment groups based on randomization.', 2) Generated SAP says 'Patients will be assigned to treatment groups based on randomization.', 3) Comparison: Match, 4) Conclusion: Correct

#### 7. Pharmacokinetic (PK) Population - Name

- **evaluation type:** exact_match
- **original SAP text:** Pharmacokinetic Population
- **generated SAP text:** PK Population
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP says 'Pharmacokinetic Population', 2) Generated SAP says 'PK Population', 3) Comparison: Match (abbreviation used), 4) Conclusion: Correct

#### 8. Pharmacokinetic (PK) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The PK population will consist of all randomly assigned patients who receive at least one full dose (as defined in Section 4.4.2) of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result. Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population. If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not.
- **generated SAP text:** The PK population is defined as all patients who receive at least one full dose of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result. If any patients are found to be non-compliant with respect to dosing, a decision will be made on a case-by-case basis at the blinded data review meeting before unblinding.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population
- **omission impact:** potential
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly excludes patients receiving incorrect treatment. 2) Generated SAP omits this specific exclusion criterion. 3) Comparison: Less detailed. 4) Impact: Potential, as incorrect treatment handling is not specified. 5) Conclusion: Acceptable

#### 9. Pharmacokinetic (PK) Population - Treatment Assignment

- **evaluation type:** semantic
- **original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received during the Induction Study Period.
- **generated SAP text:** Patients will be assigned to treatment groups based on treatment actually received.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** during the Induction Study Period
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP specifies assignment based on treatment received 'during the Induction Study Period'. 2) Generated SAP says 'based on treatment actually received'. 3) Comparison: Less detailed. 4) Conclusion: Acceptable

#### 10. Safety Population - Name

- **evaluation type:** exact_match
- **original SAP text:** Safety Population
- **generated SAP text:** Safety Population
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP says 'Safety Population', 2) Generated SAP says 'Safety Population', 3) Comparison: Match, 4) Conclusion: Correct

#### 11. Safety Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The safety population will consist of all randomly assigned patients who receive at least one dose (partial or full) of study drug (CT-P16 or EU-Approved Avastin). A patient will be considered to have received study drug if the patient is recorded as having study drug administered on the ‘Study Treatment Administration’ eCRF page.
- **generated SAP text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug (CT-P16 or EU-Approved Avastin).
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** A patient will be considered to have received study drug if the patient is recorded as having study drug administered on the ‘Study Treatment Administration’ eCRF page.
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP includes operational definition referencing eCRF page. 2) Generated SAP omits this. 3) Comparison: Less detailed. 4) Conclusion: Acceptable

#### 12. Safety Population - Treatment Assignment

- **evaluation type:** semantic
- **original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received. Treatment patients actually received will be based on the kit number recorded on the ‘Study Treatment Administration’ eCRF page. Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group. All other patients will be analyzed under the EU-Approved Avastin treatment group.
- **generated SAP text:** Patients will be assigned to treatment groups based on treatment actually received.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Treatment patients actually received will be based on the kit number recorded on the ‘Study Treatment Administration’ eCRF page. Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group. All other patients will be analyzed under the EU-Approved Avastin treatment group.
- **omission impact:** potential
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP provides specific logic for mixed treatment cases (at least one CT-P16 = CT-P16 group). 2) Generated SAP omits this logic and is generic. 3) Comparison: Less detailed. 4) Impact: Potential, as handling of mixed treatment is not specified. 5) Conclusion: Acceptable

---

### Issues Found (0 items)

*No issues found.*

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (4 items)

#### 1. Pharmacokinetic Population – Maintenance Period Subset

- **content type:** entire_population
- **original SAP text:** The PK population – Maintenance Period Subset will consist of all patients in PK population who received at least 1 dose (full) of either of the study drugs and have at least one post treatment PK result during the Maintenance Study Period. Patients who received incorrect treatment during the Maintenance Study Period will be excluded from the PK population – Maintenance Period Subset. If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not. Patients will be assigned to treatment groups based on treatment they actually received.
- **protocol text:** Searched Section 7.4 Analysis Sets - not found
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Entire population defined in Original SAP is missing from Generated SAP.
- **reasoning:** Chain-of-thought: 1) Original SAP defines this subset. 2) Protocol does not define this subset. 3) Absence is acceptable as it is not required by Protocol. 4) Impact: Analysis of maintenance PK may be affected.

#### 2. General Tabulation

- **content type:** general_instruction
- **original SAP text:** The number of patients in each population will be tabulated by treatment group for the ITT population. A listing will also be provided displaying this data.
- **protocol text:** Searched Section 7.4 Analysis Sets - not found
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Instruction to tabulate population counts is missing.
- **reasoning:** Chain-of-thought: 1) Original SAP includes this instruction. 2) Protocol does not require it. 3) Absence is acceptable.

#### 3. Intent-to-Treat (ITT) Population - Usage

- **content type:** usage_statement
- **original SAP text:** The primary population for the primary efficacy analysis will be the ITT population.
- **protocol text:** Searched Section 7.4 Analysis Sets - not found
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Statement defining ITT as primary efficacy population is missing from definition block.
- **reasoning:** Chain-of-thought: 1) Original SAP includes this usage statement in definition. 2) Generated SAP omits it here (though implies it in efficacy section). 3) Absence from definition block is acceptable.

#### 4. Per-Protocol (PP) Population - Usage

- **content type:** usage_statement
- **original SAP text:** A supportive efficacy analysis will be repeated using the PP population.
- **protocol text:** Searched Section 7.4 Analysis Sets - not found
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Statement defining PP as supportive efficacy population is missing from definition block.
- **reasoning:** Chain-of-thought: 1) Original SAP includes this usage statement in definition. 2) Generated SAP omits it here. 3) Absence from definition block is acceptable.

---

### Reasoning

Step-by-step chain-of-thought reasoning trace: 1) Found ITT, PP, PK, and Safety populations in Protocol. 2) Found ITT, PP, PK, PK Maintenance Subset, and Safety populations in Original SAP. 3) Found ITT, PP, PK, and Safety populations in Generated SAP. 4) Compared content: Generated SAP definitions are consistently less detailed than Original SAP, omitting specific operational criteria (e.g., 'successfully screened', 'full dose' eCRF checks, specific assignment logic for mixed treatments). 5) Checked existence: The 'PK Maintenance Subset' found in Original SAP is missing in Generated SAP, but confirmed as NOT required by Protocol, so this is acceptable. 6) The Generated SAP text appears to be copied from the Protocol rather than the Original SAP, leading to the loss of SAP-specific details. 7) Rating DECENT because all required populations are present and definitions are fundamentally correct, despite the loss of operational detail.

---

### Summary

The Generated SAP includes all Protocol-required analysis populations (ITT, PP, PK, Safety). However, the definitions are less detailed than the Original SAP, omitting specific operational criteria for inclusion (e.g., 'successfully screened', 'full dose' definitions) and treatment assignment logic (e.g., handling of mixed treatment exposure). The 'PK Population – Maintenance Period Subset' defined in the Original SAP is absent, but this is acceptable as it is not required by the Protocol.