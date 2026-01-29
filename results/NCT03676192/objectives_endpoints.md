## Objectives Endpoints Evaluation

**Section:** objectives_endpoints
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **sections read:** 2.1, 2.2, 8.1, 8.2.1, 8.2.2, 8.2.2.1, 8.2.2.2, 8.2.2.3, 8.2.2.4, 8.2.2.5, 8.3, 8.4
- **elements per section:** 2.1: 1, 2.2: 4, 8.1: 18, 8.2.1: 4, 8.2.2: 12, 8.2.2.1: 5, 8.2.2.2: 6, 8.2.2.3: 5, 8.2.2.4: 3, 8.2.2.5: 8, 8.3: 3, 8.4: 1
- **elements extracted:** 70
- **elements in evaluation table:** 62
- **elements in missing from generated SAP:** 8
- **counts match:** True

---

### Evaluation Table (91 items)

#### 1. Primary Objective

- **evaluation type:** exact_match
- **original SAP text:** To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) during the Induction Study Period
- **generated SAP text:** To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) up to Cycle 6 during the Induction Study Period
- **protocol text:** To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) up to Cycle 6 during the Induction Study Period
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 2. Secondary Objective: Efficacy Profiles

- **evaluation type:** exact_match
- **original SAP text:** To evaluate additional efficacy profiles including ORR during the Whole Study Period, response duration, time to progression (TTP), progression-free survival (PFS), and overall survival (OS)
- **generated SAP text:** To evaluate additional efficacy profiles including ORR during the Whole Study Period, response duration, time to progression (TTP), progression-free survival (PFS), and overall survival (OS)
- **protocol text:** To evaluate additional efficacy profiles including ORR during the Whole Study Period, response duration, time to progression (TTP), progression-free survival (PFS), and overall survival (OS)
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 3. Secondary Objective: PK

- **evaluation type:** exact_match
- **original SAP text:** To evaluate the Pharmacokinetic (PK) parameter of trough serum concentration (Ctrough)
- **generated SAP text:** To evaluate the pharmacokinetics (PK) of trough serum concentration (Ctrough)
- **protocol text:** To evaluate the pharmacokinetics (PK) of trough serum concentration (Ctrough)
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 4. Secondary Objective: Safety

- **evaluation type:** exact_match
- **original SAP text:** To evaluate safety profile including immunogenicity
- **generated SAP text:** To evaluate safety profile including immunogenicity
- **protocol text:** To evaluate safety profile including immunogenicity
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 5. Secondary Objective: QoL

- **evaluation type:** exact_match
- **original SAP text:** To evaluate quality of life (QoL)
- **generated SAP text:** To evaluate quality of life (QoL)
- **protocol text:** To evaluate quality of life (QoL)
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 6. Primary Endpoint Definition

- **evaluation type:** exact_match
- **original SAP text:** The primary efficacy endpoint is ORR based on BOR during the Induction Study Period by RECIST version 1.1
- **generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR) during the Induction Study Period (up to Cycle 6) as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **protocol text:** Objective response rate (ORR, %) based on BOR during the Induction Study Period by RECIST v.1.1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 7. ORR Definition

- **evaluation type:** semantic
- **original SAP text:** The ORR is defined as the proportion of patients with a confirmed BOR of CR or PR (the 'responder').
- **generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR)
- **protocol text:** Objective response rate will be calculated as the number of patients with a response of CR or PR divided by the number of patients in the corresponding population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 8. Non-responder Definition

- **evaluation type:** semantic
- **original SAP text:** All other patients in the ITT or PP population except responders will be considered as non-responder including patients without post-baseline tumor assessment.
- **generated SAP text:** Patients with no post-baseline tumor assessment or whose response cannot be evaluated (NE) will be treated as non-responders for the primary analysis.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 9. Similarity Criterion

- **evaluation type:** exact_match
- **original SAP text:** The similarity criterion has been set such that the confidence limits of the 95% CI of the difference in ORR from each treatment group will be entirely bounded by the interval (-12.5, 12.5).
- **generated SAP text:** Therapeutic similarity will be concluded if the 2-sided 95% CI for the difference in ORR is entirely contained within the equivalence margin of (-12.5%, 12.5%).
- **protocol text:** The similarity criterion has been set such that the confidence limits of the 95% CI of the difference in ORR will be entirely bounded by the interval (-12.5, 12.5).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 10. Primary Analysis Model

