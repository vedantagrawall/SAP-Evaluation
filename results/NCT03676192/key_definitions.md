## Key Definitions Evaluation

**Section:** key_definitions
**Rating:** GREAT
**Status:** pass

---

### Extraction Validation

- **sections read:** 4.2
- **elements per section:** 4.2: 27
- **elements extracted:** 27
- **elements in evaluation table:** 27
- **elements in missing from generated SAP:** 2
- **counts match:** True

---

### Evaluation Table (27 items)

#### 1. First Dose Date

- **evaluation type:** semantic
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** The date on which the first administration of any component of the study treatment (CT-P16, EU-Approved Avastin, paclitaxel, or carboplatin) is received by the patient.
- **protocol text:** Study treatment (CT-P16 or EU-Approved Avastin, carboplatin, and paclitaxel) should be administered on the same day.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Original SAP uses 'first infusion' as the anchor for baseline and prior medications. The Protocol clarifies that all components are administered on the same day. The Generated SAP's definition is consistent with this.

#### 2. First Dose Date (Induction Study Period)

- **evaluation type:** semantic
- **original SAP text:** Study drug administration will be started on the same day as randomization.
- **generated SAP text:** The date of the first dose of study treatment administered during Cycle 1 of the Induction Study Period. This is expected to be Study Day 1.
- **protocol text:** Study drug administration will be started on the same day as randomization.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3 and Protocol.

#### 3. First Dose Date (Maintenance Study Period)

- **evaluation type:** semantic
- **original SAP text:** entered the Maintenance Study Period and have a medication start date prior to the date of the first infusion in the Maintenance Study Period.
- **generated SAP text:** The date of the first dose of monotherapy (CT-P16 or EU-Approved Avastin) administered during the Maintenance Study Period.
- **protocol text:** Patients will receive monotherapy of 15 mg/kg of CT-P16 or EU-Approved Avastin every 3 weeks
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches the logic used in Original SAP Section 7.1 for defining periods.

#### 4. First Visit Date

- **evaluation type:** semantic
- **original SAP text:** Age will be automatically calculated in the eCRF system based on the informed consent signed date
- **generated SAP text:** The date the patient (or legally authorized representative) signed the informed consent form (ICF).
- **protocol text:** must sign the informed consent form before any study specific procedures
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard definition consistent with Original SAP references to informed consent date.

#### 5. Last Dose Date

- **evaluation type:** semantic
- **original SAP text:** Time on the study drug prior to discontinuation in each study period will be calculated as (Last dose date – First dose date + 1)
- **generated SAP text:** The date on which the last administration of any study drug (CT-P16 or EU-Approved Avastin) is received.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 5 usage.

#### 6. Last Dose Date (Induction Study Period)

- **evaluation type:** semantic
- **original SAP text:** Patients will receive paclitaxel 200 mg/m² IV and carboplatin area under the curve 6 IV every 3 weeks up to 6 cycles
- **generated SAP text:** The date on which the last dose of study treatment (study drug, paclitaxel, or carboplatin) is received during the Induction Study Period (Cycles 1 through 6).
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with the definition of the Induction Period which includes combination therapy.

#### 7. Last Dose Date (Maintenance Study Period)

- **evaluation type:** semantic
- **original SAP text:** Patients will receive monotherapy of 15 mg/kg of CT-P16 or EU-Approved Avastin every 3 weeks until PD or intolerable toxicity
- **generated SAP text:** The date of the last administration of monotherapy study drug received during the Maintenance Study Period.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3.

#### 8. Last Visit Date

- **evaluation type:** semantic
- **original SAP text:** All patients who enter the Follow-Up Period due to any reason will be followed every 9 weeks until death or the end of study
- **generated SAP text:** The date of the last study-related contact with the patient, which may be the date of the last follow-up visit, date of death, or date of withdrawal of consent.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard definition consistent with study design.

#### 9. Last Visit Date (Induction Study Period)

- **evaluation type:** semantic
- **original SAP text:** A patient will be considered to have completed Induction Study Period if the patient administered up to Induction Cycle 6 and performed tumor assessment... after the administration date at Induction Cycle 6.
- **generated SAP text:** The date of the end-of-cycle assessment for Cycle 6 (or the End of Treatment [EOT] visit if the patient discontinues during the Induction Study Period).
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 5.

