## Safety Lab Analysis Evaluation

**Section:** safety_lab_analysis
**Rating:** POOR
**Status:** fail

---

### Extraction Validation

- **sections read:** 7.1.3, 7.1.3.1, 7.1.3.2, 7.1.3.3, 7.1.3.4, 7.1.3.5, 7.1.3.6
- **elements per section:** 7.1.3: 3, 7.1.3.1: 4, 7.1.3.2: 3, 7.1.3.3: 2, 7.1.3.4: 5, 7.1.3.5: 2, 7.1.3.6: 3
- **elements extracted:** 22
- **elements in evaluation table:** 22
- **elements in missing from generated SAP:** 5
- **counts match:** True

---

### Evaluation Table (22 items)

#### 1. Laboratory Categories

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized
- **generated SAP text:** Clinical laboratory assessments include hematology, clinical chemistry, urinalysis, and coagulation.
- **protocol text:** Clinical laboratory tests: hematology, clinical chemistry, urinalysis... Coagulation
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Both documents list the same four high-level categories.

#### 2. Sample Collection Reference

- **evaluation type:** semantic
- **generated SAP text:** Laboratory samples will be collected according to the Schedule of Assessments (Section 11.1).
- **protocol text:** Blood and urine samples for clinical laboratory assessments will be collected at the time points specified in the schedule of events (Table 11-1).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard reference to schedule.

#### 3. Local Lab and SI Units

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

#### 4. Hematology Parameters

- **evaluation type:** semantic
- **original SAP text:** The CTCAE terms and ranges for applicable parameters are listed in Appendix 14.2.
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
- **reasoning:** Generated SAP lists specific parameters which match the Protocol. Original SAP refers to Appendix 14.2 for terms; listing them explicitly is acceptable.

#### 5. Clinical Chemistry Parameters

- **evaluation type:** semantic
- **original SAP text:** The CTCAE terms and ranges for applicable parameters are listed in Appendix 14.2.
- **generated SAP text:** Clinical Chemistry: Albumin, alkaline phosphatase (ALP), alanine aminotransferase (ALT), aspartate aminotransferase (AST), blood urea nitrogen (BUN), calcium, chloride, creatine phosphokinase (CPK), creatine kinase-myocardial band (CK-MB) isoenzyme, total cholesterol, creatinine, creatinine clearance (CrCl)... gamma-glutamyl transferase (GGT), glucose, lactate dehydrogenase (LDH), triglyceride, high-density lipoprotein (HDL) cholesterol, phosphate, potassium, sodium, total bilirubin, direct bilirubin, total protein, and uric acid.
- **protocol text:** Clinical chemistry: albumin, alkaline phosphatase, alanine aminotransferase, aspartate aminotransferase, blood urea nitrogen, calcium, chloride, creatine phosphokinase, creatine kinase-myocardial band isoenzyme, total cholesterol, creatinine, CrCl... gamma-glutamyl transferase, glucose, lactate dehydrogenase, triglyceride, high-density lipoprotein cholesterol, phosphate, potassium, sodium, total bilirubin, direct bilirubin, total protein, uric acid
- **protocol consulted:** yes
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists specific parameters matching Protocol. Original SAP refers to Appendix 14.2.

#### 6. Urinalysis Parameters

- **evaluation type:** semantic
- **original SAP text:** The results for all non-numeric urinalysis parameters including microscopic urinalysis collected as qualitative format will be categorized into normal and abnormal... A row denoted “Not Done” will be included...
- **generated SAP text:** Urinalysis: Bilirubin, blood, glucose, ketones, leukocytes, nitrite, pH, protein, specific gravity, and urobilinogen via dipstick. Microscopic examination and 24-hour urine collection (for protein) will be performed if indicated.
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

#### 7. Coagulation Parameters

- **evaluation type:** semantic
- **original SAP text:** Coagulation (prothrombin time, prothrombin time international normalized ratio) test will be performed... for the patient who has been administered aspirin.
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
- **reasoning:** Matches Original SAP and Protocol.

#### 8. Baseline Definition

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
- **reasoning:** Cross-reference to Section 4.2 is acceptable.

#### 9. Post-baseline Summaries Scope

- **evaluation type:** semantic
- **original SAP text:** Laboratory data will be summarized in the Induction Study Period... Maintenance Study Period... Follow-Up Period...
- **generated SAP text:** Post-baseline summaries will include all scheduled visits during the Induction Study Period (Cycles 1 through 6), Maintenance Study Period (Cycles 1 and every 3 cycles thereafter), and the End of Treatment (EOT) visit.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** less_detailed
- **omitted content:** Specific logic for assigning EOT/Unscheduled visits to periods based on dates relative to infusion
- **omission impact:** low
- **result:** acceptable
- **issue type:** none
- **severity:** none
- **reasoning:** Generated SAP lists the periods but omits the complex logic for assigning data to these periods found in Original SAP 10.2.

#### 10. Data Listings

- **evaluation type:** semantic
- **original SAP text:** Clinical chemistry, hematology, urinalysis and coagulation data will be presented in separate listings...
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

