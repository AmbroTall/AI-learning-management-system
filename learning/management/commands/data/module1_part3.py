"""
Module 1 Part 3: Real-World Cybersecurity & Professional Scenarios
Challenges 17-24: Practical applications from the real world (4-5 hours)
Inspired by: AI Prompt Engineering for Cybersecurity Pros
"""

MODULE1_PART3_CHALLENGES = [
    {
        'title': 'Security Incident Response Report',
        'description': 'Use AI to help document security incidents',
        'difficulty': 'intermediate',
        'order': 17,
        'points': 35,
        'instructions': '''In cybersecurity, documenting incidents clearly is critical!

**Real-World Scenario:**
You're a SOC analyst. You detected suspicious activity:
- Multiple failed login attempts from unusual IP
- Attempts targeted admin accounts
- Happened at 2AM (odd time)
- Stopped after 30 minutes

**Your Goal:**
Get AI to help you write a clear incident report for your manager.

**What to include in your prompt:**
1. The incident details (timeline, what happened)
2. Your initial assessment
3. What format you need (executive summary? technical details?)
4. Who will read it (manager? CISO? technical team?)

**Challenge:**
Write a prompt that gets AI to create a professional incident report structure you can fill in.''',
        'example_prompt': '''I need to write a security incident report for my manager. Help me structure it professionally.

**Incident Details:**
- Date/Time: Jan 15, 2024, 2:17 AM - 2:43 AM EST
- Type: Suspicious authentication attempts
- Target: Admin portal (admin.company.com)
- Source IP: 185.220.101.x (TOR exit node)
- Failed attempts: 47 login attempts across 3 admin accounts
- Pattern: Systematic username enumeration
- Action taken: IP blocked via firewall at 2:45 AM
- Result: No successful breach

**Initial Assessment:**
Likely automated brute force attack, possibly reconnaissance phase. No data compromised.

**Audience:**
Security Manager (technical but wants executive summary first)

**Request:**
Create a report structure with:
1. Executive Summary (3-4 lines, non-technical)
2. Technical Details section
3. Impact Assessment
4. Immediate Actions Taken
5. Recommended Follow-up Actions

Make it clear, professional, and action-oriented. Use security industry standard terminology.''',
    },
    {
        'title': 'Threat Intelligence Briefing',
        'description': 'Summarize complex security threats',
        'difficulty': 'intermediate',
        'order': 18,
        'points': 35,
        'instructions': '''Security professionals need to communicate threats clearly to non-technical stakeholders.

**Real-World Scenario:**
There's a new ransomware campaign targeting small businesses. You need to brief your company's leadership (non-technical) about:
- What it is
- Why it matters to your company
- What to watch for
- How to prevent it

**Your Goal:**
Get AI to help you create a clear, non-technical briefing.

**Challenge:**
Write a prompt that produces a 1-page briefing that's:
- Clear for non-technical readers
- Action-oriented
- Not fear-mongering, but serious
- Includes specific prevention steps''',
        'example_prompt': '''Create a security briefing for our leadership team about a current ransomware threat.

**Context:**
- Audience: CEO, COO, Department Heads (non-technical)
- Company: Mid-size manufacturing company, 200 employees
- Current security: Basic (firewalls, antivirus, but no advanced training)
- Recent news: Ransomware hit 3 similar companies in our industry

**The Threat:**
- Ransomware called "BlackCat" 
- Spreads via phishing emails with fake invoices
- Encrypts files and demands payment
- Targeting manufacturing/logistics sector
- Recent victim paid $150K ransom

**Briefing Requirements:**
1. **Executive Summary** (2-3 sentences: What is it? Why care?)
2. **How It Works** (Simple, no jargon, 4-5 bullets)
3. **Why We're At Risk** (Specific to manufacturing industry)
4. **Warning Signs** (What employees should watch for)
5. **Prevention Steps** (5 actionable items for leadership to approve)
6. **If It Happens** (Quick response checklist)

Tone: Professional, clear, urgent but not panicked. One page max. Use real numbers and examples. Make it scannable with headers and bullets.''',
    },
    {
        'title': 'Security Automation Workflow',
        'description': 'Design automated security processes with AI',
        'difficulty': 'advanced',
        'order': 19,
        'points': 40,
        'instructions': '''Modern SOC teams automate repetitive tasks. Learn to use AI as a planning partner.

**Real-World Scenario:**
You want to automate the response to failed login alerts. Currently, an analyst:
1. Gets alert email
2. Checks if IP is known bad actor
3. Looks up user account history
4. Decides: ignore, investigate, or block
5. Updates ticket system

You want to automate steps 1-3.

**Your Goal:**
Get AI to help you design the automation workflow.

**Challenge:**
Create a prompt that:
- Explains current manual process
- Identifies what to automate
- Asks for workflow design
- Requests pseudocode or logic flow''',
        'example_prompt': '''Help me design an automated security workflow for our SOC team.

**Current Manual Process:**
When we get a "Failed Login Alert":

1. **Alert arrives** (email from SIEM tool)
   - Contains: Username, IP address, timestamp, # of attempts
   
2. **Analyst checks threat intelligence** (manual lookup)
   - Is this IP on VirusTotal/AbuseIPDB?
   - Is it a known VPN/TOR node?
   - Any previous incidents from this IP?
   
3. **Analyst checks user history** (manual lookup)
   - Is this user traveling? (normal for new IP?)
   - Recent password changes?
   - Previous failed login patterns?
   
4. **Analyst decides** (manual judgment):
   - **Ignore:** False positive (user typo, known IP)
   - **Investigate:** Suspicious, needs deeper look
   - **Block:** Clear threat, block IP immediately
   
5. **Update ticket** (manual entry)
   - Log decision and reasoning
   - Close or escalate ticket

**What I Want to Automate:**
Steps 2-3 (lookups), and provide recommendation for step 4.

**Your Task:**
1. Design a workflow that automates the lookups
2. Show what data sources to query
3. Create decision logic (when to recommend block/investigate/ignore)
4. Write pseudocode for the automation

**Constraints:**
- We use Splunk SIEM
- Have VirusTotal API access
- Python preferred for scripting
- Need confidence score (0-100) for recommendations

Make it practical and implementable!''',
    },
    {
        'title': 'Explaining Technical Concepts Simply',
        'description': 'Translate complex security terms for stakeholders',
        'difficulty': 'intermediate',
        'order': 20,
        'points': 35,
        'instructions': '''Security pros must explain technical concepts to non-technical people!

**Real-World Scenario:**
Your manager asked: "What's the difference between a firewall and an IDS, and why do we need both?"

They're non-technical but control the budget. You need a clear explanation that:
- Avoids jargon
- Uses analogies they'd understand
- Explains the value (why spend money on both?)
- Is memorable

**Challenge:**
Get AI to explain using a business/security analogy (like building security, bank security, etc.)''',
        'example_prompt': '''I need to explain the difference between a Firewall and an IDS (Intrusion Detection System) to my non-technical manager who controls our security budget.

**Context:**
- Audience: Operations Manager, no IT background
- They understand: physical security, business risks, ROI
- Question: "Why do we need both? Isn't that redundant?"
- Budget concern: Adding IDS costs $50K/year

**Requirements:**
1. Explain each using a **physical security analogy** (building security, bank security, etc.)
2. Make it memorable and simple
3. Explain why we need BOTH (not redundant)
4. Show the business value (what risks does each prevent?)
5. Keep it under 200 words total
6. End with a clear recommendation

Avoid these terms (or explain if you must use them):
- "Packets"
- "Network traffic"  
- "Protocol"
- Any other jargon

Make them understand WHY it's worth the investment!''',
    },
    {
        'title': 'Security Policy Drafting',
        'description': 'Use AI to help create clear security policies',
        'difficulty': 'intermediate',
        'order': 21,
        'points': 35,
        'instructions': '''Good security policies are clear, specific, and enforceable.

**Real-World Scenario:**
Your company needs a "Password Policy" that employees will actually follow. It must:
- Be secure (meet industry standards)
- Be clear (no confusion)
- Be enforceable (IT can verify compliance)
- Explain WHY (so employees don't resist)

**Your Goal:**
Get AI to help draft a password policy that balances security and usability.

**Challenge:**
Create a prompt that produces a policy document with:
- Clear rules
- Explanations for each rule
- Examples
- Consequences for non-compliance''',
        'example_prompt': '''Help me draft a Password Policy for our company.

**Company Context:**
- Small business, 50 employees
- Mix of technical and non-technical staff
- Currently: No password policy (people use "123456")
- Had a phishing incident last month
- Need to comply with client security requirements

**Policy Requirements:**
Must address:
1. Password complexity (length, character types)
2. Password expiration (how often to change?)
3. Password reuse (can't use same password)
4. Multi-factor authentication (when required?)
5. Password managers (allowed? encouraged?)
6. Sharing passwords (never okay?)

**Format Needed:**
For each requirement:
- **The Rule** (clear, specific)
- **Why This Matters** (1-2 sentences, relatable)
- **Example** (good vs bad)
- **How We'll Enforce** (technical controls)
- **Exception Process** (if any)

**Tone:**
- Professional but friendly
- Explain the "why" (not just rules)
- Show you care about security AND usability
- Not intimidating or condescending

**Length:** 1-2 pages

Make it something employees will actually read and follow!''',
    },
    {
        'title': 'Vulnerability Assessment Report',
        'description': 'Communicate security findings effectively',
        'difficulty': 'advanced',
        'order': 22,
        'points': 40,
        'instructions': '''After finding vulnerabilities, you must communicate them clearly with appropriate urgency.

**Real-World Scenario:**
Your security scan found several vulnerabilities in the company's web application:
- 2 Critical (SQL injection, authentication bypass)
- 5 High (XSS, outdated libraries)
- 12 Medium (various configuration issues)
- 30 Low (informational)

You need to present this to:
1. Technical team (developers who will fix it)
2. Management (who will approve time/budget)

**Challenge:**
Get AI to help you create TWO versions of the same report - one technical, one executive.''',
        'example_prompt': '''I need to report security vulnerabilities found in our web application. Create TWO versions of the same findings.

**Vulnerability Details:**

**Critical #1: SQL Injection**
- Location: Login form (username field)
- Impact: Attacker can dump entire database
- CVSS Score: 9.8
- Exploit difficulty: Easy
- Proof of concept: Tested with: ' OR '1'='1
- Affected: All users, all data

**Critical #2: Authentication Bypass**
- Location: Password reset function
- Impact: Take over any account without password
- CVSS Score: 9.1
- Exploit difficulty: Medium
- Found: Predictable reset tokens

**High Priority (summary):**
- 5 XSS vulnerabilities (user input not sanitized)
- Outdated JavaScript libraries (jQuery 1.x - known CVEs)

**VERSION 1 - For Development Team:**
Create a technical report with:
- Exact vulnerability details
- How to reproduce
- Code snippets showing the issue
- Recommended fix (specific)
- Priority/timeline for each

**VERSION 2 - For Management/Executive:**
Create an executive summary with:
- Business impact (what could happen?)
- Risk level (Critical/High/Medium/Low explained in business terms)
- Effort required to fix (time/resources)
- Recommended action plan with timeline
- Comparison to industry standards
- No technical jargon

Both versions should convey urgency but not panic. Be factual and solution-oriented.''',
    },
    {
        'title': 'Security Training Content Creation',
        'description': 'Develop engaging security awareness materials',
        'difficulty': 'intermediate',
        'order': 23,
        'points': 35,
        'instructions': '''Security awareness training is crucial but often boring. Make it engaging!

**Real-World Scenario:**
You need to create a 5-minute security awareness lesson on "Phishing Emails" for quarterly training.

Employees typically ignore this training because it's:
- Boring and repetitive
- Not relevant to their daily work
- Too technical
- No real examples

**Your Goal:**
Get AI to help create engaging training content.

**Challenge:**
Create a prompt that produces a mini-lesson that's:
- Story-based (real scenario)
- Interactive (questions, examples)
- Memorable (key takeaways)
- Practical (what to do RIGHT NOW)''',
        'example_prompt': '''Create an engaging 5-minute security awareness lesson on phishing emails for our quarterly training.

**Audience:**
- 50 employees, various departments
- Ages 25-60, mixed tech comfort
- They think: "This doesn't apply to me"
- Previous training: Boring PowerPoints they ignored

**Lesson Requirements:**

**1. Hook (30 seconds):**
- Start with a real story/example that's relatable
- Make them think: "Wait, that could happen to me"
- No generic "cyber criminals are bad" intro

**2. The Scenario (2 minutes):**
Create a realistic phishing example that:
- Could fool anyone (not obviously fake)
- Targets something they care about (payroll, benefits, company news)
- Show the email and explain red flags

**3. Interactive Element (1 minute):**
- 3 example emails (real vs phishing)
- Ask them to spot the fake
- Explain what to look for

**4. Practical Action Steps (1 minute):**
- What to do if they receive a suspicious email (specific steps)
- Who to contact (make it easy)
- What NOT to do

**5. Memorable Takeaway (30 seconds):**
- 3-rule checklist they'll actually remember
- Make it catchy or use acronym

**Format:**
- Conversational tone
- Short paragraphs (scannable)
- Include example images (describe what they should show)
- Add quiz questions throughout
- End with "You'll remember this because..."

Make it something people actually want to read, not just click through to finish!''',
    },
    {
        'title': 'Security Metrics Dashboard Design',
        'description': 'Present security data meaningfully',
        'difficulty': 'advanced',
        'order': 24,
        'points': 40,
        'instructions': '''Security leaders need dashboards that tell a story, not just show numbers.

**Real-World Scenario:**
Your CISO asked for a monthly security dashboard. Current reports are:
- Too technical (raw numbers)
- No context (is 500 alerts good or bad?)
- No trends (can't see improvement)
- Boring (just tables of numbers)

They want a dashboard that shows:
- Are we getting better or worse?
- Where should we focus?
- What's the business impact?

**Challenge:**
Get AI to help design a meaningful security metrics dashboard.''',
        'example_prompt': '''Help me design a monthly security metrics dashboard for our CISO.

**Current Metrics We Track:**
- Failed login attempts: 15,000/month
- Blocked malware attempts: 250/month
- Phishing emails caught: 1,200/month
- Vulnerability scan findings: 150 (30 critical, 120 medium/low)
- Security incidents: 5/month
- Patch compliance: 87%
- Security training completion: 92%
- Mean time to detect incidents: 4 hours
- Mean time to respond: 12 hours

**The Problem:**
These are just numbers with no context. The CISO can't tell:
- Is 15,000 failed logins normal or a spike?
- Are we improving or getting worse?
- What needs immediate attention?
- How do we compare to industry standards?

**Dashboard Requirements:**

**Section 1: Executive Summary (Top of Dashboard)**
- 3-5 key metrics that tell the overall story
- Red/Yellow/Green indicators
- Trend arrows (↑↓→)
- One-sentence insight for each

**Section 2: Areas of Concern**
- Top 3 risks right now
- Why they matter (business impact)
- Recommended actions

**Section 3: Improvements**
- What got better this month
- Why (what we did)
- Celebrate wins!

**Section 4: Detailed Metrics**
- The full numbers (for deep dive)
- Month-over-month comparison
- Industry benchmarks (if available)

**Section 5: Action Items**
- What needs to happen next month
- Owners and deadlines

**Design Guidance:**
- How should I visualize each metric? (charts, graphs, heat maps?)
- What colors/symbols for good/bad?
- How to show trends over time?
- How to make it scannable (CISO only has 5 minutes)?

Create a detailed mockup description I can give to a designer. Explain WHY each element is included and what story it tells.''',
    },
]