- **evaluation type:** semantic
- **original SAP text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance status at baseline (0 vs. 1) as covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect.
- **generated SAP text:** The model will include treatment group as a fixed effect. Covariates will include the stratification factors: sex (female vs. male), disease status (recurrence vs. metastatic), and ECOG performance score (0 vs. 1). Country will be included as a covariate unless there are sparse data across centers/countries, in which case it may be pooled by region.
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 11. Pooling Country

- **evaluation type:** semantic
- **original SAP text:** Country can be pooled into region (EMEA vs. America vs. Asia) for statistical analysis when there are not enough patients within each country.
- **generated SAP text:** Country will be included as a covariate unless there are sparse data across centers/countries, in which case it may be pooled by region.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 12. ORR Difference Calculation

- **evaluation type:** semantic
- **original SAP text:** A point estimate and 95% CI of the risk difference of ORR between CT-P16 group and EU-Approved Avastin group will be produced.
- **generated SAP text:** Population-level Summary: Difference in ORR (%) between CT-P16 and EU-Approved Avastin.
- **protocol text:** The resulting odds ratio and 95% CI will be converted into difference of proportions using the Delta method for the purpose of comparison.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 13. Primary Analysis Population

- **evaluation type:** exact_match
- **original SAP text:** The primary analysis will be conducted in the ITT population.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 14. Supportive Analysis Population

- **evaluation type:** exact_match
- **original SAP text:** A supportive analysis will be conducted in the PP population and also be provided in the table.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 15. Central Review for Primary

- **evaluation type:** exact_match
- **original SAP text:** For the primary analysis, central review results will be used.
- **generated SAP text:** as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **protocol text:** For primary analysis, central review result will be used.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 16. Local Review Sensitivity

- **evaluation type:** exact_match
- **original SAP text:** Local review results will be used for a sensitivity analysis.
- **generated SAP text:** The primary analysis methodology described in Section 6.1.1.2 will be repeated using the BOR as determined by the investigator's local review to support the findings of the central review.
- **protocol text:** Local review result will be used as supportive data (sensitivity analysis).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 17. Delta Method Usage

- **evaluation type:** semantic
- **original SAP text:** The Delta Method for estimating difference of proportion is explained in the following process.
- **generated SAP text:** The resulting odds ratio and its 95% CI will be converted into a difference in proportions (CT-P16 – EU-Approved Avastin) using the Delta method.
- **protocol text:** The resulting odds ratio and 95% CI will be converted into difference of proportions using the Delta method for the purpose of comparison.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Specific formulas for Delta method calculation (steps 1-5)
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP mentions Delta method but omits the explicit formulas provided in Original SAP.

#### 18. Secondary Endpoint: Whole Study ORR

- **evaluation type:** exact_match
- **original SAP text:** For the secondary efficacy endpoint, ORR based on BOR during the Whole Study Period by RECIST version 1.1 will be analyzed.
- **generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed for both the ITT and PP populations.
- **protocol text:** ORR based on BOR during the Whole Study Period by RECIST v.1.1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 19. Whole Study ORR Populations

- **evaluation type:** exact_match
- **original SAP text:** A table will be produced using both central review data and local review data from all treatment periods including Induction Study Period, Maintenance Study Period and EOT visit in the ITT and PP population.
- **generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed for both the ITT and PP populations.
- **protocol text:** The secondary endpoint, both locally reviewed ORR and centrally reviewed ORR during the Whole Study Period, will be summarized using proportion and its corresponding 95% CI for each treatment group in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 20. TTE Analysis Endpoints

- **evaluation type:** exact_match
- **original SAP text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population.
- **generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations. - Progression-Free Survival (PFS)... - Time to Progression (TTP)... - Overall Survival (OS)... - Response Duration...
- **protocol text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 21. TTE Summaries

