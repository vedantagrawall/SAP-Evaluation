## Safety Lab Analysis Evaluation

**Section:** safety_lab_analysis
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **sections read:** 7.1.3, 7.1.3.1, 7.1.3.2, 7.1.3.3, 7.1.3.4, 7.1.3.5, 7.1.3.6
- **elements per section:** 7.1.3: 3, 7.1.3.1: 5, 7.1.3.2: 5, 7.1.3.3: 3, 7.1.3.4: 5, 7.1.3.5: 2, 7.1.3.6: 3
- **elements extracted:** 26
- **elements in evaluation table:** 26
- **elements in missing from generated SAP:** 4
- **counts match:** True

---

### Evaluation Table (26 items)

#### 1. Clinical laboratory assessments scope

- **evaluation type:** exact_match
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized
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
- **reasoning:** Generated SAP correctly identifies the scope of assessments.

#### 2. Sample collection reference

- **evaluation type:** semantic
- **original SAP text:** Clinical laboratory test samples will be analyzed at the local laboratory.
- **generated SAP text:** Laboratory samples will be collected according to the Schedule of Assessments (Section 11.1).
- **protocol text:** Clinical laboratory test samples will be analyzed at the local laboratory.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard reference to schedule.

#### 3. Local laboratory and SI units

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
- **reasoning:** Both specify local lab analysis and unit standardization.

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
- **reasoning:** Generated SAP lists specific parameters consistent with Protocol and Original SAP's general requirement.

#### 5. Clinical Chemistry parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry... will be summarized
- **generated SAP text:** Clinical Chemistry: Albumin, alkaline phosphatase (ALP), alanine aminotransferase (ALT), aspartate aminotransferase (AST), blood urea nitrogen (BUN), calcium, chloride, creatine phosphokinase (CPK), creatine kinase-myocardial band (CK-MB) isoenzyme, total cholesterol, creatinine, creatinine clearance (CrCl) (estimated by Cockcroft-Gault formula, see Section 11.6), gamma-glutamyl transferase (GGT), glucose, lactate dehydrogenase (LDH), triglyceride, high-density lipoprotein (HDL) cholesterol, phosphate, potassium, sodium, total bilirubin, direct bilirubin, total protein, and uric acid.
- **protocol text:** Clinical chemistry: albumin, alkaline phosphatase, alanine aminotransferase, aspartate aminotransferase, blood urea nitrogen, calcium, chloride, creatine phosphokinase, creatine kinase-myocardial band isoenzyme, total cholesterol, creatinine, CrCl... gamma-glutamyl transferase, glucose, lactate dehydrogenase, triglyceride, high-density lipoprotein cholesterol, phosphate, potassium, sodium, total bilirubin, direct bilirubin, total protein, uric acid
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists specific parameters consistent with Protocol and Original SAP's general requirement.

#### 6. Urinalysis parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis... will be summarized... The results for all non-numeric urinalysis parameters including microscopic urinalysis... will be categorized into normal and abnormal... and will be summarized in a shift table.
- **generated SAP text:** Urinalysis: Bilirubin, blood, glucose, ketones, leukocytes, nitrite, pH, protein, specific gravity, and urobilinogen via dipstick.
- **protocol text:** Urinalysis: bilirubin, blood, glucose, ketones, leukocytes (white blood cells), nitrite, pH, protein, specific gravity, urobilinogen and microscopic examination
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Parameter list matches Protocol.

#### 7. Microscopic urinalysis and 24-hour collection

- **evaluation type:** semantic
- **original SAP text:** The results for all non-numeric urinalysis parameters including microscopic urinalysis... will be categorized into normal and abnormal... and will be summarized in a shift table.
- **generated SAP text:** Microscopic examination and 24-hour urine collection (for protein) will be performed if indicated.
- **protocol text:** 24 hour urine collection if indicated at Screening
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Protocol requirement for indicated performance.

