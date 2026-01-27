## Efficacy Analysis Evaluation

**Section:** efficacy_analysis
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **sections read:** 8, 8.1, 8.2, 8.2.1, 8.2.2, 8.2.2.1, 8.2.2.2, 8.2.2.3, 8.2.2.4, 8.2.2.5, 8.3, 8.4
- **elements per section:** 8: 13, 8.1: 26, 8.2.1: 5, 8.2.2: 19, 8.2.2.1: 9, 8.2.2.2: 9, 8.2.2.3: 9, 8.2.2.4: 4, 8.2.2.5: 12, 8.3: 4, 8.4: 1
- **elements extracted:** 111
- **elements in evaluation table:** 111
- **elements in missing from generated SAP:** 0
- **counts match:** True

---

### Evaluation Table (111 items)

#### 1. Focus of Final CSR

- **evaluation type:** semantic
- **original SAP text:** Efficacy analyses for the final CSR focus on secondary efficacy endpoints (Section 8.2) based on patients' long-term follow-up data.
- **generated SAP text:** The final analysis will include the final assessment of all secondary efficacy, pharmacokinetic, quality of life, and safety endpoints.
- **protocol text:** The sponsor plans to prepare 3 CSRs... To report all data until the end of study.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both documents identify the final analysis focus on secondary endpoints/long-term data.

#### 2. Primary Analysis Completion Status

- **evaluation type:** semantic
- **original SAP text:** It is noted that the primary efficacy analysis (Section 8.1) was completed in the 1st CSR.
- **generated SAP text:** The primary analysis of efficacy and safety is planned after all patients have completed Cycle 6 of the Induction Study Period
- **protocol text:** The sponsor plans to prepare 3 CSRs... To report data after completion of the Induction Study Period
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** none
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** The Original SAP (Version 3.0) states the primary analysis was *already* completed in the 1st CSR. The Generated SAP describes it as a planned future event. This reflects a difference in the document version/timing context.

#### 3. Primary Endpoint Analysis in Final CSR

- **evaluation type:** semantic
- **original SAP text:** In the final CSR, the analysis for the primary efficacy endpoint will be performed as a sensitivity analysis using the same method as 1st CSR.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** none
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP treats the primary endpoint analysis in this document as a sensitivity analysis (since the primary analysis was done in 1st CSR). Generated SAP treats it as the main primary analysis.

#### 4. Efficacy Assessment Methods

- **evaluation type:** semantic
- **original SAP text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **generated SAP text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **protocol text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 5. RECIST Version

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

#### 6. Endpoints Determination

- **evaluation type:** semantic
- **original SAP text:** The primary endpoint, ORR during the Induction Study Period, and the secondary endpoint, ORR during the Whole Study Period, will be determined by the BOR.
- **generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR)...
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

#### 7. Confirmation Requirement

- **evaluation type:** semantic
- **original SAP text:** For CR or PR, BOR must be confirmed by the subsequent assessment.
- **generated SAP text:** While the primary endpoint requires confirmation (as per RECIST 1.1)...
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

#### 8. Response Categories

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

#### 9. Image Review

- **evaluation type:** semantic
- **original SAP text:** Images for tumor assessment will be reviewed separately by central and local, and both image review results from central (central independent reviewer) and local (eCRF) will be analyzed and listed separately.
- **generated SAP text:** as determined by an Independent Tumor Review Committee (central review)... The primary analysis methodology described in Section 6.1.1.2 will be repeated using the BOR as determined by the investigator's local review
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

#### 10. Time-to-Event Endpoints List

- **evaluation type:** exact_match
- **original SAP text:** Time-to-event analysis for the study drug (CT-P16 or EU-Approved Avastin) will be undertaken for each of the response duration, TTP, PFS, and OS.
- **generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations... Progression-Free Survival (PFS)... Time to Progression (TTP)... Overall Survival (OS)... Response Duration
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

#### 11. Primary Analysis Population

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

#### 12. Supportive Analysis Population

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

#### 13. Efficacy Data Listing

- **evaluation type:** semantic
- **original SAP text:** All efficacy data will be listed for the ITT population by treatment group unless otherwise specified.
- **generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **protocol text:** All safety data including immunogenicity will be listed
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 14. Primary Endpoint Sensitivity Analysis (Final CSR)