- **evaluation type:** semantic
- **original SAP text:** The number of patients experiencing events and the number of censored patients will be summarized by treatment group with reasons for an event/censoring.
- **generated SAP text:** The number of patients experiencing events and the number of censored patients will be summarized by treatment group with reasons for an event/censoring.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 22. KM Method

- **evaluation type:** exact_match
- **original SAP text:** The median survival time and its corresponding 95% CI for each treatment group will be estimated using the Kaplan-Meier method.
- **generated SAP text:** Kaplan-Meier (KM) Method: Used to estimate the survival distributions for each treatment group. Summary Statistics: Median TTE... will be calculated with 95% CIs.
- **protocol text:** the median time and its corresponding 95% CI for each treatment group for each secondary endpoint of time-to-event analysis will be estimated using the Kaplan-Meier method.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 23. Brookmeyer-Crowley

- **evaluation type:** exact_match
- **original SAP text:** The Brookmeyer-Crowley methodology will be used to construct the 95% CI for each percentile.
- **generated SAP text:** The 95% CI for the median will be calculated using the Brookmeyer-Crowley method.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 24. Survival Rates

- **evaluation type:** semantic
- **original SAP text:** In addition, the estimate of survival rates (at 6, 12, 24, 36 months for response duration, TTP, PFS and at 12, 24, 36 months for OS) will be displayed along with their corresponding 95% CI.
- **generated SAP text:** survival rates at specific landmarks (e.g., 6 months, 12 months) will be calculated with 95% CIs.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Specific timepoints (24, 36 months) and distinction between endpoints
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP mentions landmarks but omits the specific list.

#### 25. Cox Regression Model

- **evaluation type:** semantic
- **original SAP text:** In PFS and OS analyses, an adjusted stratified cox regression model will be used to estimate the hazard ratio and its 95% CI for receiving CT-P16 compared with receiving EU-Approved Avastin using country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance score at baseline (0 vs. 1) as stratification factors.
- **generated SAP text:** Hazard Ratio (HR): A stratified Cox proportional hazards model, including the same stratification factors used in the randomization, will be used to estimate the HR (CT-P16 / EU-Approved Avastin) and its 95% CI.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 26. Response Duration Definition

- **evaluation type:** exact_match
- **original SAP text:** Response duration is defined as the time between initial response (CR or PR) that is confirmed by the subsequent assessment after study treatment administration and PD/recurrence or death from any cause (whichever occurs first).
- **generated SAP text:** Response Duration: Time from the first documented response (CR or PR) until the first documentation of PD or death (among responders only).
- **protocol text:** Response duration: the time between initial response (CR or PR) and PD/recurrence
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 27. Response Duration Population

- **evaluation type:** exact_match
- **original SAP text:** Time-to-event analysis for response duration will be performed for patients who have confirmed BOR of CR or PR.
- **generated SAP text:** (among responders only).
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 28. Response Duration Event

- **evaluation type:** exact_match
- **original SAP text:** PD/recurrence or death that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **generated SAP text:** until the first documentation of PD or death
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 29. Response Duration Censoring - No Event

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No event and no anticancer therapy -> Last tumor assessment date
- **generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment, without disease progression/or recurrence.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 30. Response Duration Censoring - New Therapy

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
- **generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment, without disease progression/or recurrence, before starting another anticancer therapy.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 31. Response Duration Censoring - Missing Assessments

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* -> Last tumor assessment date before event
- **generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment, without disease progression/or recurrence.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 32. TTP Definition

- **evaluation type:** exact_match
- **original SAP text:** TTP is defined as time from randomization to determined PD/recurrence.
- **generated SAP text:** Time to Progression (TTP): Time from randomization until the first documentation of PD.
- **protocol text:** TTP: the time from randomization until PD/recurrence
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 33. TTP Event

- **evaluation type:** exact_match
- **original SAP text:** PD/recurrence that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **generated SAP text:** Time to Progression (TTP): Time from randomization until the first documentation of PD.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 34. TTP Censoring - No Assessment

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No tumor assessment -> The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Censoring rule for no tumor assessment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Implicit in standard TTE analysis, but explicitly stated in Original SAP.

#### 35. TTP Censoring - No Event

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No event and no anticancer therapy -> Last tumor assessment date
- **generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 36. TTP Censoring - New Therapy

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
- **generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment... before starting another anticancer therapy.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 37. PFS Definition

