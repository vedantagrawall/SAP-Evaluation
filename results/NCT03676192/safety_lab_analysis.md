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
- **elements in missing from generated SAP:** 3
- **counts match:** True

---

### Evaluation Table (26 items)

#### 1. Laboratory Categories

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
- **reasoning:** Both documents list the same high-level categories.

#### 2. Sample Collection Schedule

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
- **reasoning:** Generated SAP references the schedule; Original SAP implies collection by mentioning analysis.

#### 3. Local Lab and Unit Standardization

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
- **reasoning:** Both specify local laboratory analysis and standardization of units.

#### 4. Hematology Parameters

- **evaluation type:** semantic
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
- **reasoning:** Original SAP 10.2 does not list parameters, but Generated SAP matches Protocol list exactly.

#### 5. Clinical Chemistry Parameters

- **evaluation type:** semantic
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
- **reasoning:** Original SAP 10.2 does not list parameters, but Generated SAP matches Protocol list exactly.

#### 6. Urinalysis Parameters

- **evaluation type:** semantic
- **generated SAP text:** Urinalysis: Bilirubin, blood, glucose, ketones, leukocytes, nitrite, pH, protein, specific gravity, and urobilinogen via dipstick.
- **protocol text:** Urinalysis: bilirubin, blood, glucose, ketones, leukocytes (white blood cells), nitrite, pH, protein, specific gravity, urobilinogen
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Original SAP 10.2 does not list parameters, but Generated SAP matches Protocol list exactly.

#### 7. Microscopic Urinalysis/24hr Urine

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
- **reasoning:** Both mention microscopic urinalysis.

#### 8. Coagulation Parameters

- **evaluation type:** semantic
- **original SAP text:** coagulation
- **generated SAP text:** Coagulation: Prothrombin time (PT) and prothrombin time international normalized ratio (INR) (for patients receiving aspirin).
- **protocol text:** Coagulation: ... should perform prothrombin time and prothrombin time international normalized ratio tests.
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP matches Protocol specifics.

#### 9. Baseline Definition

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
- **reasoning:** Generated SAP cross-references its own definition section.

#### 10. Post-baseline Summary Visits

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline... will be summarized... by... visit.
- **generated SAP text:** Post-baseline summaries will include all scheduled visits during the Induction Study Period (Cycles 1 through 6), Maintenance Study Period (Cycles 1 and every 3 cycles thereafter), and the End of Treatment (EOT) visit.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with visit-based summary requirement.

#### 11. Data Listings

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
- **reasoning:** Both require listings for all data.

#### 12. Summary Statistics (Hem/Chem)

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology... will be summarized using descriptive statistics
- **generated SAP text:** Summaries of actual values and change from baseline will be provided for hematology and clinical chemistry.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches requirement for Hem/Chem.

#### 13. Summary Statistics (Coag/Urine)

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized using descriptive statistics
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** none
- **omission impact:** none
- **result:** problem
- **issue type:** contradiction_original
- **severity:** minor
- **reasoning:** Original SAP explicitly requires summaries for numeric urinalysis and coagulation; Generated SAP explicitly excludes them.

#### 14. Descriptive Statistics Grouping

- **evaluation type:** exact_match
- **original SAP text:** summarized using descriptive statistics by treatment group, laboratory category, test parameter and visit.
- **generated SAP text:** Laboratory parameters will be summarized by treatment group and visit using descriptive statistics.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches grouping requirements.

#### 15. Actual and Change

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

#### 16. Scheduled Visits Only

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table. (Implies visit tables are scheduled only)
- **generated SAP text:** As established in Section 4.5, nominal visits will be used for these summaries. Only scheduled visits will be included in by-visit summaries.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP's handling of unscheduled visits.

#### 17. Toxicity Grading

- **evaluation type:** exact_match
- **original SAP text:** according to CTCAE version 5.0.
- **generated SAP text:** Laboratory abnormalities will be graded according to the National Cancer Institute (NCI) Common Terminology Criteria for Adverse Events (CTCAE) version 5.0, where applicable.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches version.

#### 18. Shift Table Methodology

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients with a result for each grade will be summarized... A shift table will be also produced... Only the most severe case... will be included for the post-baseline result in the shift table.
- **generated SAP text:** Shift tables will be used to summarize the number and percentage of patients by baseline category (Grade 0 through 4) versus the worst post-baseline category.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches the 'most severe case' (worst post-baseline) methodology.

#### 19. Worst Post-Baseline Definition

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
- **reasoning:** Matches inclusion of unscheduled visits for worst case.

#### 20. Non-CTCAE Shift Tables

- **evaluation type:** semantic
- **original SAP text:** Reported parameters with units that cannot be converted to standard units will be summarized separately using the original units.
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High) relative to the laboratory reference range versus the worst post-baseline category.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Original SAP is silent on L/N/H shift tables for numeric parameters; this is an acceptable methodological addition.

#### 21. High/Low Direction Analysis

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
- **reasoning:** Acceptable methodological detail.

#### 22. Treatment-Emergent Definition

- **evaluation type:** semantic
- **generated SAP text:** The number and percentage of patients with treatment-emergent laboratory abnormalities (defined as an increase in CTCAE grade from baseline) will be summarized by treatment group.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Acceptable definition for summarizing abnormalities.

#### 23. Grade 3/4 Focus

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients with a result for each grade will be summarized
- **generated SAP text:** Particular focus will be placed on Grade 3 or 4 abnormalities.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with standard reporting.

