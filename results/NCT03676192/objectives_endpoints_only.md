## Objectives Endpoints Only Evaluation

**Section:** objectives_endpoints
**Rating:** POOR
**Status:** fail

---

### Evaluation Summary Table

| Component | Evaluation Type | Matches Original SAP | Protocol Consulted | Result | Issue Type | Severity |
|-----------|-----------------|---------------------|-------------------|--------|------------|----------|
| Primary Objective | exact_match | yes | yes | correct | none | none |
| Secondary Objective - Efficacy | exact_match | yes | yes | correct | none | none |
| Secondary Objective - PK | exact_match | yes | yes | correct | none | none |
| Secondary Objective - Safety | exact_match | yes | yes | correct | none | none |
| Secondary Objective - QoL | exact_match | yes | yes | correct | none | none |
| Efficacy Endpoint Determination | semantic | yes | yes | correct | none | none |
| Confirmation of Response | semantic | yes | yes | correct | none | none |
| BOR Categories | semantic | yes | yes | correct | none | none |
| Primary Endpoint Definition | exact_match | yes | yes | correct | none | none |
| ORR Definition | semantic | yes | yes | correct | none | none |
| Secondary Endpoint - ORR Whole Study | exact_match | yes | yes | correct | none | none |
| Time-to-Event Analysis List | exact_match | yes | yes | correct | none | none |
| TTE Reporting Units | semantic | yes | no | correct | none | none |
| Days to Months Conversion | exact_match | no | no | problem | none | minor |
| Response Duration Definition | semantic | yes | yes | correct | none | none |
| Response Duration Event | semantic | yes | no | correct | none | none |
| Response Duration Censoring (No event) | semantic | yes | yes | correct | none | none |
| Response Duration Censoring (New therapy) | semantic | yes | yes | correct | none | none |
| Response Duration Censoring (Missing assessments) | semantic | yes | yes | correct | none | none |
| Response Duration Missing Exception | semantic | yes | yes | correct | none | none |
| Response Duration Formula | exact_match | no | no | problem | none | minor |
| TTP Definition | exact_match | yes | yes | correct | none | none |
| TTP Event | semantic | yes | no | correct | none | none |
| TTP Censoring (No assessment) | exact_match | no | yes | problem | none | minor |
| TTP Censoring (No event) | semantic | yes | yes | correct | none | none |
| TTP Censoring (New therapy) | semantic | yes | yes | correct | none | none |
| TTP Censoring (Missing assessments) | semantic | yes | yes | correct | none | none |
| TTP Missing Exception | semantic | yes | yes | correct | none | none |
| TTP Formula | exact_match | no | no | problem | none | minor |
| PFS Definition | exact_match | yes | yes | correct | none | none |
| PFS Event | semantic | yes | no | correct | none | none |
| PFS Censoring (No assessment) | exact_match | no | yes | problem | none | minor |
| PFS Censoring (No event) | semantic | yes | yes | correct | none | none |
| PFS Censoring (New therapy) | semantic | yes | yes | correct | none | none |
| PFS Censoring (Missing assessments) | semantic | yes | yes | correct | none | none |
| PFS Missing Exception | semantic | yes | yes | correct | none | none |
| PFS Formula | exact_match | no | no | problem | none | minor |
| OS Definition | exact_match | yes | yes | correct | none | none |
| OS Event | semantic | yes | no | correct | none | none |
| OS Censoring | exact_match | no | yes | problem | none | minor |
| OS Formula | exact_match | no | no | problem | none | minor |
| PK Parameter Definition | semantic | yes | yes | acceptable | none | none |
| PK Exclusion i | exact_match | no | no | problem | none | minor |
| PK Exclusion ii | exact_match | no | no | problem | none | minor |
| TEAE Definition | semantic | no | yes | problem | contradiction_original | minor |
| AESI 1 | exact_match | no | yes | problem | none | minor |
| AESI 2 | exact_match | no | yes | problem | none | minor |
| AESI 3 | exact_match | no | yes | problem | none | minor |
| AESI 4 | exact_match | no | yes | problem | none | minor |
| AESI 5 | exact_match | no | yes | problem | none | minor |
| AESI 6 | exact_match | no | yes | problem | none | minor |
| AESI 7 | exact_match | no | yes | problem | none | minor |
| AESI 8 | exact_match | no | yes | problem | none | minor |
| AESI 9 | exact_match | no | yes | problem | none | minor |
| AESI 10 | exact_match | no | yes | problem | none | minor |
| AESI 11 | exact_match | no | yes | problem | none | minor |
| Immunogenicity Assays | semantic | yes | yes | correct | none | none |
| ADA Transformation | exact_match | no | no | problem | none | minor |
| NAb Transformation | exact_match | no | no | problem | none | minor |
| QoL Instruments | exact_match | yes | yes | correct | none | none |
| QoL Raw Score Formula | exact_match | no | no | problem | none | minor |
| QoL Functional Score Formula | exact_match | no | no | problem | none | minor |
| QoL Symptom Score Formula | exact_match | no | no | problem | none | minor |

