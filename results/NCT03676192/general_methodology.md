## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **sections read:** 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9
- **elements per section:** 4: 21, 4.1: 0, 4.2: 2, 4.3: 9, 4.4: 25, 4.5: 2, 4.6: 10, 4.7: 1, 4.8: 3, 4.9: 7
- **paragraphs processed:** 80
- **elements extracted:** 80
- **elements in evaluation table:** 20
- **elements in missing from generated SAP:** 60
- **counts match:** True

---

### Evaluation Table (20 items)

#### 1. Descriptive statistics definition

- **evaluation type:** exact_match
- **original SAP text:** Continuous data will be summarized using descriptive statistics: the number of observations (n), mean, standard deviation, minimum, median and maximum unless otherwise indicated.
- **generated SAP text:** The term “descriptive statistics” refers to the number of patients (n), mean, median, standard deviation (SD), minimum, and maximum for continuous variables
- **matches original SAP:** yes
- **protocol text:** Continuous variables will be summarized by reporting the number of observations (n), mean, standard deviation, median, minimum, and maximum.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 2. Categorical data summary

- **evaluation type:** exact_match
- **original SAP text:** Categorical data will be summarized using numbers and percentages of patients.
- **generated SAP text:** refers to the number and/or percentage of patients (or events) for categorical variables.
- **matches original SAP:** yes
- **protocol text:** Categorical variables will be summarized using frequency tables showing the number and percentage of patients within a particular category.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 3. Listing content

- **evaluation type:** exact_match
- **original SAP text:** But, all data will be displayed in listings.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **matches original SAP:** yes
- **protocol text:** Data will be listed.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent requirement.

#### 4. Stratification factors

- **evaluation type:** exact_match
- **original SAP text:** stratified by country, sex (female vs. male), disease status (recurrence vs. metastatic), Eastern Cooperative Oncology Group (ECOG) performance status (0 vs. 1).
- **generated SAP text:** Covariates will include the stratification factors: sex (female vs. male), disease status (recurrence vs. metastatic), and ECOG performance score (0 vs. 1). Country will be included as a covariate
- **matches original SAP:** yes
- **protocol text:** stratified by country, sex (female vs. male), disease status (recurrence vs. metastatic), and ECOG performance score (0 vs. 1)
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Factors match.

#### 5. Double-blind design

- **evaluation type:** exact_match
- **original SAP text:** This study will be double-blinded during both the Induction Study Period and the Maintenance Study Period.
- **generated SAP text:** A Double-Blind... Study
- **matches original SAP:** yes
- **protocol text:** This study will be double-blind
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Design matches.

#### 6. Unblinding for reporting

- **evaluation type:** exact_match
- **original SAP text:** The database will be unblinded for the 1st CSR for a reporting purpose.
- **generated SAP text:** At this time, the study will be unblinded to pre-defined personnel from the Sponsor and Contract Research Organization (CRO) for reporting purposes
- **matches original SAP:** yes
- **protocol text:** The study will be unblinded to the pre-defined unblinded personnel... after the completion of Cycle 6... for the reporting purposes.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Procedure matches.

#### 7. Blinding maintenance

- **evaluation type:** exact_match
- **original SAP text:** However, the study will remain blinded to the investigators and patients until study termination.
- **generated SAP text:** The study will remain blinded to the investigators, patients, and other pre-defined blinded personnel until the end of the study.
- **matches original SAP:** yes
- **protocol text:** The study will remain blinded to the investigators, patients... until all patients have completed the study
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Procedure matches.

#### 8. ITT Definition

- **evaluation type:** semantic
- **original SAP text:** The ITT population will consist of all randomized patients who are randomly assigned to study drug regardless of whether or not any study treatment dosing is completed and successfully screened based on the ‘Screening Pass/Fail’ eCRF page.
- **generated SAP text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **matches original SAP:** no
- **protocol text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP omits 'successfully screened' clause found in Original SAP, but matches Protocol definition exactly. Therefore correct.

#### 9. Treatment assignment (ITT)