- **evaluation type:** semantic
- **original SAP text:** In the final CSR, the analysis for the protocol-specified primary efficacy endpoint will be performed as a sensitivity analysis using method described in this section.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** none
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Generated SAP does not distinguish between the primary analysis timing and the final CSR sensitivity analysis.

#### 15. Primary Endpoint Definition

- **evaluation type:** exact_match
- **original SAP text:** The primary efficacy endpoint is ORR based on BOR during the Induction Study Period by RECIST version 1.1 (Appendix 14.5).
- **generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR) during the Induction Study Period (up to Cycle 6) as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **protocol text:** The primary efficacy endpoint will be the ORR based on BOR during the Induction Study Period by RECIST v.1.1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 16. ORR Definition

- **evaluation type:** exact_match
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

#### 17. Non-Responder Definition

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

#### 18. Similarity Criterion

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

#### 19. Primary Analysis Model

- **evaluation type:** exact_match
- **original SAP text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance status at baseline (0 vs. 1) as covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect.
- **generated SAP text:** The model will include treatment group as a fixed effect. Covariates will include the stratification factors: sex (female vs. male), disease status (recurrence vs. metastatic), and ECOG performance score (0 vs. 1). Country will be included as a covariate
- **protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 20. Pooling Country

- **evaluation type:** semantic
- **original SAP text:** Country can be pooled into region (EMEA vs. America vs. Asia) for statistical analysis when there are not enough patients within each country.
- **generated SAP text:** Country will be included as a covariate unless there are sparse data across centers/countries, in which case it may be pooled by region.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Specific regions (EMEA vs. America vs. Asia)
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Gen SAP mentions pooling by region but omits the specific regions defined in Original SAP.

#### 21. Region Discussion

- **evaluation type:** semantic
- **original SAP text:** Use of region instead of country in statistical analyses was discussed at the blinded DRM.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Statement about DRM discussion
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Procedural detail not required in SAP text.

#### 22. ORR Table

- **evaluation type:** semantic
- **original SAP text:** A table presenting ORR during the Induction Study Period with the analysis result will be produced.
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

#### 23. ORR and 95% CI Presentation

- **evaluation type:** semantic
- **original SAP text:** The ORR and its corresponding 95% CI for each treatment group will also be presented.
- **generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders...
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Explicit mention of 95% CI for each group
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Implied by standard descriptive statistics.

#### 24. Risk Difference Presentation

- **evaluation type:** semantic
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

#### 25. Response Category Presentation

- **evaluation type:** semantic
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

#### 26. Primary Analysis Population (ITT)

- **evaluation type:** exact_match
- **original SAP text:** The primary analysis will be conducted in the ITT population.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed... in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 27. Supportive Analysis Population (PP)

- **evaluation type:** exact_match
- **original SAP text:** A supportive analysis will be conducted in the PP population and also be provided in the table.
- **generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The primary analysis for the primary endpoint will be performed... in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 28. Central Review for Primary

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

#### 29. Local Review Sensitivity

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

#### 30. Tipping Point Analysis

- **evaluation type:** exact_match
- **original SAP text:** Tipping point analysis will also be conducted using central review data based on exact binomial approach in the ITT population for a sensitivity analysis.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Tipping point analysis
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol, so acceptable difference.

#### 31. Delta Method Explanation

- **evaluation type:** semantic
- **original SAP text:** The Delta Method for estimating difference of proportion is explained in the following process.
- **generated SAP text:** The resulting odds ratio and its 95% CI will be converted into a difference in proportions (CT-P16 – EU-Approved Avastin) using the Delta method.
- **protocol text:** The resulting odds ratio and 95% CI will be converted into difference of proportions using the Delta method for the purpose of comparison.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Detailed steps 1-5 and formulas
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Gen SAP mentions Delta method but omits the detailed mathematical steps. This is acceptable as the method is standard.

#### 32. Delta Method Step 1

- **evaluation type:** semantic
- **original SAP text:** (1) The individual odds and standard errors (SEs) for both treatments will be obtained from the model.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Step 1 details
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Part of detailed formula.

