## Objectives Endpoints Only Evaluation

**Section:** objectives_endpoints
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **sections read:** 2.1, 2.2, 8, 8.1, 8.2.1, 8.2.2, 8.2.2.1, 8.2.2.2, 8.2.2.3, 8.2.2.4, 9.2, 10.1, 10.1.5, 10.9, 11
- **elements per section:** 2.1: 1, 2.2: 4, 8: 3, 8.1: 2, 8.2.1: 1, 8.2.2: 3, 8.2.2.1: 7, 8.2.2.2: 8, 8.2.2.3: 8, 8.2.2.4: 4, 9.2: 3, 10.1: 1, 10.1.5: 11, 10.9: 3, 11: 4
- **elements extracted:** 63
- **elements in evaluation table:** 63
- **elements in missing from generated SAP:** 28
- **counts match:** True

---

### Evaluation Table (63 items)

#### 1. Primary Objective

- **evaluation type:** exact_match
- **original SAP text:** The primary objective of the study is: To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) during the Induction Study Period
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

#### 2. Secondary Objective - Efficacy

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

#### 3. Secondary Objective - PK

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

#### 4. Secondary Objective - Safety

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

#### 5. Secondary Objective - QoL

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

#### 6. Efficacy Endpoint Determination

- **evaluation type:** semantic
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
- **reasoning:** Matches concept.

#### 7. Confirmation of Response

- **evaluation type:** semantic
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
- **reasoning:** Matches concept.

#### 8. BOR Categories

- **evaluation type:** semantic
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
- **reasoning:** Matches categories.

#### 9. Primary Endpoint Definition

- **evaluation type:** exact_match
- **original SAP text:** The primary efficacy endpoint is ORR based on BOR during the Induction Study Period by RECIST version 1.1
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

#### 10. ORR Definition

- **evaluation type:** semantic
- **original SAP text:** The ORR is defined as the proportion of patients with a confirmed BOR of CR or PR (the 'responder').
- **generated SAP text:** defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR)
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

#### 11. Secondary Endpoint - ORR Whole Study

- **evaluation type:** exact_match
- **original SAP text:** For the secondary efficacy endpoint, ORR based on BOR during the Whole Study Period by RECIST version 1.1 will be analyzed.
- **generated SAP text:** ORR based on BOR during the Whole Study Period by RECIST v.1.1
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

#### 12. Time-to-Event Analysis List

- **evaluation type:** exact_match
- **original SAP text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population.
- **generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations. Progression-Free Survival (PFS)... Time to Progression (TTP)... Overall Survival (OS)... Response Duration...
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

#### 13. TTE Reporting Units

- **evaluation type:** semantic
- **original SAP text:** All time-to-event data will be reported in months with reasons for an event/censoring and summarized by treatment group.
- **generated SAP text:** Median TTE and survival rates at specific landmarks (e.g., 6 months, 12 months) will be calculated
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Implies months.

#### 14. Days to Months Conversion

- **evaluation type:** exact_match
- **original SAP text:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Conversion factor missing.

#### 15. Response Duration Definition

- **evaluation type:** semantic
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

#### 16. Response Duration Event

- **evaluation type:** semantic
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
- **reasoning:** Implied by censoring rule.

#### 17. Response Duration Censoring (No event)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No event and no anticancer therapy - Last tumor assessment date
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

#### 18. Response Duration Censoring (New therapy)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy - Last tumor assessment date before anticancer therapy
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

#### 19. Response Duration Censoring (Missing assessments)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* - Last tumor assessment date before event
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

#### 20. Response Duration Missing Exception

- **evaluation type:** semantic
- **original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored
- **protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Implied.

#### 21. Response Duration Formula

- **evaluation type:** exact_match
- **original SAP text:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Formula missing.

#### 22. TTP Definition

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

#### 23. TTP Event

- **evaluation type:** semantic
- **original SAP text:** PD/recurrence that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Implied.

#### 24. TTP Censoring (No assessment)

- **evaluation type:** exact_match
- **original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Specific censoring rule missing.

#### 25. TTP Censoring (No event)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No event and no anticancer therapy - Last tumor assessment date
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

#### 26. TTP Censoring (New therapy)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy - Last tumor assessment date before anticancer therapy
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

#### 27. TTP Censoring (Missing assessments)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* - Last tumor assessment date before event
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

#### 28. TTP Missing Exception

- **evaluation type:** semantic
- **original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored
- **protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Implied.

#### 29. TTP Formula

- **evaluation type:** exact_match
- **original SAP text:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Formula missing.

#### 30. PFS Definition

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

#### 31. PFS Event

- **evaluation type:** semantic
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
- **reasoning:** Implied.

#### 32. PFS Censoring (No assessment)

