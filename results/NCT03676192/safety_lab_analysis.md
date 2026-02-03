## Safety Lab Analysis Evaluation

**Section:** safety_lab_analysis
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **sections read:** 7.1.3, 7.1.3.1, 7.1.3.2, 7.1.3.3, 7.1.3.4, 7.1.3.5, 7.1.3.6
- **elements per section:** 7.1.3: 3, 7.1.3.1: 5, 7.1.3.2: 5, 7.1.3.3: 4, 7.1.3.4: 5, 7.1.3.5: 2, 7.1.3.6: 3
- **elements extracted:** 27
- **elements in evaluation table:** 27
- **elements in missing from generated SAP:** 3
- **counts match:** True

---

### Evaluation Table (27 items)

#### 1. Clinical laboratory assessments scope

- **evaluation type:** exact_match
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized using descriptive statistics
- **generated SAP text:** Clinical laboratory assessments include hematology, clinical chemistry, urinalysis, and coagulation.
- **protocol text:** Clinical laboratory tests: hematology, clinical chemistry, urinalysis
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both documents list the same high-level categories.

#### 2. Sample collection schedule

- **evaluation type:** semantic
- **original SAP text:** Clinical laboratory test samples will be analyzed at the local laboratory.
- **generated SAP text:** Laboratory samples will be collected according to the Schedule of Assessments (Section 11.1).
- **protocol text:** Clinical laboratory tests... will be performed within 3 days prior to Day 1 of each cycle.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard reference to schedule.

#### 3. Analysis location and units

- **evaluation type:** semantic
- **original SAP text:** Clinical laboratory test samples will be analyzed at the local laboratory. Reported units and normal ranges are various among sites. Reported units will be converted to standard units, if applicable.
- **generated SAP text:** Clinical laboratory test samples will be analyzed at the local laboratory for routine monitoring; however, data will be standardized to International System (SI) units for reporting and analysis.
- **protocol text:** Clinical laboratory test samples will be analyzed at the local laboratory.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both specify local laboratory analysis and unit standardization.

#### 4. Hematology parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... hematology... will be summarized
- **generated SAP text:** Hematology: Hematocrit, hemoglobin, white blood cell count, absolute neutrophil count (ANC), and platelets.
- **protocol text:** Hematology: hematocrit, hemoglobin, white blood cell count, absolute neutrophil count and platelets
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists specific parameters which match the Protocol. Original SAP refers to categories generally.

#### 5. Clinical Chemistry parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry... will be summarized
- **generated SAP text:** Clinical Chemistry: Albumin, alkaline phosphatase (ALP), alanine aminotransferase (ALT), aspartate aminotransferase (AST), blood urea nitrogen (BUN), calcium, chloride, creatine phosphokinase (CPK), creatine kinase-myocardial band (CK-MB) isoenzyme, total cholesterol, creatinine, creatinine clearance (CrCl) (estimated by Cockcroft-Gault formula, see Section 11.6), gamma-glutamyl transferase (GGT), glucose, lactate dehydrogenase (LDH), triglyceride, high-density lipoprotein (HDL) cholesterol, phosphate, potassium, sodium, total bilirubin, direct bilirubin, total protein, and uric acid.
- **protocol text:** Clinical chemistry: albumin, alkaline phosphatase... [list matches Generated SAP]
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists specific parameters which match the Protocol. Original SAP refers to categories generally.

#### 6. Urinalysis parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis... will be summarized... The results for all non-numeric urinalysis parameters... will be categorized into normal and abnormal
- **generated SAP text:** Urinalysis: Bilirubin, blood, glucose, ketones, leukocytes, nitrite, pH, protein, specific gravity, and urobilinogen via dipstick.
- **protocol text:** Urinalysis: bilirubin, blood, glucose... [list matches Generated SAP]
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists specific parameters which match the Protocol.

#### 7. Additional urinalysis