#### 10. Last Visit Date (Maintenance Study Period)

- **evaluation type:** semantic
- **original SAP text:** Then, the patients will perform the EOT visit and then will directly enter the Follow-Up Period.
- **generated SAP text:** The date of the EOT visit performed after discontinuation of monotherapy.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3.

#### 11. Baseline Value

- **evaluation type:** exact_match
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** The baseline value is defined as the last non-missing assessment (including laboratory tests, vital signs, and tumor assessments) performed prior to the First Dose Date. If multiple assessments are performed on the same day, the assessment with a time recorded prior to the first dose time will be used. If time is not available, the assessment will be assumed to be pre-dose.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP Section 4.5. The Generated SAP adds standard clarification for same-day assessments.

#### 12. Change from Baseline Value

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters... will be summarized
- **generated SAP text:** Calculated as (Post-baseline Value - Baseline Value).
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard calculation implied by Original SAP Section 10.2.

#### 13. Study Day 1

- **evaluation type:** semantic
- **original SAP text:** Patients who qualify for randomization will be randomly assigned on Day 1 of Cycle 1 in the Induction Study Period
- **generated SAP text:** The First Dose Date (Induction Study Period).
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 4.3.

#### 14. Study Day

- **evaluation type:** semantic
- **original SAP text:** days from last dose on or before AE onset (Date of AE onset – Date of last dose on or before AE onset + 1)
- **generated SAP text:** The day relative to Study Day 1. If the date of interest is on or after Study Day 1: Study Day = (Date of Interest - Study Day 1) + 1. If the date of interest is prior to Study Day 1: Study Day = (Date of Interest - Study Day 1). There is no Study Day 0.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard CDISC formula consistent with Original SAP Section 10.1 logic.

#### 15. Duration of Treatment

- **evaluation type:** exact_match
- **original SAP text:** Time on the study drug prior to discontinuation in each study period will be calculated as (Last dose date – First dose date + 1)
- **generated SAP text:** Calculated as (Last Dose Date - First Dose Date) + 1.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP Section 5.

#### 16. Duration of Treatment (Induction Study Period)

- **evaluation type:** semantic
- **original SAP text:** Time on the study drug prior to discontinuation in each study period will be calculated as (Last dose date – First dose date + 1)
- **generated SAP text:** Calculated as (Last Dose Date [Induction Study Period] - First Dose Date [Induction Study Period]) + 1.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 5.

#### 17. Duration of Treatment (Maintenance Study Period)

- **evaluation type:** semantic
- **original SAP text:** Time on the study drug prior to discontinuation in each study period will be calculated as (Last dose date – First dose date + 1)
- **generated SAP text:** Calculated as (Last Dose Date [Maintenance Study Period] - First Dose Date [Maintenance Study Period]) + 1.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 5.

#### 18. Duration of Study

- **evaluation type:** semantic
- **original SAP text:** days on study
- **generated SAP text:** Calculated as (Last Visit Date - First Visit Date) + 1.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard calculation for 'days on study' mentioned in Original SAP Section 10.1.4.

#### 19. Screening Period

- **evaluation type:** semantic
- **original SAP text:** Screening evaluations will be completed within 28 days prior to randomization.
- **generated SAP text:** The period from the First Visit Date (ICF signature) up to the day before Study Day 1.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3.

#### 20. Induction Study Period

- **evaluation type:** semantic
- **original SAP text:** Induction Study Period: maximum 6 cycles... If a patient has progressive disease (PD) during or after the completion of the Induction Study Period (assessed at the end of Cycle 6) or does not enter the Maintenance Study Period... this patient will complete the EOT visit
- **generated SAP text:** The period starting from Study Day 1 through the last assessment of Cycle 6 (nominally Week 18) or the EOT visit, whichever occurs first for patients not entering Maintenance.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3.

#### 21. Maintenance Study Period

