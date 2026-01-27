## Key Definitions Evaluation

**Section:** key_definitions
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **definitions in generated SAP:** 21
- **definitions in original SAP:** 25
- **definitions in protocol:** 15
- **definitions evaluated:** 21
- **definitions missing:** 4
- **definitions added:** 6
- **counts valid:** True

---

### Evaluation Table (21 items)

#### 1. Intent-to-Treat (ITT) Population

- **evaluation type:** protocol-defined
- **generated SAP text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **generated SAP location:** 3.3 Analysis Populations
- **original SAP text:** The ITT population will consist of all randomized patients who are randomly assigned to study drug regardless of whether or not any study treatment dosing is completed and successfully screened based on the ‘Screening Pass/Fail’ eCRF page.
- **original SAP location:** 4.4.1 Intent-to-Treat Population
- **protocol text:** The ITT population is defined as all patients randomly assigned to study drug, regardless of whether or not any study treatment dosing is completed.
- **protocol location:** 7.4 Analysis Sets
- **protocol consulted:** yes
- **matches original SAP:** no
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP matches Protocol text exactly. Original SAP added a specific clause about 'successfully screened', but Generated SAP is consistent with the Protocol source of truth.

#### 2. Per-Protocol (PP) Population

- **evaluation type:** protocol-defined
- **generated SAP text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose... and who do not have any major protocol deviation.
- **generated SAP location:** 3.3 Analysis Populations
- **original SAP text:** The PP population will consist of all randomly assigned patients who have at least one response evaluation after receiving at least one full dose... and who do not have any major protocol deviations
- **original SAP location:** 4.4.2 Per-Protocol Population
- **protocol text:** The PP population is defined as all randomly assigned patients who have at least one response evaluation after receiving at least one full dose... and who do not have any major protocol deviation.
- **protocol location:** 7.4 Analysis Sets
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match across all documents.

#### 3. PK Population

- **evaluation type:** protocol-defined
- **generated SAP text:** The PK population is defined as all patients who receive at least one full dose of study drug... and who have at least one post treatment PK result.
- **generated SAP location:** 3.3 Analysis Populations
- **original SAP text:** The PK population will consist of all randomly assigned patients who receive at least one full dose... and who have at least one post treatment PK result.
- **original SAP location:** 4.4.3 Pharmacokinetic Population
- **protocol text:** The PK population is defined as all patients who receive at least one full dose... and who have at least one post treatment PK result.
- **protocol location:** 7.4 Analysis Sets
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 4. Safety Population

- **evaluation type:** protocol-defined
- **generated SAP text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **generated SAP location:** 3.3 Analysis Populations
- **original SAP text:** The safety population will consist of all randomly assigned patients who receive at least one dose (partial or full) of study drug
- **original SAP location:** 4.4.5 Safety Population
- **protocol text:** The safety population is defined as all randomly assigned patients who receive at least one dose (full or partial) of study drug
- **protocol location:** 7.4 Analysis Sets
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 5. Baseline Value

- **evaluation type:** sap-originated
- **generated SAP text:** Defined as the last non-missing observation... recorded prior to the First Dose Date.
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **original SAP location:** 4.5 Definition of Baseline and Post-Baseline
- **protocol consulted:** no
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches intent of Original SAP.

#### 6. Duration of Treatment

- **evaluation type:** sap-originated
- **generated SAP text:** Calculated as (Last Dose Date – First Dose Date) + 1.
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** Actual duration of dose (weeks) = (Start Date of Last Cycle + 21 – Start Date of First Cycle) / 7
- **original SAP location:** 7.2 Exposure to Study Drug
- **protocol consulted:** no
- **matches original SAP:** no
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP explicitly defines duration of dose to include the full cycle length of the last dose (+21 days). Generated SAP defines it as the simple difference between administration dates (+1 day). This underestimates exposure duration by approximately 3 weeks compared to the Original SAP method.

#### 7. Response Duration

