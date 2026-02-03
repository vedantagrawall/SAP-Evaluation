## Safety Lab Analysis Evaluation

**Section:** safety_lab_analysis
**Rating:** DECENT
**Status:** pass_with_notes

---

### Extraction Validation

- **sections read:** 7.1.3, 7.1.3.1, 7.1.3.2, 7.1.3.3, 7.1.3.4, 7.1.3.5, 7.1.3.6
- **elements per section:** 7.1.3: 3, 7.1.3.1: 5, 7.1.3.2: 5, 7.1.3.3: 3, 7.1.3.4: 5, 7.1.3.5: 2, 7.1.3.6: 3
- **elements extracted:** 26
- **elements in evaluation table:** 26
- **elements in missing from generated SAP:** 5
- **counts match:** True

---

### Evaluation Table (26 items)

#### 1. Laboratory categories

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
- **reasoning:** Both documents list the same four main categories.

#### 2. Sample collection schedule

- **evaluation type:** semantic
- **original SAP text:** Clinical laboratory test samples will be analyzed at the local laboratory. Reported units and normal ranges are various among sites.
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
- **reasoning:** Both specify local lab analysis and standardization of units.

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
- **reasoning:** Generated SAP lists specific parameters matching the Protocol. Original SAP implies them via 'all numeric laboratory parameters' and Appendix 14.2.

#### 5. Clinical Chemistry parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry... will be summarized
- **generated SAP text:** Clinical Chemistry: Albumin, alkaline phosphatase (ALP), alanine aminotransferase (ALT), aspartate aminotransferase (AST), blood urea nitrogen (BUN), calcium, chloride, creatine phosphokinase (CPK), creatine kinase-myocardial band (CK-MB) isoenzyme, total cholesterol, creatinine, creatinine clearance (CrCl) (estimated by Cockcroft-Gault formula, see Section 11.6), gamma-glutamyl transferase (GGT), glucose, lactate dehydrogenase (LDH), triglyceride, high-density lipoprotein (HDL) cholesterol, phosphate, potassium, sodium, total bilirubin, direct bilirubin, total protein, and uric acid.
- **protocol text:** Clinical chemistry: albumin, alkaline phosphatase, alanine aminotransferase, aspartate aminotransferase, blood urea nitrogen, calcium, chloride, creatine phosphokinase, creatine kinase-myocardial band isoenzyme, total cholesterol, creatinine, CrCl..., gamma-glutamyl transferase, glucose, lactate dehydrogenase, triglyceride, high-density lipoprotein cholesterol, phosphate, potassium, sodium, total bilirubin, direct bilirubin, total protein, uric acid
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists specific parameters matching the Protocol. Original SAP implies them via 'all numeric laboratory parameters'.

#### 6. Urinalysis parameters

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis... will be summarized... The results for all non-numeric urinalysis parameters including microscopic urinalysis... will be categorized
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
- **reasoning:** Generated SAP lists specific parameters matching the Protocol.

#### 7. Microscopic urinalysis and 24-hour collection

- **evaluation type:** exact_match
- **original SAP text:** The results for all non-numeric urinalysis parameters including microscopic urinalysis... 24 hours urine collection (protein)
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
- **reasoning:** Matches Original SAP and Protocol requirements.

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
- **reasoning:** Generated SAP lists specific parameters matching the Protocol.

#### 9. Baseline definition reference

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
- **reasoning:** Cross-reference to Section 4.2 is acceptable.

#### 10. Post-baseline summary visits

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline... will be summarized... by... visit... If visit names are ‘Unscheduled’ or ‘EOT’, the post-baseline result of laboratory data will be presented by period
- **generated SAP text:** Post-baseline summaries will include all scheduled visits during the Induction Study Period (Cycles 1 through 6), Maintenance Study Period (Cycles 1 and every 3 cycles thereafter), and the End of Treatment (EOT) visit.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches the visit-based summary requirement.

#### 11. Data listings inclusion

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
- **reasoning:** Matches requirement for listings.

#### 12. Hematology and Chemistry summaries

- **evaluation type:** exact_match
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology... will be summarized
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
- **reasoning:** Matches requirement for summaries.

