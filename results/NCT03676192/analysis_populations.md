## Analysis Populations Evaluation

**Section:** analysis_populations
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **populations found:** Intent-to-treat (ITT) Population, Per-Protocol (PP) Population, PK Population, Safety Population
- **components per population:** Intent-to-treat (ITT) Population: 3, Per-Protocol (PP) Population: 3, PK Population: 3, Safety Population: 2
- **total components extracted:** 12
- **components in evaluation table:** 11
- **components in missing from generated SAP:** 1
- **counts match:** True

---

### Evaluation Table (11 items)

#### 1. Intent-to-treat (ITT) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The ITT population will consist of all randomized patients who are randomly assigned to study drug regardless of whether or not any study treatment dosing is completed and successfully screened based on the ‘Screening Pass/Fail’ eCRF page.
- **generated SAP text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **protocol text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** and successfully screened based on the ‘Screening Pass/Fail’ eCRF page
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction
- **severity:** minor
- **reasoning:** Chain-of-thought: 1) Original SAP includes 'successfully screened' as an inclusion criterion. 2) Generated SAP omits this criterion. 3) Comparison: Contradiction/Different Meaning. 4) Omitted 'successfully screened', impact: Potential (Original SAP restricts ITT to screened patients, Generated SAP includes all randomized). 5) Conclusion: Problem.

#### 2. Intent-to-treat (ITT) Population - Treatment Assignment

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
- **reasoning:** Chain-of-thought: 1) Original SAP specifies assignment based on randomization. 2) Generated SAP specifies assignment based on randomization. 3) Comparison: Match. 5) Conclusion: Correct.

#### 3. Intent-to-treat (ITT) Population - Usage

- **evaluation type:** semantic
- **original SAP text:** The primary population for the primary efficacy analysis will be the ITT population.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Statement that ITT is primary population for primary efficacy analysis
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly states ITT is for primary efficacy. 2) Generated SAP omits this statement in the definition block (though it is implied in efficacy sections). 3) Comparison: Less detailed. 4) Omitted usage statement, impact: None (covered elsewhere). 5) Conclusion: Acceptable.

#### 4. Per-Protocol (PP) Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The PP population will consist of all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviations that may affect the interpretation of the primary endpoint. A patient will be considered as receiving full dose if the planned dose is recorded as ‘15mg/kg’ and the action taken is recorded as ‘Dose Not Changed’ on ‘Study Treatment Administration’ eCRF page. Final determination of the PP population was made at the Data Review Meeting (DRM) before unblinding.
- **generated SAP text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviation. A major protocol deviation is one that may affect the interpretation of the primary endpoint and it will be defined in the statistical analysis plan (SAP). Final determinations of the PP population will be made at the blinded data review meeting before unblinding.
- **protocol text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug (CT-P16 or EU-Approved Avastin) in the Induction Study Period and who do not have any major protocol deviation. A major protocol deviation is one that may affect the interpretation of the primary endpoint and it will be defined in the statistical analysis plan (SAP).
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Definition of 'full dose' (15mg/kg, Dose Not Changed)
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction
- **severity:** minor
- **reasoning:** Chain-of-thought: 1) Original SAP defines 'full dose' criteria. 2) Generated SAP omits this definition and includes self-referential text ('will be defined in the SAP') copied from Protocol. 3) Comparison: Less detailed/Incomplete. 4) Omitted full dose definition, impact: Potential (ambiguity on what constitutes full dose). 5) Conclusion: Problem.

#### 5. Per-Protocol (PP) Population - Treatment Assignment

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
- **reasoning:** Chain-of-thought: 1) Original SAP specifies assignment based on randomization. 2) Generated SAP specifies assignment based on randomization. 3) Comparison: Match. 5) Conclusion: Correct.

#### 6. Per-Protocol (PP) Population - Usage

- **evaluation type:** semantic
- **original SAP text:** A supportive efficacy analysis will be repeated using the PP population.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Statement regarding supportive efficacy analysis
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP states PP is for supportive analysis. 2) Generated SAP omits this in definition block. 3) Comparison: Less detailed. 4) Omitted usage statement, impact: None. 5) Conclusion: Acceptable.