- **evaluation type:** exact_match
- **original SAP text:** PFS is defined as time from randomization to determined PD/recurrence or death from any cause (whichever occurs first).
- **generated SAP text:** Progression-Free Survival (PFS): Time from randomization until the first documentation of PD (per RECIST v.1.1) or death due to any cause.
- **protocol text:** PFS: the time from randomization until PD/recurrence or death due to any cause, whichever occurs first
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 38. PFS Event

- **evaluation type:** exact_match
- **original SAP text:** PD/recurrence or death that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 39. PFS Censoring - No Assessment

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No tumor assessment -> The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Censoring rule for no tumor assessment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Implicit.

#### 40. PFS Censoring - No Event

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No event and no anticancer therapy -> Last tumor assessment date
- **generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 41. PFS Censoring - New Therapy

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
- **generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment... before starting another anticancer therapy.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 42. PFS Censoring - Missing Assessments

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* -> Last tumor assessment date before event
- **generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 43. OS Definition

- **evaluation type:** exact_match
- **original SAP text:** OS is defined as time from randomization to death from any cause.
- **generated SAP text:** Overall Survival (OS): Time from randomization until death due to any cause.
- **protocol text:** OS: the time from randomization until death due to any cause
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 44. OS Censoring

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Non-death -> Last known alive date
- **generated SAP text:** Patients alive... will be censored at the date of the last adequate tumor assessment. [Note: This is for PFS/TTP. For OS, standard is last known alive]
- **protocol text:** for patients whose status is unknown, data will be censored at the time when the patient is last known to be alive.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Implied in standard OS analysis.

#### 45. Efficacy Analysis Intro

- **evaluation type:** semantic
- **original SAP text:** Efficacy analyses for the final CSR focus on secondary efficacy endpoints (Section 8.2) based on patients' long-term follow-up data.
- **generated SAP text:** The final analysis will include the final assessment of all secondary efficacy, pharmacokinetic, quality of life, and safety endpoints.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 46. Primary Analysis Completed

- **evaluation type:** semantic
- **original SAP text:** It is noted that the primary efficacy analysis (Section 8.1) was completed in the 1st CSR.
- **generated SAP text:** The primary analysis of efficacy and safety is planned after all patients have completed Cycle 6 of the Induction Study Period
- **protocol text:** The sponsor plans to prepare 3 CSRs to report the following: To report data after completion of the Induction Study Period
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** none
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Tense difference (completed vs planned) due to template nature, acceptable.

#### 47. Primary Endpoint Sensitivity in Final CSR

- **evaluation type:** semantic
- **original SAP text:** In the final CSR, the analysis for the primary efficacy endpoint will be performed as a sensitivity analysis using the same method as 1st CSR.
- **generated SAP text:** The primary analysis methodology described in Section 6.1.1.2 will be repeated using the BOR as determined by the investigator's local review to support the findings of the central review.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches intent.

#### 48. Efficacy Assessment Method

- **evaluation type:** exact_match
- **original SAP text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **generated SAP text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 49. RECIST Version

- **evaluation type:** exact_match
- **original SAP text:** Response evaluation will be based on tumor responses measured and recorded by using Response Evaluation Criteria In Solid Tumors (RECIST) version 1.1.
- **generated SAP text:** as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **protocol text:** Tumor responses will be measured and recorded by using RECIST v.1.1.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 50. BOR Determination

- **evaluation type:** exact_match
- **original SAP text:** The primary endpoint, ORR during the Induction Study Period, and the secondary endpoint, ORR during the Whole Study Period, will be determined by the BOR.
- **generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR)
- **protocol text:** The primary endpoint, ORR during the Induction Study Period, and the secondary endpoint, ORR during the Whole Study Period, will be determined by the best overall response (BOR).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 51. Confirmation Requirement

- **evaluation type:** exact_match
- **original SAP text:** For CR or PR, BOR must be confirmed by the subsequent assessment.
- **generated SAP text:** While the primary endpoint requires confirmation (as per RECIST 1.1)
- **protocol text:** For CR or PR, BOR must be confirmed by the subsequent assessment based on the RECIST v.1.1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 52. Response Categories

