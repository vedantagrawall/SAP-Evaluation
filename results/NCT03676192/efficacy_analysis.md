## Efficacy Analysis Evaluation

**Section:** efficacy_analysis
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **Sections read:** 8, 8.1, 8.2, 8.2.1, 8.2.2, 8.2.2.1, 8.2.2.2, 8.2.2.3, 8.2.2.4, 8.2.2.5, 8.3, 8.4
- **Elements per section:** 8: 13, 8.1: 26, 8.2.1: 5, 8.2.2: 19, 8.2.2.1: 9, 8.2.2.2: 9, 8.2.2.3: 9, 8.2.2.4: 4, 8.2.2.5: 12, 8.3: 4, 8.4: 1
- **Elements extracted:** 111
- **Elements in evaluation table:** 111
- **Elements in missing from generated SAP:** 0
- **Counts match:** True

---

### Evaluation Table (111 items)

#### 1. Focus of Final CSR

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Efficacy analyses for the final CSR focus on secondary efficacy endpoints (Section 8.2) based on patients' long-term follow-up data.
- **Generated SAP text:** The final analysis will include the final assessment of all secondary efficacy, pharmacokinetic, quality of life, and safety endpoints.
- **Protocol text:** The sponsor plans to prepare 3 CSRs... To report all data until the end of study.
- **Reasoning:** Both documents identify the final analysis focus on secondary endpoints/long-term data.

#### 2. Primary Analysis Completion Status

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** contradiction_original
- **Severity:** minor
- **Detail level:** contradiction
- **Original SAP text:** It is noted that the primary efficacy analysis (Section 8.1) was completed in the 1st CSR.
- **Generated SAP text:** The primary analysis of efficacy and safety is planned after all patients have completed Cycle 6 of the Induction Study Period
- **Protocol text:** The sponsor plans to prepare 3 CSRs... To report data after completion of the Induction Study Period
- **Omission impact:** potential
- **Reasoning:** The Original SAP (Version 3.0) states the primary analysis was *already* completed in the 1st CSR. The Generated SAP describes it as a planned future event. This reflects a difference in the document version/timing context.

#### 3. Primary Endpoint Analysis in Final CSR

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** contradiction_original
- **Severity:** minor
- **Detail level:** contradiction
- **Original SAP text:** In the final CSR, the analysis for the primary efficacy endpoint will be performed as a sensitivity analysis using the same method as 1st CSR.
- **Generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **Protocol text:** null
- **Omission impact:** potential
- **Reasoning:** Original SAP treats the primary endpoint analysis in this document as a sensitivity analysis (since the primary analysis was done in 1st CSR). Generated SAP treats it as the main primary analysis.

#### 4. Efficacy Assessment Methods

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **Generated SAP text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **Protocol text:** Efficacy will be assessed by response evaluation and time-to-event analyses.
- **Reasoning:** Matches.

#### 5. RECIST Version

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Response evaluation will be based on tumor responses measured and recorded by using Response Evaluation Criteria In Solid Tumors (RECIST) version 1.1.
- **Generated SAP text:** as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **Protocol text:** Tumor responses will be measured and recorded by using RECIST v.1.1.
- **Reasoning:** Matches.

#### 6. Endpoints Determination

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The primary endpoint, ORR during the Induction Study Period, and the secondary endpoint, ORR during the Whole Study Period, will be determined by the BOR.
- **Generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR)...
- **Protocol text:** The primary endpoint, ORR during the Induction Study Period, and the secondary endpoint, ORR during the Whole Study Period, will be determined by the best overall response (BOR).
- **Reasoning:** Matches.

#### 7. Confirmation Requirement

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** For CR or PR, BOR must be confirmed by the subsequent assessment.
- **Generated SAP text:** While the primary endpoint requires confirmation (as per RECIST 1.1)...
- **Protocol text:** For CR or PR, BOR must be confirmed by the subsequent assessment based on the RECIST v.1.1
- **Reasoning:** Matches.

#### 8. Response Categories

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Categorization of BOR will use the following response categories: CR, PR, SD, PD and NE.
- **Generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **Protocol text:** Categorization of overall response at each visit will be based on RECIST v.1.1 using the following response categories: CR, PR, SD, PD, and inevaluable (NE)
- **Reasoning:** Matches.

#### 9. Image Review

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Images for tumor assessment will be reviewed separately by central and local, and both image review results from central (central independent reviewer) and local (eCRF) will be analyzed and listed separately.
- **Generated SAP text:** as determined by an Independent Tumor Review Committee (central review)... The primary analysis methodology described in Section 6.1.1.2 will be repeated using the BOR as determined by the investigator's local review
- **Protocol text:** In addition, all tumor assessment images will be evaluated centrally by an independent reviewer for reporting purposes
- **Reasoning:** Matches.

