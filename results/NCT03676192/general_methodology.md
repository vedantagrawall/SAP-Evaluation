## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **Sections read:** 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9
- **Elements per section:** 4: 21, 4.1: 0, 4.2: 2, 4.3: 9, 4.4: 25, 4.5: 2, 4.6: 10, 4.7: 1, 4.8: 3, 4.9: 7
- **Elements extracted:** 80
- **Elements in evaluation table:** 20
- **Elements in missing from generated SAP:** 60
- **Counts match:** True

---

### Evaluation Table (20 items)

#### 1. Descriptive statistics definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Continuous data will be summarized using descriptive statistics: the number of observations (n), mean, standard deviation, minimum, median and maximum unless otherwise indicated.
- **Generated SAP text:** The term “descriptive statistics” refers to the number of patients (n), mean, median, standard deviation (SD), minimum, and maximum for continuous variables
- **Protocol text:** Continuous variables will be summarized by reporting the number of observations (n), mean, standard deviation, median, minimum, and maximum.
- **Reasoning:** Definitions match.

#### 2. Categorical data summary

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Categorical data will be summarized using numbers and percentages of patients.
- **Generated SAP text:** refers to the number and/or percentage of patients (or events) for categorical variables.
- **Protocol text:** Categorical variables will be summarized using frequency tables showing the number and percentage of patients within a particular category.
- **Reasoning:** Definitions match.

#### 3. Listing content

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** But, all data will be displayed in listings.
- **Generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **Protocol text:** Data will be listed.
- **Reasoning:** Consistent requirement.

#### 4. Stratification factors

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** stratified by country, sex (female vs. male), disease status (recurrence vs. metastatic), Eastern Cooperative Oncology Group (ECOG) performance status (0 vs. 1).
- **Generated SAP text:** Covariates will include the stratification factors: sex (female vs. male), disease status (recurrence vs. metastatic), and ECOG performance score (0 vs. 1). Country will be included as a covariate
- **Protocol text:** stratified by country, sex (female vs. male), disease status (recurrence vs. metastatic), and ECOG performance score (0 vs. 1)
- **Reasoning:** Factors match.

#### 5. Double-blind design

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** This study will be double-blinded during both the Induction Study Period and the Maintenance Study Period.
- **Generated SAP text:** A Double-Blind... Study
- **Protocol text:** This study will be double-blind
- **Reasoning:** Design matches.

#### 6. Unblinding for reporting

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The database will be unblinded for the 1st CSR for a reporting purpose.
- **Generated SAP text:** At this time, the study will be unblinded to pre-defined personnel from the Sponsor and Contract Research Organization (CRO) for reporting purposes
- **Protocol text:** The study will be unblinded to the pre-defined unblinded personnel... after the completion of Cycle 6... for the reporting purposes.
- **Reasoning:** Procedure matches.

#### 7. Blinding maintenance

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** However, the study will remain blinded to the investigators and patients until study termination.
- **Generated SAP text:** The study will remain blinded to the investigators, patients, and other pre-defined blinded personnel until the end of the study.
- **Protocol text:** The study will remain blinded to the investigators, patients... until all patients have completed the study
- **Reasoning:** Procedure matches.

#### 8. ITT Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The ITT population will consist of all randomized patients who are randomly assigned to study drug regardless of whether or not any study treatment dosing is completed and successfully screened based on the ‘Screening Pass/Fail’ eCRF page.
- **Generated SAP text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **Protocol text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **Reasoning:** Generated SAP omits 'successfully screened' clause found in Original SAP, but matches Protocol definition exactly. Therefore correct.

#### 9. Treatment assignment (ITT)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Patients will be assigned to treatment groups based on randomization.
- **Generated SAP text:** Patients will be assigned to treatment groups based on randomization.
- **Protocol text:** Patients will be assigned to treatment groups based on randomization.
- **Reasoning:** Matches.