- **evaluation type:** sap-originated
- **generated SAP text:** Time from the first documented response (CR or PR) until the first documentation of PD or death (among responders only).
- **generated SAP location:** 6.2.2 Time-to-Event Endpoints
- **original SAP text:** Response duration... defined as the time between the initial response (CR or PR) that is confirmed... and PD/recurrence or death from any cause
- **original SAP location:** 12. CHANGES FROM PROTOCOL
- **protocol text:** Response duration: the time between initial response (CR or PR) and PD/recurrence
- **protocol location:** 7.2.1 Efficacy Endpoints
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP correctly identifies that the definition was updated in the Original SAP (Section 12) to include 'death', differing from the Protocol.

#### 8. Progression-Free Survival (PFS)

- **evaluation type:** protocol-defined
- **generated SAP text:** Time from randomization until the first documentation of PD (per RECIST v.1.1) or death due to any cause.
- **generated SAP location:** 6.2.2 Time-to-Event Endpoints
- **original SAP text:** PFS is defined as time from randomization to determined PD/recurrence or death from any cause (whichever occurs first).
- **original SAP location:** 8.2.2.3 Progression-free Survival
- **protocol text:** PFS: the time from randomization until PD/recurrence or death due to any cause, whichever occurs first
- **protocol location:** 7.2.1 Efficacy Endpoints
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 9. Time to Progression (TTP)

- **evaluation type:** protocol-defined
- **generated SAP text:** Time from randomization until the first documentation of PD.
- **generated SAP location:** 6.2.2 Time-to-Event Endpoints
- **original SAP text:** TTP is defined as time from randomization to determined PD/recurrence.
- **original SAP location:** 8.2.2.2 Time to Progression
- **protocol text:** TTP: the time from randomization until PD/recurrence
- **protocol location:** 7.2.1 Efficacy Endpoints
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 10. Overall Survival (OS)

- **evaluation type:** protocol-defined
- **generated SAP text:** Time from randomization until death due to any cause.
- **generated SAP location:** 6.2.2 Time-to-Event Endpoints
- **original SAP text:** OS is defined as time from randomization to death from any cause.
- **original SAP location:** 8.2.2.4 Overall Survival
- **protocol text:** OS: the time from randomization until death due to any cause
- **protocol location:** 7.2.1 Efficacy Endpoints
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Definitions match.

#### 11. Age

- **evaluation type:** sap-originated
- **generated SAP text:** Calculated as the integer part of (Date of Informed Consent – Date of Birth) / 365.25.
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** Age will be automatically calculated in the eCRF system based on the informed consent signed date, the year of birth and information on whether the date of birth has passed or not.
- **original SAP location:** 6.1 Demographics and Stratification Details
- **protocol consulted:** no
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard calculation method matches intent of Original SAP.

#### 12. Study Day

- **evaluation type:** generated-addition
- **generated SAP text:** For assessments on or after Study Day 1: Study Day = (Date of Assessment – Study Day 1 Date) + 1... There is no Study Day 0.
- **generated SAP location:** 4.2 Key Definitions
- **protocol consulted:** no
- **matches original SAP:** n/a
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard CDISC/ADaM definition added for clarity.

#### 13. Treatment-Emergent Abnormality (Labs)

- **evaluation type:** generated-addition
- **generated SAP text:** Defined as a post-baseline value that represents a worsening from baseline (either an increase in CTCAE grade or a shift from Normal/Low to High, or Normal/High to Low).
- **generated SAP location:** 7.1.3.5 Treatment-Emergent Abnormalities
- **original SAP text:** A shift table will be also produced... to detect changes from baseline.
- **original SAP location:** 10.2 Clinical Laboratory Evaluations
- **protocol consulted:** no
- **matches original SAP:** n/a
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP's requirement for shift tables.

#### 14. First Dose Date

- **evaluation type:** generated-addition
- **generated SAP text:** The date on which a patient receives the first administration of any component of the study treatment
- **generated SAP location:** 4.2 Key Definitions
- **protocol consulted:** no
- **matches original SAP:** n/a
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard variable definition.

#### 15. Last Dose Date