#### 33. Delta Method Step 1 (Definitions)

- **evaluation type:** semantic
- **original SAP text:** For the purposes of this algorithm, let the estimate of the odds of being a responder in the CT-P16 group be denoted by $\theta_a$ and the estimate of the odds of being a responder in the EU-Approved Avastin group be denoted by $\theta_b$.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Variable definitions
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Part of detailed formula.

#### 34. Delta Method Step 2

- **evaluation type:** semantic
- **original SAP text:** (2) Calculate the variances of these estimates, $Var(\theta_a)$ and $Var(\theta_b)$ respectively from the SEs obtained from the model.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Step 2 details
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Part of detailed formula.

#### 35. Delta Method Step 3

- **evaluation type:** semantic
- **original SAP text:** (3) Calculate the estimates of the corresponding proportions, denoted $p_a$ and $p_b$ respectively, for each of the randomized treatment groups, from the estimated odds $\theta_a$ and $\theta_b$ using the following formula: $p = \frac{\theta}{1 + \theta}$ and hence calculate the estimate of the difference of proportions $p_a - p_b$.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Step 3 details and formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Part of detailed formula.

#### 36. Delta Method Step 4

- **evaluation type:** semantic
- **original SAP text:** (4) Using Taylor expansions and the Delta method, the following formula for approximation can be obtained: $Var[f(X)] \approx (f'(E[X]))^2Var[X]$ Applying this approximation specifically to this case, and using the formula specified in step (3) we obtain the formula $Var(p) = \frac{Var(\theta)}{(1+\theta)^4}$ which should be used to calculate $Var(p_a)$ and $Var(p_b)$.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Step 4 details and formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Part of detailed formula.

#### 37. Delta Method Step 5

- **evaluation type:** semantic
- **original SAP text:** (5) Calculate the variance of the difference in proportions $Var(p_a - p_b)$ as the sum of $Var(p_a)$ and $Var(p_b)$.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Step 5 details
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Part of detailed formula.

#### 38. Delta Method CI Formula

- **evaluation type:** semantic
- **original SAP text:** Use this to obtain the SE of the difference, and hence calculate the 95% CI using the formula: $95\% \text{ Confidence Interval } = (p_a - p_b) +/- 1.96(SE(p_a - p_b))$
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** CI formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Part of detailed formula.

#### 39. Independence Assumption

- **evaluation type:** semantic
- **original SAP text:** Note: this method assumes that the estimate ORR of CT-P16 group is independent of the estimate of EU-Approved Avastin group.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Independence assumption note
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Statistical assumption.

#### 40. Secondary Endpoint: ORR Whole Study

- **evaluation type:** exact_match
- **original SAP text:** For the secondary efficacy endpoint, ORR based on BOR during the Whole Study Period by RECIST version 1.1 will be analyzed.
- **generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed
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

#### 41. Whole Study ORR Table

- **evaluation type:** semantic
- **original SAP text:** A table will be produced using both central review data and local review data from all treatment periods including Induction Study Period, Maintenance Study Period and EOT visit in the ITT and PP population.
- **generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed for both the ITT and PP populations.
- **protocol text:** The secondary endpoint, both locally reviewed ORR and centrally reviewed ORR during the Whole Study Period, will be summarized... in the ITT and PP population.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Explicit mention of central and local review for this specific endpoint
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Gen SAP mentions central/local generally, but not specifically for this endpoint.

#### 42. Whole Study ORR CI

- **evaluation type:** semantic
- **original SAP text:** The ORR and its corresponding 95% CI for each treatment group will also be presented.
- **generated SAP text:** The proportion of responders and the 2-sided 95% CI for each treatment group will be calculated using the Clopper-Pearson method.
- **protocol text:** summarized using proportion and its corresponding 95% CI
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 43. Whole Study Response Categories

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients within each response category will be summarized by treatment group.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Summary of response categories
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard reporting.

#### 44. Whole Study ORR Timing

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

#### 45. TTE Analysis Scope

- **evaluation type:** exact_match
- **original SAP text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population.
- **generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations... Progression-Free Survival (PFS)... Time to Progression (TTP)... Overall Survival (OS)... Response Duration
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

#### 46. TTE Summary

- **evaluation type:** semantic
- **original SAP text:** The number of patients experiencing events and the number of censored patients will be summarized by treatment group with reasons for an event/censoring.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Summary of events/censoring reasons
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard reporting.

#### 47. KM Median and CI

- **evaluation type:** exact_match
- **original SAP text:** The median survival time and its corresponding 95% CI for each treatment group will be estimated using the Kaplan-Meier method.
- **generated SAP text:** Kaplan-Meier (KM) Method: Used to estimate the survival distributions... Median TTE... will be calculated with 95% CIs.
- **protocol text:** the median time and its corresponding 95% CI for each treatment group... will be estimated using the Kaplan-Meier method.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 48. Survival Percentiles

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
- **reasoning:** Not in protocol.

#### 49. Brookmeyer-Crowley Method

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

#### 50. Decimal Places (Time)

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

#### 51. Survival Rates

- **evaluation type:** semantic
- **original SAP text:** In addition, the estimate of survival rates (at 6, 12, 24, 36 months for response duration, TTP, PFS and at 12, 24, 36 months for OS) will be displayed along with their corresponding 95% CI.
- **generated SAP text:** survival rates at specific landmarks (e.g., 6 months, 12 months) will be calculated with 95% CIs.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Specific timepoints (24, 36 months)
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Gen SAP mentions landmarks but omits the specific list.

#### 52. Decimal Places (Rates)

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

#### 53. Time Unit

- **evaluation type:** semantic
- **original SAP text:** All time-to-event data will be reported in months with reasons for an event/censoring and summarized by treatment group.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Reporting in months
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard practice.

#### 54. Days to Months Conversion

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
- **reasoning:** Standard practice.

#### 55. Death Date Imputation

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
- **reasoning:** Not in protocol.

#### 56. New Anticancer Therapy Censoring

- **evaluation type:** exact_match
- **original SAP text:** To determine ‘event' or ‘censoring' for response duration, TTP and PFS, initiation of new anticancer therapy will be considered.
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

#### 57. Incomplete Date Logic Reference

- **evaluation type:** semantic
- **original SAP text:** For missing or incomplete start date of new anticancer therapy, the capture logic of event or censoring will be followed in Section 8.2.2.5.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Reference to incomplete date logic
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 58. KM Plot

- **evaluation type:** exact_match
- **original SAP text:** A Kaplan-Meier plot will be presented for each of the time-to-event analyses.
- **generated SAP text:** Kaplan-Meier Plot of Progression-Free Survival... Kaplan-Meier Plot of Overall Survival
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 59. Cox Regression Model

- **evaluation type:** exact_match
- **original SAP text:** In PFS and OS analyses, an adjusted stratified cox regression model will be used to estimate the hazard ratio and its 95% CI for receiving CT-P16 compared with receiving EU-Approved Avastin using country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance score at baseline (0 vs. 1) as stratification factors.
- **generated SAP text:** A stratified Cox proportional hazards model, including the same stratification factors used in the randomization, will be used to estimate the HR (CT-P16 / EU-Approved Avastin) and its 95% CI.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 60. Pooling Country (Cox)

- **evaluation type:** semantic
- **original SAP text:** Country can be pooled into region (EMEA vs. America vs. Asia) for statistical analysis when there are not enough patients within each country.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Pooling strategy for Cox model
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Implied by randomization factors.

#### 61. TTE Analysis Timing

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

#### 62. TTE Review Basis

- **evaluation type:** semantic
- **original SAP text:** All time-to-event analyses related to response duration, TTP and PFS will be performed based on the central and local review in terms of PD/recurrence, CR and PR.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Explicit mention of both central and local review for TTE
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 63. Data Sources

- **evaluation type:** semantic
- **original SAP text:** Records on ‘Randomization', 'Survival Status', 'Response Evaluation', 'Salvage Treatment' or 'Study Treatment Termination' eCRF pages will be used.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** eCRF page references
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Data management detail.

#### 64. Response Duration Definition

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

#### 65. Response Duration Population

- **evaluation type:** exact_match
- **original SAP text:** Time-to-event analysis for response duration will be performed for patients who have confirmed BOR of CR or PR.
- **generated SAP text:** (among responders only)
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 66. Response Duration Event

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

#### 67. Response Duration Censoring (No Event)

- **evaluation type:** exact_match
- **original SAP text:** No event and no anticancer therapy -> Last tumor assessment date
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

#### 68. Response Duration Censoring (New Therapy)

- **evaluation type:** exact_match
- **original SAP text:** Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
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

#### 69. Response Duration Censoring (Missing Assessments)

- **evaluation type:** exact_match
- **original SAP text:** Event after missing two or more tumor assessment* -> Last tumor assessment date before event
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

#### 70. Censoring Date Definition

- **evaluation type:** semantic
- **original SAP text:** The last tumor assessment date on which tumor assessment's is neither ‘missing' nor ‘NE' will be used for censoring date.
- **generated SAP text:** last adequate tumor assessment
- **protocol text:** last adequate radiological assessment
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 71. Single Missing Assessment Rule

- **evaluation type:** semantic
- **original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Explicit rule for single missing assessment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Implied by the rule for missing two or more.

#### 72. Response Duration Formula

- **evaluation type:** semantic
- **original SAP text:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard calculation.

#### 73. TTP Definition

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

#### 74. TTP Event

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

#### 75. TTP Censoring (No Assessment)

- **evaluation type:** semantic
- **original SAP text:** No tumor assessment -> The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Censoring rule for no assessment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard rule.

#### 76. TTP Censoring (No Event)

- **evaluation type:** exact_match
- **original SAP text:** No event and no anticancer therapy -> Last tumor assessment date
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

#### 77. TTP Censoring (New Therapy)

- **evaluation type:** exact_match
- **original SAP text:** Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
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

#### 78. TTP Censoring (Missing Assessments)

- **evaluation type:** exact_match
- **original SAP text:** Event after missing two or more tumor assessment* -> Last tumor assessment date before event
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

#### 79. TTP Censoring Date Definition

- **evaluation type:** semantic
- **original SAP text:** The last tumor assessment date on which tumor assessment's is neither 'missing' nor 'NE' will be used for censoring date.
- **generated SAP text:** last adequate tumor assessment
- **protocol text:** last adequate radiological assessment
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 80. TTP Single Missing Assessment Rule

- **evaluation type:** semantic
- **original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Explicit rule for single missing assessment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Implied.

#### 81. TTP Formula

- **evaluation type:** semantic
- **original SAP text:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard calculation.

#### 82. PFS Definition

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

#### 83. PFS Event

- **evaluation type:** exact_match
- **original SAP text:** PD/recurrence or death that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **generated SAP text:** Progression-Free Survival (PFS): Time from randomization until the first documentation of PD (per RECIST v.1.1) or death due to any cause.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 84. PFS Censoring (No Assessment)

- **evaluation type:** semantic
- **original SAP text:** No tumor assessment -> The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Censoring rule for no assessment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard rule.

#### 85. PFS Censoring (No Event)

- **evaluation type:** exact_match
- **original SAP text:** No event and no anticancer therapy -> Last tumor assessment date
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

#### 86. PFS Censoring (New Therapy)

- **evaluation type:** exact_match
- **original SAP text:** Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
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

#### 87. PFS Censoring (Missing Assessments)

- **evaluation type:** exact_match
- **original SAP text:** Event after missing two or more tumor assessment* -> Last tumor assessment date before event
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

#### 88. PFS Censoring Date Definition

- **evaluation type:** semantic
- **original SAP text:** The last tumor assessment date on which tumor assessment's is neither ‘missing' nor ‘NE' will be used for censoring date.
- **generated SAP text:** last adequate tumor assessment
- **protocol text:** last adequate radiological assessment
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 89. PFS Single Missing Assessment Rule

- **evaluation type:** semantic
- **original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Explicit rule for single missing assessment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Implied.

#### 90. PFS Formula

- **evaluation type:** semantic
- **original SAP text:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard calculation.

#### 91. OS Definition

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

#### 92. OS Event

- **evaluation type:** exact_match
- **original SAP text:** Death will be regarded as an event.
- **generated SAP text:** Overall Survival (OS): Time from randomization until death due to any cause.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 93. OS Censoring

- **evaluation type:** exact_match
- **original SAP text:** Censoring will be defined as following: Non-death -> Last known alive date
- **generated SAP text:** Patients alive... at the time of data cutoff/study completion will be censored... (implied)
- **protocol text:** for patients whose status is unknown, data will be censored at the time when the patient is last known to be alive.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Explicit 'Last known alive date' phrasing
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard practice.

#### 94. OS Formula

- **evaluation type:** semantic
- **original SAP text:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Formula
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard calculation.

#### 95. Incomplete Date Logic (New Anticancer Therapy)

- **evaluation type:** semantic
- **original SAP text:** A patient will be considered as taking a new anticancer therapy (other than study treatments) when there is any record on ‘Salvage treatment' eCRF pages or a record of receiving anticancer therapy on ‘Survival Status' eCRF page.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Definition of new anticancer therapy source
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Data management detail.

#### 96. Incomplete Date Logic (No PD/Death)

- **evaluation type:** semantic
- **original SAP text:** When there is no PD/recurrence (or death) and the start date of new anticancer therapy is incomplete, censoring date will be determined as following: 1) If the last tumor assessment is performed during treatment periods (including EOT visit), the censoring date will be the last tumor assessment date during treatment periods.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 97. Incomplete Date Logic (Follow-Up Period - Missing Day)

