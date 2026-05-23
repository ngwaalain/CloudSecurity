# Risk Register

<div class="cs-page-header">
  <div class="eyebrow">CSPM &mdash; Risk Register</div>
  <h1>Cloud Security Risk Register</h1>
  <div class="sub">Business impact, likelihood, financial exposure, and remediation status for all tracked cloud security risks.</div>
</div>

<div class="cs-stat-grid">
  <div class="cs-stat red"><div class="num">2</div><div class="lbl">Critical</div></div>
  <div class="cs-stat amber"><div class="num">0</div><div class="lbl">High</div></div>
  <div class="cs-stat blue"><div class="num">0</div><div class="lbl">Medium</div></div>
  <div class="cs-stat green"><div class="num">0</div><div class="lbl">Low</div></div>
</div>

<div class="rr-sections">

<!-- ══ SECTION 1: OVERVIEW ══════════════════════════════════════════════ -->
<div class="rr-section" id="rr-overview">
  <div class="rr-section-header" onclick="rrToggle('rr-overview')">
    <div class="rr-section-left">
      <div class="rr-section-icon" style="background:#EDE0CC;color:#8B5A2B;">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><circle cx="9" cy="9" r="6" stroke="currentColor" stroke-width="1.4"/><path d="M9 8v4M9 6v.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </div>
      <div>
        <div class="rr-section-title">Overview</div>
        <div class="rr-section-sub">What is a risk register &middot; how to read it &middot; audience guide</div>
      </div>
    </div>
    <div class="rr-chevron" id="chev-rr-overview">&#9662;</div>
  </div>
  <div class="rr-section-body" id="body-rr-overview">
    <div class="rr-overview-grid">
      <div class="rr-overview-card">
        <div class="rr-ov-icon" style="background:#EDE0CC;color:#8B5A2B;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><rect x="3" y="3" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M6 7h8M6 10h8M6 13h5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
        </div>
        <div class="rr-ov-title">What is a risk register?</div>
        <div class="rr-ov-body">A structured record of identified security risks — what could go wrong, how likely it is, what the business impact would be, and what we are doing about it. It is the single source of truth for cloud security risk posture.</div>
      </div>
      <div class="rr-overview-card">
        <div class="rr-ov-icon" style="background:#E1F5EE;color:#085041;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M10 2L16 5V10Q16 15 10 17Q4 15 4 10V5Z" stroke="currentColor" stroke-width="1.4"/><path d="M7 10l2 2 4-4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="rr-ov-title">For stakeholders</div>
        <div class="rr-ov-body">The <strong>Stakeholder Summary</strong> section shows risks in business language — what is at risk, the financial exposure, and current status. No technical knowledge required. This is the view for leadership and business owners.</div>
      </div>
      <div class="rr-overview-card">
        <div class="rr-ov-icon" style="background:#EEEDFE;color:#3C3489;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><rect x="2" y="4" width="16" height="12" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M6 8l2 2-2 2M10 12h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="rr-ov-title">For technical teams</div>
        <div class="rr-ov-body">The <strong>Technical Detail</strong> section contains controls, compliance mapping, remediation steps, detection source, and residual risk per finding. This is the working view for Cloud Security, Platform, and IAM teams.</div>
      </div>
      <div class="rr-overview-card">
        <div class="rr-ov-icon" style="background:#FAEEDA;color:#633806;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M10 3v7M10 14v.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.4"/></svg>
        </div>
        <div class="rr-ov-title">How to update</div>
        <div class="rr-ov-body">Edit this file directly on GitHub at <code>docs/cspm/risk-register/index.md</code> and commit to <code>main</code>. Changes are live within 60 seconds. To add a new risk, copy an existing risk block and update the fields.</div>
      </div>
    </div>
  </div>
</div>