#### 7. PK Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The PK population will consist of all randomly assigned patients who receive at least one full dose (as defined in Section 4.4.2) of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result. Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population. If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not.
- **generated SAP text:** The PK population is defined as all patients who receive at least one full dose of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result. If any patients are found to be non-compliant with respect to dosing, a decision will be made on a case-by-case basis at the blinded data review meeting before unblinding.
- **protocol text:** The PK population is defined as all patients who receive at least one full dose of study drug (CT-P16 or EU-Approved Avastin) and who have at least one post treatment PK result.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population.
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction
- **severity:** minor
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly excludes patients who received incorrect treatment. 2) Generated SAP omits this exclusion and implies assignment by treatment received (see Treatment Assignment). 3) Comparison: Contradiction. 4) Omitted exclusion criterion, impact: Potential (Generated SAP includes patients Original SAP excludes). 5) Conclusion: Problem.

#### 8. PK Population - Treatment Assignment

- **evaluation type:** semantic
- **original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received during the Induction Study Period.
- **generated SAP text:** Patients will be assigned to treatment groups based on treatment actually received.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** during the Induction Study Period
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP specifies assignment based on treatment received during Induction. 2) Generated SAP specifies assignment based on treatment received. 3) Comparison: Less detailed. 4) Omitted 'during Induction', impact: Low. 5) Conclusion: Acceptable.

#### 9. Safety Population - Definition

- **evaluation type:** semantic
- **original SAP text:** The safety population will consist of all randomly assigned patients who receive at least one dose (partial or full) of study drug (CT-P16 or EU-Approved Avastin). A patient will be considered to have received study drug if the patient is recorded as having study drug administered on the ‘Study Treatment Administration’ eCRF page.
- **generated SAP text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug (CT-P16 or EU-Approved Avastin).
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Reference to 'Study Treatment Administration' eCRF page
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP defines Safety population and eCRF source. 2) Generated SAP defines Safety population but omits eCRF source. 3) Comparison: Less detailed. 4) Omitted eCRF reference, impact: None. 5) Conclusion: Acceptable.

#### 10. Safety Population - Treatment Assignment

- **evaluation type:** semantic
- **original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received. Treatment patients actually received will be based on the kit number recorded on the ‘Study Treatment Administration’ eCRF page. Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group. All other patients will be analyzed under the EU-Approved Avastin treatment group.
- **generated SAP text:** Patients will be assigned to treatment groups based on treatment actually received.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific priority rule: Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group.
- **omission impact:** potential
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP provides specific logic for mixed treatments (CT-P16 priority). 2) Generated SAP provides general 'treatment received' rule. 3) Comparison: Less detailed. 4) Omitted priority rule, impact: Potential (ambiguity for mixed cases). 5) Conclusion: Acceptable (standard phrase used).

#### 11. General - Tabulation

- **evaluation type:** semantic
- **original SAP text:** The number of patients in each population will be tabulated by treatment group for the ITT population. A listing will also be provided displaying this data.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Requirement for tabulation and listing of populations
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Chain-of-thought: 1) Original SAP requires tabulation/listing. 2) Generated SAP omits this specific instruction in this section. 3) Comparison: Less detailed. 4) Omitted output requirement, impact: None (standard output). 5) Conclusion: Acceptable.

---

### Issues Found (3 items)

#### 1. Intent-to-treat (ITT) Population - Definition

- **issue type:** contradiction
- **severity:** minor
- **original SAP text:** consist of all randomized patients... and successfully screened based on the ‘Screening Pass/Fail’ eCRF page
- **generated SAP text:** defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed
- **protocol text:** defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed
- **why they conflict:** Original SAP adds a 'successfully screened' requirement that Generated SAP omits.
- **description:** Generated SAP omits the 'successfully screened' inclusion criterion present in the Original SAP.
- **reasoning:** Chain-of-thought: 1) Issue: Missing inclusion criterion. 2) Identified by comparing definitions. 3) Original SAP requires screening success; Generated SAP does not. 4) Severity: Minor (usually randomized implies screened, but Original SAP is explicit). 5) Impact: Potential inclusion of screen failures in ITT.

