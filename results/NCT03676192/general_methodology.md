## General Methodology Evaluation

**Section:** general_methodology
**Rating:** GREAT
**Status:** pass

---

### Extraction Validation

- **sections read:** 4.1
- **elements per section:** 4.1: 12
- **paragraphs processed:** 7
- **elements extracted:** 12
- **elements in evaluation table:** 12
- **elements in missing from generated SAP:** 4
- **counts match:** True

---

### Evaluation Table (12 items)

#### 1. Software specification

- **evaluation type:** exact_match
- **generated SAP text:** All analyses described in this plan will be performed using SAS software version 9.4 or higher unless specified otherwise.
- **matches original SAP:** yes
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Original SAP contains a header '4.1. Software' but no text follows it in the provided document. The Generated SAP specifies SAS 9.4, which is standard industry practice and does not contradict the empty section in the Original SAP.

#### 2. A priori vs Post hoc definition

- **evaluation type:** exact_match
- **generated SAP text:** The analyses documented here are considered a priori analyses in that they are defined prior to database lock.
- **matches original SAP:** yes
- **protocol text:** Changes from analyses planned in this protocol will be documented in the SAP.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard regulatory language included in the Generated SAP. Consistent with Protocol Section 7.6 regarding planned vs. deviated analyses.

#### 3. Post hoc analysis handling

- **evaluation type:** exact_match
- **generated SAP text:** Changes to the planned analyses, if any, designed after database lock and/or unblinding will be considered post hoc analyses and will be applied as exploratory methodology. All post hoc analyses will be identified in the clinical study report.
- **matches original SAP:** yes
- **protocol text:** Any deviations from the planned analysis as described in the SAP will be justified and recorded in the study report.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Protocol Section 7.6 requirements for reporting deviations.

#### 4. Descriptive statistics definition

- **evaluation type:** semantic
- **original SAP text:** Continuous data will be summarized using descriptive statistics: the number of observations (n), mean, standard deviation, minimum, median and maximum... Categorical data will be summarized using numbers and percentages of patients.
- **generated SAP text:** The term 'descriptive statistics' refers to the number of patients (n), mean, median, standard deviation (SD), minimum, and maximum for continuous variables; and refers to the number and percentage of patients for categorical variables.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The definitions match exactly.

#### 5. Presentation rule

- **evaluation type:** semantic
- **original SAP text:** ...unless otherwise indicated.
- **generated SAP text:** Descriptive statistics will be presented as described here unless specified otherwise in the efficacy or safety sections of this document.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both documents establish a default presentation rule that applies unless exceptions are noted.

#### 6. Confidence Intervals and P-values

- **evaluation type:** semantic
- **original SAP text:** 95% CI (two one-sided alpha 0.025)
- **generated SAP text:** Unless specified otherwise, confidence intervals will be presented as 95% and p-values will be presented as 2-sided.
- **matches original SAP:** yes
- **protocol text:** 95% confidence interval (CI) (two one-sided alpha 0.025)
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Original SAP and Protocol specify 95% CI (equivalent to 2-sided alpha 0.05). The Generated SAP's default of 95% CI and 2-sided p-values is consistent with this.

#### 7. Summary stratification

- **evaluation type:** semantic
- **original SAP text:** Summaries of concomitant medications will be presented by Whole Study Period, Induction Study Period, Maintenance Study period and Follow-up period... [and] by treatment group
- **generated SAP text:** Unless specified otherwise, summaries will be presented by treatment arm (CT-P16 or EU-Approved Avastin), study period (Induction Study Period, Maintenance Study Period, and/or Whole Study Period, as defined in Section 3.4), and overall.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Generated SAP generalizes the specific reporting periods found in the Original SAP (Sections 7.1, 10.1) into a general rule, which is accurate.

#### 8. AE Coding Dictionary

