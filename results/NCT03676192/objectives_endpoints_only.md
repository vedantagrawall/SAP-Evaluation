## Objectives Endpoints Only Evaluation

**Section:** objectives_endpoints
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **Sections read:** 2.1, 2.2, 8, 8.1, 8.2.1, 8.2.2, 8.2.2.1, 8.2.2.2, 8.2.2.3, 8.2.2.4, 9.2, 10.1, 10.1.5, 10.9, 11
- **Elements per section:** 2.1: 1, 2.2: 4, 8: 3, 8.1: 2, 8.2.1: 1, 8.2.2: 3, 8.2.2.1: 7, 8.2.2.2: 8, 8.2.2.3: 8, 8.2.2.4: 4, 9.2: 3, 10.1: 1, 10.1.5: 11, 10.9: 3, 11: 4
- **Elements extracted:** 63
- **Elements in evaluation table:** 63
- **Elements in missing from generated SAP:** 28
- **Counts match:** True

---

### Evaluation Table (63 items)

#### 1. Primary Objective

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The primary objective of the study is: To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) during the Induction Study Period
- **Generated SAP text:** To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) up to Cycle 6 during the Induction Study Period
- **Protocol text:** To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) up to Cycle 6 during the Induction Study Period
- **Reasoning:** Matches.

#### 2. Secondary Objective - Efficacy

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** To evaluate additional efficacy profiles including ORR during the Whole Study Period, response duration, time to progression (TTP), progression-free survival (PFS), and overall survival (OS)
- **Generated SAP text:** To evaluate additional efficacy profiles including ORR during the Whole Study Period, response duration, time to progression (TTP), progression-free survival (PFS), and overall survival (OS)
- **Protocol text:** To evaluate additional efficacy profiles including ORR during the Whole Study Period, response duration, time to progression (TTP), progression-free survival (PFS), and overall survival (OS)
- **Reasoning:** Matches.

#### 3. Secondary Objective - PK

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** To evaluate the Pharmacokinetic (PK) parameter of trough serum concentration (Ctrough)
- **Generated SAP text:** To evaluate the pharmacokinetics (PK) of trough serum concentration (Ctrough)
- **Protocol text:** To evaluate the pharmacokinetics (PK) of trough serum concentration (Ctrough)
- **Reasoning:** Matches.

#### 4. Secondary Objective - Safety

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** To evaluate safety profile including immunogenicity
- **Generated SAP text:** To evaluate safety profile including immunogenicity
- **Protocol text:** To evaluate safety profile including immunogenicity
- **Reasoning:** Matches.

#### 5. Secondary Objective - QoL

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** To evaluate quality of life (QoL)
- **Generated SAP text:** To evaluate quality of life (QoL)
- **Protocol text:** To evaluate quality of life (QoL)
- **Reasoning:** Matches.

#### 6. Efficacy Endpoint Determination

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The primary endpoint, ORR during the Induction Study Period, and the secondary endpoint, ORR during the Whole Study Period, will be determined by the BOR.
- **Generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR)
- **Protocol text:** The primary endpoint, ORR during the Induction Study Period, and the secondary endpoint, ORR during the Whole Study Period, will be determined by the best overall response (BOR).
- **Reasoning:** Matches concept.

#### 7. Confirmation of Response

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** For CR or PR, BOR must be confirmed by the subsequent assessment.
- **Generated SAP text:** While the primary endpoint requires confirmation (as per RECIST 1.1)
- **Protocol text:** For CR or PR, BOR must be confirmed by the subsequent assessment based on the RECIST v.1.1
- **Reasoning:** Matches concept.

#### 8. BOR Categories

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Categorization of BOR will use the following response categories: CR, PR, SD, PD and NE.
- **Generated SAP text:** Descriptive statistics for the primary endpoint will include the number and percentage of responders (CR + PR) and non-responders (SD, PD, NE) per treatment group.
- **Protocol text:** Categorization of overall response at each visit will be based on RECIST v.1.1 using the following response categories: CR, PR, SD, PD, and inevaluable (NE)
- **Reasoning:** Matches categories.

