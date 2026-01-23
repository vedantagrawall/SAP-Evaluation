## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Evaluation Summary Table

| Component | Evaluation Type | Matches Original SAP | Protocol Consulted | Result | Issue Type | Severity |
|-----------|-----------------|---------------------|-------------------|--------|------------|----------|
| Continuous data summary stats | semantic | yes |  | correct | none | none |
| Categorical data summary | semantic | yes |  | correct | none | none |
| EOT visit handling | semantic | no |  | problem | contradiction_original | minor |
| Unscheduled visit handling | semantic | no |  | problem | contradiction_original | minor |
| Listing content | semantic | yes |  | correct | none | none |
| Interim unblinding | semantic | yes |  | correct | none | none |
| ITT Definition | semantic | no |  | correct | none | none |
| PP Definition | semantic | yes |  | correct | none | none |
| PK Definition | semantic | yes |  | correct | none | none |
| PK Exclusion Rule | semantic | no |  | correct | none | none |
| Safety Definition | semantic | yes |  | correct | none | none |
| Baseline Definition | semantic | yes |  | correct | none | none |
| Post-baseline Definition | semantic | yes |  | correct | none | none |
| ORR Missing Handling | semantic | yes |  | correct | none | none |

---

### Issues Found

| Issue Type | Component | Description |
|------------|-----------|-------------|
| contradiction_original | EOT visit handling | Original SAP explicitly excludes EOT from visit summaries; Generated SAP explicitly maps EOT to cycle windows for inclusion. |
| contradiction_original | Unscheduled visit handling | Original SAP strictly excludes unscheduled visits from summaries; Generated SAP allows them if they fall within windows. |

---

### Extra Information Flagged

*No extra information flagged.*

---

### ✅ Acceptable Differences (31 items)
Content in Original SAP only (not in Protocol) - acceptable to omit.

| Component | Category | Original SAP Text |
|-----------|----------|-------------------|
| Min/Max decimal precision | decimal_precision_minmax | same number of decimal places as the raw data |
| Mean decimal precision | decimal_precision_mean | one more decimal place than the raw data |
| Median decimal precision | decimal_precision_median | one more decimal place than the raw data |
| SD decimal precision | decimal_precision_sd | two more decimal places than the raw data |
| Geometric mean precision | decimal_precision_geometric_mean | same precision as the mean |
| CV decimal precision | decimal_precision_cv | two more decimal places than the raw data |
| Percentage precision | percentage_precision | one decimal place |
| Percentage suppression | percentage_zero_handling | suppressed when the count is zero |
| Not Done row | not_done_row_handling | row denoted "Not Done" will be included |
| Percentage denominator | percentage_denominator | number of patients within the treatment group |
| Listing sort order 1 | listing_sort_order | sorted by the treatment group |
| Listing sort order 2 | listing_sort_order | then patient number |
| Listing sort order 3 | listing_sort_order | and visit, if applicable |
| Additional sorting | listing_sort_order | other variables will be included in sorting |
| Quant limit summary | quantification_limit_summary | set to the respective limit |
| Quant limit listing | quantification_limit_listing | original results containing inequality sign |
| Discrepancy handling 1 | data_discrepancy_handling | listing will display only sample collection visit |
| Discrepancy handling 2 | data_discrepancy_handling | display only specimen collection visit |
| Discrepancy handling 3 | data_discrepancy_handling | display results from analytical facility |
| Schedule generation | randomization_method | unblinded statistician will generate |
| PK Maintenance Def | population_other_subsets | PK population – Maintenance Period Subset |
| Safety actual treatment | population_safety | Any CT-P16 = CT-P16 |
| Major PD 1 | protocol_deviation_definition | Mis-randomizations |
| Major PD 2 | protocol_deviation_definition | Non-compliance of Inclusion or Exclusion |
| Major PD 3 | protocol_deviation_definition | Significant GCP non-compliance |
| Major PD 4 | protocol_deviation_definition | Receiving any prohibited therapies |
| Major PD 5 | protocol_deviation_definition | Missing primary efficacy assessment |
| PD summary population | protocol_deviation_definition | summarized by treatment group for the ITT |
| COVID-19 PD analysis | protocol_deviation_definition | excluding patients with major protocol deviation... |
| Outlier exclusion | outlier_handling | not be excluded unless they are considered to be erroneous |
| Tipping point analysis | sensitivity_analyses | tipping point analyses will be conducted |

---

### ❌ Missing Required Content (16 items)
Content in both Original SAP AND Protocol - should be in Generated SAP.

| Component | Category | Original SAP Text | Protocol Text |
|-----------|----------|-------------------|---------------|
| Sample size per group | sample_size_calculation | 305 patients per group | sample size of 305 patients per group |
| Expected ORR | sample_size_calculation | expected ORR of 38% | expected ORR of 38% |
| Equivalence margin | sample_size_calculation | equivalence margin of -12.5 to 12.5 | equivalence margin of (±12.5) |
| Alpha level | sample_size_calculation | two one-sided alpha 0.025 | two one-sided alpha 0.025 |
| Total enrollment | sample_size_calculation | Approximately 678 patients | Approximately 678 patients |
| Drop-out rate | sample_size_calculation | anticipated drop-out rate of 10% | anticipated drop-out rate of 10% |
| Randomization method | randomization_method | Interactive Web Response System (IWRS) | interactive voice response system (IVRS) |
| Randomization ratio | randomization_method | 1:1 ratio | 1:1 ratio |
| Randomization type | randomization_method | permuted blocks | permuted blocks |
| Stratification factor 1 | stratification_factors | country | country |
| Stratification factor 2 | stratification_factors | sex (female vs. male) | sex (female vs. male) |
| Stratification factor 3 | stratification_factors | disease status (recurrence vs. metastatic) | disease status (recurrence vs. metastatic) |
| Stratification factor 4 | stratification_factors | ECOG performance status (0 vs. 1) | ECOG performance score (0 vs. 1) |
| Blinding duration | blinding_procedure | double-blinded during both Induction... | double-blind... during the Whole Study Period |
| Unblinding timing | blinding_procedure | until all final clinical data have been entered | until all patients have completed the study |
| Investigator blinding | blinding_procedure | blinded to the investigators and patients | blinded to the investigators... until all patients |

---

### Reasoning

The Generated SAP is missing significant portions of the General Statistical Considerations found in the Original SAP, including sample size calculations, randomization details, and specific decimal precision rules. While some of these are missing because they are typically in the Protocol (and thus 'Missing Required'), the Generated SAP also introduces methodological contradictions regarding the handling of EOT and Unscheduled visits (mapping/including them vs Original SAP's exclusion). However, the Generated SAP correctly aligns with the Protocol on the ITT population definition, correcting a restriction found in the Original SAP. The rating is DECENT because the core population definitions are correct and aligned with the Protocol, but the missing operational details and minor data handling contradictions lower the quality.

---

### Summary

The Generated SAP aligns well with the Protocol for key population definitions but lacks significant operational detail found in the Original SAP (sample size, randomization, precision rules). It introduces minor contradictions in how EOT and unscheduled visits are handled in summaries.
