## General Methodology Evaluation

**Section:** general_methodology
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **sections read:** 4.1
- **elements per section:** 4.1: 14
- **paragraphs processed:** 14
- **elements extracted:** 13
- **elements in evaluation table:** 9
- **elements in missing from generated SAP:** 4
- **counts match:** True

---

### Evaluation Table (9 items)

#### 1. Software version

- **evaluation type:** exact_match
- **generated SAP text:** All analyses described in this plan will be performed using SAS software version 9.4 or higher unless specified otherwise.
- **matches original SAP:** no
- **protocol consulted:** yes
- **result:** problem
- **issue type:** unverifiable_assumption
- **severity:** critical
- **reasoning:** The Original SAP contains the header '4.1. Software' but provides no text/specification. The Protocol is also silent on software. The Generated SAP specifies 'SAS software version 9.4 or higher'. This constitutes a critical unverifiable assumption as the Generated SAP provides a specific value where the source documents are completely silent.

#### 2. Analysis timing definitions

- **evaluation type:** semantic
- **generated SAP text:** The analyses documented here are considered a priori analyses in that they are defined prior to database lock. Changes to the planned analyses, if any, designed after database lock and/or unblinding will be considered post hoc analyses and will be applied as exploratory methodology. All post hoc analyses will be identified in the clinical study report.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard statistical boilerplate defining a priori vs post hoc analyses. While not explicitly in the Original SAP, it is consistent with standard practice and does not contradict the study design.

#### 3. Descriptive statistics definition

- **evaluation type:** semantic
- **original SAP text:** Continuous data will be summarized using descriptive statistics: the number of observations (n), mean, standard deviation, minimum, median and maximum unless otherwise indicated. ... Categorical data will be summarized using numbers and percentages of patients.
- **generated SAP text:** The term "descriptive statistics" refers to the number of patients (n), mean, median, standard deviation (SD), minimum, and maximum for continuous variables; and refers to the number and percentage of patients for categorical variables.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The definitions of descriptive statistics for continuous and categorical variables match the Original SAP.

#### 4. Confidence intervals and p-values

- **evaluation type:** semantic
- **original SAP text:** 95% CI (two one-sided alpha 0.025)
- **generated SAP text:** Unless specified otherwise, confidence intervals will be presented as 95% and p-values will be presented as 2-sided.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with the specific alpha levels mentioned in the Sample Size section of the Original SAP.

#### 5. Summary stratification

- **evaluation type:** semantic
- **original SAP text:** Categorical data will be summarized using numbers and percentages of patients. ... The denominator for all percentages will be the number of patients within the treatment group for the population of interest
- **generated SAP text:** Unless specified otherwise, summaries will be presented by treatment arm (CT-P16 or EU-Approved Avastin), study period (Induction Study Period, Maintenance Study Period, and/or Whole Study Period, as defined in Section 3.4), and overall.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with the Original SAP's instruction to summarize by treatment group. The addition of study period and overall is consistent with the study design.

#### 6. MedDRA coding version

- **evaluation type:** semantic
- **original SAP text:** Medical history... will be coded using Medical Dictionary for Regulatory Activities (MedDRA) version 24.0 or higher. ... All AEs will be classified by SOC and PT according to the MedDRA version 24.0 or higher.
- **generated SAP text:** Adverse events (AEs) will be coded to system organ class (SOC) and preferred term (PT) using the Medical Dictionary for Regulatory Activities (MedDRA) current version at the time of database lock.
- **matches original SAP:** no
- **protocol text:** Adverse events will be coded to system organ class (SOC) and preferred term (PT) using Medical Dictionary for Regulatory Activities (MedDRA).
- **protocol consulted:** yes
- **result:** problem
- **issue type:** unverifiable_assumption
- **severity:** critical
- **reasoning:** The Original SAP specifies a minimum version ('24.0 or higher'). The Generated SAP uses deferral language ('current version at the time of database lock'). According to the evaluation rules, replacing a minimum threshold with deferral language must be flagged as a critical unverifiable assumption.

#### 7. WHO Drug coding version

- **evaluation type:** semantic
- **original SAP text:** All medications will be coded using WHO Drug Dictionary version March, 2021 or later.
- **generated SAP text:** Prior and concomitant medications will be coded to drug class and PT using the World Health Organization (WHO) Drug Dictionary.
- **matches original SAP:** no
- **protocol text:** Prior and concomitant medication will be coded to drug class and PT using the World Health Organization (WHO) drug dictionary.
- **protocol consulted:** yes
- **result:** problem
- **issue type:** unverifiable_assumption
- **severity:** critical
- **reasoning:** The Original SAP specifies a minimum version ('March, 2021 or later'). The Generated SAP omits the version entirely. According to the evaluation rules, omitting a specific version requirement provided in the Original SAP must be flagged as a critical unverifiable assumption.

#### 8. Listing content

- **evaluation type:** semantic
- **original SAP text:** Listings will be sorted by the treatment group and then patient number, which is the unique subject identifier and visit, if applicable.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches the sorting/content requirements of the Original SAP.

#### 9. Analysis populations in listings

- **evaluation type:** semantic
- **original SAP text:** The number of patients in each population will be tabulated by treatment group for the ITT population. A listing will also be provided displaying this data.
- **generated SAP text:** All analysis populations (as defined in Section 3.3) will be identified in the listings.
- **matches original SAP:** yes
- **protocol consulted:** n/a
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with the requirement to list population data.