#### 11. Hematology/Chemistry Summaries

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology... will be summarized using descriptive statistics...
- **generated SAP text:** Summaries of actual values and change from baseline will be provided for hematology and clinical chemistry.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches requirement for actual/change summaries.

#### 12. Coagulation/Urinalysis Summaries

- **evaluation type:** semantic
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including... numeric urinalysis and coagulation will be summarized... The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **protocol consulted:** n/a
- **matches original SAP:** no
- **detail level:** contradiction
- **omitted content:** Requirement to summarize numeric urinalysis/coagulation and provide shift tables for qualitative urinalysis
- **omission impact:** potential
- **result:** problem
- **issue type:** contradiction_original
- **severity:** critical
- **reasoning:** Original SAP explicitly requires summaries for numeric urinalysis and coagulation, and shift tables for qualitative urinalysis. Generated SAP explicitly restricts these to listings only.

#### 13. Descriptive Statistics

- **evaluation type:** semantic
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
- **reasoning:** Standard descriptive statistics requirement.

#### 14. Scheduled Visits Only

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table. (Implies unscheduled excluded from by-visit summaries)
- **generated SAP text:** Only scheduled visits will be included in by-visit summaries.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Consistent with Original SAP logic.

#### 15. CTCAE Grading

- **evaluation type:** semantic
- **original SAP text:** Clinical laboratory parameters for clinical chemistry, hematology and urinalysis will be labeled with a CTCAE term and grading will be applied... according to CTCAE version 5.0.
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
- **reasoning:** Matches version and requirement.

#### 16. Shift Tables (CTCAE)

- **evaluation type:** semantic
- **original SAP text:** The number and percentage of patients with a result for each grade will be summarized... A shift table will be also produced... The CTCAE Grade 5 (Death) will not be applied in this analysis...
- **generated SAP text:** Shift tables will be used to summarize the number and percentage of patients by baseline category (Grade 0 through 4) versus the worst post-baseline category.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches requirement for shift tables and grade range (0-4).

#### 17. Worst Post-Baseline Value

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **generated SAP text:** Worst post-baseline value is defined as the most extreme CTCAE grade observed during the Whole Study Period... including results from unscheduled assessments.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Matches definition of worst value including unscheduled.

#### 18. Shift Tables (Non-CTCAE)

- **evaluation type:** semantic
- **original SAP text:** The results for all non-numeric urinalysis parameters... will be categorized into normal and abnormal... and will be summarized in a shift table.
- **generated SAP text:** For parameters not covered by CTCAE grading, shift tables will cross-classify patients by baseline category (Low, Normal, High) relative to the laboratory reference range versus the worst post-baseline category.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** While Original SAP specifies Normal/Abnormal for urinalysis, the Generated SAP's Low/Normal/High for non-CTCAE is a standard expansion and not a contradiction, except for the urinalysis exclusion noted elsewhere.

#### 19. High/Low Direction Analysis

- **evaluation type:** semantic
- **generated SAP text:** Analyses will be performed separately for the 'High' and 'Low' directions when both are clinically relevant (e.g., potassium).
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Extra detail, consistent with standard practice.

#### 20. Treatment-Emergent Abnormalities

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
- **reasoning:** Extra analysis, not contradictory.

#### 21. Unscheduled Assessments Handling

- **evaluation type:** semantic
- **original SAP text:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
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

#### 22. Duplicate Assessment Handling

- **evaluation type:** semantic
- **generated SAP text:** If multiple laboratory values are collected on the same study day, the value collected closest to the scheduled assessment time will be used for by-visit summaries. For the determination of the worst post-baseline value, the most extreme value among all results (scheduled or unscheduled) for that day will be used.
- **protocol consulted:** n/a
- **matches original SAP:** yes
- **detail level:** match
- **omitted content:** none
- **omission impact:** none
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** Standard data handling rule, not contradictory.

---

### Issues Found (1 items)

#### 1. Coagulation and Urinalysis Summaries

- **issue type:** contradiction_original
- **severity:** critical
- **original SAP text:** Actual result and change from baseline of all numeric laboratory parameters including clinical chemistry, hematology, numeric urinalysis and coagulation will be summarized using descriptive statistics... The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **generated SAP text:** Coagulation and urinalysis results will be presented in data listings only.
- **why they conflict:** Original SAP requires summaries (actual/change) for numeric urinalysis and coagulation, and shift tables for qualitative urinalysis. Generated SAP explicitly restricts these to listings only.
- **description:** Generated SAP removes required analysis for coagulation and urinalysis.
- **reasoning:** Original SAP explicitly mandates summaries for these parameters. Generated SAP explicitly states they will be in 'listings only', which is a direct contradiction reducing the scope of analysis.

---

### Extra Information Flagged (4 items)

#### 1. Specific parameter lists

- **content:** Specific parameter lists
- **generated SAP text:** Clinical Chemistry: Albumin... [list]
- **contradicts:** no
- **reasoning:** Generated SAP lists specific parameters (e.g., CK-MB) not explicitly listed in Original SAP 10.2 text, but consistent with Protocol.