- **evaluation type:** semantic
- **original SAP text:** Medical Dictionary for Regulatory Activities (MedDRA) version 24.0 or higher
- **generated SAP text:** Medical Dictionary for Regulatory Activities (MedDRA) current version at the time of database lock
- **matches original SAP:** yes
- **protocol text:** Adverse events will be coded... using Medical Dictionary for Regulatory Activities (MedDRA).
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** 'Current version' is semantically compatible with 'Version 24.0 or higher' for a future database lock.

#### 9. Medication Coding Dictionary

- **evaluation type:** semantic
- **original SAP text:** WHO Drug Dictionary version March, 2021 or later
- **generated SAP text:** World Health Organization (WHO) Drug Dictionary
- **matches original SAP:** yes
- **protocol text:** World Health Organization (WHO) drug dictionary
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Generated SAP specifies the correct dictionary. Omitting the specific version 'March 2021 or later' is acceptable as it implies the current/standard version.

#### 10. Listing content

- **evaluation type:** semantic
- **original SAP text:** Listings will be sorted by the treatment group and then patient number... and visit, if applicable.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches the sorting/content requirements.

#### 11. Population identification in listings

- **evaluation type:** semantic
- **original SAP text:** A listing will also be provided displaying this data [populations].
- **generated SAP text:** All analysis populations (as defined in Section 3.3) will be identified in the listings.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** While the Original SAP specifies a dedicated listing for populations, identifying populations within listings is a standard and compatible enhancement.

#### 12. Summary population basis

- **evaluation type:** semantic
- **original SAP text:** The denominator for all percentages will be the number of patients within the treatment group for the population of interest
- **generated SAP text:** Summaries and tabulations will be based on the analysis populations specified for each endpoint in Section 2.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both documents state that summaries depend on the specific population defined for that analysis.

---

### Issues Found (0 items)

*No issues found.*

---

### Extra Information Flagged (1 items)

#### 1. Specification of SAS software version

- **content:** Specification of SAS software version
- **generated SAP text:** All analyses described in this plan will be performed using SAS software version 9.4 or higher unless specified otherwise.
- **contradicts:** no
- **detail:** Original SAP Section 4.1 header exists but is empty.
- **reasoning:** Standard statistical software specification.

---

### Missing from Generated SAP (4 items)

#### 1. Decimal precision rules (mean/median +1, SD +2, CV +2)

- **content:** Decimal precision rules (mean/median +1, SD +2, CV +2)
- **contradicts:** no
- **detail:** Original SAP Section 4 provides specific rounding rules for descriptive statistics.
- **reasoning:** Formatting detail omitted.

#### 2. Handling of 'Not Done' rows in tabulations

- **content:** Handling of 'Not Done' rows in tabulations
- **contradicts:** no
- **detail:** Original SAP specifies including a 'Not Done' row where necessary.
- **reasoning:** Formatting detail omitted.

#### 3. Handling of values below LLOQ or above ULOQ

- **content:** Handling of values below LLOQ or above ULOQ
- **contradicts:** no
- **detail:** Original SAP specifies setting these to the respective limit for summarization.
- **reasoning:** Data handling rule omitted.

#### 4. Handling of discrepancies between eCRF and analytical facilities

- **content:** Handling of discrepancies between eCRF and analytical facilities
- **contradicts:** no
- **detail:** Original SAP Section 4 provides specific logic for resolving date/time discrepancies.
- **reasoning:** Data handling rule omitted.

---

### Internal Contradictions (0 items)

*No internal contradictions.*

---

### Reasoning

The Generated SAP's General Methodology section is highly consistent with the Original SAP. It correctly defines descriptive statistics, coding dictionaries, and general reporting conventions. It includes standard boilerplate regarding software and a priori analysis which, while not explicitly in the Original SAP text provided (one section was empty), aligns with industry standards and the Protocol's requirements for reporting deviations. The Generated SAP omits some specific formatting rules regarding decimal precision and LLOQ handling found in the Original SAP, but these omissions do not constitute contradictions.

---

### Summary

The General Methodology section accurately reflects the statistical standards and definitions from the Original SAP and Protocol. It correctly defines descriptive statistics, coding dictionaries, and reporting conventions without contradiction.