- **evaluation type:** exact_match
- **original SAP text:** Categorization of BOR will use the following response categories: CR, PR, SD, PD and NE.
- **generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **protocol text:** Categorization of overall response at each visit will be based on RECIST v.1.1 using the following response categories: CR, PR, SD, PD, and inevaluable (NE)
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 53. Image Review

- **evaluation type:** semantic
- **original SAP text:** Images for tumor assessment will be reviewed separately by central and local, and both image review results from central (central independent reviewer) and local (eCRF) will be analyzed and listed separately.
- **generated SAP text:** The primary analysis methodology described in Section 6.1.1.2 will be repeated using the BOR as determined by the investigator's local review to support the findings of the central review.
- **protocol text:** In addition, all tumor assessment images will be evaluated centrally by an independent reviewer for reporting purposes
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 54. TTE Analysis Scope

- **evaluation type:** exact_match
- **original SAP text:** Time-to-event analysis for the study drug (CT-P16 or EU-Approved Avastin) will be undertaken for each of the response duration, TTP, PFS, and OS.
- **generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations. - Progression-Free Survival (PFS)... - Time to Progression (TTP)... - Overall Survival (OS)... - Response Duration...
- **protocol text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 55. Primary Efficacy Population

- **evaluation type:** exact_match
- **original SAP text:** Primary analysis population for the efficacy analysis is the ITT population.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 56. Supportive Efficacy Population

- **evaluation type:** exact_match
- **original SAP text:** A supportive analysis will be repeated using the PP population.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 57. Efficacy Data Listing

- **evaluation type:** semantic
- **original SAP text:** All efficacy data will be listed for the ITT population by treatment group unless otherwise specified.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 58. Primary Endpoint Analysis Method

- **evaluation type:** exact_match
- **original SAP text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance status at baseline (0 vs. 1) as covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect.
- **generated SAP text:** The primary analysis will utilize a logistic regression model considering treatment group as a fixed effect and other covariates (to be defined in Section 4.1).
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 59. Pooling Country Strategy

- **evaluation type:** exact_match
- **original SAP text:** Country can be pooled into region (EMEA vs. America vs. Asia) for statistical analysis when there are not enough patients within each country.
- **generated SAP text:** Country will be included as a covariate unless there are sparse data across centers/countries, in which case it may be pooled by region.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 60. ORR Table

- **evaluation type:** semantic
- **original SAP text:** A table presenting ORR during the Induction Study Period with the analysis result will be produced.
- **generated SAP text:** 14.2.4 Equivalence Analysis of Objective Response Rate
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 61. ORR CI Presentation

- **evaluation type:** exact_match
- **original SAP text:** The ORR and its corresponding 95% CI for each treatment group will also be presented.
- **generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 62. Risk Difference Presentation

- **evaluation type:** exact_match
- **original SAP text:** A point estimate and 95% CI of the risk difference of ORR between CT-P16 group and EU-Approved Avastin group will be produced.
- **generated SAP text:** Population-level Summary: Difference in ORR (%) between CT-P16 and EU-Approved Avastin.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 63. Response Category Presentation

- **evaluation type:** exact_match
- **original SAP text:** The number and percentage of patients in each response category will also be presented by treatment group separately.
- **generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 64. Primary Analysis Population

- **evaluation type:** exact_match
- **original SAP text:** The primary analysis will be conducted in the ITT population.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 65. Supportive Analysis Population

- **evaluation type:** exact_match
- **original SAP text:** A supportive analysis will be conducted in the PP population and also be provided in the table.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 66. Central Review Usage

- **evaluation type:** exact_match
- **original SAP text:** For the primary analysis, central review results will be used.
- **generated SAP text:** as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **protocol text:** For primary analysis, central review result will be used.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 67. Local Review Usage

- **evaluation type:** exact_match
- **original SAP text:** Local review results will be used for a sensitivity analysis.
- **generated SAP text:** The primary analysis methodology described in Section 6.1.1.2 will be repeated using the BOR as determined by the investigator's local review to support the findings of the central review.
- **protocol text:** Local review result will be used as supportive data (sensitivity analysis).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 68. Delta Method Explanation