- **evaluation type:** exact_match
- **original SAP text:** Patients will be assigned to treatment groups based on randomization.
- **generated SAP text:** Patients will be assigned to treatment groups based on randomization.
- **matches original SAP:** yes
- **protocol text:** Patients will be assigned to treatment groups based on randomization.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 10. Primary efficacy population

- **evaluation type:** semantic
- **original SAP text:** The primary population for the primary efficacy analysis will be the ITT population.
- **generated SAP text:** For the primary objective to be met, equivalence must be demonstrated in both populations [ITT and PP].
- **matches original SAP:** no
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **protocol consulted:** yes
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP designates ITT as primary and PP as supportive (Section 4.4.2). Generated SAP requires equivalence in BOTH populations for success, which is a stricter decision criterion not explicitly mandated by the Protocol (which just says analysis is performed in both).

#### 11. PP Definition

- **evaluation type:** exact_match
- **original SAP text:** The PP population will consist of all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug... and who do not have any major protocol deviations
- **generated SAP text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug... and who do not have any major protocol deviation.
- **matches original SAP:** yes
- **protocol text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose of study drug... and who do not have any major protocol deviation.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 12. PP Determination timing

- **evaluation type:** exact_match
- **original SAP text:** Final determination of the PP population was made at the Data Review Meeting (DRM) before unblinding.
- **generated SAP text:** Final determinations of the PP population will be made at the blinded data review meeting before unblinding.
- **matches original SAP:** yes
- **protocol text:** Final determinations of the PP population will be made at the blinded data review meeting before unblinding.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 13. PK Definition

- **evaluation type:** exact_match
- **original SAP text:** The PK population will consist of all randomly assigned patients who receive at least one full dose... of study drug... and who have at least one post treatment PK result.
- **generated SAP text:** The PK population is defined as all patients who receive at least one full dose of study drug... and who have at least one post treatment PK result.
- **matches original SAP:** yes
- **protocol text:** The PK population is defined as all patients who receive at least one full dose of study drug... and who have at least one post treatment PK result.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 14. Safety Definition

- **evaluation type:** exact_match
- **original SAP text:** The safety population will consist of all randomly assigned patients who receive at least one dose (partial or full) of study drug
- **generated SAP text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **matches original SAP:** yes
- **protocol text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 15. Safety Assignment

- **evaluation type:** exact_match
- **original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received.
- **generated SAP text:** Patients will be assigned to treatment groups based on treatment actually received.
- **matches original SAP:** yes
- **protocol text:** Patients will be assigned to treatment groups based on treatment actually received.
- **protocol consulted:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 16. Baseline definition

- **evaluation type:** exact_match
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** Baseline Value: Defined as the last non-missing observation... recorded prior to the First Dose Date.
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 17. Post-baseline definition

- **evaluation type:** exact_match
- **original SAP text:** Post-baseline visits will be considered to be all visits after the first infusion.
- **generated SAP text:** For assessments on or after Study Day 1
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 18. Protocol Deviation Identification

- **evaluation type:** exact_match
- **original SAP text:** Major protocol deviations will be identified during the DRM.
- **generated SAP text:** Final determinations... made at the blinded data review meeting
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent.

#### 19. ORR Missing Handling

- **evaluation type:** exact_match
- **original SAP text:** Missing values in ORR will be considered as ‘Non-responder’ to analyze primary efficacy endpoint.
- **generated SAP text:** Patients with no post-baseline tumor assessment or whose response cannot be evaluated (NE) will be treated as non-responders for the primary analysis.
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 20. NE Handling

- **evaluation type:** exact_match
- **original SAP text:** No response evaluation result or inevaluable (NE) result evaluated in best overall response (BOR) will be considered as missing case.
- **generated SAP text:** Patients with... (NE) will be treated as non-responders
- **matches original SAP:** yes
- **protocol consulted:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches (Original SAP implies missing = non-responder).

---

### Issues Found (1 items)