- **evaluation type:** exact_match
- **original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Specific censoring rule missing.

#### 33. PFS Censoring (No event)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: No event and no anticancer therapy - Last tumor assessment date
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

#### 34. PFS Censoring (New therapy)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy - Last tumor assessment date before anticancer therapy
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

#### 35. PFS Censoring (Missing assessments)

- **evaluation type:** semantic
- **original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* - Last tumor assessment date before event
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

#### 36. PFS Missing Exception

- **evaluation type:** semantic
- **original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored
- **protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Implied.

#### 37. PFS Formula

- **evaluation type:** exact_match
- **original SAP text:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Formula missing.

#### 38. OS Definition

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

#### 39. OS Event

- **evaluation type:** semantic
- **original SAP text:** Death will be regarded as an event.
- **generated SAP text:** Time from randomization until death due to any cause.
- **protocol consulted:** no
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Implied.

#### 40. OS Censoring

- **evaluation type:** exact_match
- **original SAP text:** Censoring will be defined as following: Non-death - Last known alive date
- **protocol text:** for patients whose status is unknown, data will be censored at the time when the patient is last known to be alive.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Censoring will be defined as following: Non-death - Last known alive date
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Specific censoring rule missing.

#### 41. OS Formula

- **evaluation type:** exact_match
- **original SAP text:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Formula missing.

#### 42. PK Parameter Definition

- **evaluation type:** semantic
- **original SAP text:** PK parameter is the observed Ctrough following drug administration; calculated from the pre-dose concentration of the next dose.
- **generated SAP text:** Ctrough: Trough serum concentration
- **protocol text:** The Ctrough (prior to next dose) at each cycle during the Induction Study Period, and Ctrough during the Maintenance Study Period will be analyzed.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** calculated from the pre-dose concentration of the next dose
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Definition is less detailed but consistent.

#### 43. PK Exclusion i

- **evaluation type:** exact_match
- **original SAP text:** The samples in following cases are excluded from calculation of Ctrough; i) Post-dose concentration in the Induction Study Period
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** The samples in following cases are excluded from calculation of Ctrough; i) Post-dose concentration in the Induction Study Period
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Exclusion criteria missing.

#### 44. PK Exclusion ii

- **evaluation type:** exact_match
- **original SAP text:** The samples in following cases are excluded from calculation of Ctrough; ii) interval between the last dose date and sampling date at EOT < 18 days
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** The samples in following cases are excluded from calculation of Ctrough; ii) interval between the last dose date and sampling date at EOT < 18 days
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Exclusion criteria missing.

#### 45. TEAE Definition

- **evaluation type:** semantic
- **original SAP text:** A Treatment-Emergent Adverse Event (TEAE) is defined as any event not present before exposure to study drug or any event already present that worsen in either severity or frequency after exposure to study drug.
- **generated SAP text:** A treatment-emergent abnormality is defined as a post-baseline value that represents a worsening from baseline (either an increase in CTCAE grade or a shift from Normal/Low to High, or Normal/High to Low).
- **protocol text:** A treatment-emergent AE is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** none
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Generated SAP defines TEAE only in context of labs, missing the general clinical definition.