#### 10. Primary efficacy population

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** contradiction_original
- **Severity:** minor
- **Original SAP text:** The primary population for the primary efficacy analysis will be the ITT population.
- **Generated SAP text:** For the primary objective to be met, equivalence must be demonstrated in both populations [ITT and PP].
- **Protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **Reasoning:** Original SAP designates ITT as primary and PP as supportive (Section 4.4.2). Generated SAP requires equivalence in BOTH populations for success, which is a stricter decision criterion not explicitly mandated by the Protocol (which just says analysis is performed in both).

#### 11. PP Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The PP population will consist of all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug... and who do not have any major protocol deviations
- **Generated SAP text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug... and who do not have any major protocol deviation.
- **Protocol text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug... and who do not have any major protocol deviation.
- **Reasoning:** Matches.

#### 12. PP Determination timing

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Final determination of the PP population was made at the Data Review Meeting (DRM) before unblinding.
- **Generated SAP text:** Final determinations of the PP population will be made at the blinded data review meeting before unblinding.
- **Protocol text:** Final determinations of the PP population will be made at the blinded data review meeting before unblinding.
- **Reasoning:** Matches.

#### 13. PK Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The PK population will consist of all randomly assigned patients who receive at least one full dose... of study drug... and who have at least one post treatment PK result.
- **Generated SAP text:** The PK population is defined as all patients who receive at least one full dose of study drug... and who have at least one post treatment PK result.
- **Protocol text:** The PK population is defined as all patients who receive at least one full dose of study drug... and who have at least one post treatment PK result.
- **Reasoning:** Matches.

#### 14. Safety Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The safety population will consist of all randomly assigned patients who receive at least one dose (partial or full) of study drug
- **Generated SAP text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **Protocol text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **Reasoning:** Matches.

#### 15. Safety Assignment

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received.
- **Generated SAP text:** Patients will be assigned to treatment groups based on treatment actually received.
- **Protocol text:** Patients will be assigned to treatment groups based on treatment actually received.
- **Reasoning:** Matches.

#### 16. Baseline definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **Generated SAP text:** Baseline Value: Defined as the last non-missing observation... recorded prior to the First Dose Date.
- **Reasoning:** Matches.

#### 17. Post-baseline definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Post-baseline visits will be considered to be all visits after the first infusion.
- **Generated SAP text:** For assessments on or after Study Day 1
- **Reasoning:** Matches.

#### 18. Protocol Deviation Identification

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Major protocol deviations will be identified during the DRM.
- **Generated SAP text:** Final determinations... made at the blinded data review meeting
- **Reasoning:** Consistent.

#### 19. ORR Missing Handling

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Missing values in ORR will be considered as ‘Non-responder’ to analyze primary efficacy endpoint.
- **Generated SAP text:** Patients with no post-baseline tumor assessment or whose response cannot be evaluated (NE) will be treated as non-responders for the primary analysis.
- **Reasoning:** Matches.

#### 20. NE Handling

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** No response evaluation result or inevaluable (NE) result evaluated in best overall response (BOR) will be considered as missing case.
- **Generated SAP text:** Patients with... (NE) will be treated as non-responders
- **Reasoning:** Matches (Original SAP implies missing = non-responder).

---

### Issues Found (1 items)

#### Issue 1: Primary efficacy decision criteria

- **Issue type:** contradiction_original
- **Severity:** minor
- **Original SAP text:** The primary analysis will be conducted in the ITT population. A supportive analysis will be conducted in the PP population.
- **Generated SAP text:** For the primary objective to be met, equivalence must be demonstrated in both populations [ITT and PP].
- **Protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **Why they conflict:** Original SAP defines ITT as primary and PP as supportive. Generated SAP requires success in BOTH populations, which is a stricter hurdle not explicitly mandated by Protocol or Original SAP.
- **Description:** Generated SAP elevates the Per-Protocol population to a co-primary requirement for study success, contradicting the Original SAP's designation of it as supportive.
- **Reasoning:** While the Protocol mentions analysis in both populations, it does not explicitly state that success is required in both. The Original SAP clarifies that ITT is primary. The Generated SAP's requirement for dual success is a significant methodological deviation.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (54 items)