---

### Issues Found (3 items)

#### 1. Software version

- **issue type:** unverifiable_assumption
- **severity:** critical
- **generated SAP text:** SAS software version 9.4 or higher
- **why they conflict:** Generated SAP specifies a software version where Original SAP and Protocol are silent.
- **description:** The Generated SAP specifies 'SAS software version 9.4 or higher' while the Original SAP's software section is empty and the Protocol is silent. This is a critical unverifiable assumption.
- **reasoning:** Specifying a software version when the source documents are completely silent constitutes a critical unverifiable assumption according to the evaluation rules.

#### 2. MedDRA coding version

- **issue type:** unverifiable_assumption
- **severity:** critical
- **original SAP text:** MedDRA version 24.0 or higher
- **generated SAP text:** MedDRA current version at the time of database lock
- **protocol text:** Medical Dictionary for Regulatory Activities (MedDRA)
- **why they conflict:** Generated SAP replaces specific minimum version with deferral language.
- **description:** The Original SAP specifies 'version 24.0 or higher', but the Generated SAP defers this to 'current version at the time of database lock'.
- **reasoning:** Replacing a specific minimum version threshold with language that defers the decision to a future time point is a critical unverifiable assumption.

#### 3. WHO Drug coding version

- **issue type:** unverifiable_assumption
- **severity:** critical
- **original SAP text:** WHO Drug Dictionary version March, 2021 or later
- **generated SAP text:** World Health Organization (WHO) Drug Dictionary
- **protocol text:** World Health Organization (WHO) drug dictionary
- **why they conflict:** Generated SAP omits the specific minimum version requirement.
- **description:** The Original SAP specifies 'version March, 2021 or later', but the Generated SAP omits this version requirement entirely.
- **reasoning:** Omitting a specific version requirement provided in the Original SAP is a critical unverifiable assumption.


---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (4 items)

#### 1. Decimal precision rules

- **original SAP text:** Minimum and maximum will be presented to the same number of decimal places as the raw data, mean and median will be presented to one more decimal place than the raw data, and standard deviation will be presented to two more decimal places than the raw data. If the geometric mean is to be presented, it will be set to the same precision as the mean. Percent coefficient of variation (CV) will be presented to two more decimal places than the raw data.
- **why they conflict:** Generated SAP omits specific rounding rules present in Original SAP.
- **description:** Specific rules for decimal precision of descriptive statistics are missing.
- **severity:** minor
- **issue type:** contradiction_original
- **reasoning:** The Original SAP provides detailed instructions on decimal precision which are absent in the Generated SAP.

#### 2. Handling of values outside quantification limits

- **original SAP text:** For the purpose of summarization, any numeric values recorded below the lower limit or above the upper limit of quantification will be set to the respective limit for all related summaries unless otherwise indicated.
- **why they conflict:** Generated SAP omits rules for handling LLOQ/ULOQ values.
- **description:** Rules for handling values below/above quantification limits are missing.
- **severity:** minor
- **issue type:** contradiction_original
- **reasoning:** The Original SAP specifies how to handle values outside quantification limits, which is missing in the Generated SAP.

#### 3. Handling of 'Not Done'

- **original SAP text:** A row denoted “Not Done” will be included in count tabulations where necessary to account for cases of no assessment or missing values.
- **why they conflict:** Generated SAP omits instruction for 'Not Done' category.
- **description:** Instruction to include a 'Not Done' row in tabulations is missing.
- **severity:** minor
- **issue type:** contradiction_original
- **reasoning:** The Original SAP specifies handling of missing assessments in tabulations, which is missing in the Generated SAP.

#### 4. Data discrepancy handling

- **original SAP text:** When combining data from eCRF and analytical facilities discrepancy will be handled as following: 1. Recorded as collected sample in eCRF but no corresponding results from analytical facility... 2. No corresponding records in eCRF for results from analytical facility... 3. Discrepancy in sample collection date...
- **why they conflict:** Generated SAP omits detailed discrepancy handling rules.
- **description:** Detailed rules for handling discrepancies between eCRF and analytical data are missing.
- **severity:** minor
- **issue type:** contradiction_original
- **reasoning:** The Original SAP provides specific logic for data reconciliation which is absent in the Generated SAP.


---

### Internal Contradictions (0 items)

*No internal contradictions.*

---

### Reasoning

The Generated SAP's General Methodology section was evaluated against the Original SAP and Protocol. While standard definitions for descriptive statistics and confidence intervals were correct, the Generated SAP failed on three critical points regarding unverifiable assumptions. First, it specified 'SAS version 9.4' when the Original SAP's software section was empty and the Protocol was silent. Second, it replaced the Original SAP's specific MedDRA version requirement ('24.0 or higher') with deferral language ('current version at lock'). Third, it omitted the Original SAP's specific WHO Drug version requirement ('March, 2021 or later'). Additionally, several specific data handling rules (precision, LLOQ/ULOQ, discrepancies) present in the Original SAP were missing. Due to the presence of critical unverifiable assumptions regarding software and dictionary versions, the rating is POOR.

---

### Summary

The Generated SAP contains critical unverifiable assumptions by specifying a software version where source documents are silent and by omitting or deferring specific dictionary version requirements defined in the Original SAP. Additionally, it lacks detailed rules for decimal precision and data discrepancy handling found in the Original SAP.