#### 10. Time-to-Event Endpoints List

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Time-to-event analysis for the study drug (CT-P16 or EU-Approved Avastin) will be undertaken for each of the response duration, TTP, PFS, and OS.
- **Generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations... Progression-Free Survival (PFS)... Time to Progression (TTP)... Overall Survival (OS)... Response Duration
- **Protocol text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS
- **Reasoning:** Matches.

#### 11. Primary Analysis Population

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Primary analysis population for the efficacy analysis is the ITT population.
- **Generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **Protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **Reasoning:** Matches.

#### 12. Supportive Analysis Population

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** A supportive analysis will be repeated using the PP population.
- **Generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **Protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model... in the ITT and PP population.
- **Reasoning:** Matches.

#### 13. Efficacy Data Listing

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** All efficacy data will be listed for the ITT population by treatment group unless otherwise specified.
- **Generated SAP text:** All data collected will be listed by patient, treatment, and visit where applicable.
- **Protocol text:** All safety data including immunogenicity will be listed
- **Reasoning:** Matches.

#### 14. Primary Endpoint Sensitivity Analysis (Final CSR)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** contradiction_original
- **Severity:** minor
- **Detail level:** contradiction
- **Original SAP text:** In the final CSR, the analysis for the protocol-specified primary efficacy endpoint will be performed as a sensitivity analysis using method described in this section.
- **Protocol text:** null
- **Omission impact:** potential
- **Reasoning:** Generated SAP does not distinguish between the primary analysis timing and the final CSR sensitivity analysis.

#### 15. Primary Endpoint Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The primary efficacy endpoint is ORR based on BOR during the Induction Study Period by RECIST version 1.1 (Appendix 14.5).
- **Generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR) during the Induction Study Period (up to Cycle 6) as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **Protocol text:** The primary efficacy endpoint will be the ORR based on BOR during the Induction Study Period by RECIST v.1.1
- **Reasoning:** Matches.

#### 16. ORR Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The ORR is defined as the proportion of patients with a confirmed BOR of CR or PR (the 'responder').
- **Generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR)
- **Protocol text:** Objective response rate will be calculated as the number of patients with a response of CR or PR divided by the number of patients in the corresponding population.
- **Reasoning:** Matches.

#### 17. Non-Responder Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** All other patients in the ITT or PP population except responders will be considered as non-responder including patients without post-baseline tumor assessment.
- **Generated SAP text:** Patients with no post-baseline tumor assessment or whose response cannot be evaluated (NE) will be treated as non-responders for the primary analysis.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 18. Similarity Criterion

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The similarity criterion has been set such that the confidence limits of the 95% CI of the difference in ORR from each treatment group will be entirely bounded by the interval (-12.5, 12.5).
- **Generated SAP text:** Therapeutic similarity will be concluded if the 2-sided 95% CI for the difference in ORR is entirely contained within the equivalence margin of (-12.5%, 12.5%).
- **Protocol text:** The similarity criterion has been set such that the confidence limits of the 95% CI of the difference in ORR will be entirely bounded by the interval (-12.5, 12.5).
- **Reasoning:** Matches.

#### 19. Primary Analysis Model

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance status at baseline (0 vs. 1) as covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect.
- **Generated SAP text:** The model will include treatment group as a fixed effect. Covariates will include the stratification factors: sex (female vs. male), disease status (recurrence vs. metastatic), and ECOG performance score (0 vs. 1). Country will be included as a covariate
- **Protocol text:** The primary analysis for the primary endpoint will be performed utilizing a logistic regression model considering covariates with treatment groups (CT-P16 and EU-Approved Avastin) as a fixed effect
- **Reasoning:** Matches.

#### 20. Pooling Country

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Country can be pooled into region (EMEA vs. America vs. Asia) for statistical analysis when there are not enough patients within each country.
- **Generated SAP text:** Country will be included as a covariate unless there are sparse data across centers/countries, in which case it may be pooled by region.
- **Protocol text:** null
- **Omitted content:** Specific regions (EMEA vs. America vs. Asia)
- **Omission impact:** low
- **Reasoning:** Gen SAP mentions pooling by region but omits the specific regions defined in Original SAP.

#### 21. Region Discussion

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Use of region instead of country in statistical analyses was discussed at the blinded DRM.
- **Protocol text:** null
- **Omitted content:** Statement about DRM discussion
- **Reasoning:** Procedural detail not required in SAP text.

