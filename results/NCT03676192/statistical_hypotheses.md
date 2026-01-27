## Statistical Hypotheses Evaluation

**Section:** statistical_hypotheses
**Rating:** GREAT
**Status:** pass

---

### Extraction Validation

- **sections evaluated:** 3.7, 3.7.1, 3.7.5, 3.7.6
- **components extracted:** 4
- **components in evaluation table:** 2
- **components in missing from generated SAP:** 0
- **components in extra information flagged:** 2
- **counts match:** True

---

### Evaluation Table (2 items)

#### 1. Primary Objective Definition

- **evaluation type:** semantic
- **original SAP text:** To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) during the Induction Study Period
- **generated SAP text:** The primary objective of this study is to demonstrate that CT-P16 is similar to EU-Approved Avastin in terms of efficacy, as determined by the objective response rate (ORR) up to Cycle 6 during the Induction Study Period.
- **protocol text:** To demonstrate CT-P16 is similar to EU-Approved Avastin in terms of efficacy as determined by objective response rate (ORR) up to Cycle 6 during the Induction Study Period
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Generated SAP accurately reflects the primary objective stated in the Original SAP Section 2.1 and Protocol Section 2.1.

#### 2. Equivalence Criteria

- **evaluation type:** semantic
- **original SAP text:** The similarity criterion has been set such that the confidence limits of the 95% CI of the difference in ORR from each treatment group will be entirely bounded by the interval (-12.5, 12.5).
- **generated SAP text:** Therapeutic similarity will be concluded if the 95% confidence interval (CI) for the difference in ORR (CT-P16 minus EU-Approved Avastin) is entirely contained within the predefined equivalence margin of (-12.5%, 12.5%).
- **protocol text:** The similarity criterion has been set such that the confidence limits of the 95% CI of the difference in ORR will be entirely bounded by the interval (-12.5, 12.5).
- **protocol consulted:** yes
- **matches original SAP:** yes
- **result:** correct
- **issue type:** none
- **severity:** none
- **reasoning:** The Generated SAP correctly identifies the equivalence margin (-12.5%, 12.5%) and the statistical method (95% CI of the difference) found in Original SAP Section 8.1.

---

### Issues Found (0 items)

*No issues found.*

---

### Extra Information Flagged (2 items)

#### 1. Multiplicity Adjustment Statement

- **content:** Multiplicity Adjustment Statement
- **generated SAP text:** As there is only one primary endpoint and one primary comparison for the demonstration of similarity, no multiplicity adjustments are required for the primary analysis.
- **protocol text:** A sample size of 305 patients per group will provide 80% power to show similarity... using a 95% CI (two one-sided alpha 0.025) of the difference in ORR.
- **contradicts:** no
- **detail:** Original SAP is silent on explicit multiplicity statements but implies a single primary endpoint. Protocol sample size calculation confirms single endpoint design without adjustment. Generated SAP statement is correct and good practice.
- **reasoning:** Original SAP does not explicitly state 'no multiplicity', but the design (single primary endpoint) implies it. Protocol Section 7.3 confirms the statistical power is based on a single comparison. Therefore, the Generated SAP's explicit statement is accurate and helpful.

#### 2. Interim Analysis Statement

- **content:** Interim Analysis Statement
- **generated SAP text:** No interim analyses for the purpose of early termination for efficacy or futility are planned.
- **protocol text:** No interim analyses are planned for this study.
- **contradicts:** no
- **detail:** Original SAP outlines a reporting schedule (1st, 2nd, 3rd CSR) but is silent on 'interim analyses for early termination'. Protocol Section 7.6.7 explicitly states no interim analyses are planned. Generated SAP matches Protocol.
- **reasoning:** While the Original SAP mentions multiple reporting points (CSRs), it does not describe them as interim analyses with stopping boundaries. The Protocol explicitly negates planned interim analyses. The Generated SAP correctly captures this distinction.

---

### Missing from Generated SAP (0 items)

*No missing from generated sap.*

---

### Reasoning

The Generated SAP accurately captures the primary objective and equivalence criteria from the Original SAP. It includes explicit statements regarding multiplicity and interim analyses which, while not present in the Original SAP text, are confirmed by the Protocol and the study design (single primary endpoint, no stopping boundaries). These additions represent good statistical reporting practice.

---

### Summary

The Generated SAP correctly defines the primary hypothesis and equivalence margins (-12.5%, 12.5%) matching the Original SAP. It appropriately adds clarification regarding the absence of multiplicity adjustments and interim analyses for early termination, which is consistent with the Protocol.