#### 13. Coagulation and Urinalysis reporting

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis and coagulation will be summarized using descriptive statistics... The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Requirement to summarize numeric urinalysis and coagulation, and shift tables for non-numeric urinalysis.
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP explicitly requires summaries for numeric urinalysis and coagulation, and shift tables for non-numeric urinalysis. Generated SAP explicitly restricts these to listings only.

#### 14. Descriptive statistics summary

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
- **reasoning:** Matches summary method.

#### 15. Actual and change from baseline

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
- **reasoning:** Matches summary content.

#### 16. Scheduled visits only for summaries

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table. [Implies by-visit summaries use scheduled]
- **generated SAP text:** As established in Section 4.5, nominal visits will be used for these summaries. Only scheduled visits will be included in by-visit summaries.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard practice consistent with Original SAP implication.

#### 17. CTCAE grading

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
- **reasoning:** Matches grading standard.

#### 18. Shift table methodology

- **evaluation type:** semantic
- **original SAP text:** A shift table will be also produced... The number and percentage of patients with a result for each grade will be summarized... Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
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
- **reasoning:** Matches the worst post-baseline methodology.

#### 19. Worst post-baseline definition

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
- **reasoning:** Matches definition.

#### 20. Non-CTCAE shift tables

- **evaluation type:** semantic
- **original SAP text:** Reported parameters with units that cannot be converted to standard units will be summarized separately using the original units.
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High) relative to the laboratory reference range versus the worst post-baseline category.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP adds specific methodology for non-CTCAE parameters (Low/Normal/High shift) which is a standard safety analysis addition and does not contradict Original SAP.

#### 21. High/Low direction analysis

- **evaluation type:** semantic
- **generated SAP text:** Analyses will be performed separately for the "High" and "Low" directions when both are clinically relevant (e.g., potassium).
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard safety analysis detail added by Generated SAP.

#### 22. Treatment-emergent abnormalities

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients with a result for each grade will be summarized by laboratory category, CTCAE term, visit and CTCAE grade.
- **generated SAP text:** The number and percentage of patients with treatment-emergent laboratory abnormalities (defined as an increase in CTCAE grade from baseline) will be summarized by treatment group.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP adds a specific summary for 'treatment-emergent' (increase in grade), which complements the by-grade summary.

#### 23. Focus on Grade 3/4

- **evaluation type:** semantic
- **generated SAP text:** Particular focus will be placed on Grade 3 or 4 abnormalities.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard safety focus.

#### 24. Unscheduled visit handling

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
- **reasoning:** Matches handling rule.

#### 25. Multiple values on same day (summary)

- **evaluation type:** semantic
- **generated SAP text:** If multiple laboratory values are collected on the same study day, the value collected closest to the scheduled assessment time will be used for by-visit summaries.
- **protocol text:** n/a
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Standard data handling rule added.

#### 26. Multiple values on same day (worst case)

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
- **reasoning:** Matches worst-case logic.


---

### Issues Found (1 items)

#### 1. Coagulation and Urinalysis reporting

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized using descriptive statistics... The results for all non-numeric urinalysis parameters including microscopic urinalysis collected as qualitative format will be categorized into normal and abnormal... and will be summarized in a shift table.
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **protocol text:** n/a
- **why they conflict:** Original SAP explicitly requires summary statistics for numeric urinalysis and coagulation, and shift tables for non-numeric urinalysis. Generated SAP explicitly restricts these to listings only.
- **description:** Generated SAP removes required summaries for coagulation and urinalysis.
- **reasoning:** Chain-of-thought: 1) Original SAP mandates summaries for these parameters. 2) Generated SAP mandates 'listings only'. 3) These are mutually exclusive instructions. 4) This reduces the scope of safety reporting.


---

### Extra Information Flagged (1 items)

#### 1. Low/Normal/High shift tables for non-CTCAE parameters

- **content:** Low/Normal/High shift tables for non-CTCAE parameters
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High) relative to the laboratory reference range versus the worst post-baseline category.
- **contradicts:** no
- **detail:** Standard safety analysis addition.
- **reasoning:** Original SAP does not explicitly forbid this; it enhances reporting for non-graded parameters.


---

### Missing from Generated SAP (5 items)