#### 22. ORR Table

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** A table presenting ORR during the Induction Study Period with the analysis result will be produced.
- **Generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 23. ORR and 95% CI Presentation

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** The ORR and its corresponding 95% CI for each treatment group will also be presented.
- **Generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders...
- **Protocol text:** null
- **Omitted content:** Explicit mention of 95% CI for each group
- **Omission impact:** low
- **Reasoning:** Implied by standard descriptive statistics.

#### 24. Risk Difference Presentation

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** A point estimate and 95% CI of the risk difference of ORR between CT-P16 group and EU-Approved Avastin group will be produced.
- **Generated SAP text:** Population-level Summary: Difference in ORR (%) between CT-P16 and EU-Approved Avastin.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 25. Response Category Presentation

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The number and percentage of patients in each response category will also be presented by treatment group separately.
- **Generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 26. Primary Analysis Population (ITT)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The primary analysis will be conducted in the ITT population.
- **Generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **Protocol text:** The primary analysis for the primary endpoint will be performed... in the ITT and PP population.
- **Reasoning:** Matches.

#### 27. Supportive Analysis Population (PP)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** A supportive analysis will be conducted in the PP population and also be provided in the table.
- **Generated SAP text:** The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **Protocol text:** The primary analysis for the primary endpoint will be performed... in the ITT and PP population.
- **Reasoning:** Matches.

#### 28. Central Review for Primary

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** For the primary analysis, central review results will be used.
- **Generated SAP text:** as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **Protocol text:** For primary analysis, central review result will be used.
- **Reasoning:** Matches.

#### 29. Local Review Sensitivity

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Local review results will be used for a sensitivity analysis.
- **Generated SAP text:** The primary analysis methodology described in Section 6.1.1.2 will be repeated using the BOR as determined by the investigator's local review to support the findings of the central review.
- **Protocol text:** Local review result will be used as supportive data (sensitivity analysis).
- **Reasoning:** Matches.

#### 30. Tipping Point Analysis

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Tipping point analysis will also be conducted using central review data based on exact binomial approach in the ITT population for a sensitivity analysis.
- **Protocol text:** null
- **Omitted content:** Tipping point analysis
- **Omission impact:** low
- **Reasoning:** Not in protocol, so acceptable difference.

#### 31. Delta Method Explanation

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** The Delta Method for estimating difference of proportion is explained in the following process.
- **Generated SAP text:** The resulting odds ratio and its 95% CI will be converted into a difference in proportions (CT-P16 – EU-Approved Avastin) using the Delta method.
- **Protocol text:** The resulting odds ratio and 95% CI will be converted into difference of proportions using the Delta method for the purpose of comparison.
- **Omitted content:** Detailed steps 1-5 and formulas
- **Omission impact:** low
- **Reasoning:** Gen SAP mentions Delta method but omits the detailed mathematical steps. This is acceptable as the method is standard.

#### 32. Delta Method Step 1

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** (1) The individual odds and standard errors (SEs) for both treatments will be obtained from the model.
- **Protocol text:** null
- **Omitted content:** Step 1 details
- **Omission impact:** low
- **Reasoning:** Part of detailed formula.

#### 33. Delta Method Step 1 (Definitions)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** For the purposes of this algorithm, let the estimate of the odds of being a responder in the CT-P16 group be denoted by $\theta_a$ and the estimate of the odds of being a responder in the EU-Approved Avastin group be denoted by $\theta_b$.
- **Protocol text:** null
- **Omitted content:** Variable definitions
- **Omission impact:** low
- **Reasoning:** Part of detailed formula.

#### 34. Delta Method Step 2

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** (2) Calculate the variances of these estimates, $Var(\theta_a)$ and $Var(\theta_b)$ respectively from the SEs obtained from the model.
- **Protocol text:** null
- **Omitted content:** Step 2 details
- **Omission impact:** low
- **Reasoning:** Part of detailed formula.

#### 35. Delta Method Step 3

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** (3) Calculate the estimates of the corresponding proportions, denoted $p_a$ and $p_b$ respectively, for each of the randomized treatment groups, from the estimated odds $\theta_a$ and $\theta_b$ using the following formula: $p = \frac{\theta}{1 + \theta}$ and hence calculate the estimate of the difference of proportions $p_a - p_b$.
- **Protocol text:** null
- **Omitted content:** Step 3 details and formula
- **Omission impact:** low
- **Reasoning:** Part of detailed formula.