---

### Issues Found

| Issue Type | Severity | Component | Why They Conflict | Description |
|------------|----------|-----------|-------------------|-------------|
| contradiction_original | minor | TEAE Definition | Generated SAP defines TEAE only in the c | The definition of TEAE in the Generated  |

---

### Extra Information Flagged

*No extra information flagged.*

---

### Missing from Generated SAP (26 items)

| Component | Classification | In Protocol | Original SAP Text | Protocol Text | Reasoning |
|-----------|----------------|-------------|-------------------|---------------|-----------|
| Days to Months Conversion | acceptable_difference | no | Time-to-event in days will be converted to months by dividin... |  | Not in protocol, but standard SAP detail. |
| Response Duration Formula | acceptable_difference | no | Response duration (months) = ([Date of Event/Censoring – Dat... |  | Not in protocol, but standard SAP detail. |
| TTP Censoring (No tumor assessment) | missing_required | yes | Censoring will be defined as following: No tumor assessment ... | Any patient without any tumor assessment... | Required by protocol. |
| TTP Formula | acceptable_difference | no | TTP (months) = ([Date of Event/Censoring – Date of Randomiza... |  | Not in protocol, but standard SAP detail. |
| PFS Censoring (No tumor assessment) | missing_required | yes | Censoring will be defined as following: No tumor assessment ... | Any patient without any tumor assessment... | Required by protocol. |
| PFS Formula | acceptable_difference | no | PFS (months) = ([Date of Event/Censoring – Date of Randomiza... |  | Not in protocol, but standard SAP detail. |
| OS Censoring | missing_required | yes | Censoring will be defined as following: Non-death - Last kno... | for patients whose status is unknown, da... | Required by protocol. |
| OS Formula | acceptable_difference | no | OS (months) = ([Date of Event/Censoring – Date of Randomizat... |  | Not in protocol, but standard SAP detail. |
| PK Exclusion i | acceptable_difference | no | The samples in following cases are excluded from calculation... |  | Not in protocol. |
| PK Exclusion ii | acceptable_difference | no | The samples in following cases are excluded from calculation... |  | Not in protocol. |
| AESI 1 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | hypersensitivity/infusion-related reacti... | Required by protocol. |
| AESI 2 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | gastrointestinal perforations and fistul... | Required by protocol. |
| AESI 3 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | wound healing complications | Required by protocol. |
| AESI 4 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | hypertension | Required by protocol. |
| AESI 5 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | posterior reversible encephalopathy synd... | Required by protocol. |
| AESI 6 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | proteinuria | Required by protocol. |
| AESI 7 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | arterial thromboembolism (ATE) | Required by protocol. |
| AESI 8 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | venous thromboembolism (VTE) | Required by protocol. |
| AESI 9 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | hemorrhages | Required by protocol. |
| AESI 10 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | congestive heart failure (CHF) | Required by protocol. |
| AESI 11 | missing_required | yes | The following TEAEs will be considered as TEAEs of special i... | ovarian failure/fertility | Required by protocol. |
| ADA Transformation | acceptable_difference | no | The ADA value tagged assay will be transformed using a log t... |  | Not in protocol. |
| NAb Transformation | acceptable_difference | no | Transformed NAb value can be obtained using [log2(X/5)] + 1 ... |  | Not in protocol. |
| QoL Raw Score Formula | acceptable_difference | no | For all scales, the Raw Score (RS), is the mean of the compo... |  | Not in protocol. |
| QoL Functional Score Formula | acceptable_difference | no | Then for Functional scales: Score = {1 - (RS-1)/range} × 100 |  | Not in protocol. |
| QoL Symptom Score Formula | acceptable_difference | no | And for Symptom scales/items and Global health status/QoL: S... |  | Not in protocol. |

---

### Reasoning

The Generated SAP correctly identifies the primary and secondary objectives and endpoints. However, it lacks significant detail regarding specific calculations and definitions found in the Original SAP. Specifically, it misses the formulas for time-to-event calculations (days to months conversion), specific censoring rules for TTP and PFS (censoring at randomization for no assessment), and OS censoring rules. It also omits the list of Adverse Events of Special Interest (AESIs), which are explicitly listed in the Protocol and Original SAP. Furthermore, specific formulas for QoL scoring and immunogenicity data transformation are missing. While some of these are acceptable omissions if not in the protocol, the missing AESI list and censoring rules are critical omissions as they are protocol-required or standard analysis definitions.

---

### Summary

The Generated SAP provides a high-level overview of objectives and endpoints but lacks the necessary technical detail and specific definitions present in the Original SAP. Critical omissions include the list of Adverse Events of Special Interest and specific censoring rules for time-to-event analyses, which are required by the protocol.