#### 1. Primary efficacy decision criteria

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** The primary analysis will be conducted in the ITT population. A supportive analysis will be conducted in the PP population.
- **generated SAP text:** For the primary objective to be met, equivalence must be demonstrated in both populations [ITT and PP].
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **why they conflict:** Original SAP defines ITT as primary and PP as supportive. Generated SAP requires success in BOTH populations, which is a stricter hurdle not explicitly mandated by Protocol or Original SAP.
- **description:** Generated SAP elevates the Per-Protocol population to a co-primary requirement for study success, contradicting the Original SAP's designation of it as supportive.
- **reasoning:** While the Protocol mentions analysis in both populations, it does not explicitly state that success is required in both. The Original SAP clarifies that ITT is primary. The Generated SAP's requirement for dual success is a significant methodological deviation.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (54 items)

#### 1. Decimal places (Min/Max)

- **original SAP text:** Minimum and maximum will be presented to the same number of decimal places as the raw data
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 2. Decimal places (Mean/Median)

- **original SAP text:** mean and median will be presented to one more decimal place than the raw data
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 3. Decimal places (SD)

- **original SAP text:** standard deviation will be presented to two more decimal places than the raw data.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 4. Decimal places (Geometric Mean)

- **original SAP text:** If the geometric mean is to be presented, it will be set to the same precision as the mean.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 5. Decimal places (CV)

- **original SAP text:** Percent coefficient of variation (CV) will be presented to two more decimal places than the raw data.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 6. Decimal places (Percentages)

- **original SAP text:** Percentages will be presented to one decimal place
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 7. Suppression of zero counts

- **original SAP text:** and will be suppressed when the count is zero.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 8. Not Done row

- **original SAP text:** A row denoted “Not Done” will be included in count tabulations where necessary to account for cases of no assessment or missing values.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 9. Denominator definition

- **original SAP text:** The denominator for all percentages will be the number of patients within the treatment group for the population of interest, unless otherwise indicated.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 10. Listing sorting

- **original SAP text:** Listings will be sorted by the treatment group and then patient number, which is the unique subject identifier and visit, if applicable.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 11. Additional sorting

- **original SAP text:** In cases where more additional sorting is required, other variables will be included in sorting as applicable.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 12. LOQ handling

- **original SAP text:** For the purpose of summarization, any numeric values recorded below the lower limit or above the upper limit of quantification will be set to the respective limit for all related summaries unless otherwise indicated.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 13. Inequality signs in listings

- **original SAP text:** In listings, original results containing inequality sign will be displayed, unless otherwise specified.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Formatting detail missing.

#### 14. Discrepancy handling 1

- **original SAP text:** Recorded as collected sample in eCRF but no corresponding results from analytical facility – listing will display only sample collection visit/date/time from eCRF.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Data handling detail missing.

#### 15. Discrepancy handling 2

- **original SAP text:** No corresponding records in eCRF for results from analytical facility – listing will display only specimen collection visit/date and results from analytical facility.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Data handling detail missing.

#### 16. Discrepancy handling 3

- **original SAP text:** Discrepancy in sample collection date from eCRF and analytical facility – listing will display results from analytical facility and visit/date/time from eCRF if not missing
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Data handling detail missing.

#### 17. Discrepancy handling 4

- **original SAP text:** if sample collection date/time is missing in eCRF then use specimen collection visit/date from analytical facility.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Data handling detail missing.

#### 18. Sample size calculation

- **original SAP text:** A sample size of 305 patients per group will provide 80% power to show similarity in efficacy between CT-P16 and EU-Approved Avastin based on the expected ORR of 38% with an equivalence margin of -12.5 to 12.5 using a 95% CI (two one-sided alpha 0.025) of the difference in ORR.
- **protocol text:** A sample size of 305 patients per group will provide 80% power to show similarity in efficacy between CT-P16 and EU-Approved Avastin based on the expected ORR of 38% with an equivalence margin of -12.5 to 12.5 using a 95% CI (two one-sided alpha 0.025) of the difference in ORR.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Sample size calculation details missing from Generated SAP.

#### 19. Total enrollment

- **original SAP text:** Approximately 678 patients (339 in each group) will need to be enrolled for the anticipated drop-out rate of 10%.
- **protocol text:** Approximately 678 patients (339 in each group) will need to be enrolled for the anticipated drop-out rate of 10%.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Total enrollment details missing from Generated SAP.

#### 20. IWRS