#### 9. Primary Endpoint Definition

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The primary efficacy endpoint is ORR based on BOR during the Induction Study Period by RECIST version 1.1
- **Generated SAP text:** The primary efficacy endpoint is the Objective Response Rate (ORR), defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR) during the Induction Study Period (up to Cycle 6) as determined by an Independent Tumor Review Committee (central review) using RECIST v.1.1.
- **Protocol text:** The primary efficacy endpoint will be the ORR based on BOR during the Induction Study Period by RECIST v.1.1
- **Reasoning:** Matches.

#### 10. ORR Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** The ORR is defined as the proportion of patients with a confirmed BOR of CR or PR (the 'responder').
- **Generated SAP text:** defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR)
- **Protocol text:** Objective response rate will be calculated as the number of patients with a response of CR or PR divided by the number of patients in the corresponding population.
- **Reasoning:** Matches.

#### 11. Secondary Endpoint - ORR Whole Study

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** For the secondary efficacy endpoint, ORR based on BOR during the Whole Study Period by RECIST version 1.1 will be analyzed.
- **Generated SAP text:** ORR based on BOR during the Whole Study Period by RECIST v.1.1
- **Protocol text:** ORR based on BOR during the Whole Study Period by RECIST v.1.1
- **Reasoning:** Matches.

#### 12. Time-to-Event Analysis List

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population.
- **Generated SAP text:** Time-to-event (TTE) endpoints will be analyzed using the ITT and PP populations. Progression-Free Survival (PFS)... Time to Progression (TTP)... Overall Survival (OS)... Response Duration...
- **Protocol text:** A time-to-event analysis will be undertaken for each of the response duration, TTP, PFS, and OS in the ITT and PP population
- **Reasoning:** Matches.

#### 13. TTE Reporting Units

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** All time-to-event data will be reported in months with reasons for an event/censoring and summarized by treatment group.
- **Generated SAP text:** Median TTE and survival rates at specific landmarks (e.g., 6 months, 12 months) will be calculated
- **Protocol text:** null
- **Reasoning:** Implies months.

#### 14. Days to Months Conversion

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **Protocol text:** null
- **Omitted content:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **Omission impact:** low
- **Reasoning:** Conversion factor missing.

#### 15. Response Duration Definition

- **Evaluation type:** semantic
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

#### 16. Response Duration Event

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** PD/recurrence or death that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored
- **Protocol text:** null
- **Reasoning:** Implied by censoring rule.

#### 17. Response Duration Censoring (No event)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: No event and no anticancer therapy - Last tumor assessment date
- **Generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **Protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **Reasoning:** Matches.

#### 18. Response Duration Censoring (New therapy)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy - Last tumor assessment date before anticancer therapy
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **Protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment, without disease progression/or recurrence, before starting another anticancer therapy.
- **Reasoning:** Matches.

#### 19. Response Duration Censoring (Missing assessments)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* - Last tumor assessment date before event
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **Protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment
- **Reasoning:** Matches.

#### 20. Response Duration Missing Exception

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored
- **Protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **Reasoning:** Implied.

#### 21. Response Duration Formula

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **Protocol text:** null
- **Omitted content:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **Omission impact:** low
- **Reasoning:** Formula missing.

#### 22. TTP Definition

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

#### 23. TTP Event

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** PD/recurrence that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored
- **Protocol text:** null
- **Reasoning:** Implied.

#### 24. TTP Censoring (No assessment)

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **Protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **Omitted content:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **Omission impact:** low
- **Reasoning:** Specific censoring rule missing.

#### 25. TTP Censoring (No event)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: No event and no anticancer therapy - Last tumor assessment date
- **Generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **Protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **Reasoning:** Matches.

#### 26. TTP Censoring (New therapy)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy - Last tumor assessment date before anticancer therapy
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **Protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment, without disease progression/or recurrence, before starting another anticancer therapy.
- **Reasoning:** Matches.

#### 27. TTP Censoring (Missing assessments)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* - Last tumor assessment date before event
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **Protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment
- **Reasoning:** Matches.

#### 28. TTP Missing Exception

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored
- **Protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **Reasoning:** Implied.

#### 29. TTP Formula

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Protocol text:** null
- **Omitted content:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Omission impact:** low
- **Reasoning:** Formula missing.

#### 30. PFS Definition

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

#### 31. PFS Event

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** PD/recurrence or death that occurred on or before beginning another new anticancer therapy will be regarded as an event.
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored
- **Protocol text:** null
- **Reasoning:** Implied.