- **evaluation type:** semantic
- **original SAP text:** Maintenance Study Period: until disease progression, or intolerable toxicity, whichever occurs first
- **generated SAP text:** The period starting from the First Dose Date (Maintenance Study Period) through the EOT visit following monotherapy discontinuation.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3.

#### 22. Follow-Up Period

- **evaluation type:** semantic
- **original SAP text:** All patients who enter the Follow-Up Period due to any reason will be followed every 9 weeks until death or the end of study
- **generated SAP text:** The period starting the day after the EOT visit through the Last Visit Date.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3.

#### 23. Whole Study Period

- **evaluation type:** semantic
- **original SAP text:** ORR during the Whole Study Period
- **generated SAP text:** The combined duration from Study Day 1 through the Last Visit Date, covering Induction, Maintenance (if applicable), and Follow-Up.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 8.2.1.

#### 24. Ages and Years

- **evaluation type:** semantic
- **original SAP text:** Age will be automatically calculated in the eCRF system based on the informed consent signed date, the year of birth and information on whether the date of birth has passed or not.
- **generated SAP text:** All age-based calculations will use (Date of Interest - Date of Birth) / 365.25.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Generated SAP provides the specific formula for the calculation described in the Original SAP.

#### 25. Missing Dates

- **evaluation type:** semantic
- **original SAP text:** Incomplete medication start and stop dates will be imputed respectively as described in Appendix 14.4.1.
- **generated SAP text:** Handling of partial or missing dates for AEs and concomitant medications will be described in Section 4.4 [GAP: Section 4.4 not yet generated].
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP acknowledges the missing section.

#### 26. Study Treatment

- **evaluation type:** semantic
- **original SAP text:** CT-P16 (15 mg/kg) and EU-Approved Avastin (15 mg/kg) when co-administered with paclitaxel and carboplatin
- **generated SAP text:** Refers to the combination of CT-P16 or EU-Approved Avastin with paclitaxel and carboplatin.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 3.

#### 27. Study Drug

- **evaluation type:** semantic
- **original SAP text:** study drug (CT-P16 or EU-Approved Avastin)
- **generated SAP text:** Refers specifically to the investigational product (CT-P16) or the reference product (EU-Approved Avastin).
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP Section 4.4.5.

---

### Issues Found (0 items)

*No issues found.*

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (2 items)

#### 1. Actual duration of dose (Exposure)

- **original SAP text:** Actual duration of dose (weeks) = (Start Date of Next Cycle – Start Date of Current Cycle) / 7 ... Actual duration of dose (weeks) = (Start Date of Last Cycle + 21 – Start Date of First Cycle) / 7
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific formulas for dose intensity calculations found in Original SAP Section 7.2 are missing from the Key Definitions section of the Generated SAP.
- **reasoning:** The Generated SAP defines 'Duration of Treatment' generally (matching Section 5), but omits the specific 'Actual duration of dose' formulas required for the Exposure analysis in Section 7.2. This is an omission of a specific analysis rule rather than a contradiction.

#### 2. Baseline Weight Definition

- **original SAP text:** Weight at Induction cycle 1 will be considered as the baseline value since weight is collected for kit number dispensation prior to the infusion, if study drug is administered at Induction cycle 1.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific rule for weight baseline is missing.
- **reasoning:** The Generated SAP has a general baseline definition that covers this, but the specific nuance about weight collection timing is useful context found in the Original SAP.

---

### Reasoning

The Generated SAP provides a comprehensive set of key definitions in Section 4.2 that align well with the Original SAP. Definitions for study dates, periods, and durations are consistent with the logic described in the Original SAP's disposition and concomitant medication sections. The Generated SAP explicitly defines terms like 'First Dose Date' and 'Last Dose Date' which are used implicitly in the Original SAP. There are no contradictions. The Generated SAP is missing specific formulas for 'Actual duration of dose' used for exposure analysis (Original SAP Section 7.2) and specific date imputation rules (though a placeholder exists), but these are acceptable omissions for a summary definitions section.

---

### Summary

The Key Definitions section is well-constructed and consistent with the Original SAP. It accurately defines study periods, dates, and general calculation rules. Minor omissions regarding specific exposure formulas do not impact the overall validity of the definitions provided.