- **evaluation type:** semantic
- **original SAP text:** 2) If the last tumor assessment is performed during Follow-Up Period, censoring date will be determined as following: a. If the day of the start date of new anticancer therapy is missing, then the censoring date will be the last tumor assessment date, provided tumor assessment date < the partial start date of new anticancer therapy.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 98. Incomplete Date Logic (Follow-Up Period - Missing Day/Month)

- **evaluation type:** semantic
- **original SAP text:** b. If the day and month of the start date of new anticancer therapy is missing, censoring date will be determined as following: * If all dates of tumor assessments during Follow-Up Period >= the partial start date of new anticancer therapy, the censoring date will be the last tumor assessment during treatment periods.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 99. Incomplete Date Logic (Follow-Up Period - Missing Day/Month - Case 2)

- **evaluation type:** semantic
- **original SAP text:** * If at least one of tumor assessment during Follow-Up Period < the partial start date of new anticancer therapy, the censoring date will be the last tumor assessment, provided tumor assessment date < the partial start date of new anticancer therapy.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 100. Incomplete Date Logic (Completely Missing)

- **evaluation type:** semantic
- **original SAP text:** c. If the start date of new anticancer therapy is completely missing, censoring date will be the last tumor assessment date during treatment periods.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 101. Incomplete Date Logic (PD/Death Event)