#### 32. PFS Censoring (No assessment)

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **Protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **Omitted content:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **Omission impact:** low
- **Reasoning:** Specific censoring rule missing.

#### 33. PFS Censoring (No event)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: No event and no anticancer therapy - Last tumor assessment date
- **Generated SAP text:** Patients alive and without PD at the time of data cutoff/study completion will be censored at the date of the last adequate tumor assessment.
- **Protocol text:** if a patient has no event, it will be calculated censoring at the date of last adequate radiological assessment
- **Reasoning:** Matches.

#### 34. PFS Censoring (New therapy)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: Initiation of New anticancer therapy - Last tumor assessment date before anticancer therapy
- **Generated SAP text:** Patients starting a new anti-cancer therapy prior to PD will be censored at the date of the last adequate tumor assessment prior to the start of the new therapy.
- **Protocol text:** If a patient receives another new anticancer therapy, it will be censored at the date of adequate radiological assessment, without disease progression/or recurrence, before starting another anticancer therapy.
- **Reasoning:** Matches.

#### 35. PFS Censoring (Missing assessments)

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Censoring will be defined as following: Event after missing two or more tumor assessment* - Last tumor assessment date before event
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored at the date of the last adequate tumor assessment prior to the missing visits.
- **Protocol text:** If disease progression or death is documented after missing two or more tumor assessments, the patient will be censored for PFS at the date of their last adequate tumor assessment
- **Reasoning:** Matches.

#### 36. PFS Missing Exception

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** * If there is only one missing tumor assessment before an event, then it will be considered as an event case. Otherwise, it will be considered as a censoring case.
- **Generated SAP text:** If PD or death occurs after missing two or more consecutive scheduled tumor assessments, the patient will be censored
- **Protocol text:** If disease progression or death is documented after missing one tumor assessment, the PFS time of these patients will be calculated assuming the event occurred on the date of progression (or death).
- **Reasoning:** Implied.

#### 37. PFS Formula

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Protocol text:** null
- **Omitted content:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Omission impact:** low
- **Reasoning:** Formula missing.

#### 38. OS Definition

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

#### 39. OS Event

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Death will be regarded as an event.
- **Generated SAP text:** Time from randomization until death due to any cause.
- **Protocol text:** null
- **Reasoning:** Implied.

#### 40. OS Censoring

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** Censoring will be defined as following: Non-death - Last known alive date
- **Protocol text:** for patients whose status is unknown, data will be censored at the time when the patient is last known to be alive.
- **Omitted content:** Censoring will be defined as following: Non-death - Last known alive date
- **Omission impact:** low
- **Reasoning:** Specific censoring rule missing.

#### 41. OS Formula

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Protocol text:** null
- **Omitted content:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Omission impact:** low
- **Reasoning:** Formula missing.

#### 42. PK Parameter Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Detail level:** less_detailed
- **Original SAP text:** PK parameter is the observed Ctrough following drug administration; calculated from the pre-dose concentration of the next dose.
- **Generated SAP text:** Ctrough: Trough serum concentration
- **Protocol text:** The Ctrough (prior to next dose) at each cycle during the Induction Study Period, and Ctrough during the Maintenance Study Period will be analyzed.
- **Omitted content:** calculated from the pre-dose concentration of the next dose
- **Omission impact:** low
- **Reasoning:** Definition is less detailed but consistent.

#### 43. PK Exclusion i

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The samples in following cases are excluded from calculation of Ctrough; i) Post-dose concentration in the Induction Study Period
- **Protocol text:** null
- **Omitted content:** The samples in following cases are excluded from calculation of Ctrough; i) Post-dose concentration in the Induction Study Period
- **Omission impact:** low
- **Reasoning:** Exclusion criteria missing.

#### 44. PK Exclusion ii

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The samples in following cases are excluded from calculation of Ctrough; ii) interval between the last dose date and sampling date at EOT < 18 days
- **Protocol text:** null
- **Omitted content:** The samples in following cases are excluded from calculation of Ctrough; ii) interval between the last dose date and sampling date at EOT < 18 days
- **Omission impact:** low
- **Reasoning:** Exclusion criteria missing.

#### 45. TEAE Definition

