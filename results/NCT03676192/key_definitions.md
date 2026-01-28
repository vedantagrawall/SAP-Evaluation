## Key Definitions Evaluation

**Section:** key_definitions
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **sections read:** 4.5, 5, 6.1, 7.1, 7.2, 8.2.2, 8.2.2.1, 8.2.2.2, 8.2.2.3, 8.2.2.4, 10.1, 10.1.2, 10.1.3, 10.2, 10.3, 10.9, 11, 14.4.1, 14.4.2, 14.4.3
- **elements per section:** 4.5: 2, 5: 6, 6.1: 1, 7.1: 5, 7.2: 7, 8.2.2: 1, 8.2.2.1: 1, 8.2.2.2: 1, 8.2.2.3: 1, 8.2.2.4: 1, 10.1: 7, 10.1.2: 1, 10.1.3: 1, 10.2: 3, 10.3: 2, 10.9: 2, 11: 3, 14.4.1: 1, 14.4.2: 1, 14.4.3: 1
- **elements extracted:** 48
- **elements in evaluation table:** 5
- **elements in missing from generated SAP:** 43
- **counts match:** True

---

### Evaluation Table (5 items)

#### 1. Baseline Value Definition

- **evaluation type:** exact_match
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** Baseline Value: Defined as the last non-missing observation (including central laboratory results, vital signs, and tumor assessments) recorded prior to the First Dose Date.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP provides an equivalent definition.

#### 2. Post-baseline Visits Definition

- **evaluation type:** semantic
- **original SAP text:** Post-baseline visits will be considered to be all visits after the first infusion.
- **generated SAP text:** Change from Baseline Value: Calculated as (Post-Baseline Value – Baseline Value).
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** While not explicitly defined as a standalone term, the concept is implied in the Change from Baseline calculation and consistent with the First Dose Date definition.

#### 3. Time on Study Drug Calculation

- **evaluation type:** exact_match
- **original SAP text:** Time on the study drug prior to discontinuation in each study period will be calculated as (Last dose date – First dose date + 1)
- **generated SAP text:** Duration of Treatment: Calculated as (Last Dose Date – First Dose Date) + 1.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Formula matches exactly.

#### 4. Age Calculation

- **evaluation type:** semantic
- **original SAP text:** Age will be automatically calculated in the eCRF system based on the informed consent signed date, the year of birth and information on whether the date of birth has passed or not.
- **generated SAP text:** Age: Calculated as the integer part of (Date of Informed Consent – Date of Birth) / 365.25.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP provides a standard formulaic implementation of the logic described in Original SAP.

#### 5. Weight Baseline Definition

- **evaluation type:** semantic
- **original SAP text:** Weight at Induction cycle 1 will be considered as the baseline value since weight is collected for kit number dispensation prior to the infusion, if study drug is administered at Induction cycle 1.
- **generated SAP text:** Baseline for all assessments is defined in Section 4.2. ... Baseline Value: Defined as the last non-missing observation ... recorded prior to the First Dose Date.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP general baseline definition covers this specific case.

---

### Issues Found (0 items)

*No issues found.*

---

### Extra Information Flagged (2 items)

#### 1. Study Day Definition

- **content:** Study Day Definition
- **generated SAP text:** Study Day: Defined as the number of days from Study Day 1. ... There is no Study Day 0.
- **contradicts:** no
- **detail:** Standard definition added.
- **reasoning:** Consistent with standard practice.

#### 2. Controlled Disease Definition

- **content:** Controlled Disease Definition
- **generated SAP text:** Controlled Disease: Defined as a patient achieving a Best Overall Response (BOR) of Complete Response (CR), Partial Response (PR), or Stable Disease (SD) as assessed at the end of Cycle 6
- **contradicts:** no
- **detail:** Explicit definition added.
- **reasoning:** Consistent with Original SAP study design description.

---

### Missing from Generated SAP (43 items)

#### 1. Randomized Definition

- **original SAP text:** A patient will be considered to be randomized if the randomization date is recorded on the ‘Randomization’ eCRF page and the response of ‘Is the patient eligible to participate in this study?’ on ‘Screening Pass/Fail’ eCRF page is ‘Yes’.
- **protocol text:** Patients who qualify for randomization will be randomly assigned on Day 1 of Cycle 1 of the Induction Study Period
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific eCRF-based derivation logic is missing.
- **reasoning:** Protocol describes the process but not the specific data derivation rule.

#### 2. Initiated Induction Period Definition