#### Missing 1: Decimal places (Min/Max)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Minimum and maximum will be presented to the same number of decimal places as the raw data
- **Description:** Formatting detail missing.

#### Missing 2: Decimal places (Mean/Median)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** mean and median will be presented to one more decimal place than the raw data
- **Description:** Formatting detail missing.

#### Missing 3: Decimal places (SD)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** standard deviation will be presented to two more decimal places than the raw data.
- **Description:** Formatting detail missing.

#### Missing 4: Decimal places (Geometric Mean)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** If the geometric mean is to be presented, it will be set to the same precision as the mean.
- **Description:** Formatting detail missing.

#### Missing 5: Decimal places (CV)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Percent coefficient of variation (CV) will be presented to two more decimal places than the raw data.
- **Description:** Formatting detail missing.

#### Missing 6: Decimal places (Percentages)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Percentages will be presented to one decimal place
- **Description:** Formatting detail missing.

#### Missing 7: Suppression of zero counts

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** and will be suppressed when the count is zero.
- **Description:** Formatting detail missing.

#### Missing 8: Not Done row

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** A row denoted “Not Done” will be included in count tabulations where necessary to account for cases of no assessment or missing values.
- **Description:** Formatting detail missing.

#### Missing 9: Denominator definition

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** The denominator for all percentages will be the number of patients within the treatment group for the population of interest, unless otherwise indicated.
- **Description:** Formatting detail missing.

#### Missing 10: Listing sorting

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Listings will be sorted by the treatment group and then patient number, which is the unique subject identifier and visit, if applicable.
- **Description:** Formatting detail missing.

#### Missing 11: Additional sorting

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** In cases where more additional sorting is required, other variables will be included in sorting as applicable.
- **Description:** Formatting detail missing.

#### Missing 12: LOQ handling

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** For the purpose of summarization, any numeric values recorded below the lower limit or above the upper limit of quantification will be set to the respective limit for all related summaries unless otherwise indicated.
- **Description:** Formatting detail missing.

#### Missing 13: Inequality signs in listings

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** In listings, original results containing inequality sign will be displayed, unless otherwise specified.
- **Description:** Formatting detail missing.

#### Missing 14: Discrepancy handling 1

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Recorded as collected sample in eCRF but no corresponding results from analytical facility – listing will display only sample collection visit/date/time from eCRF.
- **Description:** Data handling detail missing.

#### Missing 15: Discrepancy handling 2

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** No corresponding records in eCRF for results from analytical facility – listing will display only specimen collection visit/date and results from analytical facility.
- **Description:** Data handling detail missing.

#### Missing 16: Discrepancy handling 3

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Discrepancy in sample collection date from eCRF and analytical facility – listing will display results from analytical facility and visit/date/time from eCRF if not missing
- **Description:** Data handling detail missing.

#### Missing 17: Discrepancy handling 4

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** if sample collection date/time is missing in eCRF then use specimen collection visit/date from analytical facility.
- **Description:** Data handling detail missing.

#### Missing 18: Sample size calculation

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** A sample size of 305 patients per group will provide 80% power to show similarity in efficacy between CT-P16 and EU-Approved Avastin based on the expected ORR of 38% with an equivalence margin of -12.5 to 12.5 using a 95% CI (two one-sided alpha 0.025) of the difference in ORR.
- **Protocol text:** A sample size of 305 patients per group will provide 80% power to show similarity in efficacy between CT-P16 and EU-Approved Avastin based on the expected ORR of 38% with an equivalence margin of -12.5 to 12.5 using a 95% CI (two one-sided alpha 0.025) of the difference in ORR.
- **Description:** Sample size calculation details missing from Generated SAP.

#### Missing 19: Total enrollment

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** Approximately 678 patients (339 in each group) will need to be enrolled for the anticipated drop-out rate of 10%.
- **Protocol text:** Approximately 678 patients (339 in each group) will need to be enrolled for the anticipated drop-out rate of 10%.
- **Description:** Total enrollment details missing from Generated SAP.