- **Evaluation type:** semantic
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** contradiction_original
- **Severity:** minor
- **Detail level:** contradiction
- **Original SAP text:** A Treatment-Emergent Adverse Event (TEAE) is defined as any event not present before exposure to study drug or any event already present that worsen in either severity or frequency after exposure to study drug.
- **Generated SAP text:** A treatment-emergent abnormality is defined as a post-baseline value that represents a worsening from baseline (either an increase in CTCAE grade or a shift from Normal/Low to High, or Normal/High to Low).
- **Protocol text:** A treatment-emergent AE is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **Omission impact:** potential
- **Reasoning:** Generated SAP defines TEAE only in context of labs, missing the general clinical definition.

#### 46. AESI 1

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypersensitivity/IRR
- **Protocol text:** adverse events of special interest (AESIs) (hypersensitivity/infusion-related reactions...
- **Omitted content:** Hypersensitivity/IRR
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 47. AESI 2

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Gastrointestinal perforations and fistulae
- **Protocol text:** gastrointestinal perforations and fistulae
- **Omitted content:** Gastrointestinal perforations and fistulae
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 48. AESI 3

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Wound healing complications
- **Protocol text:** wound healing complications
- **Omitted content:** Wound healing complications
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 49. AESI 4

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypertension
- **Protocol text:** hypertension
- **Omitted content:** Hypertension
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 50. AESI 5

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: posterior reversible encephalopathy syndrome (PRES)
- **Protocol text:** posterior reversible encephalopathy syndrome (PRES)
- **Omitted content:** posterior reversible encephalopathy syndrome (PRES)
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 51. AESI 6

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Proteinuria
- **Protocol text:** proteinuria
- **Omitted content:** Proteinuria
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 52. AESI 7

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: arterial thromboembolism (ATE)
- **Protocol text:** arterial thromboembolism (ATE)
- **Omitted content:** arterial thromboembolism (ATE)
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 53. AESI 8

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: venous thromboembolism (VTE)
- **Protocol text:** venous thromboembolism (VTE)
- **Omitted content:** venous thromboembolism (VTE)
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 54. AESI 9

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hemorrhages
- **Protocol text:** hemorrhages
- **Omitted content:** Hemorrhages
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 55. AESI 10

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: congestive heart failure (CHF)
- **Protocol text:** congestive heart failure (CHF)
- **Omitted content:** congestive heart failure (CHF)
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 56. AESI 11

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Ovarian failure/fertility.
- **Protocol text:** ovarian failure/fertility
- **Omitted content:** Ovarian failure/fertility
- **Omission impact:** low
- **Reasoning:** List of AESIs missing.

#### 57. Immunogenicity Assays

- **Evaluation type:** semantic
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** Immunogenicity assessment consists of both anti-drug antibody (ADA) and neutralizing antibody (NAb) assays.
- **Generated SAP text:** Immunogenicity, as assessed by the incidence of antidrug antibody and neutralized antidrug antibody.
- **Protocol text:** Immunogenicity, as assessed by the incidence of antidrug antibody and neutralized antidrug antibody.
- **Reasoning:** Matches.

#### 58. ADA Transformation

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** The ADA value tagged assay will be transformed using a log transformation. Transformed ADA value can be obtained using [log3(X/42)] + 1 transformation.
- **Protocol text:** null
- **Omitted content:** The ADA value tagged assay will be transformed using a log transformation. Transformed ADA value can be obtained using [log3(X/42)] + 1 transformation.
- **Omission impact:** low
- **Reasoning:** Transformation formula missing.

#### 59. NAb Transformation

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** Transformed NAb value can be obtained using [log2(X/5)] + 1 transformation.
- **Protocol text:** null
- **Omitted content:** Transformed NAb value can be obtained using [log2(X/5)] + 1 transformation.
- **Omission impact:** low
- **Reasoning:** Transformation formula missing.

#### 60. QoL Instruments

- **Evaluation type:** exact_match
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Detail level:** match
- **Original SAP text:** QoL will be assessed... using EORTC QLQ. The QLQ core 30 (QLQ-C30) and QLQ lung cancer-specific module (QLQ-LC13) will be used.
- **Generated SAP text:** QLQ-C30 and QLQ-LC13, using EORTC QLQ
- **Protocol text:** Quality of Life will be assessed using the validated European Organization for Research and Treatment of Cancer Quality of Life Questionnaire (EORTC QLQ). The QLQ core 30 (QLQ-C30) and QLQ lung cancer-specific module (QLQ-LC13) will be used.
- **Reasoning:** Matches.

#### 61. QoL Raw Score Formula

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** For all scales, the Raw Score (RS), is the mean of the component items: RS = (I1 + I2 + … + In)/n
- **Protocol text:** null
- **Omitted content:** For all scales, the Raw Score (RS), is the mean of the component items: RS = (I1 + I2 + … + In)/n
- **Omission impact:** low
- **Reasoning:** Formula missing.

#### 62. QoL Functional Score Formula

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** Then for Functional scales: Score = {1 - (RS-1)/range} × 100
- **Protocol text:** null
- **Omitted content:** Then for Functional scales: Score = {1 - (RS-1)/range} × 100
- **Omission impact:** low
- **Reasoning:** Formula missing.

#### 63. QoL Symptom Score Formula

- **Evaluation type:** exact_match
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** none
- **Severity:** minor
- **Detail level:** less_detailed
- **Original SAP text:** And for Symptom scales/items and Global health status/QoL: Score = {(RS-1)/range} × 100
- **Protocol text:** null
- **Omitted content:** And for Symptom scales/items and Global health status/QoL: Score = {(RS-1)/range} × 100
- **Omission impact:** low
- **Reasoning:** Formula missing.

---

### Issues Found (1 items)

#### Issue 1: TEAE Definition

- **Issue type:** contradiction_original
- **Severity:** minor
- **Original SAP text:** A Treatment-Emergent Adverse Event (TEAE) is defined as any event not present before exposure to study drug or any event already present that worsen in either severity or frequency after exposure to study drug.
- **Generated SAP text:** A treatment-emergent abnormality is defined as a post-baseline value that represents a worsening from baseline (either an increase in CTCAE grade or a shift from Normal/Low to High, or Normal/High to Low).
- **Protocol text:** A treatment-emergent AE is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **Why they conflict:** Generated SAP defines TEAE only in the context of laboratory abnormalities, missing the broader clinical definition provided in the Original SAP and Protocol.
- **Description:** The definition of TEAE in the Generated SAP is restricted to laboratory abnormalities, whereas the Original SAP and Protocol provide a general definition applicable to all adverse events.
- **Reasoning:** 1) Original SAP defines TEAE broadly for all events. 2) Generated SAP defines 'treatment-emergent abnormality' specifically for labs in Section 7.1.3.5 but lacks a general TEAE definition in the safety section. 3) This restricts the scope of TEAEs in the Generated SAP compared to the Original. 4) Both cannot be true as the Generated SAP implies a narrower definition.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (26 items)

