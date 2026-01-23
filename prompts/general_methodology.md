## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Evaluation Summary Table

| Component | Evaluation Type | Matches Original SAP | Protocol Consulted | Result | Issue Type | Severity |
|-----------|-----------------|---------------------|-------------------|--------|------------|----------|
| ITT Population Definition | semantic | no |  | correct | none | none |
| PP Population Definition | semantic | yes |  | correct | none | none |
| Safety Population Definition | semantic | yes |  | correct | none | none |
| PK Population Definition | semantic | yes |  | correct | none | none |
| Baseline Definition | semantic | yes |  | correct | none | none |
| Missing Data (Primary Endpoint) | semantic | yes |  | correct | none | none |
| EOT Visit Handling | semantic | no |  | problem | contradiction_original | minor |
| Unscheduled Visit Handling | semantic | no |  | problem | contradiction_original | minor |
| Software Version | semantic | no |  | correct | none | none |
| Stratification Factors | semantic | yes |  | correct | none | none |
| Safety Assignment Rule | semantic | no |  | correct | none | none |

---

### Issues Found

| Issue Type | Component | Description |
|------------|-----------|-------------|
| contradiction_original | EOT Visit Handling | Original SAP excludes EOT from visit summaries by default; Generated SAP maps it to cycles. |
| contradiction_original | Unscheduled Visit Handling | Original SAP excludes unscheduled visits by default; Generated SAP includes them if closest to target. |

---

### Extra Information Flagged

| Content | Contradicts | Detail |
|---------|-------------|--------|
| Software Version |  | Generated SAP specifies software version where Original was silent. |

---

### ✅ Acceptable Differences (38 items)

Content in Original SAP only (not in Protocol) - acceptable to omit.

| Component | Category | Original SAP Text |
|-----------|----------|-------------------|
| Tipping Point Analysis | sensitivity_analyses | additional analyses with tipping point analyses wi |
| Decimal Precision (Mean) | decimal_precision_mean | mean... will be presented to one more decimal plac |
| Decimal Precision (Median) | decimal_precision_median | median will be presented to one more decimal place |
| Decimal Precision (SD) | decimal_precision_sd | standard deviation will be presented to two more d |
| Decimal Precision (Min/Max) | decimal_precision_minmax | Minimum and maximum will be presented to the same  |
| Decimal Precision (GeoMean) | decimal_precision_geometric_mean | geometric mean... set to the same precision as the |
| Decimal Precision (CV) | decimal_precision_cv | Percent coefficient of variation (CV) will be pres |
| Percentage Precision | percentage_precision | Percentages will be presented to one decimal place |
| Percentage Suppression | percentage_zero_handling | suppressed when the count is zero |
| Not Done Row | not_done_row_handling | A row denoted 'Not Done' will be included... where |
| Percentage Denominator | percentage_denominator | denominator... will be the number of patients with |
| Listing Sort Order | listing_sort_order | sorted by the treatment group and then patient num |
| Quantification Limit (Low) | quantification_limit_summary | values recorded below the lower limit... set to th |
| Quantification Limit (High) | quantification_limit_summary | values... above the upper limit... set to the resp |
| Inequality Signs in Listings | listing_inequality_signs | original results containing inequality sign will b |
| Data Discrepancy (eCRF only) | data_discrepancy_handling | listing will display only sample collection visit/ |
| Data Discrepancy (Lab only) | data_discrepancy_handling | listing will display only specimen collection visi |
| Data Discrepancy (Date) | data_discrepancy_handling | listing will display results from analytical facil |
| PK Maintenance Subset | population_other_subsets | PK population - Maintenance Period Subset |
| Post-Baseline Definition | post_baseline_definition | all visits after the first infusion |
| Major Deviation (Mis-randomization) | protocol_deviation_definition | Mis-randomizations |
| Major Deviation (Inc/Exc) | protocol_deviation_definition | Non-compliance of Inclusion or Exclusion criteria |
| Major Deviation (GCP) | protocol_deviation_definition | Significant Good Clinical Practice (GCP) non-compl |
| Major Deviation (Prohibited) | protocol_deviation_definition | Receiving any prohibited therapies |
| Major Deviation (Missing Efficacy) | protocol_deviation_definition | Missing primary efficacy assessment |
| COVID-19 Deviations | protocol_deviation_definition | primary analysis will be performed excluding patie |
| General Comments Listing | listing_sort_order | Data collected on the 'General Comments' eCRF page |
| Outlier Handling | outlier_handling | outliers will not be excluded unless they are cons |
| Screening Failure Summary | population_other_subsets | number of screening failures and the primary reaso |
| Disposition Summary | population_other_subsets | number of patients who have been randomized... ini |
| Demographics Summary | population_other_subsets | Age... Fertility... Race... Ethnicity... Smoking.. |
| Gene Screening Summary | population_other_subsets | table and listing of gene screening will be provid |
| Viral Serology Summary | population_other_subsets | Viral serology will be summarized by treatment gro |
| Medical History Summary | population_other_subsets | Medical history will be summarized by treatment gr |
| Disease Characteristic Summary | population_other_subsets | Disease characteristic will be displayed in a summ |
| Previous Treatment Summary | population_other_subsets | Previous treatment for NSCLC will be summarized |
| Inc/Exc Criteria Listing | population_other_subsets | listing of the inclusion and exclusion criteria... |
| Medication Summary | population_other_subsets | Prior and concomitant medication data will be pres |

---

### ❌ Missing Required Content (6 items)

Content in both Original SAP AND Protocol - should be in Generated SAP.

| Component | Category | Original SAP Text | Protocol Text |
|-----------|----------|-------------------|---------------|
| Sample Size | sample_size_calculation | Sample size of 305 patients per group... | Sample size of 305 patients per group... |
| Randomization System | randomization_method | Interactive Web Response System (IWRS) | IVRS or IWRS |
| Randomization Ratio | randomization_method | 1:1 ratio | 1:1 ratio |
| Randomization Method | randomization_method | permuted blocks | permuted blocks |
| Blinding Procedure | blinding_procedure | double-blinded... randomization code wil | double-blind... randomization codes will |
| Unblinding for Reporting | blinding_procedure | database will be unblinded for the 1st C | unblinded... after the completion of Cyc |

---

### Reasoning

The Generated SAP is generally consistent with the Original SAP in terms of core methodology (populations, endpoints, primary analysis method). However, there are two notable contradictions regarding the handling of EOT and Unscheduled visits in summaries (Original excludes, Generated maps/includes). Additionally, the Sample Size calculation, which is a required element present in the Protocol, is missing from the Generated SAP. The ITT definition in the Generated SAP correctly matches the Protocol, whereas the Original SAP had added an extra constraint ('successfully screened'), so this difference is actually a correction. The missing formatting/precision rules are acceptable differences.

---

### Summary

The Generated SAP correctly defines populations and primary analysis methods, aligning well with the Protocol. However, it contradicts the Original SAP's specific instructions for handling EOT and unscheduled visits in summaries and omits the required Sample Size calculation.