#### 46. AESI 1

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypersensitivity/IRR
- **protocol text:** adverse events of special interest (AESIs) (hypersensitivity/infusion-related reactions...
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Hypersensitivity/IRR
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 47. AESI 2

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Gastrointestinal perforations and fistulae
- **protocol text:** gastrointestinal perforations and fistulae
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Gastrointestinal perforations and fistulae
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 48. AESI 3

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Wound healing complications
- **protocol text:** wound healing complications
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Wound healing complications
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 49. AESI 4

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypertension
- **protocol text:** hypertension
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Hypertension
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 50. AESI 5

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: posterior reversible encephalopathy syndrome (PRES)
- **protocol text:** posterior reversible encephalopathy syndrome (PRES)
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** posterior reversible encephalopathy syndrome (PRES)
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 51. AESI 6

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Proteinuria
- **protocol text:** proteinuria
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Proteinuria
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 52. AESI 7

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: arterial thromboembolism (ATE)
- **protocol text:** arterial thromboembolism (ATE)
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** arterial thromboembolism (ATE)
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 53. AESI 8

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: venous thromboembolism (VTE)
- **protocol text:** venous thromboembolism (VTE)
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** venous thromboembolism (VTE)
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 54. AESI 9

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hemorrhages
- **protocol text:** hemorrhages
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Hemorrhages
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 55. AESI 10

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: congestive heart failure (CHF)
- **protocol text:** congestive heart failure (CHF)
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** congestive heart failure (CHF)
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 56. AESI 11

- **evaluation type:** exact_match
- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Ovarian failure/fertility.
- **protocol text:** ovarian failure/fertility
- **protocol consulted:** yes
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Ovarian failure/fertility
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** List of AESIs missing.

#### 57. Immunogenicity Assays

- **evaluation type:** semantic
- **original SAP text:** Immunogenicity assessment consists of both anti-drug antibody (ADA) and neutralizing antibody (NAb) assays.
- **generated SAP text:** Immunogenicity, as assessed by the incidence of antidrug antibody and neutralized antidrug antibody.
- **protocol text:** Immunogenicity, as assessed by the incidence of antidrug antibody and neutralized antidrug antibody.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 58. ADA Transformation

- **evaluation type:** exact_match
- **original SAP text:** The ADA value tagged assay will be transformed using a log transformation. Transformed ADA value can be obtained using [log3(X/42)] + 1 transformation.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** The ADA value tagged assay will be transformed using a log transformation. Transformed ADA value can be obtained using [log3(X/42)] + 1 transformation.
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Transformation formula missing.

#### 59. NAb Transformation

- **evaluation type:** exact_match
- **original SAP text:** Transformed NAb value can be obtained using [log2(X/5)] + 1 transformation.
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Transformed NAb value can be obtained using [log2(X/5)] + 1 transformation.
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Transformation formula missing.

#### 60. QoL Instruments

- **evaluation type:** exact_match
- **original SAP text:** QoL will be assessed... using EORTC QLQ. The QLQ core 30 (QLQ-C30) and QLQ lung cancer-specific module (QLQ-LC13) will be used.
- **generated SAP text:** QLQ-C30 and QLQ-LC13, using EORTC QLQ
- **protocol text:** Quality of Life will be assessed using the validated European Organization for Research and Treatment of Cancer Quality of Life Questionnaire (EORTC QLQ). The QLQ core 30 (QLQ-C30) and QLQ lung cancer-specific module (QLQ-LC13) will be used.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 61. QoL Raw Score Formula

- **evaluation type:** exact_match
- **original SAP text:** For all scales, the Raw Score (RS), is the mean of the component items: RS = (I1 + I2 + … + In)/n
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** For all scales, the Raw Score (RS), is the mean of the component items: RS = (I1 + I2 + … + In)/n
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Formula missing.

#### 62. QoL Functional Score Formula

- **evaluation type:** exact_match
- **original SAP text:** Then for Functional scales: Score = {1 - (RS-1)/range} × 100
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** Then for Functional scales: Score = {1 - (RS-1)/range} × 100
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Formula missing.

#### 63. QoL Symptom Score Formula

- **evaluation type:** exact_match
- **original SAP text:** And for Symptom scales/items and Global health status/QoL: Score = {(RS-1)/range} × 100
- **protocol consulted:** no
- **matches original SAP:** no
- **detail level:** less_detailed
- **omitted content:** And for Symptom scales/items and Global health status/QoL: Score = {(RS-1)/range} × 100
- **omission impact:** low
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Formula missing.

---

### Issues Found (1 items)

#### 1. TEAE Definition

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** A Treatment-Emergent Adverse Event (TEAE) is defined as any event not present before exposure to study drug or any event already present that worsen in either severity or frequency after exposure to study drug.
- **generated SAP text:** A treatment-emergent abnormality is defined as a post-baseline value that represents a worsening from baseline (either an increase in CTCAE grade or a shift from Normal/Low to High, or Normal/High to Low).
- **protocol text:** A treatment-emergent AE is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **why they conflict:** Generated SAP defines TEAE only in the context of laboratory abnormalities, missing the broader clinical definition provided in the Original SAP and Protocol.
- **description:** The definition of TEAE in the Generated SAP is restricted to laboratory abnormalities, whereas the Original SAP and Protocol provide a general definition applicable to all adverse events.
- **reasoning:** 1) Original SAP defines TEAE broadly for all events. 2) Generated SAP defines 'treatment-emergent abnormality' specifically for labs in Section 7.1.3.5 but lacks a general TEAE definition in the safety section. 3) This restricts the scope of TEAEs in the Generated SAP compared to the Original. 4) Both cannot be true as the Generated SAP implies a narrower definition.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (26 items)

#### 1. Days to Months Conversion

- **original SAP text:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific conversion factor for days to months is missing.
- **reasoning:** Not in protocol, but standard SAP detail.

#### 2. Response Duration Formula

- **original SAP text:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific formula for response duration is missing.
- **reasoning:** Not in protocol, but standard SAP detail.

#### 3. TTP Censoring (No tumor assessment)

- **original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Censoring rule for patients with no tumor assessment is missing for TTP.
- **reasoning:** Required by protocol.

#### 4. TTP Formula

- **original SAP text:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific formula for TTP is missing.
- **reasoning:** Not in protocol, but standard SAP detail.