#### 2. High/Low Direction Analysis

- **content:** High/Low Direction Analysis
- **generated SAP text:** Analyses will be performed separately for the 'High' and 'Low' directions when both are clinically relevant
- **contradicts:** no
- **reasoning:** Standard analysis detail.

#### 3. Treatment-Emergent Abnormalities

- **content:** Treatment-Emergent Abnormalities
- **generated SAP text:** The number and percentage of patients with treatment-emergent laboratory abnormalities... will be summarized
- **contradicts:** no
- **reasoning:** Additional analysis not in Original SAP.

#### 4. Duplicate Handling

- **content:** Duplicate Handling
- **generated SAP text:** If multiple laboratory values are collected on the same study day...
- **contradicts:** no
- **reasoning:** Data handling rule not in Original SAP.

---

### Missing from Generated SAP (5 items)

#### 1. Unit Conversion Handling

- **original SAP text:** Reported parameters with units that cannot be converted to standard units will be summarized separately using the original units.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Handling of non-convertible units is missing.
- **reasoning:** Procedural detail not in Protocol.

#### 2. Clinical Input Grades

- **original SAP text:** Grades that require clinical input only will not be assigned to these parameters. Grades which are part numeric and part clinical input will be assigned based on the numeric portion only.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Rule for handling clinical input grades is missing.
- **reasoning:** Procedural detail not in Protocol.

#### 3. No Grade Classification

- **original SAP text:** If the post-baseline result for a patient does not satisfy any CTCAE grade, it will be classified as ‘No grade’.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Explicit classification for non-graded results is missing (though Grade 0 is used).
- **reasoning:** Procedural detail not in Protocol.

#### 4. Shift Tables by Period

- **original SAP text:** A shift table will be also produced by the Whole Study Period and each study period.
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Requirement for shift tables by 'each study period' is missing (only Whole Study Period mentioned).
- **reasoning:** Protocol requires safety summaries but doesn't specify shift tables by period.

#### 5. Period Assignment Logic

- **original SAP text:** If visit names are ‘Unscheduled’ or ‘EOT’, the post-baseline result of laboratory data will be presented by period, defined as follows... [detailed logic]
- **in protocol:** no
- **classification:** acceptable_difference
- **description:** Specific logic for assigning EOT/Unscheduled visits to periods is missing.
- **reasoning:** Procedural detail not in Protocol.

---

### Reverse Check (5 items)

#### 1. Item 1

- **original SAP statement:** The CTCAE Grade 5 (Death) will not be applied in this analysis since death cannot be determined from a laboratory result.
- **checked against elements:** ['Shift Tables (CTCAE)']
- **contradiction found:** no
- **explanation:** Generated SAP uses 'Grade 0 through 4', which aligns with the exclusion of Grade 5.

#### 2. Item 2

- **original SAP statement:** Only the most severe case during unscheduled and scheduled visits will be included for the post-baseline result in the shift table.
- **checked against elements:** ['Worst Post-Baseline Value']
- **contradiction found:** no
- **explanation:** Generated SAP includes unscheduled visits in worst post-baseline determination, which matches.

#### 3. Item 3

- **original SAP statement:** Grades that require clinical input only will not be assigned to these parameters.
- **checked against elements:** ['CTCAE Grading']
- **contradiction found:** no
- **explanation:** Generated SAP is silent on this, which is a missing detail but not a contradiction.

#### 4. Item 4

- **original SAP statement:** The results for all non-numeric urinalysis parameters... will be summarized in a shift table.
- **checked against elements:** ['Coagulation/Urinalysis Summaries']
- **contradiction found:** yes
- **contradicting element:** Coagulation/Urinalysis Summaries
- **explanation:** Generated SAP states urinalysis results will be presented in data listings only, contradicting the requirement for a shift table.

#### 5. Item 5

- **original SAP statement:** Actual result and change from baseline of all numeric laboratory parameters including... coagulation will be summarized...
- **checked against elements:** ['Coagulation/Urinalysis Summaries']
- **contradiction found:** yes
- **contradicting element:** Coagulation/Urinalysis Summaries
- **explanation:** Generated SAP states coagulation results will be presented in data listings only, contradicting the requirement for summaries.

---

### Reasoning

The Generated SAP generally follows the Original SAP for hematology and clinical chemistry, including CTCAE grading and shift tables. However, it introduces a critical contradiction regarding Urinalysis and Coagulation. The Original SAP explicitly requires summaries (actual/change) for numeric urinalysis and coagulation, and shift tables for qualitative urinalysis. The Generated SAP explicitly restricts these two categories to 'data listings only'. This significantly reduces the scope of analysis required by the Original SAP. Additionally, several procedural details regarding unit conversion, clinical input grades, and period assignment logic are missing.

---

### Summary

The Generated SAP fails to meet the requirements of the Original SAP due to a critical contradiction where required summaries for Coagulation and Urinalysis are replaced with 'listings only'. While Hematology and Clinical Chemistry are handled correctly, the exclusion of analysis for two major laboratory categories warrants a POOR rating.