- **evaluation type:** semantic
- **original SAP text:** When PD/recurrence (or death) is occurred and the start of new anticancer therapy is incomplete, event will be determined as following: 1) If the first PD/recurrence (or death) is occurred during treatment periods, it will be regarded as 'event'.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 102. Incomplete Date Logic (PD/Death Follow-Up - Missing Day)

- **evaluation type:** semantic
- **original SAP text:** 2) If the first PD/recurrence (or death) is occurred during Follow-Up Period, and a. If the day of the start date of new anticancer therapy is missing, and i. If the first PD/recurrence (or death) date < the partial start date of new anticancer therapy, it will be regarded as 'event'.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 103. Incomplete Date Logic (PD/Death Follow-Up - Missing Day - Censored)

- **evaluation type:** semantic
- **original SAP text:** ii. If the first PD/recurrence (or death) date >= the partial start date of new anticancer therapy, it will be censored. The censoring date will be the last tumor assessment, provided the tumor assessment date < the partial start date of new anticancer therapy.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 104. Incomplete Date Logic (PD/Death Follow-Up - Missing Day/Month)

- **evaluation type:** semantic
- **original SAP text:** b. If the day and month of start date of new anticancer therapy is missing, and i. If the first PD/recurrence (or death) date < the partial start date of new anticancer therapy, it will be regarded as 'event'.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 105. Incomplete Date Logic (PD/Death Follow-Up - Missing Day/Month - Censored)

