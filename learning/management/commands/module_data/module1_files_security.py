# Module 1: AI Chat Mastery - File Interactions & Real-World Security Scenarios
# 12 challenges teaching file handling and cybersecurity-specific use cases (inspired by the Dion Training course)

FILE_AND_SECURITY_CHALLENGES = [
    {
        'title': 'Lesson 26: Analyzing Security Logs with AI',
        'description': 'Learn to upload and analyze log files for security insights',
        'difficulty': 'intermediate',
        'order': 26,
        'points': 25,
        'instructions': '''AI can analyze files you upload! 📄

**What You'll Learn:**
- How to share files with Claude
- Asking the right analysis questions
- Extracting security insights from logs

**The Feature:**
Claude can read files you upload - logs, reports, configs, policies, etc.

**Your Challenge:**
Write a prompt for analyzing a security log file.

**Your Prompt Should:**
1. Explain what the file is
2. Specify what you're looking for
3. Ask for specific analysis
4. Request actionable output

**Example Structure:**
"I'm uploading a firewall log from the past 24 hours. Please analyze it for:
- Suspicious connection attempts
- Port scanning activities  
- Unusual traffic patterns
- Top source IPs
- Recommended firewall rules

Format findings as: [Finding] - [Severity] - [Recommended Action]"

**Real-World:**
Log analysis is time-consuming. AI can help you spot patterns and anomalies faster!

**Note:** For this challenge, write the prompt you would use with an actual log file. Describe what analysis you'd request.''',
        'example_prompt': '''I'm uploading our firewall logs from the past 24 hours (CSV format with fields: timestamp, source_ip, dest_ip, port, action, protocol).

Please analyze these logs for security threats and anomalies:

1. THREAT DETECTION:
   - Port scanning attempts (multiple ports from single source)
   - Brute force patterns (repeated connection attempts)
   - Known malicious IPs (any patterns suggesting C2 communication)
   - DDoS indicators (unusual traffic volume)

2. TRAFFIC ANALYSIS:
   - Top 10 source IPs by connection count
   - Most targeted ports
   - Blocked vs allowed connections ratio
   - Unusual protocol usage

3. GEOGRAPHIC ANALYSIS:
   - Countries generating most traffic
   - Unexpected geographic sources
   - Known high-risk regions

4. TIME PATTERNS:
   - Traffic patterns throughout the day
   - Unusual activity during off-hours
   - Sudden spikes or drops

5. ACTIONABLE OUTPUT:
   For each finding, provide:
   - Severity (Critical/High/Medium/Low)
   - Evidence (specific log entries)
   - Recommended action (block IP, adjust rule, investigate further)
   - Priority (immediate, this week, monitor)

Present findings in order of severity. Focus on items requiring immediate action first.''',
    },
    {
        'title': 'Lesson 27: Vulnerability Report Analysis',
        'description': 'Analyze vulnerability scan reports and prioritize remediation',
        'difficulty': 'intermediate',
        'order': 27,
        'points': 25,
        'instructions': '''Turn vulnerability scans into action plans! 🔍

**What You'll Learn:**
- Analyzing vulnerability reports
- Prioritization strategies
- Creating remediation roadmaps

**The Scenario:**
You run a vulnerability scan (Nessus, Qualys, etc.) and get a 50-page report with 200+ findings. Overwhelming!

**Your Challenge:**
Write a prompt to help AI analyze the report and create a practical remediation plan.

**Your Prompt Should Ask For:**
1. Critical vulnerabilities requiring immediate action
2. Risk-based prioritization (not just CVSS scores)
3. Grouping by system/department
4. Estimated remediation effort
5. Quick wins vs complex fixes
6. Remediation roadmap with timeline

**Example:**
"Analyze this Nessus scan report. We have limited resources - only 1 system admin and a 2-week window before our audit. Help me:
- Identify critical issues we MUST fix
- Group remaining issues by ease of remediation
- Create a 2-week action plan
- Identify what we can defer safely"

**Real-World:**
You can't fix everything at once. AI helps you prioritize smartly!''',
        'example_prompt': '''I'm uploading a Nessus vulnerability scan report for our network (45 hosts: servers, workstations, network devices).

Context for prioritization:
- Upcoming compliance audit in 30 days
- Limited resources: 1 system admin (me), 2 network engineers
- Business-critical systems: Database servers, web servers, file shares
- Users can tolerate brief downtime for workstations (after hours)
- Network devices require change control (1-week lead time)

Please analyze and create an actionable remediation plan:

1. IMMEDIATE THREATS (Fix this week):
   - Critical/High vulns on internet-facing systems
   - Anything actively exploited in the wild
   - Easy fixes with high impact

2. PRE-AUDIT PRIORITIES (Fix before audit in 30 days):
   - Compliance-relevant findings
   - Items likely to be tested by auditors
   - Quick wins that improve overall score

3. GROUPED BY REMEDIATION TYPE:
   - Patching (estimate downtime needed)
   - Configuration changes (no downtime)
   - Network segmentation/firewall rules
   - Decommission/remove (end-of-life systems)

4. RESOURCE ALLOCATION:
   - What I can do alone (system admin work)
   - What needs network engineers
   - What requires change control

5. RISK-BASED RANKING:
   Don't just use CVSS scores - consider:
   - Asset criticality
   - Internet exposure
   - Ease of exploitation
   - Availability of patches
   - Business impact of remediation

6. TWO-WEEK SPRINT PLAN:
   Week 1 priorities, Week 2 priorities
   Include time estimates for each group of fixes

7. POST-AUDIT ROADMAP:
   What can we safely defer for 60-90 days?

Format as: [System/Group] - [Vulnerability] - [Remediation] - [Effort] - [Priority] - [Week to address]''',
    },
    {
        'title': 'Lesson 28: Policy Document Review',
        'description': 'Analyze security policies for gaps and improvements',
        'difficulty': 'intermediate',
        'order': 28,
        'points': 25,
        'instructions': '''AI can review your security policies! 📋

**What You'll Learn:**
- Policy gap analysis
- Best practice comparison
- Compliance checking

**The Task:**
Upload a security policy (password policy, acceptable use, incident response, etc.) and ask AI to review it.

**Your Prompt Should Request:**
1. Comparison to industry standards
2. Gaps or weaknesses
3. Compliance alignment (SOC 2, ISO 27001, etc.)
4. Clarity issues (is it understandable?)
5. Enforceability concerns
6. Specific improvements
7. Updated version incorporating fixes

**Example:**
"Review this password policy against NIST guidelines and SOC 2 requirements. Identify:
- What's missing or weak
- What's outdated
- What's unclear to users
- Specific wording improvements
Then provide an updated version."

**Real-World:**
Policy reviews take hours. AI can spot gaps quickly and suggest improvements based on frameworks!

**Your Task:**
Write a comprehensive policy review prompt that would help you improve a security policy document.''',
        'example_prompt': '''I'm uploading our company's Password Security Policy (last updated 2019). Please conduct a comprehensive review:

1. STANDARDS COMPARISON:
   Compare against:
   - NIST SP 800-63B (current password guidance)
   - CIS Controls v8
   - SOC 2 requirements
   - HIPAA security rule (we're in healthcare)
   
   What modern best practices are we missing?

2. OUTDATED ELEMENTS:
   - What guidance is now considered obsolete?
   - Are we requiring things that actually harm security? (like forced regular changes)
   - Any requirements contradict current NIST guidance?

3. GAP ANALYSIS:
   What's missing entirely?
   - Multi-factor authentication requirements
   - Password manager guidance
   - Passphrase vs password options
   - Account lockout specifics
   - Password reset procedures
   - Privileged account requirements
   - Service account/API key handling

4. CLARITY AND USABILITY:
   - Is it written for a general employee audience?
   - Any technical jargon that needs simplification?
   - Are requirements clear and measurable?
   - Examples provided where helpful?

5. ENFORCEABILITY:
   - Can we actually enforce these requirements?
   - Any rules that conflict with user productivity?
   - Technical controls available to enforce each requirement?

6. ORGANIZATIONAL CONTEXT:
   We're a 100-person healthcare organization with:
   - Mix of technical and non-technical staff
   - HIPAA compliance requirement
   - Limited IT staff (3 people)
   - Mix of Windows, Mac, mobile devices
   - Cloud apps (M365, Salesforce, EMR system)

7. PROVIDE:
   - Summary of critical gaps (top 5)
   - Specific wording improvements (with before/after examples)
   - Updated policy incorporating all fixes
   - Implementation guidance (what technical changes needed)
   - User communication recommendations (how to roll this out)

Make the updated policy clear, modern, and realistic for our organization to implement and enforce.''',
    },
    {
        'title': 'Lesson 29: Incident Report Documentation',
        'description': 'Transform raw incident notes into professional reports',
        'difficulty': 'intermediate',
        'order': 29,
        'points': 25,
        'instructions': '''Create professional incident reports from messy notes! 📝

**What You'll Learn:**
- Structuring incident documentation
- Professional reporting
- Extracting timeline and impact

**The Scenario:**
You've handled a security incident. You have rough notes, chat logs, timestamps - all messy. Need a professional report for leadership.

**Your Challenge:**
Upload or paste your messy incident notes and ask AI to create a professional incident report.

**Your Prompt Should:**
1. Provide the raw notes/timeline
2. Specify report audience (technical team vs executives)
3. Request specific sections
4. Ask for professional formatting
5. Include lessons learned

**Structure:**
"Transform these raw incident notes into a professional incident report for executive leadership. Include:
- Executive summary (3 bullet points)
- Incident timeline
- Impact assessment
- Response actions taken
- Root cause
- Preventive measures
- Estimated costs

Use professional tone, avoid jargon."

**Real-World:**
Incident documentation is required but time-consuming. AI can structure your notes professionally while you focus on response!''',
        'example_prompt': '''Transform these raw incident response notes into a professional incident report for our executive team (CEO, CFO, CISO).

RAW NOTES:
```
9:45 AM - Alert from EDR: suspicious process on finance workstation (FINANCE-PC-04)
9:48 AM - Checked user: Jennifer from accounts payable, says she clicked a link in an email about an "invoice"
9:50 AM - Isolated workstation from network
9:52 AM - Found: ransomware dropper, not yet encrypted files but trying to contact C2 server
10:05 AM - Checked other systems: 2 more workstations with same initial infection (FINANCE-PC-07, FINANCE-PC-12)
10:10 AM - Isolated those too
10:15 AM - Blocked C2 domain in firewall
10:30 AM - Forensics: Email was very convincing fake invoice from "known vendor" - actually phishing
11:00 AM - Found 15 other employees received same email, 3 clicked (only 3 got infected)
11:30 AM - Cleaned infected systems, restored from backup
1:00 PM - Systems back online, no data encrypted
2:00 PM - Implemented email rule to block sender domain
2:30 PM - Sent warning to all staff about this campaign
```

KNOWN FACTS:
- Ransomware variant: RansomX (we identified it)
- Attack vector: Phishing email with malicious link
- Targeted: Finance department specifically
- Close call: If EDR hadn't caught it, could have encrypted entire finance share drive (~500GB of data, 7 years of records)
- Downtime: 3 workstations offline for 3.5 hours
- No data lost, no ransom paid
- This matches recent campaigns we've seen in security bulletins

CREATE A REPORT WITH:

1. EXECUTIVE SUMMARY:
   3-4 bullets, non-technical, focus on "what happened" and "what's the impact"

2. INCIDENT OVERVIEW:
   - Date/Time
   - Type of attack
   - How discovered
   - Systems affected
   - Current status

3. TIMELINE:
   Professional format, clear sequence of events

4. IMPACT ASSESSMENT:
   - Systems affected
   - Downtime duration
   - Data at risk (even if not lost)
   - Business operations impact
   - Financial impact estimate

5. RESPONSE ACTIONS:
   What we did well, how we contained it

6. ROOT CAUSE:
   Why did this happen? (focus on the phishing success, not blaming Jennifer)

7. LESSONS LEARNED:
   What worked, what didn't

8. PREVENTIVE MEASURES:
   Specific actions we're taking to prevent recurrence:
   - Immediate (already done)
   - Short-term (next 30 days)
   - Long-term (strategic improvements)

9. RECOMMENDATIONS:
   What investments/changes leadership should consider

Format professionally. Use clear section headers. Keep technical jargon minimal - this is for executives. Emphasize that quick detection prevented major damage.''',
    },
    {
        'title': 'Lesson 30: SOC Workflow Automation (From Cybersecurity Course!)',
        'description': 'Learn to use AI for Security Operations Center tasks',
        'difficulty': 'advanced',
        'order': 30,
        'points': 35,
        'instructions': '''Accelerate SOC operations with AI! 🚨 (Inspired by "AI Prompt Engineering for Cybersecurity Pros")

**What You'll Learn:**
- Automating alert triage
- Enrichment queries
- Playbook execution
- Investigation workflows

**The Course Reference:**
This lesson is inspired by professional cybersecurity courses on AI-powered SOC workflows!

**Your Challenge:**
Create a comprehensive SOC workflow where AI helps with:
1. Alert triage and prioritization
2. Threat intelligence enrichment
3. Initial investigation steps
4. Recommended responses
5. Documentation generation

**The Scenario:**
You're a SOC analyst. Alerts are pouring in. You need AI to help you work faster and smarter.

**Your Prompt Should:**
- Present alert data (IP, domain, user, activity type)
- Ask for threat intelligence lookup
- Request risk assessment
- Get investigation recommendations
- Generate incident documentation if needed

**Real-World SOC Workflow:**
Alert → Triage → Enrich → Investigate → Respond → Document

AI can accelerate EVERY step!

**Your Task:**
Design a comprehensive SOC workflow prompt that covers the full investigation cycle.''',
        'example_prompt': '''I'm a SOC analyst and need AI assistance for alert triage and investigation. Here's my workflow:

ALERT DETAILS:
- Type: Suspicious outbound connection
- Source: Workstation SALES-PC-23 (user: mjohnson)
- Destination IP: 185.220.101.42
- Destination Port: 443 (HTTPS)
- Timestamp: 2024-12-10 14:23:17 UTC
- Data transferred: 2.3 MB outbound
- Alert source: Network monitoring detected connection to IP not seen before
- Context: User clicked link in email 5 minutes before this connection

AI, HELP ME TRIAGE THIS:

1. THREAT INTELLIGENCE ENRICHMENT:
   - Is this IP known malicious? (check reputation databases conceptually)
   - Any association with threat actors or campaigns?
   - Geographic location and hosting provider
   - Domain reputation (if domain resolves)
   - WHOIS information insights

2. BEHAVIORAL ANALYSIS:
   - Is this traffic pattern normal for a sales user?
   - Red flags in the timing/volume?
   - Connection to email click suspicious?

3. RISK ASSESSMENT:
   Based on available info, what's the likely risk level?
   - Critical: Active C2, immediate threat
   - High: Likely malicious, needs quick investigation
   - Medium: Suspicious, investigate when possible
   - Low: Likely false positive, low priority

4. INVESTIGATION STEPS:
   Give me a prioritized checklist:
   - What to check on the workstation?
   - What logs to review?
   - What other systems to check?
   - User interview questions?
   - Timeline reconstruction steps?

5. CONTAINMENT RECOMMENDATIONS:
   Should I:
   - Isolate the workstation immediately?
   - Block the IP/domain?
   - Just monitor?
   Explain the tradeoffs of each action.

6. IF THIS IS MALICIOUS:
   - What type of attack does this resemble?
   - What's the likely attacker objective?
   - What else should we look for (lateral movement, data exfil, etc.)?
   - What's the potential business impact?

7. DOCUMENTATION:
   If this turns out to be an incident, generate:
   - Initial incident report template
   - Investigation checklist
   - Stakeholder notification draft (for my CISO)

Work through this systematically. Start with enrichment, then risk assessment, then recommend next steps. Think like an experienced SOC analyst and help me work this alert efficiently.''',
    },
{
        'title': 'Lesson 31: Phishing Email Analysis',
        'description': 'Use AI to analyze and report on phishing emails',
        'difficulty': 'intermediate',
        'order': 31,
        'points': 30,
        'instructions': '''Dissect phishing emails with AI assistance! 🎣

**What You'll Learn:**
- Phishing indicator identification
- Email header analysis
- Link and attachment investigation
- User reporting workflows

**The Challenge:**
Users forward suspicious emails to your security team. You need to analyze them quickly and determine if they're real threats.

**Your Prompt Should:**
1. Provide email details (from, subject, body, headers)
2. Ask for phishing indicators
3. Request link/attachment analysis
4. Get response recommendations
5. Generate user communication

**Analysis Checklist:**
- Sender authenticity
- Subject line red flags
- Body content analysis
- Link destinations
- Attachment risks
- Header analysis
- Urgency/pressure tactics

**Your Task:**
Create a phishing analysis workflow that helps you quickly assess emails users report.

**Real-World:**
SOC teams analyze dozens of reported phishing emails daily. AI speeds this up dramatically!''',
        'example_prompt': '''A user forwarded me a suspicious email. Help me analyze it for phishing indicators and decide on next steps.

EMAIL DETAILS:
From: "IT Department" <support@company-helpdesk.net>
To: jsmith@ourcompany.com
Subject: URGENT: Your email account will be suspended - Action Required
Date: Today, 9:15 AM

Body:
"Dear Employee,

We detected unusual activity on your email account. Your account will be suspended within 24 hours unless you verify your identity.

Click here to verify now: [link to: http://secure-verify-portal.net/company/verify?id=7483]

Failure to verify will result in permanent account closure and loss of all email data.

Thank you,
IT Security Team
Employee Services Department"

ANALYZE THIS EMAIL:

1. SENDER ANALYSIS:
   - Is the sending domain legitimate?
   - Display name vs actual email address (spoofing?)
   - Is "company-helpdesk.net" related to our actual domain?

2. CONTENT RED FLAGS:
   - Urgency/threat tactics?
   - Grammar/spelling issues?
   - Generic greeting vs personalized?
   - Tone and professionalism assessment?

3. LINK ANALYSIS:
   - Where does that link actually go? (domain analysis)
   - Does the URL match the display text?
   - Any signs of typosquatting?
   - Is it using URL shorteners or redirects?

4. TECHNICAL INDICATORS:
   What would we see in email headers? Consider:
   - SPF/DKIM/DMARC authentication
   - Reply-to address different from sender?
   - Received-from headers

5. ATTACK PATTERN:
   - What type of phishing is this? (credential harvesting, malware delivery, etc.)
   - What's the attacker's likely goal?
   - Targeted (spear phishing) or mass campaign?

6. THREAT LEVEL:
   Rate as: Critical/High/Medium/Low and explain why

7. RECOMMENDED ACTIONS:
   - Block sender domain?
   - Add link to blocklist?
   - Company-wide warning needed?
   - Additional user training indicated?

8. USER RESPONSE:
   Draft a reply to the user who reported this:
   - Confirm it's phishing (or not)
   - Thank them for reporting
   - Explain what made it suspicious
   - Remind them what to do with similar emails
   Keep it brief and encouraging!

9. INDICATORS TO WATCH:
   - Should we scan for this domain in other users' mailboxes?
   - Any compromise indicators to look for?
   - Follow-up monitoring needed?

Analyze systematically and help me respond quickly.''',
    },
    {
        'title': 'Lesson 32: Threat Hunting with AI',
        'description': 'Use AI to develop threat hunting hypotheses and queries',
        'difficulty': 'advanced',
        'order': 32,
        'points': 35,
        'instructions': '''Proactive threat hunting with AI! 🔎

**What You'll Learn:**
- Developing hunting hypotheses
- Creating detection queries
- Analyzing hunting results
- Iterative refinement

**The Concept:**
Threat hunting is proactive - looking for threats that evaded detection. AI can help you develop hypotheses and hunting strategies.

**Your Challenge:**
Create a threat hunting plan for a specific attack technique.

**Your Prompt Should:**
1. Choose an attack technique (MITRE ATT&CK)
2. Ask AI for hunting hypotheses
3. Request detection queries
4. Get analysis guidance
5. Build playbook

**Example:**
"I want to hunt for credential dumping in our environment. Help me:
- Understand how this attack works
- Identify what logs/data sources to check
- Write queries to detect it
- Analyze results
- Create response playbook"

**Real-World:**
Threat hunting is advanced security work. AI makes it accessible to analysts with less experience!

**Your Task:**
Design a comprehensive threat hunt for a specific technique.''',
        'example_prompt': '''I want to conduct a threat hunt for "Living off the Land" (LOLBin) attacks in our Windows environment. Help me develop a comprehensive hunting plan.

BACKGROUND:
- Environment: 300 Windows 10/11 workstations, 50 Windows servers
- Logging: Windows Event Logs, Sysmon, EDR telemetry
- Tools: Splunk for log aggregation, CrowdStrike EDR
- No recent alerts, but want to hunt proactively
- Focus: PowerShell and WMI abuse

HELP ME WITH:

1. ATTACK UNDERSTANDING:
   - What are "Living off the Land" attacks?
   - Why are they effective at evading detection?
   - What specific techniques should we hunt for?
   - Real-world examples of LOLBin abuse?

2. HYPOTHESIS DEVELOPMENT:
   Create 3-5 specific hunting hypotheses like:
   "Hypothesis 1: Attackers may be using PowerShell to download and execute payloads from remote servers"
   
   For each hypothesis:
   - What attacker behavior we're looking for
   - Why this might be happening undetected
   - What normal activity might look similar

3. DATA SOURCES:
   What logs/telemetry should I focus on?
   - Windows Event IDs
   - Sysmon events
   - PowerShell logging
   - WMI event subscriptions
   - Process creation events
   - Network connections

4. DETECTION QUERIES:
   Provide Splunk queries (or query logic) to find:
   - Suspicious PowerShell execution patterns
   - WMI being used for persistence or lateral movement
   - Encoded PowerShell commands
   - Remote WMI connections
   - Suspicious parent-child process relationships
   
   For each query:
   - What it detects
   - Expected false positive rate
   - How to filter noise

5. BASELINE UNDERSTANDING:
   What's "normal" in our environment that I need to know?
   - Legitimate PowerShell usage patterns
   - Admin scripts that might trigger detections
   - Legitimate WMI usage
   - How to establish baseline behavior?

6. HUNT EXECUTION:
   Step-by-step process:
   - Week 1 activities
   - What to look for in results
   - How to pivot when something interesting appears
   - When to escalate to incident response

7. RESULT ANALYSIS:
   If I find suspicious activity, how do I:
   - Determine if it's malicious vs benign?
   - Scope the potential compromise?
   - Collect additional evidence?
   - Decide on response actions?

8. DETECTION ENGINEERING:
   If we find a good hunting technique:
   - How to convert it to an automated alert?
   - What thresholds to set?
   - How to reduce false positives?

9. DOCUMENTATION:
   Create a threat hunting playbook template for this hunt that includes:
   - Technique description
   - Data sources
   - Queries
   - Analysis guidance
   - Response procedures

Make this practical and actionable. I want to actually execute this hunt next week.''',
    },
    {
        'title': 'Lesson 33: Security Architecture Review',
        'description': 'Use AI to review and improve security architecture',
        'difficulty': 'advanced',
        'order': 33,
        'points': 35,
        'instructions': '''Review security architecture with AI expertise! 🏗️

**What You'll Learn:**
- Architecture assessment
- Defense-in-depth analysis
- Finding gaps and weaknesses
- Improvement recommendations

**Your Challenge:**
Describe your current security architecture and ask AI to identify weaknesses and improvements.

**Your Prompt Should:**
1. Describe current architecture (network, controls, tools)
2. Specify business context (industry, size, threats)
3. Request gap analysis
4. Ask for prioritized improvements
5. Get implementation roadmap

**What to Include:**
- Network segmentation
- Access controls
- Security tools deployed
- Data protection measures
- Monitoring capabilities
- Incident response capability

**Your Task:**
Create a comprehensive architecture review request.

**Real-World:**
Architecture reviews are expensive consulting engagements. Use AI for initial assessment!''',
        'example_prompt': '''Review our security architecture and provide detailed improvement recommendations.

ORGANIZATION CONTEXT:
- Industry: Healthcare (HIPAA-regulated)
- Size: 250 employees, 3 locations
- Revenue: $50M annually
- IT Staff: 4 people (1 security-focused)
- Recent growth: Doubled in size in 2 years (architecture hasn't kept up)

CURRENT ARCHITECTURE:

Network:
- Single flat network (192.168.1.0/24)
- No segmentation between departments
- Perimeter firewall (Fortinet)
- Site-to-site VPN between locations
- Employee VPN for remote access (60% of staff work remotely)
- Guest WiFi on same network as corporate

Endpoints:
- Windows 10/11 workstations (200)
- Mix of Windows and Linux servers (25 total)
- Mobile devices (BYOD, no MDM)
- Antivirus on endpoints (Windows Defender)
- No EDR solution

Identity:
- Active Directory (on-premises)
- No multi-factor authentication except for VPN
- Local admin rights common
- No identity governance

Data:
- Electronic Health Records (EHR) system - critical
- File servers with patient data
- Email (Microsoft 365)
- No data classification
- No DLP solution
- Backups: Daily, stored on-site

Monitoring:
- Firewall logs (not centralized)
- No SIEM
- No centralized log collection
- Alerts only for AV detections
- No threat intelligence feeds

Policies:
- Basic acceptable use policy
- Password policy (8 characters, 90-day expiration)
- No formal incident response plan
- Annual security training (just video)

CONCERNS:
- Recent ransomware attacks in healthcare sector
- Upcoming HIPAA audit
- Compliance gaps identified in last audit
- Limited visibility into what's happening on network
- Worried about insider threats (no monitoring)

ANALYZE AND PROVIDE:

1. CRITICAL GAPS (Fix immediately):
   What's missing that creates serious risk?
   Prioritize by risk level

2. ARCHITECTURE WEAKNESSES:
   - Single flat network issues
   - Lack of segmentation problems
   - Defense-in-depth gaps
   - Monitoring blind spots

3. COMPLIANCE GAPS:
   HIPAA requirements we're not meeting

4. QUICK WINS:
   Improvements we can make quickly (<30 days, low cost)

5. STRATEGIC IMPROVEMENTS:
   Longer-term architectural changes needed (3-12 months)

6. REFERENCE ARCHITECTURE:
   Describe what our architecture SHOULD look like:
   - Network segmentation approach
   - Zero trust concepts we should adopt
   - Security controls by layer
   - Monitoring and detection strategy

7. PRIORITIZED ROADMAP:
   Phase 1 (Next 30 days): [immediate risks]
   Phase 2 (31-90 days): [foundational improvements]
   Phase 3 (3-6 months): [strategic enhancements]
   Phase 4 (6-12 months): [advanced capabilities]

8. BUDGET GUIDANCE:
   Rough cost estimates for each phase
   - What can we do with existing tools?
   - What requires new investment?
   - Realistic budget expectations?

9. RESOURCE REQUIREMENTS:
   - Can our 4-person team handle this?
   - Where do we need external help?
   - Training needs?

10. METRICS:
    How do we measure improvement?
    What KPIs should we track?

Be thorough but realistic. We're a small team with limited budget. Help us prioritize what matters most for our risk profile.''',
    },
    {
        'title': 'Lesson 34: Compliance Mapping & Gap Analysis',
        'description': 'Map security controls to compliance requirements',
        'difficulty': 'advanced',
        'order': 34,
        'points': 35,
        'instructions': '''Navigate compliance with AI! 📜

**What You'll Learn:**
- Mapping controls to frameworks
- Gap identification
- Remediation planning
- Documentation generation

**The Challenge:**
You need to demonstrate compliance with multiple frameworks (SOC 2, ISO 27001, HIPAA, PCI DSS, etc.)

**Your Prompt Should:**
1. List your current security controls
2. Specify target framework(s)
3. Request control mapping
4. Ask for gap analysis
5. Get remediation guidance

**Your Task:**
Create a compliance gap analysis request.

**Real-World:**
Compliance mapping is tedious but required. AI can accelerate this significantly!''',
        'example_prompt': '''Help me perform a compliance gap analysis for SOC 2 Type II audit.

OUR CURRENT SECURITY CONTROLS:

Access Control:
- Active Directory with group-based access
- No MFA except for VPN
- Password policy: 12 chars, 90-day expiration, complexity required
- Quarterly access reviews (manual spreadsheet)
- Terminated employees removed within 24 hours

Network Security:
- Perimeter firewall with rule reviews
- Segmented network (production separate from corporate)
- IDS/IPS at perimeter
- No internal network monitoring
- VPN for remote access

Endpoint Security:
- Antivirus on all endpoints
- Patch management (WSUS for Windows, manual for others)
- No mobile device management
- BitLocker encryption on laptops

Monitoring & Logging:
- Firewall logs kept for 90 days
- Windows event logs kept for 30 days
- No centralized log collection
- No SIEM
- Manual log review monthly

Backup & Recovery:
- Daily backups of critical systems
- Backups stored offsite
- Annual disaster recovery test
- RTO: 24 hours, RPO: 24 hours

Vulnerability Management:
- Quarterly vulnerability scans
- No continuous monitoring
- Patches applied within 30 days for critical
- No bug bounty or penetration testing

Incident Response:
- Documented IR plan (last updated 2 years ago)
- IR team identified
- No regular IR drills
- No formal forensics capability

Change Management:
- Change request process for production
- Peer review for code changes
- No automated testing

Training & Awareness:
- Annual security training (all employees)
- No role-specific training
- No phishing simulations

PERFORM THIS ANALYSIS:

1. SOC 2 CONTROL MAPPING:
   Map each of our controls to relevant SOC 2 Trust Service Criteria
   Which criteria do we address? Which do we miss?

2. GAP IDENTIFICATION:
   For each gap:
   - Which criterion is not met?
   - What specifically is missing?
   - Risk level if not addressed?
   - Auditor likely response?

3. CRITICAL GAPS:
   What must we fix before audit? (Priority 1 items)

4. EVIDENCE REQUIREMENTS:
   For each control area:
   - What evidence will auditors request?
   - Do we have it documented?
   - How should we document it?

5. REMEDIATION PLAN:
   For each gap, provide:
   - Specific action to remediate
   - Estimated effort/cost
   - Timeline (realistic for audit in 120 days)
   - Who should own this?

6. CONTINUOUS COMPLIANCE:
   How do we maintain compliance ongoing?
   - What processes need formalization?
   - What automation could help?
   - What regular reviews needed?

7. DOCUMENTATION NEEDS:
   What policies/procedures must we create or update?

8. AUDIT PREPARATION:
   - What to prepare before audit starts?
   - How to organize evidence?
   - Common audit questions to prep for?

9. IMPLEMENTATION ROADMAP:
   120-day plan to audit-ready state:
   Days 1-30: [immediate fixes]
   Days 31-60: [foundational work]
   Days 61-90: [documentation & testing]
   Days 91-120: [audit prep & practice]

10. COST ESTIMATE:
    Rough costs for:
    - Tool/service purchases needed
    - Consulting/expert help
    - Staff time (at $100/hour loaded cost)
    - Total investment to achieve compliance?

Be specific and actionable. Assume I'm doing this for the first time.''',
    },
    {
        'title': 'Lesson 35: Career Development & Skill Mapping',
        'description': 'Plan your cybersecurity career path with AI guidance',
        'difficulty': 'beginner',
        'order': 35,
        'points': 30,
        'instructions': '''Map your cybersecurity career journey! 🚀

**What You'll Learn:**
- Career path planning
- Skill gap identification
- Certification guidance
- Learning roadmap creation

**The Challenge:**
You're in cybersecurity (or transitioning to it). Where should your career go? What skills do you need?

**Your Prompt Should:**
1. Describe your current situation (role, experience, skills)
2. State your career goals (where you want to be)
3. Ask for gap analysis
4. Request learning roadmap
5. Get certification guidance

**Your Task:**
Create a personalized career development plan.

**Real-World:**
Career planning is crucial. AI can help you identify the best path based on your goals!''',
        'example_prompt': '''Help me plan my cybersecurity career path and create a learning roadmap.

MY CURRENT SITUATION:
- Role: Junior SOC Analyst (8 months in role)
- Background: 2 years in IT help desk before this
- Education: Bachelor's in Computer Science
- Technical skills:
  * Comfortable with Windows/Linux basics
  * Can read firewall logs and simple Splunk queries
  * Basic understanding of networking (TCP/IP, subnetting)
  * Familiar with SIEM concepts
  * Some Python (introductory level)
  * No certifications yet

WHAT I DO DAILY:
- Monitor security alerts in SIEM
- Triage incidents (determine real vs false positive)
- Document incidents
- Escalate to senior analysts when needed
- Some vulnerability scan analysis
- Help with user security issues

WHAT I WANT:
- Goal: Become a Senior SOC Analyst, then Security Engineer
- Timeline: 3-5 years
- Interest areas: Threat hunting, incident response, maybe penetration testing eventually
- Want to be more technical, less "following playbooks"

CONSTRAINTS:
- Full-time job (can study evenings/weekends)
- Budget: ~$5K/year for training/certs
- Can't take extended time off for bootcamps
- Need to show progress to justify raise/promotion

HELP ME WITH:

1. CAREER PATH:
   Realistic progression from Junior SOC Analyst to my goals:
   - Typical steps/roles
   - Timeline expectations
   - What each role requires

2. SKILL GAP ANALYSIS:
   What skills do I need that I don't have?
   - Technical skills
   - Tools/technologies
   - Soft skills
   - Security domains to strengthen

3. CERTIFICATION ROADMAP:
   What certs make sense and in what order?
   - Entry level: Should I get Security+?
   - Intermediate: What after that?
   - Advanced: What's the end goal?
   - Cost-benefit of each
   - Which employers value most?

4. TECHNICAL SKILLS TO DEVELOP:
   Prioritized list:
   - What to learn next (top 3)
   - How to learn it (books, courses, hands-on)
   - How to practice/demonstrate skill
   - Estimated time investment

5. PRACTICAL EXPERIENCE:
   How do I get hands-on experience?
   - Projects I can do at current job
   - Home lab ideas (affordable)
   - Capture the Flag (CTF) competitions?
   - Contributing to open source?
   - Bug bounty programs?

6. 12-MONTH LEARNING PLAN:
   Month-by-month breakdown:
   - What to focus on each quarter
   - Certification timeline
   - Skills to build
   - Projects to complete
   - Milestones to hit

7. INTERVIEW PREP:
   For moving to Senior SOC Analyst:
   - What technical knowledge tested?
   - Common interview questions
   - How to demonstrate I'm ready?

8. NETWORKING/VISIBILITY:
   - Industry groups to join?
   - Conferences worth attending?
   - Online communities?
   - How to build professional network?

9. REALITY CHECK:
   - Is my 3-5 year goal realistic?
   - What might delay progress?
   - Backup plans/alternative paths?
   - What if I realize I don't like SOC work?

10. SUCCESS METRICS:
    How do I know I'm making progress?
    What should I track?
    When am I ready for next role?

Be honest about what's realistic. Give me a practical roadmap I can follow while working full-time.''',
    },
    {
        'title': 'Lesson 36: Security Training Content Creation',
        'description': 'Use AI to develop engaging security awareness content',
        'difficulty': 'intermediate',
        'order': 36,
        'points': 30,
        'instructions': '''Create engaging security training with AI! 👨‍🏫

**What You'll Learn:**
- Training content development
- Audience adaptation
- Engagement strategies
- Assessment creation

**The Challenge:**
You need to train employees on security topics, but traditional training is boring and ineffective.

**Your Prompt Should:**
1. Define training topic and audience
2. Specify desired outcome/behavior
3. Request engaging content format
4. Ask for real-world examples
5. Include assessment questions

**Your Task:**
Create an engaging security awareness module using AI.

**Real-World:**
Security awareness is required but often fails due to boring content. AI can help make it engaging!''',
        'example_prompt': '''Help me create an engaging security awareness training module.

TRAINING TOPIC: Identifying and Reporting Phishing Emails

TARGET AUDIENCE:
- All employees (250 people)
- Mix of technical levels (from receptionists to engineers)
- Ages 22-65
- Some very resistant to "more training"
- Previous training was boring PowerPoint slides (25% didn't complete)

OBJECTIVES:
After this training, employees should be able to:
1. Identify common phishing indicators
2. Know what to do when they receive suspicious email
3. Feel confident reporting (not embarrassed)
4. Understand why this matters for company

CONSTRAINTS:
- Must complete in 15-20 minutes (people won't do longer)
- Needs to work on mobile (many employees use phones)
- Must be engaging enough that people actually pay attention
- Need to measure completion and comprehension

CREATE TRAINING MODULE WITH:

1. HOOK/INTRODUCTION (2 min):
   - Grab attention immediately
   - Make it relevant to THEIR lives (not just work)
   - Real story/example that makes them care
   - No boring "cybersecurity is important" speech

2. CORE CONTENT (8-10 min):
   Teach phishing identification through:
   - Real examples (screenshot mock-ups)
   - Interactive elements (spot the red flags)
   - Simple, memorable framework (not a 20-point checklist)
   - "Why attackers do this" (understand the threat)
   
   Cover these red flags in engaging way:
   - Sender email doesn't match organization
   - Urgent/threatening language
   - Requests for credentials/personal info
   - Suspicious links (hover to reveal)
   - Grammar/spelling errors
   - Too good to be true offers
   - Unexpected attachments

3. REAL-WORLD SCENARIOS (3 min):
   3-4 interactive scenarios where they:
   - Look at email
   - Decide: Legitimate or Phishing?
   - Get immediate feedback with explanation
   - See consequences of wrong choice
   
   Make scenarios realistic to our organization:
   - HR notification
   - IT support request
   - Invoice from vendor
   - Package delivery notification

4. WHAT TO DO (2 min):
   Simple, clear instructions:
   - If you think it's phishing, do this...
   - How to report (specific steps)
   - What happens after you report
   - "You won't get in trouble for reporting!"

5. KNOWLEDGE CHECK (3 min):
   5-7 questions that:
   - Test actual understanding (not just memory)
   - Use scenario-based questions
   - Provide teaching moments in feedback
   - Required to pass (80% correct)

6. CLOSING:
   - Reinforce key message
   - Thank them for protecting the company
   - Reminder that they're part of security team
   - Easy way to ask questions later

ADDITIONAL REQUIREMENTS:

- Tone: Conversational, not lecturing
- Avoid fear tactics (empower, don't scare)
- Use humor where appropriate
- Make it feel like 15 minutes well spent
- Inclusive examples (diverse names/scenarios)
- No technical jargon

GAMIFICATION IDEAS?:
- Can we make this fun?
- Points or badges?
- Leaderboard for reporting real phishing?
- Monthly "phish of the month" showcases?

Also provide:
- Script for each section
- Suggestions for visuals/graphics
- Interactive element descriptions
- Assessment questions with answers
- Follow-up reinforcement ideas (monthly tips?)

Make this training people actually want to complete!''',
    },
    {
        'title': 'Lesson 37: Advanced Prompt Mastery - Final Challenge',
        'description': 'Demonstrate mastery of all prompt engineering techniques',
        'difficulty': 'advanced',
        'order': 37,
        'points': 50,
        'instructions': '''Master-level challenge! Combine everything you've learned! 🏆

**What You'll Learn:**
- Integrating multiple techniques
- Complex multi-step workflows
- Real-world problem-solving at scale

**The Ultimate Challenge:**
You're leading a major security initiative. Create a comprehensive prompt that demonstrates mastery of:
- Context setting
- Memory utilization
- File analysis
- Multi-step reasoning
- Role assignment
- Structured output
- Follow-up planning

**Your Task:**
Choose a complex, real-world security scenario and create a prompt that:
1. Sets comprehensive context
2. Uses memory features
3. Requests sophisticated analysis
4. Produces actionable output
5. Sets up ongoing collaboration

**This Is Your Capstone:**
Show that you can use AI as a true partner in complex security work.

**Evaluation Criteria:**
- Completeness of context
- Sophistication of request
- Practical applicability
- Use of multiple techniques
- Quality of output specification

**Real-World:**
This is how security leaders actually use AI - for complex, multi-faceted challenges that require expertise.

You've learned all the pieces. Now put them together!''',
        'example_prompt': '''[YOUR COMPREHENSIVE PROMPT HERE]

This is your chance to demonstrate everything you've learned. Create a prompt for a significant, real-world security challenge that shows mastery of:
- Advanced context setting
- Memory and continuity
- Structured analysis
- Practical outputs
- Multiple prompt engineering techniques

Choose a scenario like:
- Major incident response
- Security program development
- Complex compliance project
- Architecture transformation
- Large-scale risk assessment

Make it realistic, comprehensive, and actionable. Show what you can do!''',
    },
]