#### 8. Coagulation parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... coagulation will be summarized
- **generated SAP text:** Coagulation: Prothrombin time (PT) and prothrombin time international normalized ratio (INR) (for patients receiving aspirin).
- **protocol text:** Coagulation: Any patients who continue with low dose aspirin... should perform prothrombin time and prothrombin time international normalized ratio tests.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Protocol requirement.

#### 9. Baseline definition reference

- **evaluation type:** semantic
- **original SAP text:** The baseline value for all analyses will be the last non-missing value prior to the first infusion unless otherwise specified.
- **generated SAP text:** Baseline is defined in Section 4.2.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Cross-reference to baseline definition is acceptable.

#### 10. Post-baseline summary visits

- **evaluation type:** semantic
- **original SAP text:** If visit names are ‘Unscheduled’ or ‘EOT’, the post-baseline result of laboratory data will be presented by period... Laboratory data will be summarized in the Induction Study Period if... Laboratory data will be summarized in the Maintenance Study Period if... Laboratory data will be summarized in Follow-Up Period if...
- **generated SAP text:** Post-baseline summaries will include all scheduled visits during the Induction Study Period (Cycles 1 through 6), Maintenance Study Period (Cycles 1 and every 3 cycles thereafter), and the End of Treatment (EOT) visit.
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Original SAP maps EOT to periods for summarization logic. Generated SAP includes EOT as a visit column.
- **omission impact:** low
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP defines logic to map EOT visits to specific study periods for summarization. Generated SAP treats EOT as a distinct visit column in the summary tables. This is a difference in display strategy.

#### 11. Data listings inclusion

- **evaluation type:** exact_match
- **original SAP text:** Clinical chemistry, hematology, urinalysis and coagulation data will be presented in separate listings
- **generated SAP text:** All laboratory data will be included in the data listings.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent requirement.

#### 12. Hematology and Chemistry summaries

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology... will be summarized
- **generated SAP text:** Summaries of actual values and change from baseline will be provided for hematology and clinical chemistry.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches requirement for these parameters.

#### 13. Coagulation and Urinalysis analysis method

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis and coagulation will be summarized... The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Summaries for numeric urinalysis/coagulation and shift tables for non-numeric urinalysis.
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** critical
- **reasoning:** Original SAP explicitly requires summaries for numeric urinalysis and coagulation, and shift tables for non-numeric urinalysis. Generated SAP restricts these to listings only. This is critical because Proteinuria (urinalysis) is a key safety risk for Bevacizumab.

#### 14. Descriptive statistics summary

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline... will be summarized using descriptive statistics by treatment group, laboratory category, test parameter and visit.
- **generated SAP text:** Laboratory parameters will be summarized by treatment group and visit using descriptive statistics.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches general summary requirement.

#### 15. Actual and change from baseline

- **evaluation type:** exact_match
- **original SAP text:** Actual result and change from baseline... will be summarized
- **generated SAP text:** Summaries will include both actual values and change from baseline values.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches requirement.

#### 16. Scheduled visits only

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table. (Implies unscheduled are excluded from by-visit summaries)
- **generated SAP text:** As established in Section 4.5, nominal visits will be used for these summaries. Only scheduled visits will be included in by-visit summaries.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with standard practice and Original SAP implication.

#### 17. CTCAE grading version

- **evaluation type:** exact_match
- **original SAP text:** according to CTCAE version 5.0.
- **generated SAP text:** Laboratory abnormalities will be graded according to the National Cancer Institute (NCI) Common Terminology Criteria for Adverse Events (CTCAE) version 5.0, where applicable.
- **protocol text:** according to the Common Terminology Criteria for Adverse Events (CTCAE) v.5.0.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches version.

#### 18. Shift table definition

- **evaluation type:** semantic
- **original SAP text:** A shift table will be also produced by the Whole Study Period and each study period.
- **generated SAP text:** Shift tables will be used to summarize the number and percentage of patients by baseline category (Grade 0 through 4) versus the worst post-baseline category.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Requirement for shift tables for 'each study period' (Induction, Maintenance, Follow-up).
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP defines shift tables but omits the specific requirement to produce them for each study period separately, only mentioning Whole Study Period.