- **original SAP text:** A patient will be considered to have initiated the Induction Study Period and the Maintenance Study Period if the administration date is recorded on the ‘Study Treatment Administration’ eCRF page for Induction Study Period and Maintenance Study Period, respectively.
- **protocol text:** During the Induction Study Period, patients will receive 15 mg/kg IV of either CT-P16 or EU-Approved Avastin
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific eCRF-based derivation logic is missing.
- **reasoning:** Protocol describes the period but not the specific data derivation rule.

#### 3. Initiated Follow-Up Period Definition

- **original SAP text:** If the Follow-Up visit date is recorded on ‘Survival Status’ eCRF page and its ‘Patient Status’ is ‘Alive’, then the patient will be considered to have initiated Follow-Up Period.
- **protocol text:** All patients who enter the Follow-Up Period due to any reason will be followed every 9 weeks
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific eCRF-based derivation logic is missing.
- **reasoning:** Protocol describes the period but not the specific data derivation rule.

#### 4. Completed Induction Period Definition

- **original SAP text:** A patient will be considered to have completed Induction Study Period if the patient administered up to Induction Cycle 6 and performed tumor assessment (i.e. ‘Response Evaluation’ eCRF page) after the administration date at Induction Cycle 6.
- **protocol text:** If a patient has progressive disease (PD) during or after the completion of the Induction Study Period (assessed at the end of Cycle 6)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific eCRF-based derivation logic is missing.
- **reasoning:** Protocol describes completion criteria generally but not the specific data derivation rule.

#### 5. Discontinued Definition

- **original SAP text:** A patient will be considered to have discontinued the study period if the discontinuation reason is recorded on the ‘Study Treatment Termination’ eCRF page.
- **protocol text:** The primary reason for withdrawal must be recorded in the patient’s medical record and on the withdrawal form in the electronic case report form (eCRF)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific eCRF-based derivation logic is missing.
- **reasoning:** Protocol describes the process but not the specific data derivation rule.

#### 6. Prior Medication Definition

- **original SAP text:** A prior medication is defined as any medication where both the start and stop dates are before the date of first infusion.
- **protocol text:** All medications used during the study, as well as all medications taken within 30 days of Day 1 of Cycle 1 in the Induction Study Period... will be collected.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific date-based definition is missing.
- **reasoning:** Protocol defines collection requirements but not the specific analysis definition.

#### 7. Concomitant Medication Definition

- **original SAP text:** A concomitant medication is defined as any medication that has a stop date that is on or after the date of first infusion or missing.
- **protocol text:** Concomitant medications include all prescription drugs, herbal products, vitamins, minerals, and over-the-counter medications.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific date-based definition is missing.
- **reasoning:** Protocol defines collection requirements but not the specific analysis definition.

#### 8. Concomitant Meds Induction Assignment

- **original SAP text:** Concomitant medications will be summarized in the Induction Study Period if patients: did not enter the Maintenance Study Period and have a medication start date on or prior to the last date of EOT... entered the Maintenance Study Period and have a medication start date prior to the date of the first infusion in the Maintenance Study Period.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 9. Concomitant Meds Maintenance Assignment

- **original SAP text:** Concomitant medications will be summarized in the Maintenance Study Period if patients: have a medication start date on or after the first infusion in the Maintenance Study Period...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 10. Concomitant Meds Follow-Up Assignment

- **original SAP text:** Concomitant medications will be summarized in Follow-Up Period if patients: have the last date of EOT and have a medication start date after the last date of EOT...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 11. Weight-adjusted Prescribed Dose

- **original SAP text:** The weight-adjusted prescribed dose and weight-adjusted administered dose are calculated by dividing the corresponding dose recorded on the eCRF, by the patient’s weight at the same visit.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 12. Weight-adjusted Administered Dose

- **original SAP text:** The weight-adjusted prescribed dose and weight-adjusted administered dose are calculated by dividing the corresponding dose recorded on the eCRF, by the patient’s weight at the same visit.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 13. Actual Duration of Dose

- **original SAP text:** Actual duration of dose (weeks) = (Start Date of Next Cycle – Start Date of Current Cycle) / 7
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 14. Administered Dose Intensity

- **original SAP text:** administered dose intensity (weight-adjusted administered dose / actual duration of dose) (mg/kg/week)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 15. Relative Dose Intensity

- **original SAP text:** relative dose intensity (administered dose intensity / planned dose intensity * 100) (%)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 16. Adjusted Carboplatin Dose Formula