#### Missing 20: IWRS

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** An Interactive Web Response System (IWRS) will be used for the randomization
- **Protocol text:** An interactive voice response system (IVRS) or an interactive web response system (IWRS) will be used for the randomization
- **Description:** Randomization system details missing.

#### Missing 21: Unblinded statistician

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** and an unblinded statistician will generate a computer-generated randomization schedule for IWRS, which will link sequential patient randomization numbers to treatment codes.
- **Description:** Specific role detail missing.

#### Missing 22: Randomization ratio

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** Patients who qualify for randomization will be randomly assigned on Day 1 of Cycle 1 in the Induction Study Period in a 1:1 ratio to receive CT-P16 or EU-Approved Avastin.
- **Protocol text:** randomly assigned in a 1:1 ratio
- **Description:** Randomization ratio missing.

#### Missing 23: Permuted blocks

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The randomization will be balanced by using permuted blocks
- **Protocol text:** balanced by using permuted blocks
- **Description:** Randomization method missing.

#### Missing 24: Code secrecy

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The randomization code will not be revealed to study patients, investigators, or study site personnel, until all final clinical data have been entered onto the database and the database is locked and released for analysis.
- **Protocol text:** The randomization codes will not be revealed to study patients, investigators, and study site personnel... until all final clinical data have been entered into the database
- **Description:** Blinding maintenance details missing.

#### Missing 25: Population tabulation

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** The number of patients in each population will be tabulated by treatment group for the ITT population.
- **Description:** Reporting detail missing.

#### Missing 26: Population listing

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** A listing will also be provided displaying this data.
- **Description:** Reporting detail missing.

#### Missing 27: Full dose definition

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** A patient will be considered as receiving full dose if the planned dose is recorded as ‘15mg/kg’ and the action taken is recorded as ‘Dose Not Changed’ on ‘Study Treatment Administration’ eCRF page.
- **Description:** Specific definition of 'full dose' missing.

#### Missing 28: Supportive analysis (PP)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** A supportive efficacy analysis will be repeated using the PP population.
- **Description:** Generated SAP elevates PP to co-primary (see issues).

#### Missing 29: Incorrect treatment exclusion (PK)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population.
- **Description:** Exclusion criteria missing.

#### Missing 30: PK Maintenance Subset Definition

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** The PK population – Maintenance Period Subset will consist of all patients in PK population who received at least 1 dose (full) of either of the study drugs and have at least one post treatment PK result during the Maintenance Study Period.
- **Description:** Population subset missing.

#### Missing 31: PK Maintenance Subset Exclusion

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Patients who received incorrect treatment during the Maintenance Study Period will be excluded from the PK population – Maintenance Period Subset.
- **Description:** Population subset missing.

#### Missing 32: PK Maintenance Subset DRM

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not.
- **Description:** Population subset missing.

#### Missing 33: PK Maintenance Subset Assignment

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received.
- **Description:** Population subset missing.

#### Missing 34: Received definition (Safety)

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** A patient will be considered to have received study drug if the patient is recorded as having study drug administered on the ‘Study Treatment Administration’ eCRF page.
- **Description:** Specific definition missing.

#### Missing 35: Kit number

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Treatment patients actually received will be based on the kit number recorded on the ‘Study Treatment Administration’ eCRF page.
- **Description:** Data source detail missing.

#### Missing 36: CT-P16 assignment rule

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group.
- **Description:** Specific assignment rule missing.

#### Missing 37: Avastin assignment rule

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** All other patients will be analyzed under the EU-Approved Avastin treatment group.
- **Description:** Specific assignment rule missing.

#### Missing 38: Major Protocol Deviation Definition

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** A major protocol deviation is one that may affect the interpretation of primary endpoint or the patient’s rights, safety or welfare.
- **Protocol text:** A major protocol deviation is one that may affect the interpretation of primary endpoint and it will be defined in the SAP.
- **Description:** Definition of Major Protocol Deviations missing (Protocol delegates to SAP, Gen SAP fails to define).