- **evaluation type:** semantic
- **original SAP text:** The Delta Method for estimating difference of proportion is explained in the following process.
- **generated SAP text:** The resulting odds ratio and its 95% CI will be converted into a difference in proportions (CT-P16 – EU-Approved Avastin) using the Delta method.
- **protocol text:** The resulting odds ratio and 95% CI will be converted into difference of proportions using the Delta method for the purpose of comparison.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Specific formulas and steps
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP mentions method but omits detailed formulas.

#### 69. Secondary Endpoint: Whole Study ORR

- **evaluation type:** exact_match
- **original SAP text:** For the secondary efficacy endpoint, ORR based on BOR during the Whole Study Period by RECIST version 1.1 will be analyzed.
- **generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed for both the ITT and PP populations.
- **protocol text:** ORR based on BOR during the Whole Study Period by RECIST v.1.1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 70. Whole Study ORR Table

- **evaluation type:** exact_match
- **original SAP text:** A table will be produced using both central review data and local review data from all treatment periods including Induction Study Period, Maintenance Study Period and EOT visit in the ITT and PP population.
- **generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed for both the ITT and PP populations.
- **protocol text:** The secondary endpoint, both locally reviewed ORR and centrally reviewed ORR during the Whole Study Period, will be summarized using proportion and its corresponding 95% CI for each treatment group in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 71. Whole Study ORR CI

- **evaluation type:** exact_match
- **original SAP text:** The ORR and its corresponding 95% CI for each treatment group will also be presented.
- **generated SAP text:** The proportion of responders and the 2-sided 95% CI for each treatment group will be calculated using the Clopper-Pearson method.
- **protocol text:** summarized using proportion and its corresponding 95% CI for each treatment group
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 72. Whole Study ORR Categories

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients within each response category will be summarized by treatment group.
- **generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 73. Whole Study ORR Timing

- **evaluation type:** semantic
- **original SAP text:** The ORR based on BOR during the Whole Study Period will be analyzed only for the final CSR.
- **generated SAP text:** The final analysis will include the final assessment of all secondary efficacy... endpoints.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 74. TTE Analysis

- **evaluation type:** exact_match
- **original SAP text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population.
- **generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations.
- **protocol text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 75. TTE Summaries

- **evaluation type:** semantic
- **original SAP text:** The number of patients experiencing events and the number of censored patients will be summarized by treatment group with reasons for an event/censoring.
- **generated SAP text:** The number of patients experiencing events and the number of censored patients will be summarized by treatment group with reasons for an event/censoring.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 76. KM Method

- **evaluation type:** exact_match
- **original SAP text:** The median survival time and its corresponding 95% CI for each treatment group will be estimated using the Kaplan-Meier method.
- **generated SAP text:** Kaplan-Meier (KM) Method: Used to estimate the survival distributions for each treatment group. Summary Statistics: Median TTE... will be calculated with 95% CIs.
- **protocol text:** the median time and its corresponding 95% CI for each treatment group for each secondary endpoint of time-to-event analysis will be estimated using the Kaplan-Meier method.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 77. Percentiles

- **evaluation type:** semantic
- **original SAP text:** The 25th percentile and 75th percentile for the survival times along with the corresponding 95% CI for the percentiles will also be displayed.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** 25th and 75th percentiles
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP omits specific percentiles but mentions summary statistics.

#### 78. Brookmeyer-Crowley

- **evaluation type:** exact_match
- **original SAP text:** The Brookmeyer-Crowley methodology will be used to construct the 95% CI for each percentile.
- **generated SAP text:** The 95% CI for the median will be calculated using the Brookmeyer-Crowley method.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 79. Decimal Places

- **evaluation type:** semantic
- **original SAP text:** Survival times and their corresponding 95% CIs will be presented to one decimal place.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Decimal place specification
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Formatting detail.

#### 80. Survival Rates

- **evaluation type:** semantic
- **original SAP text:** In addition, the estimate of survival rates (at 6, 12, 24, 36 months for response duration, TTP, PFS and at 12, 24, 36 months for OS) will be displayed along with their corresponding 95% CI.
- **generated SAP text:** survival rates at specific landmarks (e.g., 6 months, 12 months) will be calculated with 95% CIs.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Specific timepoints (24, 36 months) and distinction between endpoints
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP mentions landmarks but omits the specific list.