- **evaluation type:** semantic
- **original SAP text:** The results for all non-numeric urinalysis parameters including microscopic urinalysis collected as qualitative format will be categorized into normal and abnormal
- **generated SAP text:** Microscopic examination and 24-hour urine collection (for protein) will be performed if indicated.
- **protocol text:** microscopic examination... 24 hour urine collection if indicated at Screening
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP and Protocol.

#### 8. Coagulation parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... coagulation will be summarized
- **generated SAP text:** Coagulation: Prothrombin time (PT) and prothrombin time international normalized ratio (INR) (for patients receiving aspirin).
- **protocol text:** Coagulation: ... prothrombin time and prothrombin time international normalized ratio tests
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists specific parameters which match the Protocol.

#### 9. Baseline definition

- **evaluation type:** semantic
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** Baseline is defined in Section 4.2.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Cross-reference to general baseline definition is acceptable.

#### 10. Post-baseline summary scope

- **evaluation type:** semantic
- **original SAP text:** If visit names are ‘Unscheduled’ or ‘EOT’, the post-baseline result of laboratory data will be presented by period, defined as follows... [detailed logic for Induction, Maintenance, Follow-Up]
- **generated SAP text:** Post-baseline summaries will include all scheduled visits during the Induction Study Period (Cycles 1 through 6), Maintenance Study Period (Cycles 1 and every 3 cycles thereafter), and the End of Treatment (EOT) visit.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Detailed logic for assigning EOT and unscheduled visits to specific study periods based on dates relative to infusion.
- **omission impact:** potential
- **result:** problem
- **issue type:** none
- **severity:** minor
- **reasoning:** Generated SAP omits the specific logic found in the Original SAP for assigning data to study periods, which is important for a study with distinct phases.

#### 11. Data listings

- **evaluation type:** exact_match
- **original SAP text:** Clinical chemistry, hematology, urinalysis and coagulation data will be presented in separate listings
- **generated SAP text:** All laboratory data will be included in the data listings.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both require listings for all data.

#### 12. Descriptive statistics scope (Hematology/Chemistry)

- **evaluation type:** exact_match
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology... will be summarized using descriptive statistics
- **generated SAP text:** Summaries of actual values and change from baseline will be provided for hematology and clinical chemistry.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP for these categories.

#### 13. Descriptive statistics scope (Coagulation/Urinalysis)

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis and coagulation will be summarized using descriptive statistics
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Descriptive statistics for coagulation and numeric urinalysis.
- **omission impact:** low
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP requires descriptive summaries for coagulation and numeric urinalysis; Generated SAP explicitly restricts them to listings only.

#### 14. Descriptive statistics methodology

- **evaluation type:** exact_match
- **original SAP text:** Actual result and change from baseline... will be summarized using descriptive statistics by treatment group, laboratory category, test parameter and visit.
- **generated SAP text:** Laboratory parameters will be summarized by treatment group and visit using descriptive statistics.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard descriptive statistics methodology.

#### 15. Summary content

- **evaluation type:** exact_match
- **original SAP text:** Actual result and change from baseline... will be summarized
- **generated SAP text:** Summaries will include both actual values and change from baseline values.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP.

#### 16. Nominal visits

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline... will be summarized... by... visit
- **generated SAP text:** As established in Section 4.5, nominal visits will be used for these summaries.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP's visit-based summary approach.

#### 17. Scheduled visits only

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table. [Implies by-visit summaries are scheduled only]
- **generated SAP text:** Only scheduled visits will be included in by-visit summaries.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with standard practice and Original SAP's handling of unscheduled visits.

#### 18. CTCAE Grading

- **evaluation type:** exact_match
- **original SAP text:** Clinical laboratory parameters... will be labeled with a CTCAE term and grading will be applied... according to CTCAE version 5.0.
- **generated SAP text:** Laboratory abnormalities will be graded according to the National Cancer Institute (NCI) Common Terminology Criteria for Adverse Events (CTCAE) version 5.0, where applicable.
- **protocol text:** Adverse events will be reported for term and grade according to the Common Terminology Criteria for Adverse Events (CTCAE) v.5.0.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP and Protocol.

#### 19. Shift tables (Graded)

