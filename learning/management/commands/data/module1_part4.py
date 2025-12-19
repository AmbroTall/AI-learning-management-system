"""
Module 1 Part 4: Advanced Techniques & File Handling
Challenges 25-30: Working with documents and advanced prompting (3-4 hours)
"""

MODULE1_PART4_CHALLENGES = [
    {
        'title': 'Document Analysis and Summarization',
        'description': 'Learn to work with documents using AI',
        'difficulty': 'intermediate',
        'order': 25,
        'points': 35,
        'instructions': '''AI can analyze documents and extract key information.

**Real-World Scenario:**
You receive a 20-page security compliance document (ISO 27001 requirements). You need to:
- Understand the key requirements
- Identify what applies to your company
- Create an action plan

**Your Goal:**
Learn to prompt AI to analyze documents effectively.

**Challenge:**
Write a prompt that asks AI to analyze a (hypothetical) document with specific extraction goals.

**Note:** Imagine you're uploading a compliance document. What would you ask AI to extract?''',
        'example_prompt': '''I'm uploading our vendor's security compliance document (ISO 27001 requirements - 20 pages). I need your help analyzing it.

**Context:**
- Our company: Small tech startup, 30 employees
- Current security: Basic (we have firewalls, use cloud services)
- Reason: Major client requires ISO 27001 compliance
- Timeline: Need to be compliant in 6 months

**What I Need from This Analysis:**

1. **Quick Summary (3-4 sentences)**
   - What is this document about?
   - Main purpose/goal?

2. **Critical Requirements for Us (Top 5)**
   - What are the MUST-HAVE requirements?
   - Which apply to a small tech company?
   - Flag anything expensive or time-consuming

3. **Easy Wins (Quick Compliance Items)**
   - Requirements we might already meet
   - Things we can implement quickly (1-2 weeks)

4. **Major Gaps**
   - Requirements we definitely don't meet
   - Things that need significant work/budget

5. **Action Plan Template**
   - Month 1-2: [What to focus on]
   - Month 3-4: [What to focus on]
   - Month 5-6: [What to focus on]

6. **Budget Estimate**
   - Rough costs for compliance (tools, consultants, etc.)

**Output Format:**
- Use clear sections with headers
- Bullet points for scanability  
- Highlight anything CRITICAL in your summary
- Be specific about what we need to do

Make it practical and action-oriented. I need to present this to our CEO.

[NOTE: In real use, the document would be uploaded here]''',
    },
    {
        'title': 'Policy Document Creation',
        'description': 'Generate comprehensive policy documents',
        'difficulty': 'advanced',
        'order': 26,
        'points': 40,
        'instructions': '''Create complete, professional documents with AI assistance.

**Real-World Scenario:**
Your company needs a "Remote Work Security Policy" due to increase in work-from-home employees.

**Document Requirements:**
- Professional format
- Clear sections
- Specific rules (not vague)
- Employee responsibilities
- IT responsibilities
- Consequences for violations
- Approval/update process

**Challenge:**
Create a prompt that generates a complete, usable policy document.''',
        'example_prompt': '''Create a complete "Remote Work Security Policy" document for our company.

**Company Profile:**
- Tech company, 40 employees
- 60% work remotely (permanent)
- Roles: Developers, support staff, sales, management
- Handle: Customer data, payment info, proprietary code
- Tools: Slack, GitHub, AWS, Salesforce, Google Workspace

**Policy Must Cover:**

1. **Scope & Purpose**
   - Who this applies to
   - Why we have this policy
   - When it was created/last updated

2. **Acceptable Remote Work Locations**
   - Where employees can work from
   - What's NOT allowed (coffee shops with public WiFi?)
   - Travel considerations

3. **Device Security Requirements**
   - What devices are approved (company vs BYOD?)
   - Required security software
   - Encryption requirements
   - Screen locks, passwords

4. **Network Security**
   - Home WiFi security requirements
   - VPN requirements (when must they use it?)
   - Public WiFi rules
   - Guest network policies

5. **Data Handling**
   - What data can be accessed remotely
   - Downloading/storing sensitive data
   - Sharing files securely
   - Printing restrictions

6. **Physical Security**
   - Securing home office
   - Locking devices when away
   - Family/roommate access restrictions

7. **Employee Responsibilities**
   - What they must do
   - What they must NOT do
   - Reporting security incidents
   - Lost/stolen device procedures

8. **IT Department Responsibilities**
   - What IT will provide
   - Support availability
   - Monitoring (what's monitored, privacy concerns)

9. **Violations & Consequences**
   - What happens if policy is violated
   - Progressive discipline (warning → termination)

10. **Policy Acknowledgment**
    - How employees confirm they read/understand

**Format Requirements:**
- Professional document structure
- Clear section numbering (1.0, 1.1, 1.2, etc.)
- No legal jargon (plain English)
- Include a version number and date
- Add a signature section at the end

**Tone:**
- Professional but not intimidating
- Explain WHY behind rules
- Balance security with usability
- Show you trust employees

Create the complete policy document (aim for 3-4 pages when formatted).''',
    },
    {
        'title': 'Report Generation from Data',
        'description': 'Transform raw data into narrative reports',
        'difficulty': 'advanced',
        'order': 27,
        'points': 40,
        'instructions': '''Turn raw data/numbers into compelling narratives.

**Real-World Scenario:**
You ran a security audit and have raw data:
- 47 vulnerabilities found
- 12 critical, 20 high, 15 medium
- Affected systems: Web app (8), database (15), network (24)
- Estimated fix time: 120 hours
- Budget needed: $15,000

You need to write a report that:
- Tells the story (not just lists numbers)
- Shows urgency without panic
- Recommends specific actions
- Gets budget approved

**Challenge:**
Transform this raw data into a compelling executive report.''',
        'example_prompt': '''Transform this raw security audit data into an executive report that will get us the budget and resources we need.

**Raw Audit Data:**
- Total vulnerabilities: 47
- Critical: 12 (potential data breach, authentication bypass, SQL injection)
- High: 20 (XSS, outdated software, config errors)
- Medium: 15 (informational, low-impact)
- Affected systems:
  - Customer web app: 8 vulnerabilities
  - Internal database: 15 vulnerabilities  
  - Network infrastructure: 24 vulnerabilities
- Estimated fix time: 120 engineer hours
- Budget needed: $15,000 (tools, contractor help, training)
- Timeline: Critical fixes needed in 30 days, all fixes in 90 days
- Risk if ignored: Potential GDPR fine ($20M max), data breach, reputation damage

**Audience:**
- CEO (non-technical, cares about business risk)
- CFO (will approve budget, needs ROI)
- Board members (oversight, liability concerns)

**Report Structure Required:**

1. **Executive Summary (1 paragraph)**
   - What we found (in business terms)
   - Level of urgency
   - What we're asking for (budget/time)
   - What happens if we do nothing

2. **Current Security Posture**
   - Paint the picture of our situation
   - Use analogies (house with unlocked doors?)
   - Show it in context of industry standards

3. **Key Findings (The Story)**
   - Don't just list vulnerabilities
   - Group by business impact
   - Explain WHAT each means for the business
   - Use real-world breach examples

4. **Risk Analysis**
   - What's the worst that could happen?
   - Probability + Impact = Risk level
   - Compare to recent headlines (similar companies that got breached)

5. **Recommended Action Plan**
   - Phase 1 (0-30 days): Critical fixes - $8K
   - Phase 2 (30-60 days): High priority - $5K
   - Phase 3 (60-90 days): Remaining items - $2K
   - Specific deliverables for each phase

6. **Budget Justification**
   - $15K investment vs. potential $20M fine
   - Cost of data breach (avg: $4.45M per IBM study)
   - Customer trust (priceless)
   - Cheaper to fix now than after breach

7. **Next Steps**
   - Approve budget: [Date]
   - Begin work: [Date]
   - Status updates: Weekly
   - Completion: 90 days

**Tone & Style:**
- Factual but compelling
- Urgent but not alarmist
- Business-focused (not technical)
- Solution-oriented
- Include specific numbers (they're impressive)

**Length:** 2-3 pages

Make them WANT to approve this budget. Show the ROI is obvious.''',
    },
    {
        'title': 'Meeting Notes to Action Items',
        'description': 'Extract actionable items from discussions',
        'difficulty': 'intermediate',
        'order': 28,
        'points': 35,
        'instructions': '''Transform messy meeting notes into structured action plans.

**Real-World Scenario:**
Security team meeting about improving our security posture. Notes are messy (typical meeting notes). 

You need to:
- Extract all action items
- Assign owners
- Set deadlines
- Identify dependencies

**Challenge:**
Give AI your raw notes and get a structured action plan.''',
        'example_prompt': '''Transform these messy security meeting notes into a structured action plan.

**Meeting:** Security Improvement Initiative Kickoff
**Date:** January 15, 2024
**Attendees:** Sarah (CISO), Mike (IT Director), You (Security Analyst), Jennifer (HR)

**Raw Notes:**
"Sarah opened discussing recent phishing incident - 3 employees clicked bad link last week. Mike mentioned we need better email filtering, he'll look into options. Jennifer said HR can help with training but needs security team to create content. We all agreed training is priority #1. Sarah wants monthly security newsletters too.

Mike brought up vulnerability scanning - we haven't done one in 6 months (yikes). He'll schedule one for next week but needs approval for the tool renewal ($5K/year). Sarah approved pending CFO signoff.

Password policy came up - still no MFA on most systems. Mike said implementing MFA for Google Workspace is easy, can do it this month. But MFA for VPN is harder, needs new hardware ($10K). Table that for Q2.

Jennifer asked about security badges for office - currently anyone can walk in. Not really cyber security but Sarah said we should do it anyway. Mike will get quotes.

Action items (from whiteboard):
- Better email filter
- Security training
- Vulnerability scan
- MFA for Google
- Password manager rollout
- Monthly newsletter

Mike said he's slammed with other projects, can't do everything at once. Agreed to prioritize: Training first, then email filter, then MFA.

Next meeting in 2 weeks to check progress."

**Transform This Into:**

1. **Action Items Table**
   For each action, show:
   - Task description (specific)
   - Owner
   - Deadline
   - Priority (High/Medium/Low)
   - Status (Not Started/In Progress/Complete)
   - Dependencies (what needs to happen first?)
   - Budget (if applicable)

2. **Priority 1 (Must Complete This Month)**
   - List with specific success criteria

3. **Priority 2 (Complete Within Quarter)**
   - List with target dates

4. **Blockers & Dependencies**
   - What's waiting on what?
   - What needs approval/budget?

5. **Budget Summary**
   - Total budget needed
   - What needs CFO approval

6. **Next Meeting Agenda**
   - What will we review?
   - Date: 2 weeks from now

Make it crystal clear who needs to do what by when. This will be sent to all attendees.''',
    },
    {
        'title': 'Technical Documentation Simplification',
        'description': 'Make technical docs accessible to all skill levels',
        'difficulty': 'intermediate',
        'order': 29,
        'points': 35,
        'instructions': '''Create documentation that works for multiple audiences.

**Real-World Scenario:**
You wrote a detailed incident response playbook (very technical). Now you need:
- A quick reference guide for SOC analysts
- A summary for managers
- A training handout for new hires

Same content, three different audiences!

**Challenge:**
Show how to adapt one technical document for three different audience levels.''',
        'example_prompt': '''I have a technical incident response playbook (detailed). Help me create 3 versions for different audiences.

**Original Technical Playbook (Summary):**

**Incident: Suspected Data Breach**

1. **Detection & Initial Assessment** (Tier 1 SOC Analyst)
   - Monitor SIEM alerts for data exfiltration patterns
   - Check DLP (Data Loss Prevention) logs
   - Verify if alerts correlate with:
     * Unusual outbound traffic (>100MB to external IPs)
     * Off-hours database queries
     * Multiple failed authentication attempts followed by success
   - Capture: Source IP, destination IP, user account, timestamp, data volume
   - Initial severity: Low/Medium/High/Critical

2. **Escalation Criteria** (When to escalate to Tier 2)
   - Confirmed data exfiltration >1GB
   - Sensitive data types involved (PII, PHI, financial)
   - Compromised admin/privileged account
   - Lateral movement detected
   - Attack in progress (not just attempt)

3. **Containment Actions** (Tier 2 Analyst + Manager Approval)
   - Isolate affected systems (network segmentation)
   - Disable compromised accounts (AD lockout)
   - Block malicious IPs at firewall
   - Preserve logs and evidence
   - Notify: CISO, Legal, PR (if customer data)

4. **Investigation Steps** (Forensics Team)
   - Timeline reconstruction
   - Scope determination (what data, how much, where it went)
   - Root cause analysis
   - Check all systems for same vulnerability

5. **Recovery & Lessons Learned**
   - System restoration procedures
   - Vulnerability remediation
   - Post-incident report
   - Policy/process updates

**Create 3 Versions:**

**VERSION 1: Quick Reference Card (SOC Analysts)**
- One-page, laminated card format
- Checklist style
- Technical terms OK (they know them)
- Focus on: What to look for, when to escalate, immediate actions
- No long explanations
- Include key commands/tool names

**VERSION 2: Manager Summary (Security Managers)**
- 2-3 pages
- Less technical, more process-focused
- When do they need to be notified?
- What decisions do they need to make?
- Who to coordinate with?
- Flowchart or decision tree format

**VERSION 3: Training Handout (New SOC Hires)**
- 4-5 pages
- Educational tone
- Explain WHY behind each step
- Include examples
- Define technical terms
- Practice scenarios at end

Make each version appropriate for its audience. Don't just simplify - optimize for how each group will USE it.''',
    },
    {
        'title': 'Prompt Engineering Mastery Challenge',
        'description': 'Demonstrate all skills learned in Module 1',
        'difficulty': 'advanced',
        'order': 30,
        'points': 50,
        'instructions': '''Final challenge! Apply everything you've learned.

**The Scenario:**
You're a security analyst at a healthcare company. You need AI to help you:

1. Analyze a security alert
2. Write an incident report
3. Create a prevention plan
4. Draft a patient notification (if needed)
5. Update the team in Slack

This is complex and requires multiple prompts with context management.

**Challenge:**
Write a series of 3-4 prompts that:
- Build on each other
- Maintain context
- Use all techniques learned (specificity, format, tone, examples, iteration)
- Show professional real-world application

**The Alert:**
Ransomware detected on a file server containing patient medical records. Partial encryption occurred before isolation. Potentially affects 1,200 patients.''',
        'example_prompt': '''**PROMPT 1: Initial Analysis & Assessment**

I need help analyzing a critical security incident. Context first:

**My Role:** Security Analyst, Regional Medical Center (450-bed hospital)
**Incident:** Ransomware detected 45 minutes ago
**System:** File server "MED-FS-01" (patient medical records storage)
**Impact:** Partial file encryption before isolation
**Affected:** Estimated 1,200 patient records
**Current Status:** Server isolated, encryption stopped, ransom note left
**Compliance:** HIPAA-regulated (patient data)

**What I Know:**
- Ransomware: LockBit variant
- Entry point: Phishing email clicked by staff member
- Time window: 2:15 AM - 3:00 AM (45 min encryption period)
- Backup status: Last backup was yesterday 11 PM (good)
- Encrypted files: ~30% of patient records folder
- Ransom demand: $50,000 in Bitcoin

**Immediate Actions Taken:**
- Server isolated from network (2:55 AM)
- Notified on-call manager
- Preserved logs
- Blocked sender email domain
- Reset affected user's credentials

**What I Need From You:**

1. **Severity Assessment**
   - On scale 1-5, how serious is this? (consider: healthcare, HIPAA, ransomware)
   - What makes it critical vs. manageable?

2. **Immediate Next Steps (Priority Order)**
   - What must I do in the next hour?
   - What must management do?
   - Who else needs to be notified? (legal? patients? HHS?)

3. **Key Questions to Answer**
   - Can we restore from backup? (considerations?)
   - Should we pay the ransom? (pros/cons in healthcare context)
   - What's our HIPAA reporting requirement? (timeline?)

4. **Potential Consequences**
   - Best case scenario?
   - Worst case scenario?
   - Most likely scenario?

Keep it action-oriented. I need to brief my CISO in 30 minutes.

---

**PROMPT 2: Incident Report Drafting** (After AI Response)

Based on your analysis, help me draft the incident report for our CISO and compliance officer.

**Additional Details I've Gathered:**
- Confirmed: 1,247 patient records affected (file count verified)
- Data types: Names, DOB, SSN, diagnosis codes, visit dates
- No treatment data or clinical notes affected (different system)
- Backup restoration: IT says 4-hour process, 95% recovery expected
- Phishing email: Fake "IT Security Alert" sent to 45 staff, only 1 clicked
- Patient notification: Required under HIPAA within 60 days

**Report Requirements:**

**Section 1: Executive Summary**
- What happened (2-3 sentences, non-technical)
- Impact scope (how many patients, what data)
- Current status
- Immediate actions required from leadership

**Section 2: Incident Timeline**
- Detailed timeline of events (from phishing to containment)

**Section 3: Technical Details**
- Ransomware variant and behavior
- Attack vector (how it got in)
- Systems affected
- Containment measures

**Section 4: Data Breach Assessment**
- Exactly what patient data was affected
- Is this a reportable breach under HIPAA? (yes/no + reasoning)
- Notification requirements and timeline

**Section 5: Immediate Actions Needed** (Decisions for CISO/Compliance)
- [ ] Approve backup restoration (4 hours downtime)
- [ ] Do NOT pay ransom (recommendation + justification)
- [ ] Notify HHS within 60 days (required)
- [ ] Notify affected patients (mailing cost ~$2,500)
- [ ] Engage forensics firm (estimate $15K)

**Section 6: Root Cause & Prevention**
- Why this happened (phishing success)
- What we're doing differently (immediate)
- Long-term improvements needed

**Tone:** Professional, factual, urgent but not panicked. This goes to executives AND possibly regulators.

**Length:** 3-4 pages

---

**PROMPT 3: Patient Notification Letter** (After Report)

Now I need to draft the patient notification letter. Based on our discussion about the 1,247 affected patients and HIPAA requirements:

**Letter Requirements:**

**Format:** Official letter on hospital letterhead (describe structure)

**Must Include (HIPAA Requirements):**
1. What happened (simple, non-scary language)
2. What information was involved (be specific but not overly technical)
3. What we're doing about it
4. What patients should do (actionable steps)
5. Resources available (credit monitoring? hotline?)
6. How to contact us with questions

**Tone Requirements:**
- Empathetic and apologetic (we take responsibility)
- Clear and simple (8th-grade reading level)
- Reassuring but honest
- Professional but warm
- NOT defensive or making excuses

**Additional Context:**
- Our hospital has good reputation (45 years in community)
- This is our first major security incident
- We're offering 1 year free credit monitoring
- We've set up a hotline: 1-800-XXX-XXXX
- Contact: Patient Privacy Officer

**What to Avoid:**
- Legal jargon
- Minimizing the incident
- Blaming the employee who clicked
- Over-technical explanations of ransomware
- Anything that sounds like boilerplate

**Length:** 1 page (will be mailed)

Draft the letter that I'll send to legal for review.

---

**PROMPT 4: Team Slack Update** (Final)

Last task: I need to update our security team in Slack about this incident and next steps.

**Context of Slack Update:**
- Audience: 8-person security team (mix of analysts and engineers)
- They know something happened (were alerted overnight)
- Need them coordinated on next steps
- Some working on recovery, some on investigation
- Format: Slack message (can be longer, but scannable)

**What to Cover:**

**1. Incident Summary (Quick Overview)**
- What happened
- Current status
- Patient impact

**2. Great Work Shoutout**
- Thank the team for quick response
- Specific callouts (who did what well)

**3. Current Priorities** (Next 24-48 Hours)
- Backup restoration (owner: IT, we support)
- Forensics investigation (owner: Security team)
- Patient notification prep (owner: Compliance, we provide data)
- Phishing training (owner: All staff, immediate)

**4. Task Assignments**
- Who's doing what
- Any blockers or needs

**5. Lessons Already Learning**
- What went right (good backup, quick isolation)
- What needs improvement (email filtering, training)

**6. Next Team Meeting**
- When and what we'll cover

**Tone:**
- Team huddle vibe (we're in this together)
- Acknowledge it's been a tough night
- Focus on solutions
- Encourage collaboration

Keep it under 500 words but comprehensive. Make them feel informed and empowered.''',
    },
]