#### 1. Shift tables per study period

- **original SAP text:** A shift table will be also produced by the Whole Study Period and each study period.
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Original SAP requires shift tables for each study period (Induction, Maintenance, Follow-up) in addition to Whole Study Period. Generated SAP implies only Whole Study Period shift tables.
- **reasoning:** Generated SAP defines worst post-baseline as 'observed during the Whole Study Period', omitting the per-period requirement.

#### 2. Period assignment logic

- **original SAP text:** If visit names are ‘Unscheduled’ or ‘EOT’, the post-baseline result of laboratory data will be presented by period, defined as follows... [Detailed logic for assigning EOT/Unscheduled to Induction/Maintenance/Follow-up periods based on infusion dates]
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Original SAP provides specific logic for assigning unscheduled/EOT data to study periods. Generated SAP omits this logic.
- **reasoning:** Generated SAP simplifies period summaries to 'scheduled visits' and omits the logic for assigning other data to periods.

#### 3. CTCAE Grade 5 exclusion

- **original SAP text:** The CTCAE Grade 5 (Death) will not be applied in this analysis since death cannot be determined from a laboratory result.
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Rule to exclude Grade 5 from lab analysis.
- **reasoning:** Specific grading rule omitted.

#### 4. Clinical input grade exclusion

- **original SAP text:** Grades that require clinical input only will not be assigned to these parameters. Grades which are part numeric and part clinical input will be assigned based on the numeric portion only.
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Rule to exclude grades requiring clinical input.
- **reasoning:** Specific grading rule omitted.

#### 5. No grade classification

- **original SAP text:** If the post-baseline result for a patient does not satisfy any CTCAE grade, it will be classified as ‘No grade’.
- **protocol text:** n/a
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Classification rule for results not meeting CTCAE criteria.
- **reasoning:** Specific classification rule omitted.


---

### Reverse Check (5 items)

#### 1. Item 1

- **original SAP statement:** The CTCAE Grade 5 (Death) will not be applied in this analysis since death cannot be determined from a laboratory result.
- **checked against elements:** ['CTCAE grading']
- **contradiction found:** no
- **explanation:** Generated SAP is silent on this exclusion.

#### 2. Item 2

- **original SAP statement:** Grades that require clinical input only will not be assigned to these parameters.
- **checked against elements:** ['CTCAE grading']
- **contradiction found:** no
- **explanation:** Generated SAP is silent on this exclusion.

#### 3. Item 3

- **original SAP statement:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized
- **checked against elements:** ['Coagulation and Urinalysis reporting']
- **contradiction found:** yes
- **contradicting element:** Coagulation and Urinalysis reporting
- **explanation:** Generated SAP restricts Coagulation and Urinalysis to listings only.

#### 4. Item 4

- **original SAP statement:** The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **checked against elements:** ['Coagulation and Urinalysis reporting']
- **contradiction found:** yes
- **contradicting element:** Coagulation and Urinalysis reporting
- **explanation:** Generated SAP restricts Urinalysis to listings only.

#### 5. Item 5

- **original SAP statement:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **checked against elements:** ['Worst post-baseline definition']
- **contradiction found:** no
- **explanation:** Generated SAP matches this logic.


---

### Reasoning

The Generated SAP is generally accurate regarding hematology and chemistry parameters and analysis methods (descriptive stats, shift tables, worst post-baseline logic). However, it explicitly contradicts the Original SAP regarding Coagulation and Urinalysis. The Original SAP requires summaries for numeric parameters and shift tables for non-numeric urinalysis, while the Generated SAP restricts these to 'listings only'. This is a reduction in safety reporting scope. Additionally, the Generated SAP omits the detailed logic for assigning unscheduled/EOT data to specific study periods (Induction vs Maintenance) and omits specific CTCAE grading rules (excluding Grade 5 and clinical input grades). These omissions are minor, but the contradiction regarding coagulation/urinalysis summaries is a clear deviation.

---

### Summary

The Generated SAP accurately captures the main hematology and chemistry analysis methods but contradicts the Original SAP by restricting coagulation and urinalysis to listings only, whereas the Original SAP requires summaries. It also omits detailed logic for assigning data to study periods and specific CTCAE grading rules.