- **evaluation type:** generated-addition
- **generated SAP text:** The date of the last administration of any component of the study treatment
- **generated SAP location:** 4.2 Key Definitions
- **protocol consulted:** no
- **matches original SAP:** n/a
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard variable definition.

#### 16. Controlled Disease

- **evaluation type:** protocol-defined
- **generated SAP text:** Defined as a patient achieving a Best Overall Response (BOR) of Complete Response (CR), Partial Response (PR), or Stable Disease (SD) as assessed at the end of Cycle 6
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** patients with controlled disease (complete response (CR), partial response (PR), or stable disease (SD), assessed at the end of Cycle 6)
- **original SAP location:** 3. OVERALL STUDY DESIGN AND PLAN
- **protocol text:** patients with controlled disease (complete response [CR], partial response [PR], or stable disease [SD], assessed at the end of Cycle 6)
- **protocol location:** 3.1 Study Design
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Protocol and Original SAP.

#### 17. Induction Study Period

- **evaluation type:** protocol-defined
- **generated SAP text:** Defined as the period from Study Day 1 through the day before the first dose of monotherapy in the Maintenance Study Period, or until the EOT visit
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** Induction Study Period: maximum 6 cycles
- **original SAP location:** 3. OVERALL STUDY DESIGN AND PLAN
- **protocol text:** Induction Study Period: maximum 6 cycles
- **protocol location:** Figure 1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP operationalizes the protocol definition into specific dates.

#### 18. Maintenance Study Period

- **evaluation type:** protocol-defined
- **generated SAP text:** Defined as the period from the First Dose Date for the Maintenance Study Period through the date of the EOT visit.
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** Maintenance Study Period: until disease progression, or intolerable toxicity
- **original SAP location:** 3. OVERALL STUDY DESIGN AND PLAN
- **protocol text:** Maintenance Study Period: until disease progression, or intolerable toxicity
- **protocol location:** Figure 1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP operationalizes the protocol definition into specific dates.

#### 19. Follow-Up Period

- **evaluation type:** protocol-defined
- **generated SAP text:** Defined as the period beginning the day after the EOT visit until the date of death, withdrawal of consent, or the end of the study
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** Follow-Up Period: up to approximately 3 years from the last patient enrolled
- **original SAP location:** 3. OVERALL STUDY DESIGN AND PLAN
- **protocol text:** Follow-Up Period: up to approximately 3 years from the last patient enrolled
- **protocol location:** Figure 1
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP operationalizes the protocol definition into specific dates.

#### 20. Objective Response Rate (ORR)

- **evaluation type:** protocol-defined
- **generated SAP text:** defined as the proportion of patients achieving a Best Overall Response (BOR) of either Complete Response (CR) or Partial Response (PR)
- **generated SAP location:** 6.1.1.1 Definition of Endpoint(s)
- **original SAP text:** The ORR is defined as the proportion of patients with a confirmed BOR of CR or PR
- **original SAP location:** 8.1 Primary Efficacy Endpoint
- **protocol text:** Objective response rate (ORR, %) based on BOR during the Induction Study Period
- **protocol location:** Protocol Synopsis
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches.

#### 21. Screening Period

- **evaluation type:** protocol-defined
- **generated SAP text:** Defined as the period from the First Visit Date (ICF signature) to the day before the First Dose Date.
- **generated SAP location:** 4.2 Key Definitions
- **original SAP text:** Screening evaluations will be completed within 28 days prior to randomization.
- **original SAP location:** 3. OVERALL STUDY DESIGN AND PLAN
- **protocol text:** Screening evaluations will be completed within 28 days prior to randomization.
- **protocol location:** 3.1 Study Design
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP operationalizes the protocol definition.

---

### Issues Found (1 items)

#### 1. Duration of Treatment

- **issue type:** contradiction_original
- **severity:** minor
- **source text:** Actual duration of dose (weeks) = (Start Date of Last Cycle + 21 – Start Date of First Cycle) / 7
- **generated text:** Calculated as (Last Dose Date – First Dose Date) + 1
- **why they conflict:** Original SAP includes the full duration of the last cycle (+21 days) in the calculation, whereas Generated SAP only calculates the time between the first and last administration dates. This results in a discrepancy of approximately 3 weeks in exposure duration.
- **description:** Calculation method for treatment duration differs significantly from Original SAP.
- **reasoning:** The Original SAP has a specific formula for 'Actual duration of dose' used for dose intensity that accounts for the therapeutic coverage of the last dose. The Generated SAP uses a generic duration formula that underestimates this coverage.