- **original SAP text:** Adjusted Carboplatin Dose (AUC) = Carboplatin Dose (mg)/(CrCl+25).
- **protocol text:** Carboplatin dose (mg) = target AUC 6 (mg‧min/mL) x (GFR* + 25)
- **in protocol:** yes
- **classification:** missing_required
- **description:** Calvert formula for Carboplatin dose calculation is missing.
- **reasoning:** Explicitly defined in Protocol Section 5.3.3.

#### 17. Actual Duration of Dose (Period)

- **original SAP text:** Actual duration of dose in each period is given by the following formula: Actual duration of dose (weeks) = (Start Date of Last Cycle + 21 – Start Date of First Cycle) / 7
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 18. Time-to-Event Conversion Factor

- **original SAP text:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Conversion factor is missing.
- **reasoning:** Not in Protocol.

#### 19. Response Duration Formula

- **original SAP text:** Response duration (months) = (Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment +1)/30.4
- **protocol text:** Response duration: the time between initial response (CR or PR) and PD/recurrence
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific calculation formula with +1 and /30.4 is missing.
- **reasoning:** Protocol defines the concept but not the specific calculation formula.

#### 20. Time to Progression Formula

- **original SAP text:** TTP (months) = (Date of Event/Censoring – Date of Randomization +1)/30.4
- **protocol text:** TTP: the time from randomization until PD/recurrence
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific calculation formula with +1 and /30.4 is missing.
- **reasoning:** Protocol defines the concept but not the specific calculation formula.

#### 21. Progression-Free Survival Formula

- **original SAP text:** PFS (months) = (Date of Event/Censoring – Date of Randomization +1)/30.4
- **protocol text:** PFS: the time from randomization until PD/recurrence or death due to any cause, whichever occurs first
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific calculation formula with +1 and /30.4 is missing.
- **reasoning:** Protocol defines the concept but not the specific calculation formula.

#### 22. Overall Survival Formula

- **original SAP text:** OS (months) = (Date of Event/Censoring – Date of Randomization +1)/30.4
- **protocol text:** OS: the time from randomization until death due to any cause
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific calculation formula with +1 and /30.4 is missing.
- **reasoning:** Protocol defines the concept but not the specific calculation formula.

#### 23. Adverse Event Definition

- **original SAP text:** An adverse event (AE) is defined as any untoward medical occurrence in a patient enrolled into this study (i.e., when the ‘Informed Consent’ eCRF page is signed), regardless of its causal relationship to study drug.
- **protocol text:** An AE is defined as any untoward medical occurrence in a patient entered in this study regardless of its causal relationship to study drug.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Standard AE definition is missing.
- **reasoning:** Explicitly defined in Protocol Section 6.5.1.1.

#### 24. Treatment-Emergent AE Definition

- **original SAP text:** A Treatment-Emergent Adverse Event (TEAE) is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **protocol text:** A treatment-emergent AE is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Standard TEAE definition is missing.
- **reasoning:** Explicitly defined in Protocol Section 6.5.1.1.

#### 25. AE Duration Calculation

- **original SAP text:** duration of AE in days (Duration = Stop Date – Start Date + 1)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 26. Days from Last Dose Calculation

- **original SAP text:** days from last dose on or before AE onset (Date of AE onset – Date of last dose on or before AE onset + 1)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Calculation formula is missing.
- **reasoning:** Not in Protocol.

#### 27. TEAE Induction Assignment

- **original SAP text:** TEAEs will be summarized in the Induction Study Period if patients: did not enter the Maintenance Study Period and have an AE onset date on or prior to the last date of EOT... entered the Maintenance Study Period and have an AE onset date prior to the date of the first infusion in the Maintenance Study Period.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 28. TEAE Maintenance Assignment

- **original SAP text:** TEAEs will be summarized in the Maintenance Study Period if patients: have an AE onset date on or after the first infusion in the Maintenance Study Period...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 29. TEAE Follow-Up Assignment

- **original SAP text:** TEAEs will be summarized in Follow-Up Period if patients: have the last date of EOT and have an AE onset after the last date of EOT...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 30. Serious Adverse Event Definition

- **original SAP text:** A serious adverse event (SAE) is defined as any event that is immediately life threatening, requires inpatient hospitalization or prolongation of existing hospitalization, results in persistent or significant disability/incapacity, is a congenital anomaly/birth defect or results in death.
- **protocol text:** An SAE is defined as any untoward medical occurrence that at any dose: Results in death, Is immediately life threatening... Requires inpatient hospitalization... Results in persistent or significant disability/incapacity, Is a congenital anomaly/birth defect
- **in protocol:** yes
- **classification:** missing_required
- **description:** Standard SAE definition is missing.
- **reasoning:** Explicitly defined in Protocol Section 6.5.1.1.2.