<!-- ══ SECTION 2: STAKEHOLDER SUMMARY ══════════════════════════════════ -->
<div class="rr-section" id="rr-stakeholder">
  <div class="rr-section-header" onclick="rrToggle('rr-stakeholder')">
    <div class="rr-section-left">
      <div class="rr-section-icon" style="background:#FCEBEB;color:#791F1F;">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9 2L15 5V9Q15 13.5 9 16Q3 13.5 3 9V5Z" stroke="currentColor" stroke-width="1.4"/><path d="M6 9l2 2 4-4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <div>
        <div class="rr-section-title">Stakeholder summary</div>
        <div class="rr-section-sub">Business view &middot; financial exposure &middot; disruption impact &middot; status</div>
      </div>
    </div>
    <div class="rr-section-badges">
      <span class="rr-badge rr-badge-critical">2 Critical</span>
      <span class="rr-badge rr-badge-open">1 Open</span>
      <span class="rr-badge rr-badge-progress">1 In Progress</span>
    </div>
    <div class="rr-chevron" id="chev-rr-stakeholder">&#9662;</div>
  </div>
  <div class="rr-section-body" id="body-rr-stakeholder">
    <p style="font-size:.8rem;color:#C49A6C;margin-bottom:14px;font-style:italic;">This view is for business and executive audiences. It focuses on what is at risk, the business consequence, and current remediation status.</p>

    <div class="rr-risk-card rr-critical">
      <div class="rr-risk-header">
        <div class="rr-risk-id">IAM-001</div>
        <div class="rr-risk-name">Overprivileged IAM Roles</div>
        <span class="rr-severity rr-sev-critical">&#128308; Critical</span>
        <span class="rr-status rr-status-open">Open</span>
      </div>
      <div class="rr-risk-meta-row">
        <div class="rr-meta-item"><div class="rr-meta-label">Category</div><div class="rr-meta-val">IAM</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Environment</div><div class="rr-meta-val">AWS Production</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Financial exposure</div><div class="rr-meta-val rr-financial">High &gt; $500K</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Target date</div><div class="rr-meta-val">2026-06-15</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Owner</div><div class="rr-meta-val">Cloud Platform Team</div></div>
      </div>
      <div class="rr-impact-box">
        <div class="rr-impact-label">&#9888; Business disruption</div>
        <div class="rr-impact-text">Multiple IAM roles have administrator-level permissions without business justification. A single compromised credential could result in full environment takeover, data exfiltration, or ransomware deployment — affecting all cloud-hosted production workloads. Financial exposure includes breach notification, regulatory fines (GDPR/CCPA), incident response, and business disruption exceeding <strong>$500K</strong>.</div>
      </div>
    </div>

    <div class="rr-risk-card rr-critical">
      <div class="rr-risk-header">
        <div class="rr-risk-id">NET-001</div>
        <div class="rr-risk-name">Publicly Exposed Security Groups</div>
        <span class="rr-severity rr-sev-critical">&#128308; Critical</span>
        <span class="rr-status rr-status-progress">In Progress</span>
      </div>
      <div class="rr-risk-meta-row">
        <div class="rr-meta-item"><div class="rr-meta-label">Category</div><div class="rr-meta-val">Network Security</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Environment</div><div class="rr-meta-val">AWS Production</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Financial exposure</div><div class="rr-meta-val rr-financial">High &gt; $500K</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Target date</div><div class="rr-meta-val">2026-05-30</div></div>
        <div class="rr-meta-item"><div class="rr-meta-label">Owner</div><div class="rr-meta-val">Network Security Team</div></div>
      </div>
      <div class="rr-impact-box">
        <div class="rr-impact-label">&#9888; Business disruption</div>
        <div class="rr-impact-text">Security groups allow unrestricted inbound access from 0.0.0.0/0. Internet-facing workloads are directly exposed to scanning, brute force, and exploitation. For production EC2 instances this creates risk of service disruption, data exfiltration, and regulatory non-compliance. Financial exposure includes incident response, downtime, and potential fines exceeding <strong>$500K</strong>.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══ SECTION 3: TECHNICAL DETAIL ═════════════════════════════════════ -->