- **original SAP text:** An Interactive Web Response System (IWRS) will be used for the randomization
- **protocol text:** An interactive voice response system (IVRS) or an interactive web response system (IWRS) will be used for the randomization
- **in protocol:** yes
- **classification:** missing_required
- **description:** Randomization system details missing.

#### 21. Unblinded statistician

- **original SAP text:** and an unblinded statistician will generate a computer-generated randomization schedule for IWRS, which will link sequential patient randomization numbers to treatment codes.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific role detail missing.

#### 22. Randomization ratio

- **original SAP text:** Patients who qualify for randomization will be randomly assigned on Day 1 of Cycle 1 in the Induction Study Period in a 1:1 ratio to receive CT-P16 or EU-Approved Avastin.
- **protocol text:** randomly assigned in a 1:1 ratio
- **in protocol:** yes
- **classification:** missing_required
- **description:** Randomization ratio missing.

#### 23. Permuted blocks

- **original SAP text:** The randomization will be balanced by using permuted blocks
- **protocol text:** balanced by using permuted blocks
- **in protocol:** yes
- **classification:** missing_required
- **description:** Randomization method missing.

#### 24. Code secrecy

- **original SAP text:** The randomization code will not be revealed to study patients, investigators, or study site personnel, until all final clinical data have been entered onto the database and the database is locked and released for analysis.
- **protocol text:** The randomization codes will not be revealed to study patients, investigators, and study site personnel... until all final clinical data have been entered into the database
- **in protocol:** yes
- **classification:** missing_required
- **description:** Blinding maintenance details missing.

#### 25. Population tabulation

- **original SAP text:** The number of patients in each population will be tabulated by treatment group for the ITT population.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Reporting detail missing.

#### 26. Population listing

- **original SAP text:** A listing will also be provided displaying this data.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Reporting detail missing.

#### 27. Full dose definition

- **original SAP text:** A patient will be considered as receiving full dose if the planned dose is recorded as ‘15mg/kg’ and the action taken is recorded as ‘Dose Not Changed’ on ‘Study Treatment Administration’ eCRF page.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific definition of 'full dose' missing.

#### 28. Supportive analysis (PP)

- **original SAP text:** A supportive efficacy analysis will be repeated using the PP population.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Generated SAP elevates PP to co-primary (see issues).

#### 29. Incorrect treatment exclusion (PK)

- **original SAP text:** Patients who received incorrect treatment during the Induction Study Period will be excluded from the PK population.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Exclusion criteria missing.

#### 30. PK Maintenance Subset Definition

- **original SAP text:** The PK population – Maintenance Period Subset will consist of all patients in PK population who received at least 1 dose (full) of either of the study drugs and have at least one post treatment PK result during the Maintenance Study Period.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Population subset missing.

#### 31. PK Maintenance Subset Exclusion

- **original SAP text:** Patients who received incorrect treatment during the Maintenance Study Period will be excluded from the PK population – Maintenance Period Subset.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Population subset missing.

#### 32. PK Maintenance Subset DRM

- **original SAP text:** If a patient does not receive full dose, the patient will be discussed during the DRM to confirm whether the patient can be considered as receiving full dose or not.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Population subset missing.

#### 33. PK Maintenance Subset Assignment

- **original SAP text:** Patients will be assigned to treatment groups based on treatment they actually received.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Population subset missing.

#### 34. Received definition (Safety)

- **original SAP text:** A patient will be considered to have received study drug if the patient is recorded as having study drug administered on the ‘Study Treatment Administration’ eCRF page.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific definition missing.

#### 35. Kit number

- **original SAP text:** Treatment patients actually received will be based on the kit number recorded on the ‘Study Treatment Administration’ eCRF page.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Data source detail missing.

#### 36. CT-P16 assignment rule

- **original SAP text:** Patients receiving at least one dose of CT-P16 will be analyzed under the CT-P16 treatment group.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific assignment rule missing.

#### 37. Avastin assignment rule

- **original SAP text:** All other patients will be analyzed under the EU-Approved Avastin treatment group.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific assignment rule missing.

#### 38. Major Protocol Deviation Definition

