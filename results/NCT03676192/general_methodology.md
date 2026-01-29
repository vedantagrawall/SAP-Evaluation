## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **sections read:** 4.1
- **elements per section:** 4.1: 12
- **paragraphs processed:** 12
- **elements extracted:** 12
- **elements in evaluation table:** 12
- **elements in missing from generated SAP:** 3
- **counts match:** True

---

### Evaluation Table (12 items)

#### 1. software used

- **evaluation type:** exact_match
- **original SAP text:** 4.1. Software [Section is empty]
- **generated SAP text:** All analyses described in this plan will be performed using SAS v9.4 or higher unless specified otherwise.
- **matches original SAP:** no
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Original SAP includes a header for Software but leaves it blank. The Generated SAP fills this gap by specifying SAS v9.4, which is a reasonable addition and not a contradiction.

#### 2. analysis timing definition

- **evaluation type:** semantic
- **generated SAP text:** The analyses documented here are considered a priori analyses in that they are defined prior to database lock.
- **matches original SAP:** no
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard administrative definition added in the Generated SAP. Does not contradict the Original SAP.

#### 3. post hoc analysis definition

- **evaluation type:** semantic
- **generated SAP text:** Changes to the planned analyses, if any, designed after database lock and/or unblinding will be considered post hoc analyses and will be applied as exploratory methodology.
- **matches original SAP:** no
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard administrative definition added in the Generated SAP. Does not contradict the Original SAP.

#### 4. post hoc identification

- **evaluation type:** semantic
- **generated SAP text:** All post hoc analyses will be identified in the clinical study report.
- **matches original SAP:** no
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard administrative definition added in the Generated SAP. Does not contradict the Original SAP.

#### 5. descriptive statistics (continuous)

- **evaluation type:** semantic
- **original SAP text:** Continuous data will be summarized using descriptive statistics: the number of observations (n), mean, standard deviation, minimum, median and maximum unless otherwise indicated.
- **generated SAP text:** The term “descriptive statistics” refers to the number of patients (n), mean, median, standard deviation (SD), minimum, and maximum for continuous variables;
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 6. descriptive statistics (categorical)

- **evaluation type:** semantic
- **original SAP text:** Categorical data will be summarized using numbers and percentages of patients.
- **generated SAP text:** and refers to the number and/or percentage of patients (or events) for categorical variables.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 7. summary by treatment arm

- **evaluation type:** semantic
- **original SAP text:** The denominator for all percentages will be the number of patients within the treatment group for the population of interest, unless otherwise indicated.
- **generated SAP text:** Unless specified otherwise, summaries will be presented by treatment arm (CT-P16 and EU-Approved Avastin).
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both specify summarization by treatment group.

#### 8. overall population summary

- **evaluation type:** semantic
- **generated SAP text:** Where specified in Section 6 or Section 7, certain efficacy and safety endpoints may also be summarized for the overall population.
- **matches original SAP:** no
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Additional detail provided in Generated SAP regarding overall summaries. Not a contradiction.

#### 9. primary efficacy analysis model

- **evaluation type:** semantic
- **original SAP text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model...
- **generated SAP text:** For the primary efficacy analysis (see Section 3.7.3), a logistic regression model will be utilized.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both specify logistic regression for the primary analysis.

#### 10. listing content

- **evaluation type:** semantic
- **original SAP text:** Listings will be sorted by the treatment group and then patient number, which is the unique subject identifier and visit, if applicable.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both specify listings will include patient, treatment, and visit.

#### 11. visit windows usage

- **evaluation type:** semantic
- **original SAP text:** EOT and unscheduled visit will not be summarized in visit-based tables, unless otherwise indicated.
- **generated SAP text:** Summaries of efficacy and safety parameters that are presented by-visit will use pre-defined visit windows as described in Section 4.5.
- **matches original SAP:** no
- **protocol text:** Visit window (days) ... ±3 [Schedule of Events]
- **protocol consulted:** yes
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** The Original SAP explicitly states that EOT and unscheduled visits will NOT be summarized in visit-based tables (implying a nominal visit approach). The Generated SAP states that visit-based summaries WILL use pre-defined visit windows (which typically map unscheduled/EOT visits to analysis visits). This is a methodological contradiction. The Protocol defines windows for data collection but does not mandate an analysis strategy.