- **evaluation type:** semantic
- **original SAP text:** A shift table will be also produced... Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **generated SAP text:** Shift tables will be used to summarize the number and percentage of patients by baseline category (Grade 0 through 4) versus the worst post-baseline category.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP's requirement for shift tables using worst/most severe post-baseline value.

#### 20. Worst post-baseline definition

- **evaluation type:** exact_match
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **generated SAP text:** Worst post-baseline value is defined as the most extreme CTCAE grade observed during the Whole Study Period (as defined in Section 4.2), including results from unscheduled assessments.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP.

#### 21. Shift tables (Non-graded)

- **evaluation type:** semantic
- **original SAP text:** The results for all non-numeric urinalysis parameters... will be categorized into normal and abnormal... and will be summarized in a shift table.
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High) relative to the laboratory reference range versus the worst post-baseline category.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP generalizes the shift table requirement to all non-graded parameters (L/N/H), which covers the intent of the Original SAP.

#### 22. Directional analysis

- **evaluation type:** semantic
- **generated SAP text:** Analyses will be performed separately for the "High" and "Low" directions when both are clinically relevant (e.g., potassium).
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Extra detail consistent with standard practice.

#### 23. Treatment-emergent abnormalities

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients with a result for each grade will be summarized by laboratory category, CTCAE term, visit and CTCAE grade.
- **generated SAP text:** The number and percentage of patients with treatment-emergent laboratory abnormalities (defined as an increase in CTCAE grade from baseline) will be summarized by treatment group.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP specifies 'treatment-emergent' (increase from baseline) while Original SAP asks for summaries by grade. These are compatible safety summaries.

#### 24. Grade 3/4 focus

- **evaluation type:** semantic
- **generated SAP text:** Particular focus will be placed on Grade 3 or 4 abnormalities.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard safety focus.

#### 25. Unscheduled assessment handling

- **evaluation type:** exact_match
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **generated SAP text:** Unscheduled laboratory assessments will be excluded from by-visit summaries but will be included in the determination of the worst post-baseline values and in all listings.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP.

#### 26. Duplicate assessment handling

- **evaluation type:** semantic
- **generated SAP text:** If multiple laboratory values are collected on the same study day, the value collected closest to the scheduled assessment time will be used for by-visit summaries.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard data handling rule.

#### 27. Worst value determination

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **generated SAP text:** For the determination of the worst post-baseline value, the most extreme value among all results (scheduled or unscheduled) for that day will be used.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP.


---

### Issues Found (2 items)

#### 1. Coagulation analysis scope

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... coagulation will be summarized using descriptive statistics
- **generated SAP text:** Coagulation... results will be presented in data listings only.
- **protocol text:** n/a
- **why they conflict:** Original SAP requires descriptive summaries for coagulation; Generated SAP explicitly restricts them to listings only.
- **description:** Generated SAP removes the requirement for descriptive statistics for coagulation parameters.
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly includes coagulation in the list of parameters to be summarized with descriptive statistics. 2) Generated SAP explicitly states coagulation results will be presented in data listings only. 3) These statements are mutually exclusive. 4) This is a contradiction reducing the scope of analysis.

#### 2. Urinalysis analysis scope

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis... will be summarized... The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **generated SAP text:** Urinalysis results will be presented in data listings only.
- **protocol text:** n/a
- **why they conflict:** Original SAP requires descriptive summaries for numeric urinalysis and shift tables for non-numeric urinalysis; Generated SAP explicitly restricts all urinalysis to listings only.
- **description:** Generated SAP removes the requirement for descriptive statistics and shift tables for urinalysis parameters.
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly requires summaries for numeric urinalysis and shift tables for non-numeric urinalysis. 2) Generated SAP explicitly states urinalysis results will be presented in data listings only. 3) These statements are mutually exclusive. 4) This is a contradiction reducing the scope of analysis.


---

### Extra Information Flagged (1 items)

#### 1. Duplicate assessment handling

