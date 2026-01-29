## General Methodology Evaluation

**Section:** general_methodology
**Rating:** GREAT
**Status:** pass

---

### Extraction Validation

- **sections read:** 4.1
- **elements per section:** 4.1: 15
- **paragraphs processed:** 15
- **elements extracted:** 15
- **elements in evaluation table:** 11
- **elements in missing from generated SAP:** 4
- **counts match:** True

---

### Evaluation Table (11 items)

#### 1. descriptive statistics definition (continuous)

- **evaluation type:** exact_match
- **original SAP text:** Continuous data will be summarized using descriptive statistics: the number of observations (n), mean, standard deviation, minimum, median and maximum unless otherwise indicated.
- **generated SAP text:** The term “descriptive statistics” refers to the number of patients (n), mean, median, standard deviation (SD), minimum, and maximum for continuous variables
- **matches original SAP:** yes
- **protocol text:** Continuous variables will be summarized by reporting the number of observations (n), mean, standard deviation, median, minimum, and maximum.
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match perfectly.

#### 2. descriptive statistics definition (categorical)

- **evaluation type:** exact_match
- **original SAP text:** Categorical data will be summarized using numbers and percentages of patients.
- **generated SAP text:** and refers to the number and/or percentage of patients (or events) for categorical variables.
- **matches original SAP:** yes
- **protocol text:** Categorical variables will be summarized using frequency tables showing the number and percentage of patients within a particular category.
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 3. summarization by treatment

- **evaluation type:** semantic
- **original SAP text:** The denominator for all percentages will be the number of patients within the treatment group for the population of interest, unless otherwise indicated.
- **generated SAP text:** Unless specified otherwise, summaries will be presented by treatment arm (CT-P16 and EU-Approved Avastin).
- **matches original SAP:** yes
- **protocol text:** Continuous variables will be summarized... Categorical variables will be summarized... (implied by study design)
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both specify summarization by treatment group.

#### 4. primary efficacy analysis method

- **evaluation type:** exact_match
- **original SAP text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model
- **generated SAP text:** For the primary efficacy analysis (see Section 3.7.3), a logistic regression model will be utilized.
- **matches original SAP:** yes
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent methodology stated in general section.

#### 5. listings sorting/content

- **evaluation type:** semantic
- **original SAP text:** Listings will be sorted by the treatment group and then patient number, which is the unique subject identifier and visit, if applicable.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **matches original SAP:** yes
- **protocol text:** Data will be listed.
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP is less detailed regarding sorting order but consistent regarding content.

#### 6. software

- **evaluation type:** semantic
- **original SAP text:** 4.1. Software [Section exists but is empty in text provided]
- **generated SAP text:** All analyses described in this plan will be performed using SAS v9.4 or higher unless specified otherwise.
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Original SAP has a placeholder for software. Generated SAP specifies SAS v9.4, which is standard and does not contradict the empty placeholder.

#### 7. a priori vs post hoc

- **evaluation type:** semantic
- **generated SAP text:** The analyses documented here are considered a priori analyses... Changes to the planned analyses... will be considered post hoc
- **matches original SAP:** yes
- **protocol text:** Changes from analyses planned in this protocol will be documented in the SAP. Any deviations from the planned analysis as described in the SAP will be justified and recorded in the study report.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard regulatory language included in Generated SAP; consistent with Protocol Section 7.6.

#### 8. visit windows usage

- **evaluation type:** semantic
- **original SAP text:** EOT and unscheduled visit will not be summarized in visit-based tables, unless otherwise indicated.
- **generated SAP text:** Summaries of efficacy and safety parameters that are presented by-visit will use pre-defined visit windows as described in Section 4.5.
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP explicitly mentions using visit windows, which is a standard method to handle visit-based summaries implied by the Original SAP's exclusion of unscheduled visits.

#### 9. baseline definition reference

- **evaluation type:** semantic
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** Baseline for all assessments is defined in Section 4.2.
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Structural reference to definition.

