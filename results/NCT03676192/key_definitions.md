## Key Definitions Evaluation

**Section:** key_definitions
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **Sections read:** 
- **Elements extracted:** N/A
- **Elements in evaluation table:** N/A
- **Elements in missing from generated SAP:** N/A
- **Counts match:** N/A

---

### Evaluation Table (21 items)

#### 1. Intent-to-Treat (ITT) Population

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** no
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The ITT population will consist of all randomized patients who are randomly assigned to study drug regardless of whether or not any study treatment dosing is completed and successfully screened based on the ‘Screening Pass/Fail’ eCRF page.
- **Generated SAP text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **Protocol text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **Reasoning:** Generated SAP matches Protocol text exactly. Original SAP added a specific clause about 'successfully screened', but Generated SAP is consistent with the Protocol source of truth.

#### 2. Per-Protocol (PP) Population

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The PP population will consist of all randomly assigned patients who have at least one response evaluation after receiving at least one full dose... and who do not have any major protocol deviations
- **Generated SAP text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose... and who do not have any major protocol deviation.
- **Protocol text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose... and who do not have any major protocol deviation.
- **Reasoning:** Definitions match across all documents.

#### 3. PK Population

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The PK population will consist of all randomly assigned patients who receive at least one full dose... and who have at least one post treatment PK result.
- **Generated SAP text:** The PK population is defined as all patients who receive at least one full dose of study drug... and who have at least one post treatment PK result.
- **Protocol text:** The PK population is defined as all patients who receive at least one full dose... and who have at least one post treatment PK result.
- **Reasoning:** Definitions match.

#### 4. Safety Population

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The safety population will consist of all randomly assigned patients who receive at least one dose (partial or full) of study drug
- **Generated SAP text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **Protocol text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **Reasoning:** Definitions match.

#### 5. Baseline Value

- **Evaluation type:** sap-originated
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **Generated SAP text:** Defined as the last non-missing observation... recorded prior to the First Dose Date.
- **Reasoning:** Matches intent of Original SAP.

#### 6. Duration of Treatment

- **Evaluation type:** sap-originated
- **Matches Original SAP:** no
- **Protocol consulted:** no
- **Result:** problem
- **Issue type:** contradiction_original
- **Severity:** minor
- **Original SAP text:** Actual duration of dose (weeks) = (Start Date of Last Cycle + 21 – Start Date of First Cycle) / 7
- **Generated SAP text:** Calculated as (Last Dose Date – First Dose Date) + 1.
- **Reasoning:** Original SAP explicitly defines duration of dose to include the full cycle length of the last dose (+21 days). Generated SAP defines it as the simple difference between administration dates (+1 day). This underestimates exposure duration by approximately 3 weeks compared to the Original SAP method.

#### 7. Response Duration

- **Evaluation type:** sap-originated
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Response duration... defined as the time between the initial response (CR or PR) that is confirmed... and PD/recurrence or death from any cause
- **Generated SAP text:** Time from the first documented response (CR or PR) until the first documentation of PD or death (among responders only).
- **Protocol text:** Response duration: the time between initial response (CR or PR) and PD/recurrence
- **Reasoning:** Generated SAP correctly identifies that the definition was updated in the Original SAP (Section 12) to include 'death', differing from the Protocol.

#### 8. Progression-Free Survival (PFS)

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** PFS is defined as time from randomization to determined PD/recurrence or death from any cause (whichever occurs first).
- **Generated SAP text:** Time from randomization until the first documentation of PD (per RECIST v.1.1) or death due to any cause.
- **Protocol text:** PFS: the time from randomization until PD/recurrence or death due to any cause, whichever occurs first
- **Reasoning:** Definitions match.

#### 9. Time to Progression (TTP)

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** TTP is defined as time from randomization to determined PD/recurrence.
- **Generated SAP text:** Time from randomization until the first documentation of PD.
- **Protocol text:** TTP: the time from randomization until PD/recurrence
- **Reasoning:** Definitions match.

#### 10. Overall Survival (OS)

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** OS is defined as time from randomization to death from any cause.
- **Generated SAP text:** Time from randomization until death due to any cause.
- **Protocol text:** OS: the time from randomization until death due to any cause
- **Reasoning:** Definitions match.

#### 11. Age

- **Evaluation type:** sap-originated
- **Matches Original SAP:** yes
- **Protocol consulted:** no
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Age will be automatically calculated in the eCRF system based on the informed consent signed date, the year of birth and information on whether the date of birth has passed or not.
- **Generated SAP text:** Calculated as the integer part of (Date of Informed Consent – Date of Birth) / 365.25.
- **Reasoning:** Standard calculation method matches intent of Original SAP.

#### 12. Study Day

- **Evaluation type:** generated-addition
- **Matches Original SAP:** n/a
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Generated SAP text:** For assessments on or after Study Day 1: Study Day = (Date of Assessment – Study Day 1 Date) + 1... There is no Study Day 0.
- **Reasoning:** Standard CDISC/ADaM definition added for clarity.

#### 13. Treatment-Emergent Abnormality (Labs)