- **evaluation type:** semantic
- **original SAP text:** ii. If the first PD/recurrence (or death) date >= the partial start date of new anticancer therapy, it will be censored. The censoring date will be as follows: * If all dates of tumor assessments during Follow-Up Period >= the partial start date of new anticancer therapy, the censoring date will be the last tumor assessment during treatment periods.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 106. Incomplete Date Logic (PD/Death Follow-Up - Missing Day/Month - Censored Case 2)

- **evaluation type:** semantic
- **original SAP text:** * If at least one of tumor assessment during Follow-Up Period < the partial start date of new anticancer therapy, the censoring date will be [text cuts off in source, but logic implies last tumor assessment prior to partial date]
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Specific imputation logic for incomplete dates
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 107. Salvage Treatment Listing

- **evaluation type:** semantic
- **original SAP text:** Salvage treatment during the Follow-Up Period will be recorded in ‘Salvage Treatment' eCRF pages and details will be listed and tabulated by salvage treatment category and treatment group in the ITT population.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Salvage treatment listing
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 108. Salvage Treatment Coding

- **evaluation type:** semantic
- **original SAP text:** Medications used for chemotherapy/immunotherapy/targeted therapy will be coded using the WHO Drug Dictionary version March, 2021 or later and surgery will be coded using MedDRA version 24.0 or higher.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Coding dictionaries for salvage treatment
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 109. Salvage Treatment Drug Class