#### 5. PFS Censoring (No tumor assessment)

- **original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Censoring rule for patients with no tumor assessment is missing for PFS.
- **reasoning:** Required by protocol.

#### 6. PFS Formula

- **original SAP text:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific formula for PFS is missing.
- **reasoning:** Not in protocol, but standard SAP detail.

#### 7. OS Censoring

- **original SAP text:** Censoring will be defined as following: Non-death - Last known alive date
- **protocol text:** for patients whose status is unknown, data will be censored at the time when the patient is last known to be alive.
- **in protocol:** yes
- **classification:** missing_required
- **description:** Censoring rule for OS is missing.
- **reasoning:** Required by protocol.

#### 8. OS Formula

- **original SAP text:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific formula for OS is missing.
- **reasoning:** Not in protocol, but standard SAP detail.

#### 9. PK Exclusion i

- **original SAP text:** The samples in following cases are excluded from calculation of Ctrough; i) Post-dose concentration in the Induction Study Period
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific PK exclusion criteria missing.
- **reasoning:** Not in protocol.

#### 10. PK Exclusion ii

- **original SAP text:** The samples in following cases are excluded from calculation of Ctrough; ii) interval between the last dose date and sampling date at EOT < 18 days
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific PK exclusion criteria missing.
- **reasoning:** Not in protocol.

#### 11. AESI 1

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypersensitivity/IRR
- **protocol text:** hypersensitivity/infusion-related reactions
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 12. AESI 2

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Gastrointestinal perforations and fistulae
- **protocol text:** gastrointestinal perforations and fistulae
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 13. AESI 3

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Wound healing complications
- **protocol text:** wound healing complications
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 14. AESI 4

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypertension
- **protocol text:** hypertension
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 15. AESI 5

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: posterior reversible encephalopathy syndrome (PRES)
- **protocol text:** posterior reversible encephalopathy syndrome (PRES)
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 16. AESI 6

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Proteinuria
- **protocol text:** proteinuria
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 17. AESI 7

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: arterial thromboembolism (ATE)
- **protocol text:** arterial thromboembolism (ATE)
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 18. AESI 8

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: venous thromboembolism (VTE)
- **protocol text:** venous thromboembolism (VTE)
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 19. AESI 9

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hemorrhages
- **protocol text:** hemorrhages
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 20. AESI 10

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: congestive heart failure (CHF)
- **protocol text:** congestive heart failure (CHF)
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 21. AESI 11

- **original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Ovarian failure/fertility.
- **protocol text:** ovarian failure/fertility
- **in protocol:** yes
- **classification:** missing_required
- **description:** Specific AESI missing from list.
- **reasoning:** Required by protocol.

#### 22. ADA Transformation

- **original SAP text:** The ADA value tagged assay will be transformed using a log transformation. Transformed ADA value can be obtained using [log3(X/42)] + 1 transformation.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific transformation formula missing.
- **reasoning:** Not in protocol.

#### 23. NAb Transformation

- **original SAP text:** Transformed NAb value can be obtained using [log2(X/5)] + 1 transformation.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific transformation formula missing.
- **reasoning:** Not in protocol.

#### 24. QoL Raw Score Formula

- **original SAP text:** For all scales, the Raw Score (RS), is the mean of the component items: RS = (I1 + I2 + … + In)/n
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific scoring formula missing.
- **reasoning:** Not in protocol.

#### 25. QoL Functional Score Formula

- **original SAP text:** Then for Functional scales: Score = {1 - (RS-1)/range} × 100
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific scoring formula missing.
- **reasoning:** Not in protocol.

#### 26. QoL Symptom Score Formula

- **original SAP text:** And for Symptom scales/items and Global health status/QoL: Score = {(RS-1)/range} × 100
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific scoring formula missing.
- **reasoning:** Not in protocol.

---

### Reasoning

The Generated SAP correctly identifies the primary and secondary objectives and endpoints. However, it lacks significant detail regarding specific calculations and definitions found in the Original SAP. Specifically, it misses the formulas for time-to-event calculations (days to months conversion), specific censoring rules for TTP and PFS (censoring at randomization for no assessment), and OS censoring rules. It also omits the list of Adverse Events of Special Interest (AESIs), which are explicitly listed in the Protocol and Original SAP. Furthermore, specific formulas for QoL scoring and immunogenicity data transformation are missing. While some of these are acceptable omissions if not in the protocol, the missing AESI list and censoring rules are critical omissions as they are protocol-required or standard analysis definitions.

---

### Summary

The Generated SAP provides a high-level overview of objectives and endpoints but lacks the necessary technical detail and specific definitions present in the Original SAP. Critical omissions include the list of Adverse Events of Special Interest and specific censoring rules for time-to-event analyses, which are required by the protocol.