#### 24. Unscheduled Visit Exclusion

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table. (Implies exclusion from visit tables)
- **generated SAP text:** Unscheduled laboratory assessments will be excluded from by-visit summaries but will be included in the determination of the worst post-baseline values and in all listings.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches Original SAP logic.

#### 25. Multiple Values Handling

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
- **reasoning:** Standard data handling rule, not contradictory.

#### 26. Worst Value Determination

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
- **reasoning:** Matches Original SAP logic.

---

### Issues Found (1 items)

#### 1. Summary Statistics (Coag/Urine)

- **issue type:** contradiction_original
- **severity:** minor
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized using descriptive statistics
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **why they conflict:** Original SAP mandates summary statistics for coagulation and numeric urinalysis; Generated SAP explicitly restricts them to listings only.
- **description:** Generated SAP removes required summary analyses for coagulation and urinalysis.
- **reasoning:** Chain-of-thought: 1) Original SAP explicitly lists 'numeric urinalysis and coagulation' as parameters to be summarized with descriptive statistics. 2) Generated SAP explicitly states 'Coagulation and urinalysis results will be presented in data listings only.' 3) These statements are mutually exclusive. 4) This reduces the scope of safety reporting.

---

### Extra Information Flagged (2 items)

#### 1. Specific parameter lists

- **content:** Specific parameter lists
- **generated SAP text:** Lists of specific Hematology, Chemistry, and Urinalysis parameters
- **contradicts:** no
- **detail:** Matches Protocol 6.5.2.9
- **reasoning:** Original SAP 10.2 does not list parameters, but Generated SAP includes them correctly based on Protocol.

#### 2. Low/Normal/High Shift Tables

- **content:** Low/Normal/High Shift Tables
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High)...
- **contradicts:** no
- **detail:** Methodological addition
- **reasoning:** Original SAP is silent on this specific analysis for numeric parameters; it is a standard safety analysis addition.

---

### Missing from Generated SAP (3 items)

#### 1. Non-numeric Urinalysis Shift Table

- **original SAP text:** The results for all non-numeric urinalysis parameters including microscopic urinalysis collected as qualitative format will be categorized into normal and abnormal... and will be summarized in a shift table.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Original SAP requires shift tables for non-numeric urinalysis; Generated SAP puts them in listings only.
- **reasoning:** Generated SAP explicitly excludes this analysis.

#### 2. Shift Tables by Study Period

- **original SAP text:** A shift table will be also produced by the Whole Study Period and each study period.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Original SAP requires shift tables for each study period (Induction, Maintenance); Generated SAP only specifies Whole Study Period.
- **reasoning:** Generated SAP omits the requirement for period-specific shift tables.

#### 3. Grading Rule for Mixed Grades

- **original SAP text:** Grades which are part numeric and part clinical input will be assigned based on the numeric portion only.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific rule for assigning CTCAE grades based on numeric portion is missing.
- **reasoning:** Generated SAP omits this specific grading instruction.

---

### Reverse Check (5 items)

#### 1. Item 1

- **original SAP statement:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized
- **checked against elements:** ['Summary Statistics (Coag/Urine)']
- **contradiction found:** yes
- **contradicting element:** Summary Statistics (Coag/Urine)
- **explanation:** Generated SAP restricts coagulation and urinalysis to listings only.

#### 2. Item 2

- **original SAP statement:** The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **checked against elements:** ['Summary Statistics (Coag/Urine)']
- **contradiction found:** yes
- **contradicting element:** Summary Statistics (Coag/Urine)
- **explanation:** Generated SAP restricts urinalysis to listings only, contradicting the shift table requirement.

#### 3. Item 3

- **original SAP statement:** A shift table will be also produced by the Whole Study Period and each study period.
- **checked against elements:** ['Shift Table Methodology']
- **contradiction found:** no
- **explanation:** Generated SAP mentions Whole Study Period but is silent on 'each study period'. This is an omission, not a direct contradiction.

#### 4. Item 4

- **original SAP statement:** Grades that require clinical input only will not be assigned to these parameters.
- **checked against elements:** ['Toxicity Grading']
- **contradiction found:** no
- **explanation:** Generated SAP is silent on this rule.

#### 5. Item 5

- **original SAP statement:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **checked against elements:** ['Worst Post-Baseline Definition']
- **contradiction found:** no
- **explanation:** Generated SAP matches this logic.

---

### Reasoning

The Generated SAP accurately captures the majority of the clinical laboratory analysis requirements, including the use of CTCAE v5.0, handling of unscheduled visits, and descriptive statistics for hematology and chemistry. It correctly lists the specific parameters based on the Protocol. However, it explicitly contradicts the Original SAP regarding Coagulation and Urinalysis. The Original SAP requires descriptive statistics for numeric urinalysis and coagulation, and shift tables for non-numeric urinalysis. The Generated SAP restricts all urinalysis and coagulation data to listings only. Additionally, the Generated SAP omits the requirement for shift tables by 'each study period' (Induction, Maintenance), mentioning only the Whole Study Period. These are minor reductions in scope for safety reporting but constitute clear contradictions.

---

### Summary

The Generated SAP is largely accurate but contains a minor contradiction regarding the analysis of Coagulation and Urinalysis, restricting them to listings only despite the Original SAP requiring summaries. It also omits the requirement for period-specific shift tables.