- **content:** Duplicate assessment handling
- **generated SAP text:** If multiple laboratory values are collected on the same study day, the value collected closest to the scheduled assessment time will be used for by-visit summaries.
- **contradicts:** no
- **detail:** Standard data handling rule not explicit in Original SAP Section 10.2.
- **reasoning:** Beneficial clarification.


---

### Missing from Generated SAP (3 items)

#### 1. Period assignment logic

- **original SAP text:** If visit names are ‘Unscheduled’ or ‘EOT’, the post-baseline result of laboratory data will be presented by period, defined as follows... [detailed logic for Induction, Maintenance, Follow-Up]
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Detailed logic for assigning EOT and unscheduled visits to specific study periods based on dates relative to infusion.
- **reasoning:** Original SAP provides complex logic for assigning data to study periods. Generated SAP omits this logic, which is a missing specification.

#### 2. Clinical input grading rule

- **original SAP text:** Grades that require clinical input only will not be assigned to these parameters. Grades which are part numeric and part clinical input will be assigned based on the numeric portion only.
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific rule about handling CTCAE grades requiring clinical input.
- **reasoning:** Specific grading rule missing from Generated SAP.

#### 3. Grade 5 exclusion

- **original SAP text:** The CTCAE Grade 5 (Death) will not be applied in this analysis since death cannot be determined from a laboratory result.
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Explicit exclusion of Grade 5 from laboratory grading.
- **reasoning:** Specific exclusion rule missing from Generated SAP.


---

### Reverse Check (5 items)

#### 1. Item 1

- **original SAP statement:** The CTCAE Grade 5 (Death) will not be applied in this analysis since death cannot be determined from a laboratory result.
- **checked against elements:** ['CTCAE Grading', 'Shift tables (Graded)']
- **contradiction found:** no
- **explanation:** Generated SAP does not mention Grade 5, so no contradiction.

#### 2. Item 2

- **original SAP statement:** Grades that require clinical input only will not be assigned to these parameters.
- **checked against elements:** ['CTCAE Grading']
- **contradiction found:** no
- **explanation:** Generated SAP does not mention clinical input grades, so no contradiction.

#### 3. Item 3

- **original SAP statement:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **checked against elements:** ['Shift tables (Graded)', 'Worst post-baseline definition']
- **contradiction found:** no
- **explanation:** Generated SAP matches this requirement.

#### 4. Item 4

- **original SAP statement:** Actual result and change from baseline of all numeric laboratory parameters including... coagulation will be summarized
- **checked against elements:** ['Descriptive statistics scope (Coagulation/Urinalysis)']
- **contradiction found:** yes
- **contradicting element:** Descriptive statistics scope (Coagulation/Urinalysis)
- **explanation:** Generated SAP restricts coagulation to listings only.

#### 5. Item 5

- **original SAP statement:** The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **checked against elements:** ['Descriptive statistics scope (Coagulation/Urinalysis)']
- **contradiction found:** yes
- **contradicting element:** Descriptive statistics scope (Coagulation/Urinalysis)
- **explanation:** Generated SAP restricts urinalysis to listings only.


---

### Reasoning

The Generated SAP is largely consistent with the Original SAP regarding the core laboratory analysis (hematology and clinical chemistry). It correctly identifies the parameters, the use of local laboratories, unit standardization, and the use of CTCAE v5.0 for grading. It also correctly handles unscheduled visits and worst post-baseline values for shift tables. However, there are two clear contradictions regarding the scope of analysis for ancillary parameters: the Original SAP requires descriptive statistics for coagulation and numeric urinalysis, and shift tables for non-numeric urinalysis, whereas the Generated SAP explicitly restricts these to data listings only. Additionally, the Generated SAP omits the detailed logic for assigning data to study periods (Induction vs Maintenance) and specific grading rules (clinical input, Grade 5 exclusion). These omissions and contradictions are minor in the context of the overall safety analysis but represent a reduction in reporting scope.

---

### Summary

The Generated SAP accurately captures the primary laboratory analysis methodology but contradicts the Original SAP by restricting coagulation and urinalysis to listings only, whereas the Original SAP required summaries. It also omits detailed logic for assigning data to study periods and specific grading rules found in the Original SAP.