#### 10. analysis populations reference

- **evaluation type:** semantic
- **original SAP text:** Population to be used in analysis will be specified in related sections.
- **generated SAP text:** Analysis populations referenced throughout this document... are defined in Section 3.3.
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Structural reference.

#### 11. overall population summaries

- **evaluation type:** semantic
- **generated SAP text:** Where specified in Section 6 or Section 7, certain efficacy and safety endpoints may also be summarized for the overall population.
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Permissive statement allowing overall summaries where specified; does not contradict Original SAP.

---

### Issues Found (0 items)

*No issues found.*

---

### Extra Information Flagged (2 items)

#### 1. Software version specification

- **content:** Software version specification
- **generated SAP text:** All analyses described in this plan will be performed using SAS v9.4 or higher unless specified otherwise.
- **contradicts:** no
- **detail:** Original SAP has a placeholder for software but no text.
- **reasoning:** Standard detail added.

#### 2. A priori vs Post hoc definition

- **content:** A priori vs Post hoc definition
- **generated SAP text:** The analyses documented here are considered a priori analyses... Changes... will be considered post hoc
- **contradicts:** no
- **detail:** Standard regulatory language not explicitly in Original SAP General Considerations but consistent with Protocol Section 7.6.
- **reasoning:** Standard detail added.

---

### Missing from Generated SAP (4 items)

#### 1. decimal place rules

- **original SAP text:** Minimum and maximum will be presented to the same number of decimal places as the raw data, mean and median will be presented to one more decimal place than the raw data, and standard deviation will be presented to two more decimal places than the raw data. If the geometric mean is to be presented, it will be set to the same precision as the mean. Percent coefficient of variation (CV) will be presented to two more decimal places than the raw data.
- **why they conflict:** Generated SAP omits specific formatting rules present in Original SAP.
- **description:** Specific decimal precision rules for descriptive statistics are missing.
- **reasoning:** Original SAP Section 4 provides detailed formatting rules not found in Generated SAP Section 4.1.

#### 2. categorical percentage formatting

- **original SAP text:** Percentages will be presented to one decimal place and will be suppressed when the count is zero.
- **why they conflict:** Generated SAP omits specific formatting rules.
- **description:** Rules for percentage decimal places and suppression of zero counts are missing.
- **reasoning:** Original SAP Section 4 detail missing.

#### 3. not done row

- **original SAP text:** A row denoted “Not Done” will be included in count tabulations where necessary to account for cases of no assessment or missing values.
- **why they conflict:** Generated SAP omits specific reporting convention.
- **description:** Requirement for 'Not Done' row in categorical tables is missing.
- **reasoning:** Original SAP Section 4 detail missing.

#### 4. quantification limits handling

- **original SAP text:** For the purpose of summarization, any numeric values recorded below the lower limit or above the upper limit of quantification will be set to the respective limit for all related summaries unless otherwise indicated.
- **why they conflict:** Generated SAP omits data handling rule.
- **description:** Rule for handling values below LLOQ or above ULOQ is missing.
- **reasoning:** Original SAP Section 4 detail missing.

---

### Internal Contradictions (0 items)

*No internal contradictions.*

---

### Reasoning

The Generated SAP's General Methodology section (4.1) aligns well with the Original SAP's General Statistical Considerations (Section 4). It correctly defines descriptive statistics for continuous and categorical variables and specifies summarization by treatment group. It includes a reference to the primary analysis method (logistic regression) which matches the Original SAP. The Generated SAP omits specific formatting rules found in the Original SAP (decimal places, 'Not Done' rows, LLOQ handling), but these omissions do not constitute contradictions. The Generated SAP adds standard details about software (SAS v9.4) and a priori/post hoc analysis definitions which are acceptable additions.

---

### Summary

The General Methodology section is accurate and consistent with the Original SAP. It correctly captures high-level statistical conventions but omits some specific formatting and data handling rules (e.g., decimal precision, LLOQ handling) present in the Original SAP.