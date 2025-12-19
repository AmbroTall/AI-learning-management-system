# Module 2: Build AI-Powered Tools - Security Automation Section
# 7 challenges focused on building real security automation tools

SECURITY_AUTOMATION_CHALLENGES = [
    {
        'title': 'Project 8: Automated Threat Intelligence Aggregator',
        'description': 'Build a system that collects and analyzes threat intelligence',
        'difficulty': 'intermediate',
        'order': 8,
        'points': 40,
        'instructions': '''Build a threat intelligence aggregation system! 🔍

**The Challenge:**
Threat intelligence comes from multiple sources - feeds, security blogs, vendor advisories, dark web monitoring. Build an AI system that aggregates and prioritizes this intelligence.

**What You'll Build:**
A prompt system that:
1. Takes threat intel from various sources
2. Extracts IOCs (Indicators of Compromise)
3. Assesses relevance to your environment
4. Prioritizes threats
5. Creates actionable intelligence reports
6. Suggests protective measures

**Real-World Application:**
Proactive threat hunting, early warning system, informed security decisions, vulnerability prioritization.

**Your Task:**
Design a comprehensive threat intelligence processing system that turns raw intel into actionable security measures.''',
        'example_prompt': '''I'm building a Threat Intelligence Aggregator for our security operations.

THREAT INTEL EXAMPLE:
```
SOURCE: Security Vendor Blog
DATE: Dec 18, 2024
TITLE: "New Ransomware Campaign Targeting Healthcare"

A sophisticated ransomware group (tracked as "MedLock") is actively targeting healthcare organizations with 100-500 employees using:

Attack Vector: Spear phishing emails impersonating electronic health record (EHR) vendors

IOCs:
- Email domains: ehr-support[.]net, medical-systems-update[.]com
- C2 IPs: 185.220.101.42, 198.54.123.67
- File hashes: a3f5d8e9... (dropper), c7b2e4f1... (payload)
- Registry keys: HKLM\SOFTWARE\MedLock
- Mutex: Global\MLSync2024

Techniques (MITRE ATT&CK):
- T1566.001: Spear Phishing Attachment
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery

Timeline: Active since Dec 10, 15 confirmed victims

Ransom Demand: $50K-$200K in Bitcoin
```

BUILD THIS AGGREGATOR SYSTEM:

1. THREAT ANALYZER PROMPT:
Extract and structure:
- Threat actor/group
- Attack methods
- Target profile (who's at risk?)
- Timeline (how urgent?)
- IOCs (all types: IPs, domains, hashes, etc.)
- MITRE ATT&CK techniques
- Impact severity

2. RELEVANCE ASSESSOR PROMPT:
Determine if this threat is relevant to us:
Our environment:
- Healthcare industry, 250 employees
- Use EHR systems (Epic)
- Windows endpoints
- Cloud and on-prem mix
- SOC team of 3

Questions:
- Are we in the target profile?
- Do we use targeted software?
- Are our defenses adequate?
- Is this threat active in our region?
Relevance score: 1-10 with reasoning

3. IOC EXTRACTOR PROMPT:
Pull all IOCs in structured format:
```
IPs: [list]
Domains: [list]
File Hashes: [list]
URLs: [list]
Registry Keys: [list]
Mutexes: [list]
File Paths: [list]
```
Ready for import to security tools

4. IMPACT CALCULATOR PROMPT:
Assess potential impact:
- Financial (ransom + downtime + recovery)
- Operational (systems down, recovery time)
- Reputation (patient data, regulatory)
- Compliance (HIPAA violations)
Estimate: Best case, likely case, worst case

5. DETECTION STRATEGY PROMPT:
Create detection approach:
- Can our current tools detect this?
- What logs to monitor?
- What behavioral patterns to watch?
- New detection rules needed?
- Gaps in visibility?

6. MITIGATION RECOMMENDER PROMPT:
Suggest immediate actions:
- Block IOCs (IP, domain, hash)
- Enhance email filtering
- User awareness (specific warnings)
- Backup verification
- Patch specific vulnerabilities
Prioritize by: Impact vs Effort

7. ACTIONABLE REPORT GENERATOR PROMPT:
Create report for SOC team:
- Executive summary (2 sentences)
- Threat overview (what, who, how)
- Why we care (relevance)
- What to look for (detection)
- What to do now (actions)
- Timeline (how urgent)
Format: Clear, scannable, actionable

For the MedLock ransomware example, provide:

A. COMPLETE THREAT ANALYSIS:
- All extracted data structured
- Relevance assessment for our org
- Impact calculation

B. ACTIONABLE INTELLIGENCE:
- IOCs ready for blocking
- Detection strategies
- Prioritized mitigation steps

C. SOC REPORT:
- 1-page actionable brief
- Clear next steps
- Timeline for actions

D. PLAYBOOK INTEGRATION:
- How this fits into IR playbook
- Who needs to know what
- Success metrics (how do we know we're protected?)

Make it:
- Fast to process (analysts are busy)
- Actionable (specific steps, not just FYI)
- Prioritized (do this first, then that)
- Environment-specific (relevant to us)
- Measurable (how do we verify protection?)''',
    },
    {
        'title': 'Project 9: Security Alert Triage Bot',
        'description': 'Build an AI bot that automatically triages security alerts',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 40,
        'instructions': '''Create an automated alert triage system! 🚨

**The Challenge:**
SOC teams drown in alerts. 80% are false positives. Build an AI system that automatically triages alerts before humans see them.

**What You'll Build:**
A bot that:
1. Receives security alerts
2. Enriches with context
3. Determines if it's a real threat
4. Assigns severity
5. Routes to appropriate team member
6. Suggests initial response actions

**Real-World Impact:**
Reduces analyst workload by 50-70%, speeds up response to real threats, reduces alert fatigue.

**Your Task:**
Design a complete alert triage automation system.''',
        'example_prompt': '''I'm building a Security Alert Triage Bot for our SIEM.

ALERT EXAMPLE:
```
ALERT ID: ALT-2024-15847
TIME: 2024-12-18 14:23:45 UTC
SOURCE: EDR System
TYPE: Suspicious Process Execution
SEVERITY: Medium (auto-assigned)

DETAILS:
Host: LAPTOP-Sales-042
User: mjohnson
Process: powershell.exe
Command: powershell.exe -enc JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAt...
Parent: outlook.exe
Network: Outbound connection to 45.142.212.61:443

BASELINE DEVIATION:
- User rarely runs PowerShell
- Encoded command (suspicious)
- Spawned from Outlook (potential phishing)
- Unknown external IP
- Outside business hours (2pm = lunch time)
```

BUILD THIS TRIAGE BOT:

1. ALERT ENRICHMENT PROMPT:
Enhance alert with context:
- User profile: Role, department, typical behavior
- Asset criticality: What's on this laptop? Sensitivity?
- Historical context: Has this user/host alerted before?
- Time context: Business hours? Normal for this user?
- Network context: Is destination IP known good/bad?
- Process context: Legitimate use of PowerShell?

Output: Enhanced alert with all available context

2. THREAT ASSESSMENT PROMPT:
Determine if this is a real threat:
Analyze:
- How many red flags? (list them)
- Are there innocent explanations?
- Attack technique likelihood (what attack does this resemble?)
- Sophistication level
- Confidence score (1-100): How sure are we?

Output: Threat/No Threat/Unsure + Confidence + Reasoning

3. SEVERITY CALCULATOR PROMPT:
If threat, calculate true severity:
Consider:
- Attack progression (how far along?)
- Asset value (what's at risk?)
- Data sensitivity
- Business impact if compromised
- Ease of containment
- Threat actor sophistication

Output: Critical/High/Medium/Low with justification
(Override SIEM's auto-severity if needed)

4. FALSE POSITIVE DETECTOR PROMPT:
Check for common false positive patterns:
- Legitimate admin tools
- Scheduled scripts
- Security tools themselves
- Known safe applications
- Previous FP patterns we've seen

If FP likely: What's the innocent explanation?
Confidence in FP assessment?

5. INITIAL RESPONSE RECOMMENDER PROMPT:
Suggest immediate actions:
- Isolate host? (if Critical)
- Kill process? (if malicious)
- Block IP? (if C2)
- Just monitor? (if unsure)
- Disable account? (if compromised)
- Escalate immediately? (if severe)

For each action: Risk vs Reward, Business impact

6. ROUTING DECIDER PROMPT:
Decide who should handle this:
- Tier 1 analyst (routine investigation)
- Tier 2 analyst (complex analysis)
- Senior analyst (sophisticated attack)
- Incident response team (confirmed incident)
- Can auto-resolve? (clear false positive)

Include: Why this routing? What skills needed?

7. INVESTIGATION PLAYBOOK SUGGESTER PROMPT:
Point to relevant playbook:
- Which IR playbook applies?
- What investigation steps?
- What additional data to collect?
- What questions to answer?
- Success criteria (when is investigation complete?)

For the example PowerShell alert, provide:

A. ENRICHED ALERT:
- All context added
- Unknown elements flagged
- Relevant history included

B. TRIAGE DECISION:
- Threat? Yes/No + Confidence
- Severity: [Level] + Reasoning
- False Positive Likelihood
- Priority Score (1-10)

C. ACTION PLAN:
- Immediate steps (next 5 minutes)
- Investigation approach (next 30 minutes)
- Escalation criteria (when to involve IR team)

D. ROUTING:
- Assigned to: [Team member]
- Why them: [Reasoning]
- Expected handling time
- Playbook to follow

E. AUTO-ACTIONS (if applicable):
- Can bot automatically resolve?
- What actions safe to automate?
- Human approval needed for what?

Make it:
- Fast (triage in <30 seconds)
- Accurate (low false negative rate)
- Conservative (when unsure, escalate)
- Learning (improve from analyst feedback)
- Explainable (show reasoning)

Show how this bot turns overwhelming alert volume into prioritized, contextualized, actionable queue for analysts.''',
    },
    {
        'title': 'Project 10: Phishing Email Classifier & Responder',
        'description': 'Automate phishing email analysis and user response',
        'difficulty': 'advanced',
        'order': 10,
        'points': 45,
        'instructions': '''Build a complete phishing response automation system! 🎣

**The Challenge:**
Users forward 20-50 suspicious emails daily to security team. Build an AI system that automatically analyzes, classifies, and responds.

**What You'll Build:**
A complete system that:
1. Receives forwarded emails
2. Analyzes for phishing indicators
3. Classifies threat level
4. Scans environment for other victims
5. Takes protective actions
6. Responds to user automatically
7. Generates metrics

**Real-World Impact:**
Reduces analyst workload by 60%, speeds user response from hours to minutes, catches phishing campaigns faster.

**Your Task:**
Design end-to-end phishing response automation.''',
        'example_prompt': '''I'm building a Phishing Email Classifier & Auto-Responder.

USER REPORT EXAMPLE:
```
From: user@company.com (Sarah Johnson, Accounting)
To: security@company.com
Subject: FW: Suspicious - ACTION REQUIRED: Payroll Update

Forwarded message:
---
From: "HR Department" <payroll.update@company-hr[.]net>
To: allusers@company.com
Subject: ACTION REQUIRED: Payroll Update
Date: Dec 18, 2024 9:15 AM

Dear Employee,

We are updating our payroll system this week. You must verify your bank details to ensure uninterrupted payment.

Click here to update your information: http://verify-payroll[.]net/company/update?emp=SJ847

This is mandatory and must be completed by Dec 20, 2024. Failure to update will result in delayed payment.

Questions? Contact HR at this email.

Thank you,
HR Department
Employee Services
```

Sarah's message: "This seems weird - did HR really send this? The email looks legitimate but something feels off."

BUILD THIS AUTOMATION SYSTEM:

1. EMAIL ANALYZER PROMPT:
Comprehensive analysis:

A. SENDER ANALYSIS:
- Display name vs actual email
- Domain authenticity (company-hr[.]net vs our actual domain)
- Email authentication (SPF/DKIM/DMARC - would fail)
- Sender reputation
- Previous emails from this sender?

B. CONTENT ANALYSIS:
- Urgency tactics (deadline pressure)
- Threat language (delayed payment)
- Request type (credential harvesting)
- Grammar/spelling
- Generic greeting vs personalized
- Professional tone assessment

C. LINK ANALYSIS:
- Actual destination vs display text
- Domain age and registration
- Typosquatting detection
- SSL certificate (if any)
- Known malicious indicators
- URL shorteners or redirects

D. TECHNICAL INDICATORS:
- Email headers suspicious?
- Reply-to different from sender?
- Embedded images loading tracking pixels?
- Attachments (if any)?

2. THREAT CLASSIFIER PROMPT:
Classify into:
- Definitely Phishing (block immediately)
- Likely Phishing (high confidence)
- Suspicious (needs human review)
- Probably Legitimate (low risk)
- Definitely Legitimate (whitelist sender)

Confidence score + key indicators

3. IMPACT ASSESSOR PROMPT:
If phishing, assess:
- Campaign scope (targeted or mass?)
- How many employees received it?
- How many clicked? (check email gateway logs)
- Any compromised credentials?
- Data at risk if successful?
- Urgency of response

4. AUTOMATED RESPONSE GENERATOR PROMPT:
Generate email response to Sarah:

For "Definitely Phishing":
```
Subject: ✓ Confirmed Phishing - Thank You!

Hi Sarah,

Thank you for reporting this email! You were absolutely right to be suspicious.

✓ CONFIRMED: This is a phishing attack
✓ BLOCKED: We've blocked this sender across the company
✓ SAFE: You did not click the link, so you're safe

What made this suspicious:
• Fake sender domain (company-hr.net is not our real domain)
• Urgent deadline pressure
• Requests for sensitive information (bank details)
• Suspicious link destination

WHAT TO DO:
• Delete this email
• If you clicked the link: Contact us immediately
• Watch for similar emails

You protected our company by reporting this! 

Security Team
Need help? Reply to this email or call x5555
```

For "Probably Legitimate":
```
Subject: Appears Legitimate - But Good Catch!

Hi Sarah,

Thanks for being cautious and reporting this email.

ASSESSMENT: This appears to be legitimate
- Verified sender domain
- Matches known HR communication pattern
- Link goes to our official HR portal

RECOMMENDATION:
• You can proceed with this request
• Still verify with HR directly if concerned
• Call HR at x1234 to confirm

Thank you for staying vigilant! It's always better to report and be safe.

Security Team
```

5. PROTECTIVE ACTIONS PROMPT:
If phishing, determine automatic actions:
- Block sender domain (email gateway)
- Add URLs to blocklist (proxy/firewall)
- Scan all mailboxes for this email
- Alert other users who received it
- Check for clicks/compromise
- Notify IT leadership if widespread

Which actions safe to automate vs require approval?

6. CAMPAIGN DETECTOR PROMPT:
Check if this is part of larger campaign:
- Similar emails received by others?
- Same sender/domain pattern?
- Coordinated timing?
- Industry-wide campaign? (check threat intel)
- Need company-wide warning?

7. METRICS TRACKER PROMPT:
Generate statistics:
- User report response time (automated = instant!)
- Phishing emails blocked
- Users protected
- Campaign detection speed
- False positive rate

For Sarah's phishing report, provide:

A. COMPLETE ANALYSIS:
- All indicators checked
- Classification with confidence
- Threat assessment

B. AUTO-RESPONSE EMAIL:
- Appropriate for classification
- Helpful and educational
- Clear next steps
- Encouraging tone

C. PROTECTIVE ACTIONS TAKEN:
- Automated blocks implemented
- Other users notified
- Campaign tracking initiated

D. ESCALATION (if needed):
- When to escalate to analyst
- What requires human judgment
- Notification to management

E. DASHBOARD METRICS:
- Time saved: 15 minutes of analyst time
- Users protected: 23 (who received email)
- Response time: 30 seconds (vs 2 hours manual)

Show complete flow:
User Reports → Auto-Analysis → Classification → Response → Protection → Metrics

Make it:
- Fast (sub-minute response)
- Accurate (very low false positives)
- Helpful (users feel supported)
- Protective (takes action automatically)
- Learning (improves from patterns)
- Measurable (track effectiveness)''',
    },
    {
        'title': 'Project 11: Vulnerability Prioritization Engine',
        'description': 'Build a system that intelligently prioritizes vulnerabilities for patching',
        'difficulty': 'advanced',
        'order': 11,
        'points': 45,
        'instructions': '''Create an intelligent vulnerability prioritization system! 🎯

**The Challenge:**
Vulnerability scanners find hundreds or thousands of vulns. You can't patch everything immediately. Build an AI system that prioritizes based on actual risk.

**What You'll Build:**
A system that:
1. Takes vulnerability scan results
2. Assesses actual risk (not just CVSS)
3. Considers exploitability and business context
4. Groups vulnerabilities efficiently
5. Creates prioritized remediation roadmap
6. Tracks patch deployment

**Real-World Impact:**
Focus on vulnerabilities that actually matter, efficient use of limited patching windows, measurable risk reduction.

**Your Task:**
Design a comprehensive vulnerability prioritization and remediation planning system.''',
        'example_prompt': '''I'm building a Vulnerability Prioritization Engine.

SCAN RESULTS EXAMPLE (abbreviated):
```
VULNERABILITY SCAN - 247 findings

SAMPLE FINDINGS:

1. CVE-2024-12345 - Apache Log4j Remote Code Execution
   CVSS: 10.0 (Critical)
   Affected: 5 web servers (production)
   Exploit: Public exploit available, actively exploited in wild
   Patch: Available
   Downtime: 2 hours per server (needs restart)

2. CVE-2023-98765 - Windows SMBv1 Vulnerability
   CVSS: 8.1 (High)
   Affected: 50 workstations
   Exploit: Known but requires authentication
   Patch: Available
   Downtime: None (applied during reboot)

3. CVE-2022-54321 - PHP Information Disclosure
   CVSS: 5.3 (Medium)
   Affected: 1 internal development server
   Exploit: Low severity information leak
   Patch: Available
   Downtime: 1 hour

4. CVE-2024-11111 - SSL/TLS Weak Cipher
   CVSS: 7.5 (High)
   Affected: 15 network devices
   Exploit: No known exploit, theoretical
   Patch: Configuration change required
   Downtime: None

5. CVE-2021-99999 - End-of-Life Java Version
   CVSS: 9.8 (Critical)
   Affected: 2 business-critical applications
   Exploit: Multiple known exploits
   Patch: Requires application migration (major effort)
   Downtime: Unknown, testing required
```

OUR CONSTRAINTS:
- Patching window: Every Tuesday 2-4am
- Can patch ~10 systems per window
- Business-critical systems need change approval (1 week lead time)
- Limited testing environment
- 1 system admin, 1 network engineer available

BUILD THIS PRIORITIZATION ENGINE:

1. RISK CALCULATOR PROMPT:
Calculate true risk beyond CVSS:

Consider:
- Exploitability (is it being exploited now?)
- Asset criticality (production vs dev?)
- Attack surface (internet-facing vs internal?)
- Data sensitivity (what's at risk?)
- Existing compensating controls (firewall, IDS, etc.)
- Business impact if exploited
- Ease of exploitation (authentication required?)

Output: Risk score 1-100 + reasoning
Not just CVSS - context matters!

2. REMEDIATION COMPLEXITY ASSESSOR PROMPT:
For each vulnerability, assess effort:
- Patch availability (ready to apply?)
- Downtime required
- Testing needed
- Change approval required
- Dependencies (must patch these first)
- Rollback risk
- Business impact of remediation

Output: Complexity score (Easy/Medium/Hard)

3. PRIORITY RANKER PROMPT:
Prioritize using:
- Risk score (from #1)
- Remediation complexity (from #2)
- Exploit maturity (PoC? Active? None?)
- Asset grouping (patch multiple together)
- Quick wins (high impact, low effort)

Create priority tiers:
- P0: Patch IMMEDIATELY (this week)
- P1: Next patching window (critical)
- P2: Within 30 days (important)
- P3: Within 90 days (routine)
- P4: Accept risk or defer (low priority)

4. PATCHING ROADMAP GENERATOR PROMPT:
Create week-by-week plan:

Week 1:
- Systems to patch
- Order of operations
- Backup requirements
- Rollback plans
- Success criteria

Consider:
- Patching window constraints
- System dependencies
- Business schedules (avoid month-end for finance systems)
- Resource availability
- Change approval timelines

5. GROUPING OPTIMIZER PROMPT:
Group vulnerabilities for efficiency:
- Same patch fixes multiple CVEs
- Same systems affected
- Can patch together safely
- Minimize maintenance windows
- Maximize impact per window

6. EXCEPTION MANAGER PROMPT:
For vulnerabilities we can't patch:
- Why not? (business constraint, testing needed, etc.)
- Compensating controls (what else can we do?)
- Risk acceptance justification
- Review timeline (when to revisit)
- Monitoring requirements

7. PROGRESS TRACKER PROMPT:
Track remediation:
- Patches applied
- Risk reduced (quantified)
- Vulnerabilities remaining
- Trending (getting better or worse?)
- Efficiency metrics (vulns per window)

For the example vulnerabilities, provide:

A. PRIORITIZATION:
All 5 ranked with:
- Priority tier (P0-P4)
- Risk score with reasoning
- Remediation complexity
- Recommended timeline

B. FIRST 30 DAYS ROADMAP:
Week-by-week plan:
- Which vulns to patch when
- Grouped efficiently
- Change approvals needed
- Resource allocation

C. QUICK WINS:
Identify 3-5 vulnerabilities that are:
- High impact
- Low effort
- Can do immediately

D. LONG-TERM PLAN:
For complex remediations (like End-of-Life Java):
- Assessment phase
- Testing phase
- Migration plan
- Risk mitigation during transition

E. METRICS DASHBOARD:
- Critical: 2 → 0 (after week 1)
- High: 65 → 15 (after 30 days)
- Overall risk: Reduced by 70%
- Patching efficiency: 12 vulns/window

Show how this turns overwhelming scan results into actionable, prioritized work.

Make it:
- Risk-based (not just CVSS)
- Practical (considers real constraints)
- Efficient (group work smartly)
- Measurable (track progress)
- Business-aware (minimize disruption)
- Defensible (explain decisions to auditors)''',
    },
    {
        'title': 'Project 12: Incident Response Playbook Generator',
        'description': 'Automatically generate IR playbooks for different incident types',
        'difficulty': 'advanced',
        'order': 12,
        'points': 45,
        'instructions': '''Build an AI system that generates incident response playbooks! 📘

**The Challenge:**
Every incident type needs a playbook (ransomware, DDoS, data breach, insider threat, etc.). Writing them manually takes weeks. Build an AI system that generates comprehensive IR playbooks.

**What You'll Build:**
A system that:
1. Takes incident type and context
2. Generates step-by-step response procedures
3. Includes decision trees
4. Lists required tools and access
5. Defines roles and responsibilities
6. Creates communication templates

**Real-World Value:**
Rapidly create playbooks for emerging threats, ensure consistency, improve response times, onboard new analysts faster.

**Your Task:**
Design a playbook generation system that creates production-ready IR playbooks.''',
        'example_prompt': '''I'm building an Incident Response Playbook Generator.

PLAYBOOK REQUEST:
```
Incident Type: Business Email Compromise (BEC)
Our Environment:
- Microsoft 365 for email
- 200 employees
- Finance team of 10
- ACH payment authority: CFO and 2 Finance Managers
- No MFA on executive accounts (yet)
- Email retention: 90 days
- Backup: Daily, 30-day retention

Recent Context:
- CEO email account briefly compromised last year
- Finance team targeted by phishing regularly
- Vendor payment process: Email approval workflow
```

BUILD THIS PLAYBOOK GENERATOR:

1. PLAYBOOK STRUCTURE GENERATOR PROMPT:
Create standard IR playbook structure:
- Objective (what is this playbook for?)
- Scope (what scenarios does it cover?)
- Prerequisites (tools, access, skills needed)
- Roles & Responsibilities
- Step-by-Step Procedures
- Decision Points
- Communication Plan
- Evidence Collection
- Recovery Steps
- Post-Incident Activities
- Metrics & KPIs

2. PROCEDURE GENERATOR PROMPT:
For each phase, create detailed steps:

DETECTION PHASE:
- How do we detect BEC? (indicators)
- What logs to check?
- Who typically reports it?
- False positive considerations

INITIAL ASSESSMENT:
- Questions to answer immediately
- Quick triage checklist
- Severity determination
- Escalation criteria

CONTAINMENT:
- Account actions (reset password, disable, etc.)
- Email actions (recall messages, block sender)
- Payment system protections
- Communication to finance team

INVESTIGATION:
- Email trail analysis
- Login history review
- Payment transaction check
- Identify all compromised accounts
- Determine attack timeline
- Find patient zero

ERADICATION:
- Remove attacker access
- Close attack vectors
- Clean compromised accounts
- Verify no persistence

RECOVERY:
- Restore account access
- Verify payment processes
- Resume normal operations
- Monitor for re-compromise

3. DECISION TREE GENERATOR PROMPT:
Create decision points:
- If money was transferred → [immediate wire recall procedure]
- If CEO account compromised → [executive notification protocol]
- If ongoing → [immediate containment]
- If contained but damage done → [damage assessment]

4. ROLE DEFINER PROMPT:
Define who does what:
- Incident Commander: [responsibilities]
- Technical Lead: [responsibilities]
- Communications Lead: [responsibilities]
- Finance Liaison: [responsibilities]
- Legal (when to involve): [responsibilities]
- Executive Leadership (when to notify): [responsibilities]

5. TOOL CHECKLIST PROMPT:
List required tools and access:
- M365 Admin Center access
- Email security logs
- Banking portal access
- Communication tools (Slack, phone tree)
- Evidence collection tools
- Backup systems

6. COMMUNICATION TEMPLATE GENERATOR PROMPT:
Create templates for:
- Initial notification (to management)
- User notification (if their account affected)
- Finance team alert
- Banking/vendor notification
- Post-incident summary

For each template: Tone, required info, timing, audience

7. TIMELINE & METRICS PROMPT:
Define:
- Detection to containment: Target <30 minutes
- Full investigation: Target <4 hours
- Recovery: Target <24 hours
- Success metrics: No financial loss, < $X impact, lessons learned documented

For BEC incident type, generate:

A. COMPLETE PLAYBOOK (20+ pages):
All sections filled with:
- Specific procedures for our environment
- M365-specific actions
- Finance-specific considerations
- Executive account handling
- Payment process protection

B. QUICK REFERENCE CARD (1 page):
- Critical steps
- Key contacts
- Decision flowchart
- Time targets

C. TRAINING SCENARIO:
- Sample BEC incident
- Step-through exercise
- Expected timeline
- Learning objectives

D. IMPROVEMENT RECOMMENDATIONS:
Based on generating this playbook, what gaps exist?
- MFA on executive accounts needed
- Email security enhancements
- Training requirements
- Process improvements

E. CUSTOMIZATION GUIDE:
How to adapt this playbook for:
- Different email platforms (Gmail, Exchange)
- Larger/smaller organizations
- Different payment systems
- Various compliance requirements

Show how this generates a professional, production-ready playbook that:
- Is specific to our environment
- Includes decision logic
- Has clear ownership
- Provides communication templates
- Can be used immediately

Make it:
- Comprehensive (covers all phases)
- Actionable (clear steps, no ambiguity)
- Practical (realistic for our team size)
- Tested (includes scenarios)
- Maintainable (easy to update)
- Professional (audit-ready documentation)''',
    },
    {
        'title': 'Project 13: Security Compliance Automation Assistant',
        'description': 'Build a tool that helps maintain continuous compliance',
        'difficulty': 'advanced',
        'order': 13,
        'points': 45,
        'instructions': '''Create a compliance automation assistant! ✓

**The Challenge:**
Compliance (SOC 2, ISO 27001, HIPAA, PCI DSS) requires continuous monitoring and evidence collection. Build an AI system that automates compliance tracking.

**What You'll Build:**
A system that:
1. Maps controls to requirements
2. Generates evidence collection plans
3. Automates control testing
4. Identifies compliance gaps
5. Tracks remediation
6. Prepares audit documentation

**Real-World Impact:**
Reduces compliance burden by 60%, continuous readiness for audits, automated evidence collection, early gap detection.

**Your Task:**
Design a comprehensive compliance automation system.''',
        'example_prompt': '''I'm building a Security Compliance Automation Assistant for SOC 2 Type II.

OUR SITUATION:
```
Organization: SaaS company, 150 employees
Compliance Target: SOC 2 Type II (first time)
Audit: In 6 months
Current State: Some controls in place, documentation incomplete

Trust Service Criteria Focus:
- Security (all controls)
- Availability (high priority)
- Confidentiality (customer data protection)

Known Gaps:
- Inconsistent access reviews
- Incomplete change management logs
- No formal incident response testing
- Backup testing not documented
- Vendor assessments missing
```

BUILD THIS COMPLIANCE ASSISTANT:

1. CONTROL MAPPER PROMPT:
Map our current practices to SOC 2 requirements:

For each control:
- SOC 2 criterion (CC6.1, CC7.2, etc.)
- Control description
- What we do now (current state)
- What's required (target state)
- Gap analysis (what's missing)
- Evidence needed

Output: Complete control matrix

2. EVIDENCE PLANNER PROMPT:
For each control, define evidence:
- Type (screenshot, log export, policy doc, etc.)
- Frequency (quarterly, monthly, ad-hoc)
- Owner (who collects it)
- Storage location
- Retention period
- Collection method (manual vs automated)

Create evidence collection calendar:
- What to collect when
- Who's responsible
- Automation opportunities

3. CONTROL TESTING AUTOMATOR PROMPT:
For automatable controls, design tests:

Example - Access Review Control:
"User access is reviewed quarterly"

Automated test:
- Extract current user list from AD
- Check last access review date
- Flag users not reviewed in 90 days
- Generate review assignment
- Track completion
- Collect evidence automatically

Create tests for:
- Password policy compliance
- Patch management timeliness
- Backup success rate
- Log retention compliance
- MFA enforcement

4. GAP REMEDIATOR PROMPT:
For each gap identified:
- Root cause (why is there a gap?)
- Remediation plan
- Owner
- Timeline
- Dependencies
- Cost estimate
- Risk if not remediated

Prioritize gaps by:
- Audit impact (will auditor test this?)
- Risk level
- Effort to fix
- Dependencies

5. CONTINUOUS MONITORING PROMPT:
Design ongoing compliance checks:

Daily:
- Backup success verification
- Critical security events
- Access anomaly detection

Weekly:
- Patch compliance status
- Vulnerability scan review
- Change management completeness

Monthly:
- Access review reminders
- Policy attestation tracking
- Vendor assessment status

Quarterly:
- Full control testing
- Risk assessment updates
- Board reporting

6. AUDIT PREP AUTOMATOR PROMPT:
Prepare for audit:
- Organize all evidence by control
- Create evidence cross-reference
- Identify evidence gaps
- Prepare control descriptions
- Create audit walkthrough guides
- Generate preliminary control self-assessment

7. DASHBOARD GENERATOR PROMPT:
Create compliance dashboard showing:
- Overall readiness (% of controls met)
- Evidence collection status
- Gap remediation progress
- Control test results
- Audit readiness trend
- Time to audit
- High-risk gaps

For our SOC 2 preparation, provide:

A. 6-MONTH ROADMAP:
Month-by-month plan:
- Month 1: Complete control mapping
- Month 2: Implement missing controls
- Month 3: Evidence collection automation
- Month 4: Full control testing
- Month 5: Gap remediation
- Month 6: Audit prep and practice

B. AUTOMATION OPPORTUNITIES:
10+ controls that can be automated:
- What to automate
- How to automate
- Tools needed
- Time savings
- Accuracy improvement

C. EVIDENCE COLLECTION PLAN:
Complete calendar:
- What evidence to collect when
- Who collects it
- Where it's stored
- How long to retain
- Automation status

D. GAP REMEDIATION TRACKER:
All gaps with:
- Priority
- Owner
- Timeline
- Status
- Dependencies
- Risk if not fixed

E. AUDIT READINESS ASSESSMENT:
Current state:
- Controls: 45/75 met (60%)
- Evidence: 30/75 collected (40%)
- Critical gaps: 8
- Audit-ready: No (need 3 more months)

Prediction:
- By audit date: 95% likely ready
- Confidence based on current progress
- Key risks to readiness

Show how this system:
- Automates tedious compliance work
- Ensures continuous readiness
- Reduces audit stress
- Maintains evidence systematically

Make it:
- Automated (minimal manual work)
- Continuous (not just pre-audit scramble)
- Evidence-based (collected systematically)
- Traceable (audit trail for everything)
- Efficient (focused on what matters)
- Scalable (as company grows)''',
    },
    {
        'title': 'Project 14: Security Training & Simulation Platform',
        'description': 'Build an AI-powered security awareness training and phishing simulation system',
        'difficulty': 'advanced',
        'order': 14,
        'points': 45,
        'instructions': '''Create a complete security training and simulation platform! 🎓

**The Challenge:**
Security awareness training is often boring and ineffective. Phishing simulations are manual and time-consuming. Build an AI system that creates engaging training and automated simulations.

**What You'll Build:**
A comprehensive system that:
1. Generates personalized training content
2. Creates phishing simulations
3. Tracks user behavior and learning
4. Provides targeted remediation
5. Measures training effectiveness
6. Adapts content based on performance

**Real-World Impact:**
Reduces phishing click rates by 70%, improves security culture, automated continuous training, personalized learning paths.

**Your Task:**
Design an AI-powered training and simulation platform that actually works.''',
        'example_prompt': '''I'm building a Security Training & Simulation Platform.

OUR TRAINING PROGRAM:
```
Organization: 250 employees across 5 departments
Current State:
- Annual security training: 50% completion
- Last phishing simulation: 35% click rate (bad!)
- No personalized training
- Generic content (boring)
- No follow-up for clickers

Departments:
- Executive (10): High-value targets, low tech skills
- Finance (25): Regular phishing targets
- IT (15): Tech-savvy, still need awareness
- Sales (100): Remote, mobile-heavy, busy
- Operations (100): Warehouse workers, limited computer use

Goals:
- 95% training completion
- <10% phishing simulation click rate
- Sustained behavior change
- Engaging content
- Automated and scalable
```

BUILD THIS PLATFORM:

1. TRAINING CONTENT GENERATOR PROMPT:
Create personalized training modules:

For each department, generate:
- Role-specific threats (what attacks target them?)
- Relevant scenarios (their actual work situations)
- Appropriate technical level
- Engaging format (not just slides)
- 15-20 minute modules (not too long)

Example topics:
- Executives: CEO fraud, whaling attacks
- Finance: Invoice fraud, payment scams
- IT: Credential stuffing, supply chain
- Sales: Mobile security, public WiFi risks
- Operations: Physical security, social engineering

2. PHISHING SIMULATION GENERATOR PROMPT:
Create realistic phishing emails:

Parameters:
- Difficulty level (easy/medium/hard)
- Target department (relevant to their role)
- Attack technique (credential harvesting, malware, social engineering)
- Sophistication (obvious to subtle)
- Seasonal/contextual (holiday scams, tax season, etc.)

Generate complete phishing email:
- From address (realistic but fake)
- Subject line
- Body content
- Call to action
- Landing page description

Plus tracking:
- Who clicked?
- Who reported?
- Who entered credentials?
- Time to click/report

3. BEHAVIOR ANALYZER PROMPT:
Track individual user behavior:

For each user, maintain:
- Training completion history
- Simulation performance over time
- Types of simulations failed
- Learning patterns (what works for them?)
- Risk score (how vulnerable are they?)
- Improvement trend

Identify:
- Chronic clickers (need extra help)
- Good reporters (recognize and reward)
- At-risk users (frequent targets + high access)
- Training effectiveness (improving or not?)

4. PERSONALIZED LEARNING PATH GENERATOR PROMPT:
Based on behavior, create custom training:

If user clicks phishing simulations:
- What types do they fall for? (urgency? authority? curiosity?)
- Targeted training on those specific tactics
- More frequent simulations of that type
- Remedial modules
- Manager notification (if repeated failures)

If user reports phishing:
- Positive reinforcement
- Advanced training opportunities
- Reduced simulation frequency
- Recognition program

5. REMEDIATION CONTENT GENERATOR PROMPT:
When user clicks simulation:

Immediate teachable moment:
- "This was a test - here's why it was suspicious"
- Interactive breakdown of red flags
- Comparison to real phishing
- What to do next time
- Required micro-training (5 minutes)
- Follow-up simulation in 2 weeks

Make it educational, not punitive

6. EFFECTIVENESS MEASURER PROMPT:
Track program metrics:

Leading Indicators:
- Training completion rate
- Simulation click rate over time
- Report rate (good users report suspicious emails)
- Time to report (faster is better)
- Knowledge retention (follow-up quizzes)

Lagging Indicators:
- Real phishing incidents
- Compromised credentials
- Security incidents from user error
- Support tickets for "is this phishing?"

ROI Calculation:
- Incidents prevented
- Time saved (fewer real incidents)
- Cost of prevention vs cost of incidents

7. CAMPAIGN MANAGER PROMPT:
Orchestrate training program:

Monthly themes:
- Jan: Password security
- Feb: Phishing awareness
- Mar: Mobile device security
- Apr: Data protection
- (etc.)

For each theme:
- Training content
- Matching phishing simulations
- Communications to employees
- Manager talking points
- Metrics to track
- Success criteria

For our organization, provide:

A. 12-MONTH TRAINING PROGRAM:
Month-by-month plan with:
- Training topics by department
- Phishing simulation schedule
- Expected improvement trajectory
- Resource requirements
- Success metrics

B. SAMPLE CONTENT:
Generate complete examples:
- 1 training module (Finance dept, invoice fraud)
- 3 phishing simulations (easy/medium/hard)
- 1 remediation module (for clickers)
- 1 positive reinforcement (for reporters)

C. PERSONALIZATION ENGINE:
Show how system adapts:
- User A: Executive, clicks often → intensive training + frequent simulations
- User B: IT staff, always reports → recognition + advanced training
- User C: Sales, improving → standard program, monitor progress
- User D: Finance, mixed results → targeted training on invoice fraud

D. METRICS DASHBOARD:
Track program success:
- Overall click rate: 35% → 8% (6 months)
- Completion rate: 50% → 97%
- Chronic clickers: 45 → 3
- Active reporters: 12 → 89
- Real phishing blocked: 15/month
- Cost savings: $X (avoided incidents)

E. GAMIFICATION:
Make training engaging:
- Points for completion and reporting
- Leaderboards (department level)
- Badges and achievements
- Rewards program
- Team challenges

Show how this platform:
- Makes training engaging (not boring!)
- Personalizes to each user
- Measures actual behavior change
- Scales automatically
- Reduces real phishing success

Make it:
- Engaging (people actually complete it)
- Effective (behavior actually changes)
- Automated (minimal admin work)
- Personalized (adapts to each user)
- Measurable (prove ROI)
- Positive (educate, don't shame)''',
    },
]