---

### Internal Contradictions (0 items)

*No internal contradictions.*

---

### Missing Definitions (4 items)

#### 1. Prior Medication

- **original SAP text:** A prior medication is defined as any medication where both the start and stop dates are before the date of first infusion.
- **original SAP location:** 7.1 Prior and Concomitant Medications
- **in protocol:** no
- **classification:** missing_required
- **reasoning:** Essential definition for safety analysis found in Original SAP but missing in Generated SAP.

#### 2. Concomitant Medication

- **original SAP text:** A concomitant medication is defined as any medication that has a stop date that is on or after the date of first infusion or missing.
- **original SAP location:** 7.1 Prior and Concomitant Medications
- **in protocol:** no
- **classification:** missing_required
- **reasoning:** Essential definition for safety analysis found in Original SAP but missing in Generated SAP.

#### 3. Treatment-Emergent Adverse Event (TEAE)

- **original SAP text:** A Treatment-Emergent Adverse Event (TEAE) is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **original SAP location:** 10.1 Adverse Events
- **protocol text:** A treatment-emergent AE is defined as any event not present before exposure to study drug or any event already present that worsens in either severity or frequency after exposure to study drug.
- **protocol location:** 6.5.1.1 Definitions of Adverse Events
- **in protocol:** yes
- **classification:** missing_required
- **reasoning:** Critical safety definition present in both Protocol and Original SAP is missing from the Key Definitions section of Generated SAP.

#### 4. Dose Intensity Formulas

- **original SAP text:** administered dose intensity (weight-adjusted administered dose / actual duration of dose)... relative dose intensity (administered dose intensity / planned dose intensity * 100)
- **original SAP location:** 7.2 Exposure to Study Drug
- **in protocol:** no
- **classification:** missing_required
- **reasoning:** Specific calculation formulas for exposure analysis are missing.

---

### Additions (3 items)

#### 1. First Visit Date

- **generated SAP text:** The date on which the patient signed the informed consent form (ICF).
- **generated SAP location:** 4.2 Key Definitions
- **consistent with study design:** yes
- **contradicts source:** no
- **assessment:** acceptable
- **reasoning:** Standard variable for analysis.

#### 2. Last Visit Date

- **generated SAP text:** The date of the last study-related contact with the patient
- **generated SAP location:** 4.2 Key Definitions
- **consistent with study design:** yes
- **contradicts source:** no
- **assessment:** acceptable
- **reasoning:** Standard variable for analysis.

#### 3. Study Day 1

- **generated SAP text:** Defined as the First Dose Date
- **generated SAP location:** 4.2 Key Definitions
- **consistent with study design:** yes
- **contradicts source:** no
- **assessment:** acceptable
- **reasoning:** Standard variable for analysis.

---

### Reasoning

The Generated SAP provides a solid set of definitions for populations, study periods, and efficacy endpoints, correctly incorporating the Protocol amendment regarding 'Response Duration' (including death) found in the Original SAP. However, it misses several standard definitions present in the Original SAP, such as Prior/Concomitant medications and TEAEs (though TEAEs are implied in analysis sections). A minor contradiction exists in the 'Duration of Treatment' calculation, where the Generated SAP uses a simple date difference while the Original SAP explicitly adds 21 days to account for the final cycle's duration. The ITT population definition in the Generated SAP matches the Protocol exactly, omitting a specific 'successfully screened' clause added in the Original SAP, which is acceptable.

---

### Summary

The Key Definitions section is decent, correctly capturing populations and efficacy endpoints consistent with the Protocol and Original SAP updates. However, it lacks explicit definitions for Prior/Concomitant medications and TEAEs, and the 'Duration of Treatment' calculation conflicts with the Original SAP's specific logic for dose intensity.