#### Missing 1: Days to Months Conversion

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Time-to-event in days will be converted to months by dividing the number of days by 30.4 (365.25 days/12 months).
- **Description:** Specific conversion factor for days to months is missing.
- **Reasoning:** Not in protocol, but standard SAP detail.

#### Missing 2: Response Duration Formula

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Response duration (months) = ([Date of Event/Censoring – Date of First known CR/PR that is confirmed by the subsequent assessment] +1)/30.4
- **Description:** Specific formula for response duration is missing.
- **Reasoning:** Not in protocol, but standard SAP detail.

#### Missing 3: TTP Censoring (No tumor assessment)

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **Protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **Description:** Censoring rule for patients with no tumor assessment is missing for TTP.
- **Reasoning:** Required by protocol.

#### Missing 4: TTP Formula

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** TTP (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Description:** Specific formula for TTP is missing.
- **Reasoning:** Not in protocol, but standard SAP detail.

#### Missing 5: PFS Censoring (No tumor assessment)

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** Censoring will be defined as following: No tumor assessment - The date of randomization
- **Protocol text:** Any patient without any tumor assessment during the study will be censored at the date of randomization.
- **Description:** Censoring rule for patients with no tumor assessment is missing for PFS.
- **Reasoning:** Required by protocol.

#### Missing 6: PFS Formula

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** PFS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Description:** Specific formula for PFS is missing.
- **Reasoning:** Not in protocol, but standard SAP detail.

#### Missing 7: OS Censoring

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** Censoring will be defined as following: Non-death - Last known alive date
- **Protocol text:** for patients whose status is unknown, data will be censored at the time when the patient is last known to be alive.
- **Description:** Censoring rule for OS is missing.
- **Reasoning:** Required by protocol.

#### Missing 8: OS Formula

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** OS (months) = ([Date of Event/Censoring – Date of Randomization] +1)/30.4
- **Description:** Specific formula for OS is missing.
- **Reasoning:** Not in protocol, but standard SAP detail.

#### Missing 9: PK Exclusion i

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** The samples in following cases are excluded from calculation of Ctrough; i) Post-dose concentration in the Induction Study Period
- **Description:** Specific PK exclusion criteria missing.
- **Reasoning:** Not in protocol.

