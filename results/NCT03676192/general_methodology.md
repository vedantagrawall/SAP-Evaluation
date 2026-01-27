## General Methodology Evaluation

**Section:** general_methodology
**Rating:** DECENT
**Status:** pass_with_notes

---

### Evaluation Summary Table

| Component | Evaluation Type | Matches Original SAP | Protocol Consulted | Result | Issue Type | Severity |
|-----------|-----------------|---------------------|-------------------|--------|------------|----------|
| Descriptive statistics definition | exact_match | yes | yes | correct | none | none |
| Categorical data summary | exact_match | yes | yes | correct | none | none |
| Listing content | exact_match | yes | yes | correct | none | none |
| Stratification factors | exact_match | yes | yes | correct | none | none |
| Double-blind design | exact_match | yes | yes | correct | none | none |
| Unblinding for reporting | exact_match | yes | yes | correct | none | none |
| Blinding maintenance | exact_match | yes | yes | correct | none | none |
| ITT Definition | semantic | no | yes | correct | none | none |
| Treatment assignment (ITT) | exact_match | yes | yes | correct | none | none |
| Primary efficacy population | semantic | no | yes | problem | contradiction_original | minor |
| PP Definition | exact_match | yes | yes | correct | none | none |
| PP Determination timing | exact_match | yes | yes | correct | none | none |
| PK Definition | exact_match | yes | yes | correct | none | none |
| Safety Definition | exact_match | yes | yes | correct | none | none |
| Safety Assignment | exact_match | yes | yes | correct | none | none |
| Baseline definition | exact_match | yes | no | correct | none | none |
| Post-baseline definition | exact_match | yes | no | correct | none | none |
| Protocol Deviation Identification | exact_match | yes | no | correct | none | none |
| ORR Missing Handling | exact_match | yes | no | correct | none | none |
| NE Handling | exact_match | yes | no | correct | none | none |

---

### Issues Found

| Issue Type | Severity | Component | Why They Conflict | Description |
|------------|----------|-----------|-------------------|-------------|
| contradiction_original | minor | Primary efficacy decision criteria | Original SAP defines ITT as primary and  | Generated SAP elevates the Per-Protocol  |

---

### Extra Information Flagged

*No extra information flagged.*

---

### Missing from Generated SAP (54 items)