#### Missing 39: Mis-randomization PD

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Major protocol deviations include the following: Mis-randomizations (defined as patients who received the opposite treatment to which they were assigned)
- **Description:** Specific PD missing.

#### Missing 40: IE Criteria PD

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Non-compliance of Inclusion or Exclusion criteria
- **Description:** Specific PD missing.

#### Missing 41: GCP PD

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Significant Good Clinical Practice (GCP) non-compliance (to be identified by as sites which have been closed due to scientific misconduct and/or serious GCP non-compliance)
- **Description:** Specific PD missing.

#### Missing 42: Prohibited Therapy PD

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Receiving any prohibited therapies (Section 5.10 of protocol)
- **Description:** Specific PD missing.

#### Missing 43: Missing Efficacy PD

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Missing primary efficacy assessment
- **Description:** Specific PD missing.

#### Missing 44: PD Summary/Listing

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** The major protocol deviations will be summarized by treatment group for the ITT population and will also be presented in a listing.
- **Description:** Reporting detail missing.

#### Missing 45: COVID-19 PD

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Additionally, if any case of major protocol deviation related to COVID-19 is identified during the DRM, primary analysis will be performed excluding patients with major protocol deviation related to COVID-19 in ITT population as supportive analysis and the patients will be flagged in listing.
- **Description:** COVID-19 handling missing.

#### Missing 46: General Comments Listing

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Data collected on the ‘General Comments’ eCRF page will be presented in a listing for the ITT population.
- **Description:** Listing missing.

#### Missing 47: Outlier Investigation

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Any outliers that are detected during the review of the data will be investigated and discussed during the DRM.
- **Description:** Process missing.

#### Missing 48: Outlier Exclusion

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** In general, outliers will not be excluded unless they are considered to be erroneous values.
- **Description:** Process missing.

#### Missing 49: Outlier Sensitivity

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Sensitivity analyses and exploratory analyses may be conducted using imputation or excluding outliers to ensure robustness of study conclusions.
- **Description:** Process missing.

#### Missing 50: Tipping point analysis

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** In order to evaluate the impact of missing data on the primary efficacy endpoint results, additional analyses with tipping point analyses will be conducted for the primary efficacy endpoint (central review data) for ITT population.
- **Description:** Sensitivity analysis missing.

#### Missing 51: MNAR scenarios

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Tipping point analyses will be conducted under Missing Not at Random (MNAR) scenarios.
- **Description:** Sensitivity analysis missing.

#### Missing 52: Shift imputation

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Imputation will be done by gradually shifting the number of responders by treatment group to make MNAR scenarios.
- **Description:** Sensitivity analysis missing.

#### Missing 53: Exact binomial/Shift table

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** 95% CI of the difference between two proportions (CT-P16 and EU-Approved Avastin group) will be estimated by exact binomial approach, and scenarios will be displayed by shift table.
- **Description:** Sensitivity analysis missing.

#### Missing 54: 2D plot

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** All the scenarios will be also provided using 2-dimensional plot.
- **Description:** Sensitivity analysis missing.

---

### Internal Contradictions (0 items)

*No internal contradictions found.*

---

### Reasoning

The Generated SAP generally aligns with the Original SAP and Protocol regarding populations and blinding. However, it introduces a stricter decision criterion for the primary endpoint by requiring equivalence in both ITT and PP populations, whereas the Original SAP designates PP as supportive. Additionally, the Generated SAP fails to include several required elements found in the Protocol, such as sample size calculations, randomization details (IWRS, ratio, blocks), and the definition of major protocol deviations (which the Protocol explicitly delegates to the SAP).

---

### Summary

The Generated SAP is decent but has notable omissions and one methodological contradiction. It fails to define Major Protocol Deviations despite the Protocol delegating this task to the SAP. It also omits required sample size and randomization details found in the Protocol.