- **Evaluation type:** generated-addition
- **Matches Original SAP:** n/a
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** A shift table will be also produced... to detect changes from baseline.
- **Generated SAP text:** Defined as a post-baseline value that represents a worsening from baseline (either an increase in CTCAE grade or a shift from Normal/Low to High, or Normal/High to Low).
- **Reasoning:** Consistent with Original SAP's requirement for shift tables.

#### 14. First Dose Date

- **Evaluation type:** generated-addition
- **Matches Original SAP:** n/a
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Generated SAP text:** The date on which a patient receives the first administration of any component of the study treatment
- **Reasoning:** Standard variable definition.

#### 15. Last Dose Date

- **Evaluation type:** generated-addition
- **Matches Original SAP:** n/a
- **Protocol consulted:** no
- **Result:** acceptable
- **Issue type:** none
- **Severity:** none
- **Generated SAP text:** The date of the last administration of any component of the study treatment
- **Reasoning:** Standard variable definition.

#### 16. Controlled Disease

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** patients with controlled disease (complete response (CR), partial response (PR), or stable disease (SD), assessed at the end of Cycle 6)
- **Generated SAP text:** Defined as a patient achieving a Best Overall Response (BOR) of Complete Response (CR), Partial Response (PR), or Stable Disease (SD) as assessed at the end of Cycle 6
- **Protocol text:** patients with controlled disease (complete response [CR], partial response [PR], or stable disease [SD], assessed at the end of Cycle 6)
- **Reasoning:** Matches Protocol and Original SAP.

#### 17. Induction Study Period

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Induction Study Period: maximum 6 cycles
- **Generated SAP text:** Defined as the period from Study Day 1 through the day before the first dose of monotherapy in the Maintenance Study Period, or until the EOT visit
- **Protocol text:** Induction Study Period: maximum 6 cycles
- **Reasoning:** Generated SAP operationalizes the protocol definition into specific dates.

#### 18. Maintenance Study Period

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Maintenance Study Period: until disease progression, or intolerable toxicity
- **Generated SAP text:** Defined as the period from the First Dose Date for the Maintenance Study Period through the date of the EOT visit.
- **Protocol text:** Maintenance Study Period: until disease progression, or intolerable toxicity
- **Reasoning:** Generated SAP operationalizes the protocol definition into specific dates.

#### 19. Follow-Up Period

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Follow-Up Period: up to approximately 3 years from the last patient enrolled
- **Generated SAP text:** Defined as the period beginning the day after the EOT visit until the date of death, withdrawal of consent, or the end of the study
- **Protocol text:** Follow-Up Period: up to approximately 3 years from the last patient enrolled
- **Reasoning:** Generated SAP operationalizes the protocol definition into specific dates.

#### 20. Objective Response Rate (ORR)

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** The ORR is defined as the proportion of patients with a confirmed BOR of CR or PR
- **Generated SAP text:** defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR)
- **Protocol text:** Objective response rate (ORR, %) based on BOR during the Induction Study Period
- **Reasoning:** Matches.

#### 21. Screening Period

- **Evaluation type:** protocol-defined
- **Matches Original SAP:** yes
- **Protocol consulted:** yes
- **Result:** correct
- **Issue type:** none
- **Severity:** none
- **Original SAP text:** Screening evaluations will be completed within 28 days prior to randomization.
- **Generated SAP text:** Defined as the period from the First Visit Date (ICF signature) to the day before the First Dose Date.
- **Protocol text:** Screening evaluations will be completed within 28 days prior to randomization.
- **Reasoning:** Generated SAP operationalizes the protocol definition.

---

### Issues Found (1 items)

#### Issue 1: Duration of Treatment

- **Issue type:** contradiction_original
- **Severity:** minor
- **Why they conflict:** Original SAP includes the full duration of the last cycle (+21 days) in the calculation, whereas Generated SAP only calculates the time between the first and last administration dates. This results in a discrepancy of approximately 3 weeks in exposure duration.
- **Description:** Calculation method for treatment duration differs significantly from Original SAP.
- **Reasoning:** The Original SAP has a specific formula for 'Actual duration of dose' used for dose intensity that accounts for the therapeutic coverage of the last dose. The Generated SAP uses a generic duration formula that underestimates this coverage.

---

### Extra Information Flagged (0 items)

*No extra information flagged.*

---

### Missing from Generated SAP (0 items)

*No missing content.*

---

### Reasoning

The Generated SAP provides a solid set of definitions for populations, study periods, and efficacy endpoints, correctly incorporating the Protocol amendment regarding 'Response Duration' (including death) found in the Original SAP. However, it misses several standard definitions present in the Original SAP, such as Prior/Concomitant medications and TEAEs (though TEAEs are implied in analysis sections). A minor contradiction exists in the 'Duration of Treatment' calculation, where the Generated SAP uses a simple date difference while the Original SAP explicitly adds 21 days to account for the final cycle's duration. The ITT population definition in the Generated SAP matches the Protocol exactly, omitting a specific 'successfully screened' clause added in the Original SAP, which is acceptable.

---

### Summary

The Key Definitions section is decent, correctly capturing populations and efficacy endpoints consistent with the Protocol and Original SAP updates. However, it lacks explicit definitions for Prior/Concomitant medications and TEAEs, and the 'Duration of Treatment' calculation conflicts with the Original SAP's specific logic for dose intensity.