#### 19. Worst post-baseline definition

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **generated SAP text:** Worst post-baseline value is defined as the most extreme CTCAE grade observed during the Whole Study Period (as defined in Section 4.2), including results from unscheduled assessments.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches logic of using most severe case including unscheduled.

#### 20. Non-CTCAE shift tables

- **evaluation type:** semantic
- **original SAP text:** The results for all non-numeric urinalysis parameters... will be categorized into normal and abnormal... and will be summarized in a shift table.
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High) relative to the laboratory reference range versus the worst post-baseline category.
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Specific requirement for Normal/Abnormal shift tables for non-numeric urinalysis.
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Generated SAP adds Low/Normal/High shift tables (acceptable extra) but omits the specific Normal/Abnormal shift tables for non-numeric urinalysis required by Original SAP.

#### 21. High/Low direction analysis

- **evaluation type:** semantic
- **generated SAP text:** Analyses will be performed separately for the "High" and "Low" directions when both are clinically relevant (e.g., potassium).
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard practice, not contradictory.

#### 22. Treatment-emergent abnormalities summary

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients with a result for each grade will be summarized by laboratory category, CTCAE term, visit and CTCAE grade.
- **generated SAP text:** The number and percentage of patients with treatment-emergent laboratory abnormalities (defined as an increase in CTCAE grade from baseline) will be summarized by treatment group.
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Summary of patients with a result for each grade by visit.
- **omission impact:** low
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP asks for prevalence of grades by visit. Generated SAP replaces this with incidence of treatment-emergent worsening.

#### 23. Grade 3/4 focus

- **evaluation type:** semantic
- **generated SAP text:** Particular focus will be placed on Grade 3 or 4 abnormalities.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard practice.

#### 24. Unscheduled visits exclusion

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table. (Implies exclusion from by-visit)
- **generated SAP text:** Unscheduled laboratory assessments will be excluded from by-visit summaries but will be included in the determination of the worst post-baseline values and in all listings.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches logic.

#### 25. Multiple values same day handling

- **evaluation type:** semantic
- **generated SAP text:** If multiple laboratory values are collected on the same study day, the value collected closest to the scheduled assessment time will be used for by-visit summaries.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard rule, not contradictory.

#### 26. Worst value same day handling

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **generated SAP text:** For the determination of the worst post-baseline value, the most extreme value among all results (scheduled or unscheduled) for that day will be used.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches logic.


---

### Issues Found (1 items)

#### 1. Urinalysis and Coagulation analysis

- **issue type:** contradiction_original
- **severity:** critical
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis and coagulation will be summarized... The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **why they conflict:** Original SAP requires summaries and shift tables for these parameters. Generated SAP explicitly restricts them to listings only.
- **description:** Generated SAP removes required safety analyses for Urinalysis and Coagulation. This is critical because Proteinuria (urinalysis) is a key safety risk for Bevacizumab.
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly requires summaries for numeric urinalysis/coagulation and shift tables for non-numeric urinalysis. 2) Generated SAP states these will be 'listings only'. 3) These statements contradict. 4) Proteinuria is a known risk for the study drug, making the removal of urinalysis summaries a critical safety analysis gap.


---

### Extra Information Flagged (2 items)

#### 1. Low/Normal/High shift tables for non-CTCAE parameters

- **content:** Low/Normal/High shift tables for non-CTCAE parameters
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High)...
- **contradicts:** no
- **detail:** Original SAP does not explicitly require this but does not forbid it.
- **reasoning:** Acceptable addition.

#### 2. Treatment-emergent abnormality summary

- **content:** Treatment-emergent abnormality summary
- **generated SAP text:** The number and percentage of patients with treatment-emergent laboratory abnormalities... will be summarized
- **contradicts:** no
- **detail:** Original SAP asks for grade prevalence. This is a different summary but acceptable as an addition or substitution.
- **reasoning:** Standard safety analysis.