#### 12. baseline definition reference

- **evaluation type:** semantic
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** Baseline for all assessments is defined in Section 4.2.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP Section 4.2 (visible in context) defines baseline consistently with the Original SAP.

---

### Issues Found (1 items)

#### 1. visit windows usage

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** EOT and unscheduled visit will not be summarized in visit-based tables, unless otherwise indicated.
- **generated SAP text:** Summaries of efficacy and safety parameters that are presented by-visit will use pre-defined visit windows as described in Section 4.5.
- **protocol text:** Visit window (days) ... ±3
- **why they conflict:** Original SAP excludes unscheduled visits from visit summaries (nominal approach), while Generated SAP includes them via windowing.
- **description:** The Generated SAP adopts a visit windowing strategy for summaries, whereas the Original SAP explicitly excludes unscheduled and EOT visits from visit-based tables.
- **reasoning:** This represents a change in statistical methodology. While windowing is a valid approach, it contradicts the specific exclusion instruction in the Original SAP.

---

### Extra Information Flagged (3 items)

#### 1. SAS version specification

- **content:** SAS version specification
- **generated SAP text:** All analyses described in this plan will be performed using SAS v9.4 or higher unless specified otherwise.
- **contradicts:** no
- **detail:** Original SAP has a blank section for Software.
- **reasoning:** Fills a placeholder in the Original SAP.

#### 2. A priori/Post hoc definitions

- **content:** A priori/Post hoc definitions
- **generated SAP text:** The analyses documented here are considered a priori analyses... Changes... will be considered post hoc analyses...
- **contradicts:** no
- **reasoning:** Standard administrative definitions.

#### 3. Overall population summaries

- **content:** Overall population summaries
- **generated SAP text:** Where specified in Section 6 or Section 7, certain efficacy and safety endpoints may also be summarized for the overall population.
- **contradicts:** no
- **reasoning:** Adds flexibility for overall summaries not explicitly mentioned in Original SAP General Considerations.

---

### Missing from Generated SAP (3 items)

#### 1. precision rules

- **original SAP text:** Minimum and maximum will be presented to the same number of decimal places as the raw data, mean and median will be presented to one more decimal place than the raw data, and standard deviation will be presented to two more decimal places than the raw data.
- **reasoning:** Specific rounding rules are missing.

#### 2. limit of quantification rules

- **original SAP text:** For the purpose of summarization, any numeric values recorded below the lower limit or above the upper limit of quantification will be set to the respective limit for all related summaries unless otherwise indicated.
- **reasoning:** Rules for handling values outside quantification limits are missing.

#### 3. missing value display

- **original SAP text:** A row denoted “Not Done” will be included in count tabulations where necessary to account for cases of no assessment or missing values.
- **reasoning:** Instruction to include a 'Not Done' row is missing.

---

### Internal Contradictions (0 items)

*No internal contradictions.*

---

### Reasoning

The General Methodology section is largely consistent with the Original SAP regarding descriptive statistics and general reporting conventions. It fills in missing administrative details (Software, A priori definitions) appropriately. However, there is a methodological contradiction regarding the handling of visit-based summaries: the Original SAP explicitly excludes unscheduled and EOT visits (implying a nominal visit approach), while the Generated SAP explicitly uses visit windows (implying mapping of these visits to analysis timepoints). Several specific data handling rules (precision, LOQ handling) from the Original SAP are missing.

---

### Summary

The section is generally accurate but contains a methodological contradiction regarding the use of visit windows versus nominal visits for summaries. It also omits specific data handling rules (precision, LOQ) present in the Original SAP.