#### 2. PK Population - Definition

- **issue type:** contradiction
- **severity:** minor
- **original SAP text:** Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population.
- **generated SAP text:** Patients will be assigned to treatment groups based on treatment actually received.
- **protocol text:** Patients will be assigned to treatment groups based on treatment actually received.
- **why they conflict:** Original SAP excludes incorrect treatment patients; Generated SAP assigns them by treatment received.
- **description:** Generated SAP omits the exclusion of patients who received incorrect treatment, implying they are included.
- **reasoning:** Chain-of-thought: 1) Issue: Contradictory handling of incorrect treatment. 2) Identified by comparing definitions. 3) Original SAP excludes; Generated SAP includes. 4) Severity: Minor. 5) Impact: Change in population composition.

#### 3. Per-Protocol (PP) Population - Definition

- **issue type:** incomplete
- **severity:** minor
- **original SAP text:** A patient will be considered as receiving full dose if the planned dose is recorded as ‘15mg/kg’ and the action taken is recorded as ‘Dose Not Changed’...
- **generated SAP text:** A major protocol deviation... will be defined in the statistical analysis plan (SAP).
- **protocol text:** A major protocol deviation... will be defined in the statistical analysis plan (SAP).
- **why they conflict:** Generated SAP contains self-referential placeholder text instead of definitions.
- **description:** Generated SAP fails to define 'full dose' and includes a placeholder statement ('will be defined in the SAP') instead of defining deviations.
- **reasoning:** Chain-of-thought: 1) Issue: Incomplete definition/Placeholder text. 2) Identified by reading Generated SAP text. 3) Original SAP provides definitions; Generated SAP refers to itself. 4) Severity: Minor. 5) Impact: Lack of clarity on PP criteria.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (1 items)

#### 1. Pharmacokinetic Population – Maintenance Period Subset

- **content type:** entire_population
- **original SAP text:** The PK population – Maintenance Period Subset will consist of all patients in PK population who received at least 1 dose (full) of either of the study drugs and have at least one post treatment PK result during the Maintenance Study Period. Patients who received incorrect treatment during the Maintenance Study Period will be excluded from the PK population – Maintenance Period Subset. If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not. Patients will be assigned to treatment groups based on treatment they actually received.
- **protocol text:** Searched Protocol Section 7.4 - not found
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Entire population definition missing
- **reasoning:** Chain-of-thought: 1) Original SAP defines this subset. 2) Protocol does not define this subset. 3) Classification: Acceptable difference (not required by Protocol). 4) Impact: Loss of specific analysis subset.

---

### Reasoning

Step-by-step chain-of-thought reasoning trace: 1) Found ITT, PP, PK, Safety populations in Protocol. 2) Found ITT, PP, PK, PK-Maint, Safety in Original SAP. 3) Found ITT, PP, PK, Safety in Generated SAP. 4) Compared content: Generated SAP largely copies Protocol text, missing specific refinements from Original SAP (Screening success for ITT, Full dose definition for PP, Incorrect treatment exclusion for PK, Priority rule for Safety). 5) Checked existence: PK-Maint missing from Generated SAP but not in Protocol (Acceptable). 6) Identified issues: ITT and PK definitions in Generated SAP contradict Original SAP's specific criteria. PP definition contains self-referential placeholder text ('will be defined in SAP'). 7) Rating: POOR due to multiple content discrepancies and placeholder text.

---

### Summary

The Generated SAP includes the primary populations required by the Protocol but fails to incorporate specific definitions and constraints present in the Original SAP. Notable discrepancies include the omission of the 'successfully screened' criterion for ITT, the omission of the 'incorrect treatment' exclusion for PK, and the inclusion of placeholder text for protocol deviations in the PP definition. The PK Maintenance Subset is missing but not required by Protocol.