---

### Missing from Generated SAP (4 items)

#### 1. Shift tables for each study period

- **original SAP text:** A shift table will be also produced by the Whole Study Period and each study period.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Generated SAP only defines shift tables for Whole Study Period, omitting the requirement for separate tables for Induction, Maintenance, and Follow-up.
- **reasoning:** Original SAP explicitly requires shift tables for each period.

#### 2. Summary of grades by visit

- **original SAP text:** The number and percentage of patients with a result for each grade will be summarized by laboratory category, CTCAE term, visit and CTCAE grade.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Generated SAP replaces this with a summary of treatment-emergent abnormalities.
- **reasoning:** Original SAP requires prevalence summary by grade.

#### 3. EOT mapping logic

- **original SAP text:** If visit names are ‘Unscheduled’ or ‘EOT’, the post-baseline result of laboratory data will be presented by period, defined as follows...
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Original SAP provides specific logic for mapping EOT visits to study periods for summarization. Generated SAP treats EOT as a visit column.
- **reasoning:** Difference in display strategy.

#### 4. Non-convertible units handling

- **original SAP text:** Reported parameters with units that cannot be converted to standard units will be summarized separately using the original units.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Generated SAP omits the rule for handling parameters that cannot be converted to SI units.
- **reasoning:** Minor omission.


---

### Reverse Check (5 items)

#### 1. Item 1

- **original SAP statement:** The CTCAE Grade 5 (Death) will not be applied in this analysis since death cannot be determined from a laboratory result.
- **checked against elements:** ['Shift table definition']
- **contradiction found:** no
- **explanation:** Generated SAP defines baseline category as Grade 0 through 4, implicitly excluding Grade 5.

#### 2. Item 2

- **original SAP statement:** Grades that require clinical input only will not be assigned to these parameters.
- **checked against elements:** ['CTCAE grading version']
- **contradiction found:** no
- **explanation:** Generated SAP does not mention this exclusion but does not contradict it.

#### 3. Item 3

- **original SAP statement:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **checked against elements:** ['Worst post-baseline definition']
- **contradiction found:** no
- **explanation:** Generated SAP matches this logic.

#### 4. Item 4

- **original SAP statement:** EOT and unscheduled visit will not be summarized in visit-based tables, unless otherwise indicated.
- **checked against elements:** ['Post-baseline summary visits']
- **contradiction found:** yes
- **contradicting element:** Post-baseline summary visits
- **explanation:** Generated SAP explicitly includes EOT in post-baseline summaries, whereas Original SAP maps EOT to periods.

#### 5. Item 5

- **original SAP statement:** Reported parameters with units that cannot be converted to standard units will be summarized separately using the original units.
- **checked against elements:** ['Local laboratory and SI units']
- **contradiction found:** no
- **explanation:** Generated SAP omits this rule but does not contradict it.


---

### Reasoning

The Generated SAP accurately captures the parameter lists and general analysis approach for hematology and clinical chemistry. However, it contains a critical contradiction regarding Urinalysis and Coagulation. The Original SAP explicitly requires descriptive summaries for numeric urinalysis and coagulation, and shift tables for non-numeric urinalysis. The Generated SAP restricts these parameters to 'listings only'. Since Proteinuria (detected via urinalysis) is a key safety risk for Bevacizumab (listed as an Adverse Event of Special Interest in the Original SAP), removing the summary analysis for urinalysis is a critical failure that impacts safety monitoring. Additionally, the Generated SAP omits the requirement for shift tables for 'each study period', only defining the 'Whole Study Period' analysis.

---

### Summary

The Generated SAP fails to meet requirements due to a critical contradiction in safety analysis scope. It restricts Urinalysis and Coagulation to 'listings only', whereas the Original SAP requires summaries and shift tables. This is critical because Proteinuria is a known risk for the study drug.