<div class="rr-section" id="rr-technical">
  <div class="rr-section-header" onclick="rrToggle('rr-technical')">
    <div class="rr-section-left">
      <div class="rr-section-icon" style="background:#EEEDFE;color:#3C3489;">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><rect x="2" y="4" width="14" height="10" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M5 7.5l2 2-2 2M9 11.5h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <div>
        <div class="rr-section-title">Technical detail</div>
        <div class="rr-section-sub">Controls &middot; compliance mapping &middot; remediation &middot; residual risk</div>
      </div>
    </div>
    <div class="rr-chevron" id="chev-rr-technical">&#9662;</div>
  </div>
  <div class="rr-section-body" id="body-rr-technical">

    <div class="rr-tech-block" id="rr-iam001">
      <div class="rr-tech-header" onclick="rrToggle('rr-iam001')">
        <div class="rr-risk-id" style="flex-shrink:0;">IAM-001</div>
        <div style="flex:1;font-size:.85rem;font-weight:500;color:#3D2008;">Overprivileged IAM Roles</div>
        <span class="rr-severity rr-sev-critical" style="flex-shrink:0;">&#128308; Critical</span>
        <div class="rr-chevron" id="chev-rr-iam001" style="margin-left:10px;">&#9662;</div>
      </div>
      <div class="rr-tech-body" id="body-rr-iam001">
        <div class="rr-detail-grid">
          <div class="rr-detail-item"><div class="rr-detail-label">Risk ID</div><div class="rr-detail-val">IAM-001 (CSN: IAM-IDC-001)</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Category</div><div class="rr-detail-val">IAM</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Cloud environment</div><div class="rr-detail-val">AWS Production</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Affected assets</div><div class="rr-detail-val">IAM Roles, EC2, Lambda</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Data classification</div><div class="rr-detail-val">Highly Critical</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Likelihood</div><div class="rr-detail-val">High (4/5)</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Impact</div><div class="rr-detail-val">High (4/5)</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Risk score</div><div class="rr-detail-val"><strong>4/5 &mdash; Critical</strong></div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Detection source</div><div class="rr-detail-val">Wiz</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Compliance mapping</div><div class="rr-detail-val">CIS 1.22, NIST AC-6</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Existing controls</div><div class="rr-detail-val">MFA enabled, CloudTrail logging</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Residual risk</div><div class="rr-detail-val">Medium</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Risk treatment</div><div class="rr-detail-val">Mitigate</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Exception approved</div><div class="rr-detail-val">No</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Target date</div><div class="rr-detail-val">2026-06-15</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Supporting team</div><div class="rr-detail-val">IAM Team</div></div>
        </div>
        <div class="rr-remediation-box">
          <div class="rr-rem-title">&#10003; Recommended remediation</div>
          <div class="rr-rem-body">Implement least privilege access and remove wildcard permissions. Review all cross-account roles. Enforce permission boundaries on all IAM roles. Audit roles not used in 90 days and remove or disable.</div>
        </div>
      </div>
    </div>

    <div class="rr-tech-block" id="rr-net001">
      <div class="rr-tech-header" onclick="rrToggle('rr-net001')">
        <div class="rr-risk-id" style="flex-shrink:0;">NET-001</div>
        <div style="flex:1;font-size:.85rem;font-weight:500;color:#3D2008;">Publicly Exposed Security Groups</div>
        <span class="rr-severity rr-sev-critical" style="flex-shrink:0;">&#128308; Critical</span>
        <div class="rr-chevron" id="chev-rr-net001" style="margin-left:10px;">&#9662;</div>
      </div>
      <div class="rr-tech-body" id="body-rr-net001">
        <div class="rr-detail-grid">
          <div class="rr-detail-item"><div class="rr-detail-label">Risk ID</div><div class="rr-detail-val">NET-001</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Category</div><div class="rr-detail-val">Network Security</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Cloud environment</div><div class="rr-detail-val">AWS Production</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Affected assets</div><div class="rr-detail-val">EC2 Security Groups</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Data classification</div><div class="rr-detail-val">Confidential</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Likelihood</div><div class="rr-detail-val">High (4/5)</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Impact</div><div class="rr-detail-val">High (4/5)</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Risk score</div><div class="rr-detail-val"><strong>4/5 &mdash; Critical</strong></div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Detection source</div><div class="rr-detail-val">Wiz</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Compliance mapping</div><div class="rr-detail-val">CIS 4.1, NIST SC-7</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Existing controls</div><div class="rr-detail-val">AWS Shield, WAF</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Residual risk</div><div class="rr-detail-val">Low</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Risk treatment</div><div class="rr-detail-val">Mitigate</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Exception approved</div><div class="rr-detail-val">No</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Target date</div><div class="rr-detail-val">2026-05-30</div></div>
          <div class="rr-detail-item"><div class="rr-detail-label">Supporting team</div><div class="rr-detail-val">Cloud Engineering</div></div>
        </div>
        <div class="rr-remediation-box">
          <div class="rr-rem-title">&#10003; Recommended remediation</div>
          <div class="rr-rem-body">Restrict inbound traffic to known CIDR ranges and remove 0.0.0.0/0 rules. Implement network segmentation. Prioritise internet-facing assets. Enforce security group policies via AWS Config rules to prevent re-introduction.</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ══ SECTION 4: GUIDE ═════════════════════════════════════════════════ -->