#### 36. Delta Method Step 4

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** (4) Using Taylor expansions and the Delta method, the following formula for approximation can be obtained: $Var[f(X)] \approx (f'(E[X]))^2Var[X]$ Applying this approximation specifically to this case, and using the formula specified in step (3) we obtain the formula $Var(p) = \frac{Var(\theta)}{(1+\theta)^4}$ which should be used to calculate $Var(p_a)$ and $Var(p_b)$.
- **Protocol text:** null
- **Omitted content:** Step 4 details and formula
- **Omission impact:** low
- **Reasoning:** Part of detailed formula.

#### 37. Delta Method Step 5

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** (5) Calculate the variance of the difference in proportions $Var(p_a - p_b)$ as the sum of $Var(p_a)$ and $Var(p_b)$.
- **Protocol text:** null
- **Omitted content:** Step 5 details
- **Omission impact:** low
- **Reasoning:** Part of detailed formula.

#### 38. Delta Method CI Formula

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Use this to obtain the SE of the difference, and hence calculate the 95% CI using the formula: $95\% \text{ Confidence Interval } = (p_a - p_b) +/- 1.96(SE(p_a - p_b))$
- **Protocol text:** null
- **Omitted content:** CI formula
- **Omission impact:** low
- **Reasoning:** Part of detailed formula.

#### 39. Independence Assumption

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Note: this method assumes that the estimate ORR of CT-P16 group is independent of the estimate of EU-Approved Avastin group.
- **Protocol text:** null
- **Omitted content:** Independence assumption note
- **Omission impact:** low
- **Reasoning:** Statistical assumption.

#### 40. Secondary Endpoint: ORR Whole Study

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** For the secondary efficacy endpoint, ORR based on BOR during the Whole Study Period by RECIST version 1.1 will be analyzed.
- **Generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed
- **Protocol text:** ORR based on BOR during the Whole Study Period by RECIST v.1.1
- **Reasoning:** Matches.

#### 41. Whole Study ORR Table

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** A table will be produced using both central review data and local review data from all treatment periods including Induction Study Period, Maintenance Study Period and EOT visit in the ITT and PP population.
- **Generated SAP text:** The ORR based on BOR during the Whole Study Period (Induction + Maintenance + Follow-up) will be analyzed for both the ITT and PP populations.
- **Protocol text:** The secondary endpoint, both locally reviewed ORR and centrally reviewed ORR during the Whole Study Period, will be summarized... in the ITT and PP population.
- **Omitted content:** Explicit mention of central and local review for this specific endpoint
- **Omission impact:** low
- **Reasoning:** Gen SAP mentions central/local generally, but not specifically for this endpoint.

#### 42. Whole Study ORR CI

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The ORR and its corresponding 95% CI for each treatment group will also be presented.
- **Generated SAP text:** The proportion of responders and the 2-sided 95% CI for each treatment group will be calculated using the Clopper-Pearson method.
- **Protocol text:** summarized using proportion and its corresponding 95% CI
- **Reasoning:** Matches.

#### 43. Whole Study Response Categories

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** The number and percentage of patients within each response category will be summarized by treatment group.
- **Protocol text:** null
- **Omitted content:** Summary of response categories
- **Omission impact:** low
- **Reasoning:** Standard reporting.

#### 44. Whole Study ORR Timing

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The ORR based on BOR during the Whole Study Period will be analyzed only for the final CSR.
- **Generated SAP text:** The final analysis will include the final assessment of all secondary efficacy... endpoints.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 45. TTE Analysis Scope

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population.
- **Generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations... Progression-Free Survival (PFS)... Time to Progression (TTP)... Overall Survival (OS)... Response Duration
- **Protocol text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population
- **Reasoning:** Matches.

#### 46. TTE Summary

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** The number of patients experiencing events and the number of censored patients will be summarized by treatment group with reasons for an event/censoring.
- **Protocol text:** null
- **Omitted content:** Summary of events/censoring reasons
- **Omission impact:** low
- **Reasoning:** Standard reporting.

#### 47. KM Median and CI

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The median survival time and its corresponding 95% CI for each treatment group will be estimated using the Kaplan-Meier method.
- **Generated SAP text:** Kaplan-Meier (KM) Method: Used to estimate the survival distributions... Median TTE... will be calculated with 95% CIs.
- **Protocol text:** the median time and its corresponding 95% CI for each treatment group... will be estimated using the Kaplan-Meier method.
- **Reasoning:** Matches.

#### 48. Survival Percentiles

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** The 25th percentile and 75th percentile for the survival times along with the corresponding 95% CI for the percentiles will also be displayed.
- **Protocol text:** null
- **Omitted content:** 25th and 75th percentiles
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 49. Brookmeyer-Crowley Method

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The Brookmeyer-Crowley methodology will be used to construct the 95% CI for each percentile.
- **Generated SAP text:** The 95% CI for the median will be calculated using the Brookmeyer-Crowley method.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 50. Decimal Places (Time)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Survival times and their corresponding 95% CIs will be presented to one decimal place.
- **Protocol text:** null
- **Omitted content:** Decimal place specification
- **Omission impact:** low
- **Reasoning:** Formatting detail.

#### 51. Survival Rates

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** In addition, the estimate of survival rates (at 6, 12, 24, 36 months for response duration, TTP, PFS and at 12, 24, 36 months for OS) will be displayed along with their corresponding 95% CI.
- **Generated SAP text:** survival rates at specific landmarks (e.g., 6 months, 12 months) will be calculated with 95% CIs.
- **Protocol text:** null
- **Omitted content:** Specific timepoints (24, 36 months)
- **Omission impact:** low
- **Reasoning:** Gen SAP mentions landmarks but omits the specific list.

#### 52. Decimal Places (Rates)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** The estimates of survival rates and their corresponding 95% CIs will be presented to two decimal places.
- **Protocol text:** null
- **Omitted content:** Decimal place specification
- **Omission impact:** low
- **Reasoning:** Formatting detail.

#### 53. Time Unit

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** All time-to-event data will be reported in months with reasons for an event/censoring and summarized by treatment group.
- **Protocol text:** null
- **Omitted content:** Reporting in months
- **Omission impact:** low
- **Reasoning:** Standard practice.

#### 54. Days to Months Conversion

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **Protocol text:** null
- **Omitted content:** Conversion formula
- **Omission impact:** low
- **Reasoning:** Standard practice.

#### 55. Death Date Imputation

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** For the purposes of inclusion in the survival analysis, incomplete death dates will be imputed as described in Appendix 14.4.3.
- **Protocol text:** null
- **Omitted content:** Imputation reference
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 56. New Anticancer Therapy Censoring

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** To determine ‘event' or ‘censoring' for response duration, TTP and PFS, initiation of new anticancer therapy will be considered.
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **Protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment... before starting another anticancer therapy.
- **Reasoning:** Matches.

#### 57. Incomplete Date Logic Reference

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** For missing or incomplete start date of new anticancer therapy, the capture logic of event or censoring will be followed in Section 8.2.2.5.
- **Protocol text:** null
- **Omitted content:** Reference to incomplete date logic
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 58. KM Plot

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** A Kaplan-Meier plot will be presented for each of the time-to-event analyses.
- **Generated SAP text:** Kaplan-Meier Plot of Progression-Free Survival... Kaplan-Meier Plot of Overall Survival
- **Protocol text:** null
- **Reasoning:** Matches.

#### 59. Cox Regression Model

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** In PFS and OS analyses, an adjusted stratified cox regression model will be used to estimate the hazard ratio and its 95% CI for receiving CT-P16 compared with receiving EU-Approved Avastin using country, sex (female vs. male), disease status at baseline (recurrence vs. metastatic), and ECOG performance score at baseline (0 vs. 1) as stratification factors.
- **Generated SAP text:** A stratified Cox proportional hazards model, including the same stratification factors used in the randomization, will be used to estimate the HR (CT-P16 / EU-Approved Avastin) and its 95% CI.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 60. Pooling Country (Cox)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Country can be pooled into region (EMEA vs. America vs. Asia) for statistical analysis when there are not enough patients within each country.
- **Protocol text:** null
- **Omitted content:** Pooling strategy for Cox model
- **Omission impact:** low
- **Reasoning:** Implied by randomization factors.

#### 61. TTE Analysis Timing

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** All time-to-event analyses will be conducted for 2nd CSR and final CSR.
- **Generated SAP text:** The final analysis will include the final assessment of all secondary efficacy... endpoints.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 62. TTE Review Basis

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** All time-to-event analyses related to response duration, TTP and PFS will be performed based on the central and local review in terms of PD/recurrence, CR and PR.
- **Protocol text:** null
- **Omitted content:** Explicit mention of both central and local review for TTE
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 63. Data Sources

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Records on ‘Randomization', 'Survival Status', 'Response Evaluation', 'Salvage Treatment' or 'Study Treatment Termination' eCRF pages will be used.
- **Protocol text:** null
- **Omitted content:** eCRF page references
- **Omission impact:** low
- **Reasoning:** Data management detail.

#### 64. Response Duration Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Response duration is defined as the time between initial response (CR or PR) that is confirmed by the subsequent assessment after study treatment administration and PD/recurrence or death from any cause (whichever occurs first).
- **Generated SAP text:** Response Duration: Time from the first documented response (CR or PR) until the first documentation of PD or death (among responders only).
- **Protocol text:** Response duration: the time between initial response (CR or PR) and PD/recurrence
- **Reasoning:** Matches.

#### 65. Response Duration Population

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Time-to-event analysis for response duration will be performed for patients who have confirmed BOR of CR or PR.
- **Generated SAP text:** (among responders only)
- **Protocol text:** null
- **Reasoning:** Matches.

#### 66. Response Duration Event

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** PD/recurrence or death that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **Generated SAP text:** until the first documentation of PD or death
- **Protocol text:** null
- **Reasoning:** Matches.

#### 67. Response Duration Censoring (No Event)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** No event and no anticancer therapy -> Last tumor assessment date
- **Generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **Protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **Reasoning:** Matches.

#### 68. Response Duration Censoring (New Therapy)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **Protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment... before starting another anticancer therapy.
- **Reasoning:** Matches.

#### 69. Response Duration Censoring (Missing Assessments)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Event after missing two or more tumor assessment* -> Last tumor assessment date before event
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **Protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment
- **Reasoning:** Matches.

#### 70. Censoring Date Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The last tumor assessment date on which tumor assessment's is neither ‘missing' nor ‘NE' will be used for censoring date.
- **Generated SAP text:** last adequate tumor assessment
- **Protocol text:** last adequate radiological assessment
- **Reasoning:** Matches.

#### 71. Single Missing Assessment Rule

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **Protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **Omitted content:** Explicit rule for single missing assessment
- **Omission impact:** low
- **Reasoning:** Implied by the rule for missing two or more.

#### 72. Response Duration Formula

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **Protocol text:** null
- **Omitted content:** Formula
- **Omission impact:** low
- **Reasoning:** Standard calculation.

#### 73. TTP Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** TTP is defined as time from randomization to determined PD/recurrence.
- **Generated SAP text:** Time to Progression (TTP): Time from randomization until the first documentation of PD.
- **Protocol text:** TTP: the time from randomization until PD/recurrence
- **Reasoning:** Matches.

#### 74. TTP Event

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** PD/recurrence that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **Generated SAP text:** Time to Progression (TTP): Time from randomization until the first documentation of PD.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 75. TTP Censoring (No Assessment)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** No tumor assessment -> The date of randomization
- **Protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **Omitted content:** Censoring rule for no assessment
- **Omission impact:** low
- **Reasoning:** Standard rule.

#### 76. TTP Censoring (No Event)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** No event and no anticancer therapy -> Last tumor assessment date
- **Generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **Protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **Reasoning:** Matches.

#### 77. TTP Censoring (New Therapy)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **Protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment... before starting another anticancer therapy.
- **Reasoning:** Matches.

#### 78. TTP Censoring (Missing Assessments)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Event after missing two or more tumor assessment* -> Last tumor assessment date before event
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **Protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment
- **Reasoning:** Matches.

#### 79. TTP Censoring Date Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The last tumor assessment date on which tumor assessment's is neither 'missing' nor 'NE' will be used for censoring date.
- **Generated SAP text:** last adequate tumor assessment
- **Protocol text:** last adequate radiological assessment
- **Reasoning:** Matches.

#### 80. TTP Single Missing Assessment Rule

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **Protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **Omitted content:** Explicit rule for single missing assessment
- **Omission impact:** low
- **Reasoning:** Implied.

#### 81. TTP Formula

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Protocol text:** null
- **Omitted content:** Formula
- **Omission impact:** low
- **Reasoning:** Standard calculation.

#### 82. PFS Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** PFS is defined as time from randomization to determined PD/recurrence or death from any cause (whichever occurs first).
- **Generated SAP text:** Progression-Free Survival (PFS): Time from randomization until the first documentation of PD (per RECIST v.1.1) or death due to any cause.
- **Protocol text:** PFS: the time from randomization until PD/recurrence or death due to any cause, whichever occurs first
- **Reasoning:** Matches.

#### 83. PFS Event

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** PD/recurrence or death that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **Generated SAP text:** Progression-Free Survival (PFS): Time from randomization until the first documentation of PD (per RECIST v.1.1) or death due to any cause.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 84. PFS Censoring (No Assessment)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** No tumor assessment -> The date of randomization
- **Protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **Omitted content:** Censoring rule for no assessment
- **Omission impact:** low
- **Reasoning:** Standard rule.

#### 85. PFS Censoring (No Event)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** No event and no anticancer therapy -> Last tumor assessment date
- **Generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **Protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **Reasoning:** Matches.

#### 86. PFS Censoring (New Therapy)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Initiation of New anticancer therapy -> Last tumor assessment date before anticancer therapy
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **Protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment... before starting another anticancer therapy.
- **Reasoning:** Matches.

#### 87. PFS Censoring (Missing Assessments)

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Event after missing two or more tumor assessment* -> Last tumor assessment date before event
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **Protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment
- **Reasoning:** Matches.

#### 88. PFS Censoring Date Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The last tumor assessment date on which tumor assessment's is neither ‘missing' nor ‘NE' will be used for censoring date.
- **Generated SAP text:** last adequate tumor assessment
- **Protocol text:** last adequate radiological assessment
- **Reasoning:** Matches.

#### 89. PFS Single Missing Assessment Rule

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **Protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **Omitted content:** Explicit rule for single missing assessment
- **Omission impact:** low
- **Reasoning:** Implied.

#### 90. PFS Formula

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Protocol text:** null
- **Omitted content:** Formula
- **Omission impact:** low
- **Reasoning:** Standard calculation.

#### 91. OS Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** OS is defined as time from randomization to death from any cause.
- **Generated SAP text:** Overall Survival (OS): Time from randomization until death due to any cause.
- **Protocol text:** OS: the time from randomization until death due to any cause
- **Reasoning:** Matches.

#### 92. OS Event

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Death will be regarded as an event.
- **Generated SAP text:** Overall Survival (OS): Time from randomization until death due to any cause.
- **Protocol text:** null
- **Reasoning:** Matches.

#### 93. OS Censoring

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Censoring will be defined as following: Non-death -> Last known alive date
- **Generated SAP text:** Patients alive... at the time of data cutoff/study completion will be censored... (implied)
- **Protocol text:** for patients whose status is unknown, data will be censored at the time when the patient is last known to be alive.
- **Omitted content:** Explicit 'Last known alive date' phrasing
- **Omission impact:** low
- **Reasoning:** Standard practice.

#### 94. OS Formula

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Protocol text:** null
- **Omitted content:** Formula
- **Omission impact:** low
- **Reasoning:** Standard calculation.

#### 95. Incomplete Date Logic (New Anticancer Therapy)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** A patient will be considered as taking a new anticancer therapy (other than study treatments) when there is any record on ‘Salvage treatment' eCRF pages or a record of receiving anticancer therapy on ‘Survival Status' eCRF page.
- **Protocol text:** null
- **Omitted content:** Definition of new anticancer therapy source
- **Omission impact:** low
- **Reasoning:** Data management detail.

#### 96. Incomplete Date Logic (No PD/Death)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** When there is no PD/recurrence (or death) and the start date of new anticancer therapy is incomplete, censoring date will be determined as following: 1) If the last tumor assessment is performed during treatment periods (including EOT visit), the censoring date will be the last tumor assessment date during treatment periods.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 97. Incomplete Date Logic (Follow-Up Period - Missing Day)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** 2) If the last tumor assessment is performed during Follow-Up Period, censoring date will be determined as following: a. If the day of the start date of new anticancer therapy is missing, then the censoring date will be the last tumor assessment date, provided tumor assessment date < the partial start date of new anticancer therapy.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 98. Incomplete Date Logic (Follow-Up Period - Missing Day/Month)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** b. If the day and month of the start date of new anticancer therapy is missing, censoring date will be determined as following: * If all dates of tumor assessments during Follow-Up Period >= the partial start date of new anticancer therapy, the censoring date will be the last tumor assessment during treatment periods.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 99. Incomplete Date Logic (Follow-Up Period - Missing Day/Month - Case 2)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** * If at least one of tumor assessment during Follow-Up Period < the partial start date of new anticancer therapy, the censoring date will be the last tumor assessment, provided tumor assessment date < the partial start date of new anticancer therapy.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 100. Incomplete Date Logic (Completely Missing)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** c. If the start date of new anticancer therapy is completely missing, censoring date will be the last tumor assessment date during treatment periods.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 101. Incomplete Date Logic (PD/Death Event)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** When PD/recurrence (or death) is occurred and the start of new anticancer therapy is incomplete, event will be determined as following: 1) If the first PD/recurrence (or death) is occurred during treatment periods, it will be regarded as 'event'.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 102. Incomplete Date Logic (PD/Death Follow-Up - Missing Day)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** 2) If the first PD/recurrence (or death) is occurred during Follow-Up Period, and a. If the day of the start date of new anticancer therapy is missing, and i. If the first PD/recurrence (or death) date < the partial start date of new anticancer therapy, it will be regarded as 'event'.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 103. Incomplete Date Logic (PD/Death Follow-Up - Missing Day - Censored)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** ii. If the first PD/recurrence (or death) date >= the partial start date of new anticancer therapy, it will be censored. The censoring date will be the last tumor assessment, provided the tumor assessment date < the partial start date of new anticancer therapy.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 104. Incomplete Date Logic (PD/Death Follow-Up - Missing Day/Month)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** b. If the day and month of start date of new anticancer therapy is missing, and i. If the first PD/recurrence (or death) date < the partial start date of new anticancer therapy, it will be regarded as 'event'.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 105. Incomplete Date Logic (PD/Death Follow-Up - Missing Day/Month - Censored)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** ii. If the first PD/recurrence (or death) date >= the partial start date of new anticancer therapy, it will be censored. The censoring date will be as follows: * If all dates of tumor assessments during Follow-Up Period >= the partial start date of new anticancer therapy, the censoring date will be the last tumor assessment during treatment periods.
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 106. Incomplete Date Logic (PD/Death Follow-Up - Missing Day/Month - Censored Case 2)

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** * If at least one of tumor assessment during Follow-Up Period < the partial start date of new anticancer therapy, the censoring date will be [text cuts off in source, but logic implies last tumor assessment prior to partial date]
- **Protocol text:** null
- **Omitted content:** Specific imputation logic for incomplete dates
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 107. Salvage Treatment Listing

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Salvage treatment during the Follow-Up Period will be recorded in ‘Salvage Treatment' eCRF pages and details will be listed and tabulated by salvage treatment category and treatment group in the ITT population.
- **Protocol text:** null
- **Omitted content:** Salvage treatment listing
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 108. Salvage Treatment Coding

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Medications used for chemotherapy/immunotherapy/targeted therapy will be coded using the WHO Drug Dictionary version March, 2021 or later and surgery will be coded using MedDRA version 24.0 or higher.
- **Protocol text:** null
- **Omitted content:** Coding dictionaries for salvage treatment
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 109. Salvage Treatment Drug Class

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Chemotherapy/immunotherapy/targeted therapy data will also be presented by drug class (using Anatomical Therapeutic Chemical [ATC] level 2).
- **Protocol text:** null
- **Omitted content:** ATC level 2 presentation
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 110. Salvage Treatment Summary Timing

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Salvage treatment will be summarized for 2nd CSR and final CSR.
- **Protocol text:** null
- **Omitted content:** Timing of summary
- **Omission impact:** low
- **Reasoning:** Not in protocol.

#### 111. Effusion Drainage Listing

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** Effusion drainage information will be listed by treatment group for ITT population.
- **Protocol text:** null
- **Omitted content:** Effusion drainage listing
- **Omission impact:** low
- **Reasoning:** Not in protocol.

---

### Issues Found (1 items)

#### Issue 1: Primary Analysis Context

- **Issue type:** contradiction_original
- **Severity:** minor
- **Original SAP text:** It is noted that the primary efficacy analysis (Section 8.1) was completed in the 1st CSR. In the final CSR, the analysis for the primary efficacy endpoint will be performed as a sensitivity analysis using the same method as 1st CSR.
- **Generated SAP text:** The primary analysis of efficacy and safety is planned after all patients have completed Cycle 6 of the Induction Study Period... The primary analysis will compare the ORR between the CT-P16 and EU-Approved Avastin groups in both the ITT and PP populations.
- **Protocol text:** The sponsor plans to prepare 3 CSRs... To report data after completion of the Induction Study Period... To report all data until the end of study.
- **Why they conflict:** The Original SAP is specifically for the Final CSR (3rd CSR) and states the primary analysis was already done in the 1st CSR. The Generated SAP is written as if it is the initial plan for the primary analysis.
- **Description:** The Generated SAP fails to reflect the specific context of the Original SAP (Version 3.0 for Final CSR), treating the primary analysis as a future event rather than a completed one being repeated as sensitivity.
- **Reasoning:** 1) Original SAP says primary analysis was completed in 1st CSR and will be repeated as sensitivity in Final CSR. 2) Generated SAP says primary analysis is planned after Cycle 6. 3) These conflict because the Generated SAP ignores the study status (Final CSR). 4) Both cannot be true for the same document version.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (0 items)

*No missing content.*

---

### Reasoning

The Generated SAP captures the core statistical methods (Logistic Regression, Kaplan-Meier, Cox Model) and endpoints (ORR, PFS, OS, TTP, Response Duration) correctly. However, it fails to reflect the specific context of the Original SAP, which is Version 3.0 for the Final CSR. The Original SAP explicitly states that the primary analysis was completed in the 1st CSR and is now a sensitivity analysis. The Generated SAP presents the primary analysis as the main planned analysis. Additionally, the Generated SAP omits detailed logic for handling incomplete dates for efficacy events and the specific requirement for a Tipping Point analysis for the primary endpoint, which are present in the Original SAP.

---

### Summary

The Generated SAP correctly identifies the efficacy endpoints and basic statistical methods but fails to capture the specific context of the Final CSR (treating the primary analysis as a sensitivity analysis). It also omits detailed date imputation logic and the tipping point analysis requirement.