#### 31. TEAE Leading to Discontinuation Definition

- **original SAP text:** TEAEs for which an action taken with study drug is ‘Drug Withdrawn’ will be considered TEAEs leading to study drug discontinuation.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific definition is missing.
- **reasoning:** Not in Protocol.

#### 32. Lab Data Induction Assignment

- **original SAP text:** Laboratory data will be summarized in the Induction Study Period if patients: entered the Maintenance Study Period and have an assessment date prior to the date of the first infusion in the Maintenance Study Period...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 33. Lab Data Maintenance Assignment

- **original SAP text:** Laboratory data will be summarized in the Maintenance Study Period if patients: entered the Follow-Up Period and have an assessment date on or after the first infusion in the Maintenance Study Period...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 34. Lab Data Follow-Up Assignment

- **original SAP text:** Laboratory data will be summarized in Follow-Up Period if patients: have an assessment date on or after the first visit date of Follow-Up Period.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Period assignment logic is missing.
- **reasoning:** Not in Protocol.

#### 35. BSA Calculation

- **original SAP text:** Body surface area (BSA) will be calculated in eCRF by using height collected at the screening visit and weight collected at each scheduled visit.
- **protocol text:** For dose amount calculation, the body surface area (BSA) should be calculated using either Mosteller formula or Dubois formula
- **in protocol:** yes
- **classification:** missing_required
- **description:** BSA calculation method is missing.
- **reasoning:** Protocol Section 5.3.2 specifies formulas.

#### 36. ADA Transformation Formula

- **original SAP text:** Transformed ADA value can be obtained using [log3(X/42)] + 1 transformation.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Transformation formula is missing.
- **reasoning:** Not in Protocol.

#### 37. NAb Transformation Formula

- **original SAP text:** Transformed NAb value can be obtained using [log2(X/5)] + 1 transformation.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Transformation formula is missing.
- **reasoning:** Not in Protocol.

#### 38. QLQ Raw Score Formula

- **original SAP text:** For all scales, the Raw Score (RS), is the mean of the component items: RS = (I1 + I2 + ... + In)/n
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Scoring formula is missing.
- **reasoning:** Not in Protocol.

#### 39. QLQ Functional Score Formula

- **original SAP text:** Then for Functional scales: Score = (1 - (RS-1)/range) * 100
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Scoring formula is missing.
- **reasoning:** Not in Protocol.

#### 40. QLQ Symptom Score Formula

- **original SAP text:** And for Symptom scales/items and Global health status/QoL: Score = ((RS-1)/range) * 100
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Scoring formula is missing.
- **reasoning:** Not in Protocol.

#### 41. Medication Date Imputation

- **original SAP text:** Incomplete medications start and stop dates will be imputed as follows: ...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Imputation rules are missing.
- **reasoning:** Not in Protocol.

#### 42. AE Date Imputation

- **original SAP text:** If the AE stop date is incomplete the following rules will be applied. ...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Imputation rules are missing.
- **reasoning:** Not in Protocol.

#### 43. Death Date Imputation

- **original SAP text:** For the purposes of inclusion in the survival analysis, incomplete death dates will be imputed as follow: ...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Imputation rules are missing.
- **reasoning:** Not in Protocol.

---

### Reasoning

The Generated SAP is missing several critical definitions and formulas that are present in both the Original SAP and the Protocol. Specifically, the definitions for Adverse Events (AE), Treatment-Emergent Adverse Events (TEAE), and Serious Adverse Events (SAE) are completely absent. Additionally, the specific formula for calculating the Adjusted Carboplatin Dose (Calvert formula) and the Body Surface Area (BSA) calculation method are missing, despite being specified in the Protocol. While the Generated SAP includes basic definitions for study periods and baseline, the omission of these required safety and dosing definitions constitutes a significant gap. Many other specific derivation rules (e.g., dose intensity, QoL scoring, date imputation) are also missing, but these are classified as acceptable differences as they are not explicitly required by the Protocol.

---

### Summary

The Generated SAP fails to include required definitions for Adverse Events, TEAEs, and SAEs, as well as the Protocol-specified Carboplatin dosing formula. These are critical omissions that render the document incomplete compared to the Original SAP and Protocol requirements.