<div class="rr-section" id="rr-guide">
  <div class="rr-section-header" onclick="rrToggle('rr-guide')">
    <div class="rr-section-left">
      <div class="rr-section-icon" style="background:#EAF3DE;color:#27500A;">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><rect x="3" y="2" width="12" height="14" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M6 6h6M6 9h6M6 12h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      </div>
      <div>
        <div class="rr-section-title">Guide</div>
        <div class="rr-section-sub">Scoring methodology &middot; financial exposure bands &middot; severity levels</div>
      </div>
    </div>
    <div class="rr-chevron" id="chev-rr-guide">&#9662;</div>
  </div>
  <div class="rr-section-body" id="body-rr-guide">

    <div class="rr-guide-grid">
      <div class="rr-guide-card">
        <div class="rr-guide-title">Likelihood scale</div>
        <table class="rr-guide-table"><thead><tr><th>Score</th><th>Level</th><th>Meaning</th></tr></thead><tbody>
          <tr><td>1</td><td>Rare</td><td>Exceptional circumstances only</td></tr>
          <tr><td>2</td><td>Unlikely</td><td>Could occur at some time</td></tr>
          <tr><td>3</td><td>Possible</td><td>Might occur at some time</td></tr>
          <tr><td>4</td><td>Likely</td><td>Will probably occur</td></tr>
          <tr><td>5</td><td>Almost Certain</td><td>Expected in most circumstances</td></tr>
        </tbody></table>
      </div>
      <div class="rr-guide-card">
        <div class="rr-guide-title">Impact scale</div>
        <table class="rr-guide-table"><thead><tr><th>Score</th><th>Level</th><th>Meaning</th></tr></thead><tbody>
          <tr><td>1</td><td>Negligible</td><td>No material impact</td></tr>
          <tr><td>2</td><td>Minor</td><td>Minor disruption, easily recovered</td></tr>
          <tr><td>3</td><td>Moderate</td><td>Business disruption, recoverable</td></tr>
          <tr><td>4</td><td>Major</td><td>Significant disruption, regulatory attention</td></tr>
          <tr><td>5</td><td>Severe</td><td>Catastrophic, regulatory breach</td></tr>
        </tbody></table>
      </div>
    </div>

    <div class="rr-guide-card" style="margin-top:12px;">
      <div class="rr-guide-title">Risk score bands &amp; financial exposure</div>
      <div class="rr-sev-table">
        <div class="rr-sev-row rr-sev-low"><div class="rr-sev-score">1&ndash;2</div><div class="rr-sev-name">&#128994; Low</div><div class="rr-sev-action">Monitor &middot; review annually</div><div class="rr-sev-money">&lt; $50,000</div></div>
        <div class="rr-sev-row rr-sev-medium"><div class="rr-sev-score">3</div><div class="rr-sev-name">&#128993; Medium</div><div class="rr-sev-action">Remediate within 90 days</div><div class="rr-sev-money">$50K &ndash; $500K</div></div>
        <div class="rr-sev-row rr-sev-high"><div class="rr-sev-score">4</div><div class="rr-sev-name">&#128992; High</div><div class="rr-sev-action">Remediate within 30 days</div><div class="rr-sev-money">&gt; $500K</div></div>
        <div class="rr-sev-row rr-sev-crit"><div class="rr-sev-score">5</div><div class="rr-sev-name">&#128308; Critical</div><div class="rr-sev-action">Immediate action required</div><div class="rr-sev-money">&gt; $5,000,000</div></div>
      </div>
    </div>

  </div>
</div>

</div><!-- /rr-sections -->

<script>
function rrToggle(id) {
  var body = document.getElementById('body-' + id);
  var chev = document.getElementById('chev-' + id);
  if (!body) return;
  var open = body.style.display === 'block';
  body.style.display = open ? 'none' : 'block';
  if (chev) chev.innerHTML = open ? '&#9662;' : '&#9652;';
}
// Open overview by default
document.addEventListener('DOMContentLoaded', function() {
  var b = document.getElementById('body-rr-overview');
  var c = document.getElementById('chev-rr-overview');
  if (b) { b.style.display = 'block'; }
  if (c) { c.innerHTML = '&#9652;'; }
});
</script>
