## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **sections read:** 4.1
- **elements per section:** 4.1: 11
- **paragraphs processed:** 11
- **elements extracted:** 11
- **elements in evaluation table:** 11
- **elements in missing from generated SAP:** 4
- **counts match:** True

---

### Evaluation Table (11 items)

#### 1. Software

- **evaluation type:** exact_match
- **original SAP text:** 4.1. Software [No text provided under header]
- **generated SAP text:** All analyses described in this plan will be performed using SAS software version 9.4 or higher unless specified otherwise.
- **matches original SAP:** no
- **protocol consulted:** yes
- **result:** problem
- **issue type:** unverifiable_assumption
- **severity:** minor
- **reasoning:** The Original SAP includes a header for Software but provides no text. The Generated SAP specifies SAS version 9.4 or higher. While this is a standard industry default, it is technically an assumption filling a blank in the source document.

#### 2. Analysis Timing (A priori/Post hoc)

- **evaluation type:** semantic
- **generated SAP text:** The analyses documented here are considered a priori analyses in that they are defined prior to database lock. Changes to the planned analyses, if any, designed after database lock and/or unblinding will be considered post hoc analyses and will be applied as exploratory methodology.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard statistical boilerplate consistent with GCP, though not explicitly stated in the Original SAP's general section.

#### 3. Post hoc reporting

- **evaluation type:** semantic
- **generated SAP text:** All post hoc analyses will be identified in the clinical study report.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard reporting convention.

#### 4. Descriptive Statistics Definition

- **evaluation type:** semantic
- **original SAP text:** Continuous data will be summarized using descriptive statistics: the number of observations (n), mean, standard deviation, minimum, median and maximum unless otherwise indicated. ... Categorical data will be summarized using numbers and percentages of patients.
- **generated SAP text:** The term 'descriptive statistics' refers to the number of patients (n), mean, median, standard deviation (SD), minimum, and maximum for continuous variables; and refers to the number and percentage of patients for categorical variables.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 5. Descriptive Statistics Application

- **evaluation type:** semantic
- **original SAP text:** unless otherwise indicated.
- **generated SAP text:** Descriptive statistics will be presented as described here unless specified otherwise in the efficacy or safety sections of this document.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent application rule.

#### 6. Confidence Intervals and P-values

- **evaluation type:** semantic
- **original SAP text:** The similarity criterion has been set such that the confidence limits of the 95% CI of the difference in ORR... (two one-sided alpha 0.025)
- **generated SAP text:** Unless specified otherwise, confidence intervals will be presented as 95% and p-values will be presented as 2-sided.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with the specific statistical parameters mentioned in the Original SAP (95% CI, alpha 0.025 one-sided equivalent to 0.05 two-sided).

#### 7. Primary Efficacy Method

- **evaluation type:** semantic
- **original SAP text:** equivalence margin of -12.5 to 12.5 using a 95% CI (two one-sided alpha 0.025)
- **generated SAP text:** For the primary efficacy analysis of objective response rate (ORR), the equivalence testing approach utilizing two one-sided tests at the 0.025 level of significance will be used, as described in Section 3.7.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Generated SAP describes the testing approach (TOST) while the Original SAP describes the CI approach; these are statistically equivalent.

#### 8. Summary Grouping

- **evaluation type:** semantic
- **original SAP text:** Categorical data will be summarized using numbers and percentages of patients... within the treatment group... Summaries of concomitant medications will be presented by Whole Study Period, Induction Study Period, Maintenance Study period and Follow-up period
- **generated SAP text:** Unless specified otherwise, summaries will be presented by treatment arm (CT-P16 or EU-Approved Avastin), study period (Induction Study Period, Maintenance Study Period, and/or Whole Study Period, as defined in Section 3.4), and overall.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with the grouping strategies described in the Original SAP.

#### 9. AE Coding Dictionary

- **evaluation type:** semantic
- **original SAP text:** All AEs will be classified by SOC and PT according to the MedDRA version 24.0 or higher.
- **generated SAP text:** Adverse events (AEs) will be coded to system organ class (SOC) and preferred term (PT) using the Medical Dictionary for Regulatory Activities (MedDRA) current version at the time of database lock.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** "Current version" is consistent with the requirement of "version 24.0 or higher".

#### 10. Medication Coding Dictionary

- **evaluation type:** semantic
- **original SAP text:** All medications will be coded using WHO Drug Dictionary version March, 2021 or later.
- **generated SAP text:** Prior and concomitant medications will be coded to drug class and PT using the World Health Organization (WHO) Drug Dictionary.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP omits the specific version ("March, 2021 or later") but specifies the correct dictionary. This is less detailed but not contradictory.

#### 11. Listing Sort Order

- **evaluation type:** semantic
- **original SAP text:** Listings will be sorted by the treatment group and then patient number... and visit, if applicable.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **matches original SAP:** no
- **protocol consulted:** yes
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** The Original SAP explicitly specifies sorting by Treatment then Patient. The Generated SAP specifies listing by Patient then Treatment. While minor, this is a direct contradiction in presentation standards.


---

### Issues Found (2 items)

#### 1. Listing Sort Order

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** Listings will be sorted by the treatment group and then patient number
- **generated SAP text:** listed by patient, treatment, and visit
- **why they conflict:** The Original SAP prioritizes Treatment Group as the primary sort key, while the Generated SAP implies Patient is the primary sort key.
- **description:** The Generated SAP changes the specified sort order for data listings.
- **reasoning:** In clinical data reporting, 'listed by X, Y' typically implies the sort order. The Original SAP is explicit about sorting by Treatment first. The Generated SAP puts Patient first.

#### 2. Software

- **issue type:** unverifiable_assumption
- **severity:** minor
- **original SAP text:** 4.1. Software [No text]
- **generated SAP text:** SAS software version 9.4 or higher
- **why they conflict:** The Original SAP leaves the software section blank.
- **description:** The Generated SAP specifies a software version where none was provided in the source documents.
- **reasoning:** While SAS 9.4 is a standard default, the Generated SAP is technically making a decision on an unspecified item.


---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (4 items)

- Precision rules for descriptive statistics (e.g., mean/median to one more decimal place than raw data, SD to two more).
- Handling of values below LLOQ or above ULOQ (set to the respective limit).
- Handling of 'Not Done' rows in categorical summaries.
- Discrepancy handling between eCRF and analytical facility data.

---

### Internal Contradictions (0 items)

*No internal contradictions.*

---

### Reasoning

The Generated SAP's General Methodology section is largely consistent with the Original SAP, covering the same key topics (descriptive stats, coding dictionaries, analysis populations). However, it lacks the specific precision rules (decimal places) and data handling rules (LLOQ/ULOQ) found in the Original SAP. There is a minor contradiction regarding the sort order of listings (Treatment->Patient vs Patient->Treatment) and a minor unverifiable assumption regarding the software version (filling a blank in the Original SAP).

---

### Summary

The General Methodology section is generally accurate but less detailed than the Original SAP, missing specific precision and data handling rules. It contains a minor contradiction regarding listing sort order and makes a standard assumption about software version where the Original SAP was blank.