| Component | Classification | In Protocol | Original SAP Text | Protocol Text | Reasoning |
|-----------|----------------|-------------|-------------------|---------------|-----------|
| Decimal places (Min/Max) | acceptable_difference | no | Minimum and maximum will be presented to the same number of ... |  | Formatting detail missing. |
| Decimal places (Mean/Median) | acceptable_difference | no | mean and median will be presented to one more decimal place ... |  | Formatting detail missing. |
| Decimal places (SD) | acceptable_difference | no | standard deviation will be presented to two more decimal pla... |  | Formatting detail missing. |
| Decimal places (Geometric Mean) | acceptable_difference | no | If the geometric mean is to be presented, it will be set to ... |  | Formatting detail missing. |
| Decimal places (CV) | acceptable_difference | no | Percent coefficient of variation (CV) will be presented to t... |  | Formatting detail missing. |
| Decimal places (Percentages) | acceptable_difference | no | Percentages will be presented to one decimal place |  | Formatting detail missing. |
| Suppression of zero counts | acceptable_difference | no | and will be suppressed when the count is zero. |  | Formatting detail missing. |
| Not Done row | acceptable_difference | no | A row denoted “Not Done” will be included in count tabulatio... |  | Formatting detail missing. |
| Denominator definition | acceptable_difference | no | The denominator for all percentages will be the number of pa... |  | Formatting detail missing. |
| Listing sorting | acceptable_difference | no | Listings will be sorted by the treatment group and then pati... |  | Formatting detail missing. |
| Additional sorting | acceptable_difference | no | In cases where more additional sorting is required, other va... |  | Formatting detail missing. |
| LOQ handling | acceptable_difference | no | For the purpose of summarization, any numeric values recorde... |  | Formatting detail missing. |
| Inequality signs in listings | acceptable_difference | no | In listings, original results containing inequality sign wil... |  | Formatting detail missing. |
| Discrepancy handling 1 | acceptable_difference | no | Recorded as collected sample in eCRF but no corresponding re... |  | Data handling detail missing. |
| Discrepancy handling 2 | acceptable_difference | no | No corresponding records in eCRF for results from analytical... |  | Data handling detail missing. |
| Discrepancy handling 3 | acceptable_difference | no | Discrepancy in sample collection date from eCRF and analytic... |  | Data handling detail missing. |
| Discrepancy handling 4 | acceptable_difference | no | if sample collection date/time is missing in eCRF then use s... |  | Data handling detail missing. |
| Sample size calculation | missing_required | yes | A sample size of 305 patients per group will provide 80% pow... | A sample size of 305 patients per group ... | Sample size calculation details missing from Gener... |
| Total enrollment | missing_required | yes | Approximately 678 patients (339 in each group) will need to ... | Approximately 678 patients (339 in each ... | Total enrollment details missing from Generated SA... |
| IWRS | missing_required | yes | An Interactive Web Response System (IWRS) will be used for t... | An interactive voice response system (IV... | Randomization system details missing. |
| Unblinded statistician | acceptable_difference | no | and an unblinded statistician will generate a computer-gener... |  | Specific role detail missing. |
| Randomization ratio | missing_required | yes | Patients who qualify for randomization will be randomly assi... | randomly assigned in a 1:1 ratio | Randomization ratio missing. |
| Permuted blocks | missing_required | yes | The randomization will be balanced by using permuted blocks | balanced by using permuted blocks | Randomization method missing. |
| Code secrecy | missing_required | yes | The randomization code will not be revealed to study patient... | The randomization codes will not be reve... | Blinding maintenance details missing. |
| Population tabulation | acceptable_difference | no | The number of patients in each population will be tabulated ... |  | Reporting detail missing. |
| Population listing | acceptable_difference | no | A listing will also be provided displaying this data. |  | Reporting detail missing. |
| Full dose definition | acceptable_difference | no | A patient will be considered as receiving full dose if the p... |  | Specific definition of 'full dose' missing. |
| Supportive analysis (PP) | acceptable_difference | no | A supportive efficacy analysis will be repeated using the PP... |  | Generated SAP elevates PP to co-primary (see issue... |
| Incorrect treatment exclusion (PK) | acceptable_difference | no | Patients who received incorrect treatment during the Inducti... |  | Exclusion criteria missing. |
| PK Maintenance Subset Definition | acceptable_difference | no | The PK population – Maintenance Period Subset will consist o... |  | Population subset missing. |
| PK Maintenance Subset Exclusion | acceptable_difference | no | Patients who received incorrect treatment during the Mainten... |  | Population subset missing. |
| PK Maintenance Subset DRM | acceptable_difference | no | If a patient does not receive full dose, the patient will be... |  | Population subset missing. |
| PK Maintenance Subset Assignment | acceptable_difference | no | Patients will be assigned to treatment groups based on treat... |  | Population subset missing. |
| Received definition (Safety) | acceptable_difference | no | A patient will be considered to have received study drug if ... |  | Specific definition missing. |
| Kit number | acceptable_difference | no | Treatment patients actually received will be based on the ki... |  | Data source detail missing. |
| CT-P16 assignment rule | acceptable_difference | no | Patients receiving at least one dose of CT-P16 will be analy... |  | Specific assignment rule missing. |
| Avastin assignment rule | acceptable_difference | no | All other patients will be analyzed under the EU-Approved Av... |  | Specific assignment rule missing. |
| Major Protocol Deviation Definition | missing_required | yes | A major protocol deviation is one that may affect the interp... | A major protocol deviation is one that m... | Definition of Major Protocol Deviations missing (P... |
| Mis-randomization PD | acceptable_difference | no | Major protocol deviations include the following: Mis-randomi... |  | Specific PD missing. |
| IE Criteria PD | acceptable_difference | no | Non-compliance of Inclusion or Exclusion criteria |  | Specific PD missing. |
| GCP PD | acceptable_difference | no | Significant Good Clinical Practice (GCP) non-compliance (to ... |  | Specific PD missing. |
| Prohibited Therapy PD | acceptable_difference | no | Receiving any prohibited therapies (Section 5.10 of protocol... |  | Specific PD missing. |
| Missing Efficacy PD | acceptable_difference | no | Missing primary efficacy assessment |  | Specific PD missing. |
| PD Summary/Listing | acceptable_difference | no | The major protocol deviations will be summarized by treatmen... |  | Reporting detail missing. |
| COVID-19 PD | acceptable_difference | no | Additionally, if any case of major protocol deviation relate... |  | COVID-19 handling missing. |
| General Comments Listing | acceptable_difference | no | Data collected on the ‘General Comments’ eCRF page will be p... |  | Listing missing. |
| Outlier Investigation | acceptable_difference | no | Any outliers that are detected during the review of the data... |  | Process missing. |
| Outlier Exclusion | acceptable_difference | no | In general, outliers will not be excluded unless they are co... |  | Process missing. |
| Outlier Sensitivity | acceptable_difference | no | Sensitivity analyses and exploratory analyses may be conduct... |  | Process missing. |
| Tipping point analysis | acceptable_difference | no | In order to evaluate the impact of missing data on the prima... |  | Sensitivity analysis missing. |
| MNAR scenarios | acceptable_difference | no | Tipping point analyses will be conducted under Missing Not a... |  | Sensitivity analysis missing. |
| Shift imputation | acceptable_difference | no | Imputation will be done by gradually shifting the number of ... |  | Sensitivity analysis missing. |
| Exact binomial/Shift table | acceptable_difference | no | 95% CI of the difference between two proportions (CT-P16 and... |  | Sensitivity analysis missing. |
| 2D plot | acceptable_difference | no | All the scenarios will be also provided using 2-dimensional ... |  | Sensitivity analysis missing. |

---

### Internal Contradictions (0 items)

*No internal contradictions found.*

---

### Reasoning

The Generated SAP generally aligns with the Original SAP and Protocol regarding populations and blinding. However, it introduces a stricter decision criterion for the primary endpoint by requiring equivalence in both ITT and PP populations, whereas the Original SAP designates PP as supportive. Additionally, the Generated SAP fails to include several required elements found in the Protocol, such as sample size calculations, randomization details (IWRS, ratio, blocks), and the definition of major protocol deviations (which the Protocol explicitly delegates to the SAP).

---

### Summary

The Generated SAP is decent but has notable omissions and one methodological contradiction. It fails to define Major Protocol Deviations despite the Protocol delegating this task to the SAP. It also omits required sample size and randomization details found in the Protocol.