- **evaluation type:** semantic
- **original SAP text:** Chemotherapy/immunotherapy/targeted therapy data will also be presented by drug class (using Anatomical Therapeutic Chemical [ATC] level 2).
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** ATC level 2 presentation
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 110. Salvage Treatment Summary Timing

- **evaluation type:** semantic
- **original SAP text:** Salvage treatment will be summarized for 2nd CSR and final CSR.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Timing of summary
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

#### 111. Effusion Drainage Listing

- **evaluation type:** semantic
- **original SAP text:** Effusion drainage information will be listed by treatment group for ITT population.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Effusion drainage listing
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Not in protocol.

---

### Issues Found (1 items)

#### 1. Primary Analysis Context

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** It is noted that the primary efficacy analysis (Section 8.1) was completed in the 1st CSR. In the final CSR, the analysis for the primary efficacy endpoint will be performed as a sensitivity analysis using the same method as 1st CSR.
- **generated SAP text:** The primary analysis of efficacy and safety is planned after all patients have completed Cycle 6 of the Induction Study Period... The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **protocol text:** The sponsor plans to prepare 3 CSRs... To report data after completion of the Induction Study Period... To report all data until the end of study.
- **why they conflict:** The Original SAP is specifically for the Final CSR (3rd CSR) and states the primary analysis was already done in the 1st CSR. The Generated SAP is written as if it is the initial plan for the primary analysis.
- **description:** The Generated SAP fails to reflect the specific context of the Original SAP (Version 3.0 for Final CSR), treating the primary analysis as a future event rather than a completed one being repeated as sensitivity.
- **reasoning:** 1) Original SAP says primary analysis was completed in 1st CSR and will be repeated as sensitivity in Final CSR. 2) Generated SAP says primary analysis is planned after Cycle 6. 3) These conflict because the Generated SAP ignores the study status (Final CSR). 4) Both cannot be true for the same document version.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (0 items)

*No missing from generated sap.*

---

### Reasoning

The Generated SAP captures the core statistical methods (Logistic Regression, Kaplan-Meier, Cox Model) and endpoints (ORR, PFS, OS, TTP, Response Duration) correctly. However, it fails to reflect the specific context of the Original SAP, which is Version 3.0 for the Final CSR. The Original SAP explicitly states that the primary analysis was completed in the 1st CSR and is now a sensitivity analysis. The Generated SAP presents the primary analysis as the main planned analysis. Additionally, the Generated SAP omits detailed logic for handling incomplete dates for efficacy events and the specific requirement for a Tipping Point analysis for the primary endpoint, which are present in the Original SAP.

---

### Summary

The Generated SAP correctly identifies the efficacy endpoints and basic statistical methods but fails to capture the specific context of the Final CSR (treating the primary analysis as a sensitivity analysis). It also omits detailed date imputation logic and the tipping point analysis requirement.