- **original SAP text:** A major protocol deviation is one that may affect the interpretation of primary endpoint or the patient’s rights, safety or welfare.
- **protocol text:** A major protocol deviation is one that may affect the interpretation of primary endpoint and it will be defined in the SAP.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Definition of Major Protocol Deviations missing (Protocol delegates to SAP, Gen SAP fails to define).

#### 39. Mis-randomization PD

- **original SAP text:** Major protocol deviations include the following: Mis-randomizations (defined as patients who received the opposite treatment to which they were assigned)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific PD missing.

#### 40. IE Criteria PD

- **original SAP text:** Non-compliance of Inclusion or Exclusion criteria
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific PD missing.

#### 41. GCP PD

- **original SAP text:** Significant Good Clinical Practice (GCP) non-compliance (to be identified by as sites which have been closed due to scientific misconduct and/or serious GCP non-compliance)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific PD missing.

#### 42. Prohibited Therapy PD

- **original SAP text:** Receiving any prohibited therapies (Section 5.10 of protocol)
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific PD missing.

#### 43. Missing Efficacy PD

- **original SAP text:** Missing primary efficacy assessment
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific PD missing.

#### 44. PD Summary/Listing

- **original SAP text:** The major protocol deviations will be summarized by treatment group for the ITT population and will also be presented in a listing.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Reporting detail missing.

#### 45. COVID-19 PD

- **original SAP text:** Additionally, if any case of major protocol deviation related to COVID-19 is identified during the DRM, primary analysis will be performed excluding patients with major protocol deviation related to COVID-19 in ITT population as supportive analysis and the patients will be flagged in listing.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** COVID-19 handling missing.

#### 46. General Comments Listing

- **original SAP text:** Data collected on the ‘General Comments’ eCRF page will be presented in a listing for the ITT population.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Listing missing.

#### 47. Outlier Investigation

- **original SAP text:** Any outliers that are detected during the review of the data will be investigated and discussed during the DRM.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Process missing.

#### 48. Outlier Exclusion

- **original SAP text:** In general, outliers will not be excluded unless they are considered to be erroneous values.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Process missing.

#### 49. Outlier Sensitivity

- **original SAP text:** Sensitivity analyses and exploratory analyses may be conducted using imputation or excluding outliers to ensure robustness of study conclusions.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Process missing.

#### 50. Tipping point analysis

- **original SAP text:** In order to evaluate the impact of missing data on the primary efficacy endpoint results, additional analyses with tipping point analyses will be conducted for the primary efficacy endpoint (central review data) for ITT population.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Sensitivity analysis missing.

#### 51. MNAR scenarios

- **original SAP text:** Tipping point analyses will be conducted under Missing Not at Random (MNAR) scenarios.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Sensitivity analysis missing.

#### 52. Shift imputation

- **original SAP text:** Imputation will be done by gradually shifting the number of responders by treatment group to make MNAR scenarios.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Sensitivity analysis missing.

#### 53. Exact binomial/Shift table

- **original SAP text:** 95% CI of the difference between two proportions (CT-P16 and EU-Approved Avastin group) will be estimated by exact binomial approach, and scenarios will be displayed by shift table.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Sensitivity analysis missing.

#### 54. 2D plot

- **original SAP text:** All the scenarios will be also provided using 2-dimensional plot.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Sensitivity analysis missing.

---

### Internal Contradictions (0 items)

*No internal contradictions.*

---

### Reasoning

The Generated SAP generally aligns with the Original SAP and Protocol regarding populations and blinding. However, it introduces a stricter decision criterion for the primary endpoint by requiring equivalence in both ITT and PP populations, whereas the Original SAP designates PP as supportive. Additionally, the Generated SAP fails to include several required elements found in the Protocol, such as sample size calculations, randomization details (IWRS, ratio, blocks), and the definition of major protocol deviations (which the Protocol explicitly delegates to the SAP).

---

### Summary

The Generated SAP is decent but has notable omissions and one methodological contradiction. It fails to define Major Protocol Deviations despite the Protocol delegating this task to the SAP. It also omits required sample size and randomization details found in the Protocol.