#### 81. Decimal Places

- **evaluation type:** semantic
- **original SAP text:** The estimates of survival rates and their corresponding 95% CIs will be presented to two decimal places.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Decimal place specification
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Formatting detail.

#### 82. TTE Unit

- **evaluation type:** semantic
- **original SAP text:** All time-to-event data will be reported in months with reasons for an event/censoring and summarized by treatment group.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Reporting unit (months)
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Formatting detail.

#### 83. TTE Conversion

- **evaluation type:** semantic
- **original SAP text:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Conversion formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Formatting detail.

#### 84. Death Date Imputation

- **evaluation type:** semantic
- **original SAP text:** For the purposes of inclusion in the survival analysis, incomplete death dates will be imputed as described in Appendix 14.4.3.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Imputation reference
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Imputation details are often in appendices.

#### 85. New Anticancer Therapy

- **evaluation type:** exact_match
- **original SAP text:** To determine ‘event' or ‘censoring' for response duration, TTP and PFS, initiation of new anticancer therapy will be considered.
- **generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored
- **protocol text:** If a patient receives another new anticancer therapy, it will be censored
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 86. KM Plot

- **evaluation type:** exact_match
- **original SAP text:** A Kaplan-Meier plot will be presented for each of the time-to-event analyses.
- **generated SAP text:** 14.2.F1 Kaplan-Meier Plot of Progression-Free Survival
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 87. Cox Model

- **evaluation type:** exact_match
- **original SAP text:** In PFS and OS analyses, an adjusted stratified cox regression model will be used to estimate the hazard ratio and its 95% CI for receiving CT-P16 compared with receiving EU-Approved Avastin using country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance score at baseline (0 vs. 1) as stratification factors.
- **generated SAP text:** Hazard Ratio (HR): A stratified Cox proportional hazards model, including the same stratification factors used in the randomization, will be used to estimate the HR (CT-P16 / EU-Approved Avastin) and its 95% CI.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 88. Pooling Country

- **evaluation type:** semantic
- **original SAP text:** Country can be pooled into region (EMEA vs. America vs. Asia) for statistical analysis when there are not enough patients within each country.
- **generated SAP text:** Country will be included as a covariate unless there are sparse data across centers/countries, in which case it may be pooled by region.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 89. TTE Analysis Timing

- **evaluation type:** semantic
- **original SAP text:** All time-to-event analyses will be conducted for 2nd CSR and final CSR.
- **generated SAP text:** The final analysis will include the final assessment of all secondary efficacy... endpoints.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 90. TTE Review Basis

- **evaluation type:** semantic
- **original SAP text:** All time-to-event analyses related to response duration, TTP and PFS will be performed based on the central and local review in terms of PD/recurrence, CR and PR.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specification of both central and local review for TTE
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP implies central review for primary, but doesn't explicitly state both for TTE.

#### 91. Data Sources

- **evaluation type:** semantic
- **original SAP text:** Records on ‘Randomization', 'Survival Status', 'Response Evaluation', 'Salvage Treatment' or 'Study Treatment Termination' eCRF pages will be used.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific eCRF pages
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Data source details.

---

### Issues Found (0 items)

*No issues found.*

---

### Extra Information Flagged (1 items)

#### 1. Additional Sensitivity Analyses

- **content:** Additional Sensitivity Analyses
- **generated SAP text:** Complete Case Analysis: Patients with missing or NE responses will be excluded... Confirmed vs. Unconfirmed Response... Alternative Covariate Adjustment...
- **contradicts:** no
- **detail:** Generated SAP adds sensitivity analyses not present in Original SAP.
- **reasoning:** Beneficial additions, not contradictions.

---

### Missing from Generated SAP (8 items)

#### 1. Tipping Point Analysis

- **original SAP text:** Tipping point analysis will also be conducted using central review data based on exact binomial approach in the ITT population for a sensitivity analysis.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific sensitivity analysis for primary endpoint missing.
- **reasoning:** Not in protocol, so not strictly required, but a significant omission from Original SAP.