#### Missing 10: PK Exclusion ii

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** The samples in following cases are excluded from calculation of Ctrough; ii) interval between the last dose date and sampling date at EOT < 18 days
- **Description:** Specific PK exclusion criteria missing.
- **Reasoning:** Not in protocol.

#### Missing 11: AESI 1

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypersensitivity/IRR
- **Protocol text:** hypersensitivity/infusion-related reactions
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 12: AESI 2

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Gastrointestinal perforations and fistulae
- **Protocol text:** gastrointestinal perforations and fistulae
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 13: AESI 3

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Wound healing complications
- **Protocol text:** wound healing complications
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 14: AESI 4

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hypertension
- **Protocol text:** hypertension
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 15: AESI 5

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: posterior reversible encephalopathy syndrome (PRES)
- **Protocol text:** posterior reversible encephalopathy syndrome (PRES)
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 16: AESI 6

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Proteinuria
- **Protocol text:** proteinuria
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 17: AESI 7

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: arterial thromboembolism (ATE)
- **Protocol text:** arterial thromboembolism (ATE)
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 18: AESI 8

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: venous thromboembolism (VTE)
- **Protocol text:** venous thromboembolism (VTE)
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 19: AESI 9

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Hemorrhages
- **Protocol text:** hemorrhages
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 20: AESI 10

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: congestive heart failure (CHF)
- **Protocol text:** congestive heart failure (CHF)
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 21: AESI 11

- **Classification:** missing_required
- **In protocol:** yes
- **Original SAP text:** The following TEAEs will be considered as TEAEs of special interest: Ovarian failure/fertility.
- **Protocol text:** ovarian failure/fertility
- **Description:** Specific AESI missing from list.
- **Reasoning:** Required by protocol.

#### Missing 22: ADA Transformation

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** The ADA value tagged assay will be transformed using a log transformation. Transformed ADA value can be obtained using [log3(X/42)] + 1 transformation.
- **Description:** Specific transformation formula missing.
- **Reasoning:** Not in protocol.

#### Missing 23: NAb Transformation

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Transformed NAb value can be obtained using [log2(X/5)] + 1 transformation.
- **Description:** Specific transformation formula missing.
- **Reasoning:** Not in protocol.

#### Missing 24: QoL Raw Score Formula

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** For all scales, the Raw Score (RS), is the mean of the component items: RS = (I1 + I2 + … + In)/n
- **Description:** Specific scoring formula missing.
- **Reasoning:** Not in protocol.

#### Missing 25: QoL Functional Score Formula

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** Then for Functional scales: Score = {1 - (RS-1)/range} × 100
- **Description:** Specific scoring formula missing.
- **Reasoning:** Not in protocol.

#### Missing 26: QoL Symptom Score Formula

- **Classification:** acceptable_difference
- **In protocol:** no
- **Original SAP text:** And for Symptom scales/items and Global health status/QoL: Score = {(RS-1)/range} × 100
- **Description:** Specific scoring formula missing.
- **Reasoning:** Not in protocol.

---

### Reasoning

The Generated SAP correctly identifies the primary and secondary objectives and endpoints. However, it lacks significant detail regarding specific calculations and definitions found in the Original SAP. Specifically, it misses the formulas for time-to-event calculations (days to months conversion), specific censoring rules for TTP and PFS (censoring at randomization for no assessment), and OS censoring rules. It also omits the list of Adverse Events of Special Interest (AESIs), which are explicitly listed in the Protocol and Original SAP. Furthermore, specific formulas for QoL scoring and immunogenicity data transformation are missing. While some of these are acceptable omissions if not in the protocol, the missing AESI list and censoring rules are critical omissions as they are protocol-required or standard analysis definitions.

---

### Summary

The Generated SAP provides a high-level overview of objectives and endpoints but lacks the necessary technical detail and specific definitions present in the Original SAP. Critical omissions include the list of Adverse Events of Special Interest and specific censoring rules for time-to-event analyses, which are required by the protocol.