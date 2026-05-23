# Risk Register

<div class="cs-page-header">
  <div class="eyebrow">CSPM &mdash; Risk Register</div>
  <h1>Cloud security risk register</h1>
  <div class="sub">Tracked misconfigurations and security risks &mdash; business impact, likelihood, scores, and remediation status. Update this file directly to keep the register current.</div>
</div>

<div class="cs-stat-grid">
  <div class="cs-stat red"><div class="num">1</div><div class="lbl">Critical</div></div>
  <div class="cs-stat amber"><div class="num">1</div><div class="lbl">High</div></div>
  <div class="cs-stat blue"><div class="num">0</div><div class="lbl">Medium</div></div>
  <div class="cs-stat green"><div class="num">0</div><div class="lbl">Low</div></div>
</div>

---

## How to use this register

- **Stakeholder summary** — the table below shows the business view: what is at risk, how severe, and what is being done
- **Technical detail** — each risk has a detail section below the summary with controls, remediation, and compliance mapping
- **Updating** — edit this file directly on GitHub, or raise a GitHub Issue to request an update
- **Scoring** — Likelihood (1–5) × Impact (1–5) → Risk Score (1–5). See scoring guide at the bottom of this page.

---

## Stakeholder summary

> This view is for business and executive audiences. It focuses on what is at risk, the business consequence, and the current status.

| ID | Risk | Category | Business disruption | Financial exposure | Severity | Status | Owner |
|---|---|---|---|---|---|---|---|
| IAM-001 | Overprivileged IAM roles | IAM | Unauthorised access to production systems, potential data breach | High &gt; $500K | 🔴 **Critical** | Open | Cloud Platform Team |
| NET-001 | Publicly exposed security groups | Network | Unrestricted inbound access to workloads, potential service disruption | High &gt; $500K | 🔴 **Critical** | In Progress | Network Security Team |

---

## Technical detail

### IAM-001 — Overprivileged IAM Roles

<div class="cs-page-header" style="padding:14px 18px;">
  <div class="eyebrow">IAM &mdash; Critical &mdash; Open</div>
  <h1 style="font-size:1.1rem!important;">Multiple IAM roles have administrator-level permissions without business justification</h1>
</div>

| Field | Detail |
|---|---|
| **Risk ID** | IAM-001 (CSN: IAM-IDC-001) |
| **Category** | IAM |
| **Cloud environment** | AWS Production |
| **Affected assets** | IAM Roles, EC2, Lambda |
| **Data classification** | Highly Critical |
| **Likelihood** | High (4) |
| **Impact** | High (4) |
| **Risk score** | 4 / 5 — Critical |
| **Detection source** | Wiz |
| **Compliance mapping** | CIS 1.22, NIST AC-6 |
| **Existing controls** | MFA enabled, CloudTrail logging |
| **Recommended remediation** | Implement least privilege access and remove wildcard permissions |
| **Target date** | 2026-06-15 |
| **Risk treatment** | Mitigate |
| **Exception approved** | No |
| **Residual risk** | Medium |
| **Risk owner** | Cloud Platform Team |
| **Supporting team** | IAM Team |
| **Notes** | Review all cross-account roles |

**Business impact explained**

Overprivileged roles allow any compromised identity to escalate privileges and move laterally across the entire AWS environment. A single compromised credential could result in full environment takeover, data exfiltration, or ransomware deployment. Financial exposure includes breach notification costs, regulatory fines (GDPR/CCPA), incident response, and potential business disruption exceeding **$500K**.

---

### NET-001 — Publicly Exposed Security Groups

<div class="cs-page-header" style="padding:14px 18px;">
  <div class="eyebrow">Network &mdash; Critical &mdash; In Progress</div>
  <h1 style="font-size:1.1rem!important;">Security groups allow unrestricted inbound access from 0.0.0.0/0</h1>
</div>

| Field | Detail |
|---|---|
| **Risk ID** | NET-001 |
| **Category** | Network Security |
| **Cloud environment** | AWS Production |
| **Affected assets** | EC2 Security Groups |
| **Data classification** | Confidential |
| **Likelihood** | High (4) |
| **Impact** | High (4) |
| **Risk score** | 4 / 5 — Critical |
| **Detection source** | Wiz |
| **Compliance mapping** | CIS 4.1, NIST SC-7 |
| **Existing controls** | AWS Shield, WAF |
| **Recommended remediation** | Restrict inbound traffic and implement network segmentation |
| **Target date** | 2026-05-30 |
| **Risk treatment** | Mitigate |
| **Exception approved** | No |
| **Residual risk** | Low |
| **Risk owner** | Network Security Team |
| **Supporting team** | Cloud Engineering |
| **Notes** | Prioritise internet-facing assets first |

**Business impact explained**

Open security groups expose workloads directly to the internet with no IP restriction. Attackers can probe, brute force, or exploit any service running on affected instances. For production EC2 instances this creates direct risk of service disruption, data exfiltration, and regulatory non-compliance. Financial exposure includes incident response, downtime costs, and potential regulatory fines exceeding **$500K**.

---

## Mitigated risks

| ID | Risk | Category | Closed date | Resolution |
|---|---|---|---|---|
| — | No mitigated risks yet | — | — | — |

---

## Scoring guide

| Score | Likelihood | Meaning |
|---|---|---|
| 1 | Rare | May occur only in exceptional circumstances |
| 2 | Unlikely | Could occur at some time |
| 3 | Possible | Might occur at some time |
| 4 | Likely | Will probably occur in most circumstances |
| 5 | Almost Certain | Expected to occur in most circumstances |

| Score | Impact | Meaning |
|---|---|---|
| 1 | Negligible | No material impact |
| 2 | Minor | Minor operational impact, easily recovered |
| 3 | Moderate | Moderate business disruption, recoverable |
| 4 | Major | Significant business disruption, regulatory attention |
| 5 | Severe / Critical | Catastrophic impact, regulatory breach, financial loss |

| Risk score | Level | Action required |
|---|---|---|
| 1–2 | 🟢 Low | Monitor, review annually |
| 3 | 🟡 Medium | Remediate within 90 days |
| 4 | 🟠 High | Remediate within 30 days |
| 5 | 🔴 Critical | Immediate action required |

---

## Financial exposure bands

| Band | Estimated financial exposure | Examples |
|---|---|---|
| Low | < $50,000 | Minor operational disruption, no data involved |
| Medium | $50,000 – $500,000 | Customer data at risk, regulatory reporting required |
| High | > $500,000 | Data breach, production outage, regulatory fines |
| Critical | > $5,000,000 | Full environment compromise, class action, major regulatory breach |

---

*Last updated: May 2026 &middot; Maintained by Cloud Security &middot; Source of truth: this file*