#### 2. Delta Method Formulas

- **original SAP text:** (1) The individual odds and standard errors (SEs) for both treatments will be obtained from the model... (5) Calculate the variance of the difference in proportions...
- **protocol text:** The resulting odds ratio and 95% CI will be converted into difference of proportions using the Delta method for the purpose of comparison.
- **in protocol:** yes
- **classification:** acceptable_difference
- **description:** Detailed formulas for Delta method missing.
- **reasoning:** Generated SAP mentions Delta method, which satisfies the protocol requirement. The specific formulas are implementation details.

#### 3. Incomplete Date Logic

- **original SAP text:** When there is no PD/recurrence (or death) and the start date of new anticancer therapy is incomplete, censoring date will be determined as following...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Detailed logic for handling incomplete dates of new anticancer therapy missing.
- **reasoning:** Specific data handling rules not in protocol.

#### 4. Salvage Treatment Analysis

- **original SAP text:** Salvage treatment during the Follow-Up Period will be recorded in ‘Salvage Treatment' eCRF pages and details will be listed and tabulated by salvage treatment category and treatment group in the ITT population.
- **protocol text:** Use of all medications and therapy for the treatment of nsNSCLC (e.g., surgery before enrollment or salvage treatment), from the diagnosis of disease until the last assessment date, will be recorded
- **in protocol:** yes
- **classification:** acceptable_difference
- **description:** Specific table for salvage treatment missing.
- **reasoning:** Protocol requires recording, but not explicitly a separate analysis table in the stats section.

#### 5. Effusion Drainage Listing

- **original SAP text:** Effusion drainage information will be listed by treatment group for ITT population.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Listing for effusion drainage missing.
- **reasoning:** Not in protocol.

#### 6. Tipping Point Analysis Details

- **original SAP text:** Tipping point analyses will be conducted under Missing Not at Random (MNAR) scenarios. Imputation will be done by gradually shifting the number of responders by treatment group to make MNAR scenarios.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Details of tipping point analysis missing.
- **reasoning:** Linked to missing Tipping Point Analysis.

#### 7. Tipping Point Plot

- **original SAP text:** All the scenarios will be also provided using 2-dimentional plot.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Plot for tipping point analysis missing.
- **reasoning:** Linked to missing Tipping Point Analysis.

#### 8. Incomplete Date Logic - Event

- **original SAP text:** When PD/recurrence (or death) is occurred and the start of new anticancer therapy is incomplete, event will be determined as following...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Detailed logic for handling incomplete dates of new anticancer therapy for event determination missing.
- **reasoning:** Specific data handling rules not in protocol.

---

### Reasoning

The Generated SAP accurately reflects the primary and secondary objectives and endpoints defined in the Original SAP and Protocol. It correctly identifies the primary analysis method (logistic regression with Delta method conversion) and the similarity margins. It correctly lists the secondary endpoints and the use of Kaplan-Meier and Cox regression for time-to-event analyses. 

However, the Generated SAP omits the 'Tipping Point Analysis' which was a specific sensitivity analysis in the Original SAP. Instead, it proposes other standard sensitivity analyses (Complete Case, Unconfirmed Response). Since the Protocol does not explicitly require Tipping Point Analysis (it only mentions local review as sensitivity), this is an acceptable difference, though a notable deviation from the Original SAP's specific plan. 

The Generated SAP also lacks the detailed logic for handling incomplete dates for new anticancer therapy and the specific formulas for the Delta method, which are present in the Original SAP. These are considered 'less_detailed' or 'missing_specification' but not critical failures as the general methods are correct. 

Overall, the Generated SAP is a solid draft that covers the essential regulatory and statistical requirements but lacks some of the specific granular details and one specific sensitivity analysis found in the Original SAP.

---

### Summary

The Generated SAP correctly identifies all primary and secondary objectives and endpoints. It accurately describes the statistical methods for the primary analysis (logistic regression, Delta method) and secondary time-to-event analyses (Kaplan-Meier, Cox regression). It omits the specific 'Tipping Point Analysis' for sensitivity and detailed date imputation logic found in the Original SAP, but these are not explicitly required by the Protocol.