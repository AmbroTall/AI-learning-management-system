"""
Module 4B: Capstone — Cybersecurity with AI (Track B)
Challenges 1-15: Learning defensive cybersecurity and using AI as a security analysis tool
All content is educational, defensive, and professionally oriented.
"""

MODULE4B_CYBERSECURITY_CHALLENGES = [
    {
        'title': 'Question 1: Welcome to Cybersecurity',
        'description': 'Map the cybersecurity field, understand career paths, and see where AI fits in',
        'difficulty': 'beginner',
        'order': 1,
        'points': 20,
        'instructions': '''Welcome to Track B — Cybersecurity with AI. You're entering one of the most important and fastest-growing fields in technology.

**What You'll Learn:**
- What cybersecurity actually is (and what it isn't)
- The major domains and roles in the field
- How AI is transforming security work
- What a realistic cybersecurity career path looks like

**What is Cybersecurity?**
Cybersecurity is the practice of protecting systems, networks, and data from digital attacks, damage, and unauthorised access. It's fundamentally about understanding how attackers think — so defenders can stay one step ahead.

**The Major Domains:**
- **Network Security** — Protecting infrastructure and data in transit
- **Application Security** — Making software resistant to attack
- **Information Security** — Protecting data confidentiality and integrity
- **Incident Response** — Handling breaches when they happen
- **Threat Intelligence** — Understanding who's attacking and how
- **Governance, Risk & Compliance** — Frameworks, regulations, and policies

**Career Paths:**
- Security Analyst (entry point — monitoring and response)
- Penetration Tester (authorised testing of defences — requires certifications)
- Security Engineer (building secure systems)
- CISO (Chief Information Security Officer — senior leadership)
- GRC Specialist (Governance, Risk, Compliance)
- Threat Intelligence Analyst

**How AI Fits In:**
AI doesn't replace security professionals — it amplifies them. AI helps with: log analysis at scale, threat detection, report writing, research, and pattern recognition.

**Your Challenge:**
Map the cybersecurity field and understand where you could fit in. Build your "cybersecurity landscape map" using AI as your research assistant.''',
        'example_prompt': '''Map out the cybersecurity field for someone considering it as a career path. I'm 27, non-technical background (marketing), have just completed an AI skills programme. I want to understand the landscape before committing to a path.

---

**PART 1 — THE LANDSCAPE MAP**

Create a comprehensive cybersecurity field map:

**The 6 Major Domains:**
For each domain, tell me:
1. What it focuses on (2-3 sentences)
2. The key roles within it
3. The skills and knowledge required
4. Where AI is currently being used in this domain
5. Career entry options for someone non-technical

---

**PART 2 — THE THREAT LANDSCAPE**

Help me understand what cybersecurity professionals are actually defending against.

Map the types of threats:
- Organised crime (financial motivation)
- Nation-state actors (espionage, disruption)
- Hacktivists (ideological motivation)
- Insider threats (trusted employees or contractors)
- Opportunistic attackers (automated scanning and exploitation)

For each: what are they typically after? What sectors do they target? What tactics do they commonly use?

---

**PART 3 — CAREER PATH ANALYSIS**

I want to get into cybersecurity. Given my background (marketing, non-technical, AI-fluent):

1. Which cybersecurity domain offers the most accessible entry point?
2. What transferable skills do I already have?
3. What's the realistic 2-year learning journey? (Specifics — not vague "learn the basics")
4. Which certifications should I pursue first? (Give real ones with honest assessment of difficulty and cost)
5. What does an entry-level salary look like in the UK? (Be honest about ranges)
6. The single most honest piece of advice about breaking in without a technical degree

---

**PART 4 — AI'S ROLE IN SECURITY**

Where is AI specifically changing security work TODAY — not future speculation?

For each of these security tasks, explain:
- How it was done before AI
- How AI changes it now
- What AI can't do (the limits)

Tasks: Threat detection, Log analysis, Security report writing, Phishing detection, Vulnerability assessment, Incident response documentation

---

**PART 5 — MY 90-DAY PLAN**

Given everything above, design a 90-day learning plan for me:
- Specific resources (free and paid)
- What to study each month
- A project to build by day 90 that demonstrates real skills
- How to track progress
- What "ready for a first security role" looks like''',
    },
    {
        'title': 'Question 2: Types of Cyber Attacks',
        'description': 'Understand the major attack types, how they work, and how to defend against them',
        'difficulty': 'beginner',
        'order': 2,
        'points': 20,
        'instructions': '''You can't defend against what you don't understand. This lesson covers the major types of cyber attacks — from a defender's perspective.

**What You'll Learn:**
- The major attack categories (phishing, malware, social engineering, etc.)
- How each attack type works at a conceptual level
- Why each attack is effective — the psychology and technology behind it
- Defensive measures for each category

**IMPORTANT: This is Defender Education**
Understanding attacks is essential for defence. Security professionals study attack techniques so they can:
- Build systems that resist them
- Recognise them when they happen
- Train users to spot and avoid them
- Write better security policies

**Major Attack Categories:**

**Social Engineering:**
Manipulating people rather than systems. Includes phishing, vishing, pretexting, baiting.

**Malware:**
Malicious software including ransomware, trojans, spyware, keyloggers, worms.

**Network Attacks:**
Man-in-the-middle, DDoS, DNS poisoning, password attacks.

**Application Attacks:**
SQL injection, cross-site scripting (XSS), broken authentication.

**Insider Threats:**
Malicious or negligent employees, contractor access abuse.

**Your Challenge:**
Analyse 5 real-world attack examples from a defender's perspective — understanding what happened, why it succeeded, and what could have prevented it.''',
        'example_prompt': '''Analyse 5 major cyber attack types from a defender's perspective. For each, I want to understand how it works, why it succeeds, and how to defend against it.

---

**ATTACK TYPE 1: PHISHING**

Explain phishing from a defender's education perspective:

1. **How it works:** Walk through a typical phishing attack step by step — from the attacker's setup to the victim clicking a link. (Conceptual explanation, not technical instructions.)

2. **Why it works:** The psychological principles attackers exploit (urgency, authority, fear, curiosity). Why smart people fall for phishing.

3. **Real-world examples:** Describe 2-3 notable phishing incidents (named companies/incidents that are public knowledge). What happened and what was the impact?

4. **How to spot it:** A practical checklist for recognising phishing emails and messages.

5. **Defensive measures:** Technical controls (email filtering, MFA, DNS protection) AND human measures (training, reporting culture, verification procedures).

6. **As a security analyst:** If I receive a report of a suspected phishing email, what are the first 5 things I do?

---

**ATTACK TYPE 2: RANSOMWARE**

1. How ransomware works (conceptual — the victim's experience and the technical mechanism in plain English)
2. How organisations get infected (the entry vectors)
3. The business impact (downtime, ransom amounts, reputational damage — use public examples)
4. The "to pay or not to pay" dilemma — what security professionals advise and why
5. Prevention strategy: the layered defence approach
6. If I'm a security analyst and ransomware is detected at 2am: the first 10 actions

---

**ATTACK TYPE 3: SOCIAL ENGINEERING (Beyond Phishing)**

1. The full social engineering toolkit: vishing (phone), smishing (SMS), pretexting, tailgating, baiting
2. Why social engineering bypasses technical controls
3. A case study: the Twitter 2020 hack (publicly documented) — what type of social engineering was used and how it worked
4. How to build an organisational culture that resists social engineering (technical controls help, but culture is the real defence)
5. A 5-question test to assess whether your organisation is vulnerable to social engineering

---

**ATTACK TYPE 4: DENIAL OF SERVICE (DoS/DDoS)**

1. What a DDoS attack is and how it works (conceptual — overwhelming infrastructure)
2. The different types (volumetric, protocol, application layer)
3. Who performs DDoS attacks and why (motivations: extortion, hacktivism, competitive disruption)
4. Notable public DDoS events and their impact
5. Mitigation strategies available to organisations of different sizes
6. How AI and cloud tools have changed DDoS defence

---

**ATTACK TYPE 5: INSIDER THREATS**

1. The spectrum of insider threats (malicious vs negligent vs compromised)
2. Why insiders are particularly dangerous (trust, access, knowledge)
3. Warning signs of a potential insider threat (without being paranoid — the real indicators)
4. The tension between security and privacy/trust when monitoring employees
5. Technical and procedural controls that reduce insider risk
6. How to build a security culture where people report concerns about colleagues without fear

---

**SUMMARY MATRIX:**

Create a summary table:
| Attack Type | Most Common Target | Primary Entry Vector | Hardest Part to Defend | Best First Control to Implement |''',
    },
    {
        'title': 'Question 3: Network Security Fundamentals',
        'description': 'Understand how networks are protected and draw a security-aware network diagram',
        'difficulty': 'beginner',
        'order': 3,
        'points': 25,
        'instructions': '''Almost every cyber attack involves a network at some point. Understanding network security fundamentals is essential for any security career.

**What You'll Learn:**
- How networks are structured and how data moves through them
- Key network security technologies: firewalls, VPNs, IDS/IPS
- How to think about network architecture from a security perspective
- How to identify common weaknesses in network design

**Key Concepts:**

**IP Addresses and Ports:**
Every device on a network has an IP address. Every service uses a port number (e.g., HTTP = 80, HTTPS = 443, SSH = 22). Attackers probe open ports to find entry points.

**Firewalls:**
Rules-based systems that control what traffic is allowed in and out. "Default deny" means block everything not explicitly allowed — the gold standard.

**DMZ (Demilitarised Zone):**
A separate network segment for public-facing servers — isolated from the internal corporate network. If a web server is compromised, the attacker doesn't immediately have access to internal systems.

**VPN (Virtual Private Network):**
Encrypted tunnel for remote access. Protects data in transit but doesn't make the user's device secure.

**IDS/IPS:**
Intrusion Detection Systems alert on suspicious activity. Intrusion Prevention Systems also block it.

**Zero Trust:**
"Never trust, always verify" — the modern security philosophy that assumes breaches will happen and limits blast radius.

**Your Challenge:**
Draw an annotated network diagram for a small business and identify the security weaknesses in a poorly designed network vs a well-designed one.''',
        'example_prompt': '''Help me understand network security through a practical exercise: designing and evaluating network architecture for a small business.

**THE BUSINESS:**
"Brightfield Legal" — a 30-person law firm with:
- A website (externally accessible)
- A client portal (secure document sharing)
- Internal file servers (confidential client files)
- Email server
- 30 staff computers (15 in office, 15 remote workers)
- 3 printers
- A VoIP phone system
- A security camera system

---

**PART 1 — NETWORK BASICS EXPLANATION**

Before we design anything, make sure I understand the basics:

1. **Subnets:** What is a subnet and why does segmentation matter for security?
2. **Ports and services:** Explain with 5 concrete examples why knowing which ports are open matters to a defender
3. **Traffic flow:** Explain the difference between north-south traffic (in/out of the network) and east-west traffic (within the network) and why both matter
4. **The attack surface concept:** What is an "attack surface" and how does network design affect it?

---

**PART 2 — THE INSECURE NETWORK (What NOT to do)**

Design a text-based diagram of a poorly secured network for Brightfield Legal — one that a beginning IT manager might create without thinking about security.

For this insecure design, identify:
1. Every security weakness you've introduced
2. The specific attack that each weakness enables
3. The potential business impact of each weakness being exploited

---

**PART 3 — THE SECURE NETWORK DESIGN**

Now design the secure version of the same network:

Create an annotated text-based diagram showing:
- The DMZ (what goes in it and why)
- The internal network segments (what's separated from what)
- Firewall placement and rules philosophy
- VPN access points for remote workers
- Wireless network segmentation (guest vs corporate)
- The security cameras and printers isolated from the main network (and why!)

For each design decision: explain what attack you're defending against.

---

**PART 4 — FIREWALL RULES**

For Brightfield Legal's main perimeter firewall, write the rule set in plain English:

Based on the business needs above, what traffic should be:
- Allowed IN from the internet
- Allowed OUT from internal network
- Allowed between the DMZ and internal network
- Blocked in both directions

Present this as a firewall rule table with: Direction, Source, Destination, Port/Service, Action, Reason.

---

**PART 5 — REMOTE WORKER SECURITY**

15 of Brightfield's staff work remotely. This creates specific risks.

Design the remote worker security policy:
1. What technology must every remote worker use?
2. What is the acceptable use policy for personal devices?
3. What are the non-negotiable security rules for home networks?
4. How do you handle a remote worker's laptop being lost or stolen?

Write this as an actual policy document, suitable for sending to non-technical staff.

---

**PART 6 — THE SECURITY GAP ANALYSIS**

Finally, create a gap analysis for Brightfield Legal's current network (assume they have NO security controls today):

| Security Control | Current State | Risk Without It | Priority | Implementation Cost |
List 10 controls in priority order.''',
    },
    {
        'title': 'Question 4: AI as Your Security Analyst',
        'description': 'Use AI to analyse security alerts, investigate incidents, and produce professional assessments',
        'difficulty': 'intermediate',
        'order': 4,
        'points': 25,
        'instructions': '''Security analysts process hundreds of alerts every day. AI can dramatically amplify their capacity to detect, investigate, and respond to threats.

**What You'll Learn:**
- How to use AI to analyse security alerts and log data
- How to structure security analysis prompts for accurate results
- How to produce professional security assessments with AI assistance

**The Security Analyst's Challenge:**
Modern organisations generate millions of log events daily. No human team can review them all. AI helps by:
- Filtering noise from signals (most alerts are false positives)
- Correlating events across multiple systems to find patterns
- Providing context that speeds up investigation
- Drafting findings reports that used to take hours

**The AI-Analyst Workflow:**
1. Alert fires → AI pre-triage (severity, likely cause, related alerts)
2. Human review of AI triage (decide: investigate further or dismiss)
3. Investigation → AI assists with pattern analysis and research
4. AI drafts the incident report → human reviews and signs off
5. AI suggests remediation steps → human implements

**What AI Can't Do:**
- Make the final call on whether something is truly malicious
- Have context about your specific environment and history
- Take responsible action (that requires human accountability)

**Your Challenge:**
Analyse a simulated security alert using AI as your analysis assistant. Produce a professional security assessment from a given set of alerts and log data.''',
        'example_prompt': '''Use AI to analyse a security alert scenario and produce a professional security assessment. I'm learning to be a security analyst — teach me your reasoning at every step.

**THE SCENARIO:**
It's 3:47am. The security monitoring system at "Nexus Financial" (a 200-person fintech company) has triggered an alert. I'm the on-call security analyst.

**THE ALERT:**
```
ALERT: Unusual Authentication Activity
Timestamp: 2026-02-14 03:47:22 UTC
User: j.robertson@nexusfinancial.com
Alert Type: Multiple failed logins followed by successful login
Details:
  - 23 failed login attempts from IP: 185.220.101.47 (02:15 - 03:41)
  - Successful login from IP: 185.220.101.47 (03:47)
  - Geographic location: Bucharest, Romania
  - User's normal login location: Manchester, UK
  - Time since last login from UK: 18 hours
  - Current session: Active, accessing finance reporting module
```

**ADDITIONAL CONTEXT:**
- J. Robertson is the Finance Director
- The finance reporting module contains the company's complete financial records
- The company has no known business operations in Romania
- J. Robertson has not reported any travel plans

---

**PART 1 — INITIAL TRIAGE**

As my AI analysis partner, help me triage this alert:

1. **Severity Assessment:** How serious is this? Rate 1-5 and explain your reasoning using the evidence in the alert.

2. **Most Likely Explanation:** What are the 3 most likely explanations for this pattern? For each, what evidence supports or undermines it?

3. **Immediate Risk:** If this is a genuine breach, what data is at risk right now? What's the potential business impact?

4. **Time Pressure:** Does this require me to act in the next 5 minutes, 30 minutes, or can it wait until morning? Why?

---

**PART 2 — INVESTIGATION CHECKLIST**

What should I investigate to determine if this is a genuine breach?

Provide a prioritised investigation checklist — ordered by what to check FIRST:
1. [Action] → [What to look for] → [What it would indicate]

Cover checks across: authentication logs, session activity, network logs, endpoint data, HR/business context.

---

**PART 3 — ESCALATION DECISION**

Based on the available information, should I:
A) Immediately terminate the active session and lock the account
B) Monitor the session while gathering more evidence
C) Attempt to contact J. Robertson directly before taking any action

Walk me through the decision-making process. What are the risks of each option? What additional information would change your recommendation?

---

**PART 4 — INCIDENT REPORT DRAFT**

Whether or not this turns out to be a genuine attack, I need to document this. Draft a professional security incident report:

**DRAFT INCIDENT REPORT**
- Incident ID: [Generate appropriate format]
- Classification: [Suspected/Confirmed + type]
- Severity: [Your assessment]
- Timeline (in table format)
- Systems/data potentially affected
- Actions taken
- Evidence collected
- Analysis summary
- Recommended next steps
- Analyst: [My name field]

---

**PART 5 — TEACHING THE TECHNIQUE**

After working through this scenario together, explain:

1. What made this a high-priority alert vs a low-priority one? (The specific factors)
2. What is "impossible travel" and why is it a classic indicator of credential compromise?
3. How do attackers typically get credentials in the first place? (Give me context for what "led up to" this scenario)
4. What is the one security control that would have most likely prevented this specific attack?''',
    },
    {
        'title': 'Question 5: Threat Intelligence with AI',
        'description': 'Use AI to gather, analyse, and brief threat intelligence from multiple sources',
        'difficulty': 'intermediate',
        'order': 5,
        'points': 25,
        'instructions': '''Threat intelligence is about knowing your enemy before they attack — understanding who is targeting your sector, what tools they use, and what their goals are.

**What You'll Learn:**
- What threat intelligence is and how it's used
- The different sources of threat intelligence
- How AI dramatically speeds up threat research and analysis
- How to produce a professional threat intelligence briefing

**Types of Threat Intelligence:**

**Strategic:** High-level trends, threat actor motivations, geopolitical context (for senior leadership)
**Tactical:** Specific attack techniques and procedures used by threat actors (for security teams)
**Operational:** Intelligence about specific planned or in-progress attacks (rare, high-value)
**Technical:** Specific indicators (IP addresses, file hashes, domain names) used in attacks (for security tools)

**Intelligence Sources:**
- **OSINT** (Open Source Intelligence): Public reports, security blogs, government advisories
- **ISAC** (Information Sharing and Analysis Centres): Industry-specific threat sharing
- **Commercial feeds:** Paid services with curated, up-to-date indicators
- **Internal telemetry:** Your own logs and incident history
- **Dark web monitoring:** Watching for mentions of your organisation

**How AI Transforms Threat Intelligence:**
- Synthesises dozens of reports in minutes
- Identifies patterns across disparate sources
- Translates technical indicators into plain English
- Generates professional briefings from raw intelligence

**Your Challenge:**
Create a comprehensive threat intelligence briefing for a specific organisation using AI as your research and analysis assistant.''',
        'example_prompt': '''Create a complete threat intelligence briefing for a specific organisation. Use AI to research, synthesise, and present the findings professionally.

**THE ORGANISATION:**
"CityHealth NHS Trust" — a large NHS hospital trust in the UK. Key data:
- 8,000 employees
- 3 hospitals and 15 community clinics
- Patient data for 500,000 people
- Critical medical systems (patient monitoring, prescriptions, scheduling)
- 24/7 operation — downtime is a patient safety risk

---

**PART 1 — THREAT ACTOR PROFILING**

Identify the main categories of threat actors likely to target an NHS Trust.

For each category:
- What motivates them?
- What specifically about the NHS makes it a target?
- What tactics do they typically use?
- Severity of the threat (Low/Medium/High/Critical for this type of organisation)
- Examples of public attacks on healthcare organisations (use publicly known incidents)

---

**PART 2 — CURRENT THREAT LANDSCAPE**

Based on publicly available security intelligence (your training data):

1. What are the most common attack types against healthcare organisations in 2024-2025?
2. What ransomware groups have historically targeted healthcare?
3. Are there any publicly known vulnerabilities in healthcare-specific systems that remain relevant?
4. What does the UK government's NCSC currently advise about healthcare sector threats?

**Important note to the analyst:** For every piece of intelligence, cite where a real analyst would verify this (which specific NCSC, HHS, or security vendor source).

---

**PART 3 — ATTACK SCENARIO ANALYSIS**

For the three most likely attack scenarios facing CityHealth NHS Trust, analyse each one:

**Scenario template:**
- **Attack name and category**
- **Likelihood for this specific organisation** (1-5, with reasoning)
- **Potential impact** (operational, patient safety, financial, reputational)
- **Attack chain** (how would this typically unfold, step by step?)
- **Current controls** that would help (assume standard NHS setup)
- **Gaps** that need addressing
- **Early warning indicators** to watch for

---

**PART 4 — THE INTELLIGENCE BRIEFING**

Write a complete, professional Threat Intelligence Briefing document:

**Format:**
- **Classification:** RESTRICTED (internal only)
- **Executive Summary** (for CEO/Board — 150 words, no jargon)
- **Threat Landscape** (for IT leadership — key threats summarised)
- **Priority Threat: Ransomware** (detailed analysis — for CISO and security team)
- **Recommended Immediate Actions** (3 priority actions, justified)
- **Monitoring Recommendations** (what to watch for in the next 90 days)
- **Prepared by:** [Analyst name] | Date | Classification

---

**PART 5 — THE INDICATOR OF COMPROMISE (IoC) CONCEPT**

Explain to me:
1. What is an Indicator of Compromise (IoC)?
2. What types of IoCs exist? (IP addresses, file hashes, domain names, etc.)
3. How does an organisation use IoCs in their security tools?
4. Why do IoCs "expire" and become less useful over time?
5. What is a STIX/TAXII format and why does standardisation matter for threat intelligence sharing?''',
    },
    {
        'title': 'Question 6: Incident Response Fundamentals',
        'description': 'Learn the incident response lifecycle and walk through a simulated security incident',
        'difficulty': 'intermediate',
        'order': 6,
        'points': 30,
        'instructions': '''When a breach happens, the quality of your response determines the outcome. Incident response is the difference between a manageable situation and a catastrophic one.

**What You'll Learn:**
- The incident response lifecycle (preparation → detection → containment → eradication → recovery → lessons learned)
- How to run a security incident from discovery to resolution
- How AI assists at each stage of incident response
- How to produce professional incident documentation

**The Incident Response Lifecycle:**

**1. Preparation:** Building the capability BEFORE an incident — playbooks, tools, trained team, communication plans.

**2. Detection & Analysis:** Identifying that an incident has occurred and understanding its scope.

**3. Containment:** Stopping the bleeding — preventing the attacker from doing more damage. Short-term (isolate affected systems) and long-term (patch vulnerabilities, rotate credentials).

**4. Eradication:** Removing the threat completely — malware removal, attacker access revoked, vulnerabilities closed.

**5. Recovery:** Restoring normal operations safely — bringing systems back online, verifying integrity, monitoring closely.

**6. Post-Incident Review:** Learning from what happened to prevent recurrence.

**The "Golden Hour" in IR:**
The first hour after detection is the most critical. Every minute of delay gives the attacker more time to move laterally, exfiltrate data, or establish persistence.

**Your Challenge:**
Walk through a complete security incident from detection to post-incident report — making the key decisions at each stage.''',
        'example_prompt': '''Walk me through a complete security incident from detection to post-incident review. Make the key decisions at each stage and teach me the incident response discipline.

**THE INCIDENT:**
It's Monday morning, 9:15am. A member of staff at "Greenway Insurance" (a 150-person UK insurance broker) reports that her computer is displaying a ransom note. Her name is Karen Watts, she works in the claims processing department. The message says all files are encrypted and demands Bitcoin payment.

Your role: Lead Incident Responder. You have a team of 2 analysts.

---

**PHASE 1 — DETECTION & FIRST RESPONSE (9:15am - 9:30am)**

You've just been told about Karen's screen. What are your exact first actions in the first 15 minutes?

Give me a minute-by-minute timeline:
- 9:15: [What do you do first?]
- 9:17: [Next action?]
- 9:20: [What do you need to know by now?]
- 9:25: [Key decision point]
- 9:30: [Status at 30 minutes]

For each action: explain WHY this order, and what information you're trying to get.

---

**PHASE 2 — CONTAINMENT DECISION (9:30am)**

You've confirmed: ransomware is active on Karen's computer. You don't yet know how far it's spread.

The board is asking: "Should we shut down all systems immediately?"

Help me think through this decision:
1. What are the arguments FOR an immediate full shutdown?
2. What are the arguments AGAINST (what do you lose by shutting down)?
3. What is the middle-ground option (targeted containment)?
4. Given a 150-person insurance company, what's your recommendation?
5. If you choose NOT to shut down, what specific monitoring do you implement immediately?

---

**PHASE 3 — SCOPING THE INCIDENT (9:30am - 11:00am)**

You've contained Karen's machine. Now you need to understand the scope.

Design the investigation plan:
1. What logs do you look at first? (Be specific — what systems, what time range, what to look for)
2. What questions are you trying to answer in this phase?
3. How do you identify which other systems may be infected?
4. What's the "patient zero" investigation? (Finding how ransomware got in)
5. When do you call in external incident response help?

---

**PHASE 4 — COMMUNICATION (Ongoing)**

Who needs to know what, and when?

Create a communications plan covering:
- Internal: Which staff, what message, when
- Senior leadership/Board: What they need to know, what not to alarm them with yet
- Customers: Do they need to be notified? When? (Consider GDPR implications)
- Regulators: FCA notification requirements for a UK insurance broker
- Law enforcement: When to involve police/NCSC?
- External comms/PR: Is there a media risk? How to prepare

---

**PHASE 5 — POST-INCIDENT REPORT**

48 hours later, the incident is contained. Draft the executive post-incident report:

**INCIDENT REPORT**
- Incident ID and classification
- Executive Summary (Board-level, non-technical, 200 words)
- Timeline (key events from initial infection to containment — as a table)
- Root cause analysis (how did the attacker get in?)
- Impact assessment (systems affected, data exposed, business disruption)
- Response actions taken
- Lessons learned (what would have changed the outcome?)
- Recommended improvements (priority order, with resource estimate)

---

**PHASE 6 — BUILDING BETTER DEFENCES**

Based on this incident, what 5 security improvements would have the biggest impact on preventing the next one?

For each: what it is, what attack it prevents, approximate cost/effort, and why it's prioritised over other options.''',
    },
    {
        'title': 'Question 7: Security Report Writing',
        'description': 'Master professional security report writing for technical and executive audiences',
        'difficulty': 'intermediate',
        'order': 7,
        'points': 30,
        'instructions': '''Security professionals who can write clearly have a significant career advantage. Most security findings die in technical reports that executives don't read.

**What You'll Learn:**
- How to structure security reports for different audiences
- How to translate technical findings into business risk language
- How to write recommendations that actually get implemented
- Using AI to draft and refine professional security reports

**The Two Audiences Problem:**
Every security report needs to work for two very different readers:

**Technical Audience (Security Team, IT):**
- Needs specific technical details
- Wants to know exactly what was found and how
- Needs clear, actionable remediation steps
- Uses technical terminology

**Executive Audience (CEO, Board, Investors):**
- Needs business risk language, not technical language
- Wants to know: are we safe? What should we spend money on?
- Needs clear priorities and resource implications
- Must not be overwhelmed with technical detail

**The Golden Rules of Security Report Writing:**
1. Lead with the risk to the business, not the technical finding
2. Every recommendation must have a clear rationale
3. Prioritise by business impact, not technical severity
4. Provide effort/cost estimates for recommendations
5. Be direct — avoid hedging everything with caveats

**Your Challenge:**
Write a complete security report for a simulated vulnerability discovery — producing both a technical version and an executive version from the same findings.''',
        'example_prompt': '''Write a complete professional security report for a simulated vulnerability assessment finding. I need both a technical version and an executive version.

**THE FINDING:**
You've completed a security assessment of "TechVenture Solutions" (a 50-person SaaS company, Series A startup). You discovered a significant vulnerability.

**Technical Finding:**
During assessment of the customer-facing web application, you discovered that the password reset functionality is vulnerable to account takeover. Specifically:
- The password reset token is predictable (based on timestamp + user ID with weak hashing)
- Token expiry is 24 hours (industry standard is 15-30 minutes)
- There is no rate limiting on token attempts (allows brute force)
- No account lockout after failed reset attempts
- The issue affects all 15,000 user accounts on the platform

**Business Context:**
- TechVenture processes payment data for their customers
- They are pursuing SOC 2 Type II certification (this would fail the audit)
- A competitor was breached last year via a similar vulnerability — received significant press coverage
- Fix complexity: Medium (estimated 3-5 developer days)

---

**DOCUMENT 1: TECHNICAL VULNERABILITY REPORT**

Write the complete technical finding report:

**Vulnerability Details:**
- Title: [Professional naming convention]
- CVSSv3 Score: [Calculate and justify]
- Severity: [Critical/High/Medium/Low with rationale]
- OWASP Category: [Which OWASP Top 10 category?]
- CWE Reference: [Common Weakness Enumeration number]

**Description:**
Technical explanation of the vulnerability, how it works, and what it enables.

**Proof of Concept:**
Describe (without creating a working exploit) how a researcher demonstrated this vulnerability exists. What steps did they take to verify it?

**Impact:**
Technical and business impact if exploited.

**Remediation:**
Specific, actionable steps with code examples or configuration changes (at a conceptual level):
1. [Fix 1 — specific step]
2. [Fix 2 — specific step]
3. [Fix 3 — specific step]

**References:**
Relevant CVEs, OWASP documentation, best practice standards.

---

**DOCUMENT 2: EXECUTIVE SUMMARY REPORT**

Write the executive-facing version of the same finding.

This goes to the CEO and CTO. They are technically literate but not security experts. They need to make a business decision.

Structure:
1. **The Risk** (Plain English — what could happen if this isn't fixed?)
2. **The Finding** (One paragraph — what was discovered, without jargon)
3. **Who is Affected** (What is the scope — customers, data, compliance?)
4. **What We Recommend** (Clear action, not vague advice)
5. **Urgency** (Why now? What is the window to fix this before risk materialises?)
6. **Resource Requirement** (What will it cost in time and money to fix?)
7. **What Happens If We Don't Act** (Be direct — what's the realistic downside?)

---

**DOCUMENT 3: THE FULL ASSESSMENT REPORT**

Structure a complete assessment report showing where this finding sits in context:

**Report Cover Page** (what information goes here?)
**Executive Summary** (one page for leadership — the top 3 findings and their business risk)
**Methodology** (how the assessment was conducted, scope, tools used)
**Findings Summary Table** (all findings, colour-coded by severity)
**Detailed Finding #1** (the password reset vulnerability above)
**[Additional findings sections]**
**Remediation Roadmap** (priority order for fixing all findings)
**Appendices** (technical details, tool output, raw evidence)

---

**PART 4 — THE VERBAL PRESENTATION**

You need to present this to the TechVenture board in 5 minutes. Write the talking points:
- What to say in the first 30 seconds to get their attention
- The 3 things the board must understand
- The single ask you're making
- How to answer: "Should we be scared?" (Honest but constructive)
- How to answer: "Can we fix it ourselves or do we need outside help?"''',
    },
    {
        'title': 'Question 8: Password Security & Authentication',
        'description': 'Understand password security, MFA, and modern authentication — and audit a company\'s approach',
        'difficulty': 'intermediate',
        'order': 8,
        'points': 30,
        'instructions': '''Weak authentication is involved in over 80% of data breaches. Understanding how authentication really works — and how attackers defeat it — is foundational security knowledge.

**What You'll Learn:**
- Why passwords fail as a sole security control
- How password attacks work (from a defender's education perspective)
- Multi-factor authentication: types, strengths, and weaknesses
- Modern authentication: passwordless, SSO, and zero-trust approaches
- How to design and audit an authentication policy

**Why Passwords Fail:**
- Users reuse passwords across sites
- Weak passwords are easily guessed
- Phishing captures credentials directly
- Credential stuffing uses breached databases
- Even strong passwords can be brute-forced given enough time

**How Attackers Defeat Passwords (Defender Education):**

**Credential Stuffing:** Using username/password pairs from previous data breaches on new sites. Works because 65% of people reuse passwords.

**Password Spraying:** Trying common passwords (Password1, Summer2024) against many accounts. Avoids lockout policies.

**Phishing:** Tricking users into entering credentials on fake sites.

**Brute Force:** Systematically trying all combinations. Effective against weak passwords or offline hash cracking.

**Multi-Factor Authentication (MFA):**
Requires something you know (password) + something you have (phone/hardware key) + something you are (biometric). Even if a password is compromised, MFA prevents access.

**Your Challenge:**
Audit a fictional company's authentication posture and write a comprehensive improvement plan.''',
        'example_prompt': '''Conduct a complete authentication security audit for a fictional company and produce a prioritised improvement plan.

**THE COMPANY:**
"Pinnacle Accounting" — a 75-person accountancy firm handling sensitive financial data for 200+ business clients. They process payroll, tax returns, and financial statements.

**CURRENT AUTHENTICATION SETUP (from my audit):**
- Employees use Active Directory with a 90-day password expiry policy
- Minimum password length: 8 characters, complexity not enforced
- No MFA on any systems
- Remote access via VPN — username and password only
- Client portal uses basic username/password (no MFA option)
- Shared admin passwords for some systems ("IT knows them")
- No single sign-on — employees have 8-12 different passwords
- Password reset via helpdesk call-back (anyone who knows the employee's name and department)
- Last password policy review: 2018

---

**PART 1 — CURRENT RISK ASSESSMENT**

Assess the authentication risk at Pinnacle:

1. **Risk Score:** Rate 1-10 and justify with specific reference to the above setup.

2. **Attack Scenarios:** For each of these attack types, is Pinnacle currently vulnerable?
   - Credential stuffing (using leaked passwords from other breaches)
   - Password spraying
   - Phishing capture of credentials
   - VPN account takeover
   - Helpdesk social engineering

3. **The Highest Priority Risk:** Which single vulnerability should they fix FIRST and why?

---

**PART 2 — MODERN AUTHENTICATION EDUCATION**

Explain these authentication concepts so I can include them in my recommendations:

**Multi-Factor Authentication Types:**
| MFA Type | How it works | Security level | Phishing resistant? | Best for |
Cover: SMS OTP, Authenticator app, Hardware security key (YubiKey), Push notifications, Passkeys

**Why Some MFA is Better Than Others:**
Explain why SMS MFA is better than no MFA but worse than app-based MFA — with a specific scenario showing when SMS MFA fails.

**Passwordless Authentication:**
What is it? How does it work? Is it actually more secure than passwords? What would implementing it at Pinnacle require?

**Single Sign-On (SSO):**
What problem does it solve? How does it improve both security and user experience? What's the risk of getting it wrong?

---

**PART 3 — THE AUTHENTICATION IMPROVEMENT PLAN**

Design a complete, prioritised improvement plan for Pinnacle Accounting:

**Phase 1 (Weeks 1-4): Quick Wins**
What can be improved immediately with minimal cost and disruption?

**Phase 2 (Months 2-3): Core Improvements**
What are the foundational changes?

**Phase 3 (Months 4-6): Advanced Controls**
What's the mature state to aim for?

For each phase, include:
- Specific changes to make
- Tools/products required (with realistic UK cost estimates)
- Staff communication plan (how to explain changes without causing panic)
- How to measure whether it's worked

---

**PART 4 — THE AUTHENTICATION POLICY**

Write a professional Authentication and Password Policy for Pinnacle Accounting.

Sections:
1. Purpose and scope
2. Password requirements (what the policy requires — and why, briefly)
3. MFA requirements (who must use it, on what systems)
4. Shared account rules
5. Password reset procedure (secure version)
6. Remote access authentication
7. Third-party and client portal access
8. User responsibilities
9. Enforcement and non-compliance

Make this readable by non-technical staff. Aim for under 600 words. Avoid jargon.

---

**PART 5 — STAFF AWARENESS**

Write the staff email announcement for rolling out MFA at Pinnacle:
- Why we're doing this (business reason, not just IT policy)
- What will change for them (be specific about the experience)
- When it's happening
- What they need to do to prepare
- Who to contact for help
- Reassurance that this is straightforward (because it is)

Max 250 words. Tone: helpful and reassuring, not alarmist.''',
    },
    {
        'title': 'Question 9: Social Engineering Defence',
        'description': 'Build an awareness training programme and test organisational resilience to social engineering',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 30,
        'instructions': '''Technology can be patched. Humans are harder to update. Social engineering exploits human psychology — and defending against it requires education, culture, and process.

**What You'll Learn:**
- The psychology behind why social engineering works
- How to design effective security awareness training
- How to build a culture where people report suspicious activity
- How organisations test their defences against social engineering

**Why Social Engineering Is So Effective:**
Social engineers exploit universal human tendencies:
- **Authority:** We comply with figures of perceived authority
- **Urgency:** We make poor decisions under time pressure
- **Reciprocity:** We feel obligated to return favours
- **Social proof:** We follow what others do
- **Fear:** We act to avoid perceived consequences
- **Liking:** We help people we like or feel connected to

**Common Attack Scenarios:**
- CEO fraud (impersonating executives in urgent email requests)
- IT helpdesk impersonation (calling employees claiming to be IT support)
- Vendor impersonation (fake invoices or account changes)
- Physical tailgating (following someone through a secure door)
- Vishing (voice phishing calls to extract information)

**Building a Defensive Culture:**
Technical controls help, but culture is the real defence. Employees should:
- Feel comfortable questioning unusual requests
- Know how to verify someone's identity
- Have a clear process to report suspicious contact
- Feel rewarded (not embarrassed) for reporting near-misses

**Your Challenge:**
Create a complete social engineering awareness training presentation for a non-technical workforce.''',
        'example_prompt': '''Create a complete social engineering awareness training programme for a non-technical workforce. This should actually change behaviour — not just tick a compliance box.

**THE ORGANISATION:**
"Halifax Housing Association" — a 120-person not-for-profit managing social housing. Staff includes: housing officers, repairs coordinators, finance team, HR, and management. Average tech literacy: moderate. They've had 2 phishing incidents in the past year — one resulted in a staff member transferring £4,000 to a fraudster posing as a supplier.

---

**PART 1 — THE TRAINING CONTENT**

Design a 45-minute interactive training session.

**Opening Hook (5 minutes):**
Write the opening scenario you'd use to grab the room's attention. Not a lecture — something that makes people feel it COULD happen to them. Use the real incident from their organisation (anonymised) if appropriate.

**Module 1: How Attackers Think (10 minutes)**
Explain social engineering psychology to a non-technical audience.
- The 5 psychological triggers (with workplace examples for each)
- Why smart people fall for scams
- Why "it won't happen to me" is the most dangerous attitude

**Module 2: The Attack Scenarios You'll Face (15 minutes)**
Walk through 4 realistic attack scenarios relevant to a housing association:
1. Fake supplier email requesting bank account change
2. Caller claiming to be from IT asking for system access to "fix a problem"
3. Urgent "CEO" email requesting a payment or sensitive information
4. Friendly visitor who follows a staff member through a secure door

For each scenario: describe it in detail, what the social engineer says/does, what red flags are present, and what the correct response is.

**Module 3: The Verification Toolkit (10 minutes)**
Give staff concrete tools:
- The "pause and verify" rule
- How to verify someone's identity (the right way)
- The "it's OK to say no" permission — make it explicit
- Your organisation's specific reporting process

**Closing (5 minutes):**
End on a positive, empowering note — not with fear. What message do you want people leaving with?

---

**PART 2 — THE REALISTIC SCENARIOS EXERCISE**

Create 5 scenario cards for a table exercise. Each card describes a situation and asks: "What do you do?"

For each scenario: the situation, the pressure or psychological trigger being applied, the correct action, and the explanation of why.

Make them realistic for a housing association context (not generic examples).

---

**PART 3 — THE REPORTING CULTURE**

Design a "See Something, Say Something" reporting culture:

1. Why most people DON'T report suspicious activity (and how to fix this)
2. The specific process for reporting at Halifax Housing (step by step)
3. What happens after a report is made (the feedback loop that encourages more reporting)
4. How to celebrate near-misses as successes, not embarrassments
5. The monthly security communication that keeps awareness alive without becoming background noise

---

**PART 4 — TESTING THE TRAINING**

Describe (at a conceptual level, without providing operational details) how organisations ethically test social engineering awareness:

1. What is a simulated phishing test and what does it measure?
2. What are the ethical requirements of running phishing simulations? (Consent, purpose, no punishment)
3. What metrics indicate the training is working?
4. How often should awareness training be refreshed?
5. What's the most common mistake organisations make with security awareness programmes?

---

**PART 5 — THE POLICY THAT SUPPORTS THE TRAINING**

Write a "Social Engineering and Fraud Prevention" policy for Halifax Housing:
- Clear rules for verifying requests (financial, data access, physical)
- What to do when something seems wrong
- Reporting requirements
- What staff will NOT be penalised for (good faith reports and refusals)
- Maximum 400 words — short enough that people will actually read it''',
    },
    {
        'title': 'Question 10: Vulnerability Assessment',
        'description': 'Conduct a simulated vulnerability assessment and produce a prioritised findings report',
        'difficulty': 'advanced',
        'order': 10,
        'points': 35,
        'instructions': '''Vulnerability assessment is the systematic process of identifying, classifying, and prioritising security weaknesses — before attackers find them.

**What You'll Learn:**
- The vulnerability assessment methodology
- How to identify, classify, and score vulnerabilities
- How to prioritise remediation based on risk
- Producing professional assessment reports

**Vulnerability Assessment vs Penetration Testing:**
These are often confused but they're different:

**Vulnerability Assessment:**
- Identifies potential weaknesses (does this vulnerability EXIST?)
- Broader scope, less deep
- Typically automated + manual review
- Produces a list of findings to remediate

**Penetration Testing:**
- Actively attempts to exploit vulnerabilities (can this weakness actually be used by an attacker?)
- Deeper, narrower scope
- Primarily manual (skilled human tester)
- Simulates a real attack scenario

**The CVSS Scoring System:**
The Common Vulnerability Scoring System scores vulnerabilities 0-10:
- **0.0 - 3.9:** Low
- **4.0 - 6.9:** Medium
- **7.0 - 8.9:** High
- **9.0 - 10.0:** Critical

**The Prioritisation Challenge:**
A high CVSS score doesn't always mean "fix first." You must consider:
- Is this system actually exposed to the internet?
- Is there compensating controls that reduce risk?
- What's the business impact if this is exploited?
- How easy is the fix vs risk if left open?

**Your Challenge:**
Conduct a simulated vulnerability assessment of a fictional web application and produce a complete, prioritised findings report with AI assistance.''',
        'example_prompt': '''Conduct a simulated vulnerability assessment of a fictional web application and produce a complete professional report. Teach me the assessment methodology and risk-rating approach throughout.

**THE TARGET:**
"PolicyHub" — a web application used by a medium-size insurance company. It allows insurance brokers to:
- Log in and access client policy documents
- Submit new policy applications
- Generate policy quotes with pricing calculations
- Download policy documents as PDFs
- Message the insurer's team

**SCOPE OF ASSESSMENT:**
- The PolicyHub web application (not the underlying infrastructure)
- Publicly accessible features (not requiring admin access)
- Timeframe: 3-day assessment simulation

**KNOWN TECHNICAL DETAILS:**
- Built on Python/Django framework
- PostgreSQL database
- Document storage on AWS S3
- User authentication: username/password (no MFA currently)
- Session management: cookies with 24-hour expiry
- Password reset: email link, 1-hour token expiry
- File upload: allows PDF, DOC, DOCX uploads for policy documents

---

**PART 1 — ASSESSMENT METHODOLOGY**

Before reviewing findings, explain the web application assessment methodology:

1. **Reconnaissance phase:** What information would an assessor gather about PolicyHub before active testing? (Publicly available information only — OSINT)

2. **The OWASP Top 10:** What is OWASP? Briefly explain the current OWASP Top 10 web application risks and which ones are most relevant to a Django-based insurance application.

3. **Testing approach:** What are the main testing categories for a web application assessment? (Authentication, authorisation, input validation, etc.)

---

**PART 2 — SIMULATED FINDINGS**

Based on the technical details provided, here are 6 simulated findings from the assessment. For each finding, write the complete vulnerability report entry:

**Finding 1: Insecure Direct Object Reference (IDOR)**
Description: Changing the document_id parameter in the URL (/documents/12345/download) allows access to documents belonging to other brokers.

**Finding 2: Missing Multi-Factor Authentication**
Description: Administrative and broker accounts rely on password-only authentication.

**Finding 3: Unrestricted File Upload**
Description: The document upload function accepts file types beyond PDF/DOC/DOCX and doesn't validate file content.

**Finding 4: Information Disclosure in Error Messages**
Description: Detailed Django debug error pages are visible to unauthenticated users when errors occur, revealing technical stack details.

**Finding 5: Weak Session Management**
Description: Session cookies are not set with the Secure and HttpOnly flags, and sessions don't invalidate after logout on the server side.

**Finding 6: Outdated Third-Party Components**
Description: Several Django packages and JavaScript libraries are more than 18 months behind current version with known CVEs.

**For each finding, write:**
- CVSS v3.1 Base Score and vector string
- Severity classification (Critical/High/Medium/Low)
- Description (plain English, what it is and why it matters)
- Business impact (if exploited in the context of an insurance application)
- Evidence description (how was this identified?)
- Remediation recommendation (specific, actionable steps)
- Estimated fix effort (hours/days)

---

**PART 3 — RISK PRIORITISATION**

Now prioritise the 6 findings. Create a risk matrix:

| Finding | CVSS | Business Impact | Exploitability | Fix Effort | PRIORITY |

Explain your prioritisation logic — why is the #1 priority #1? Is a CVSS 9.0 necessarily the first to fix?

---

**PART 4 — THE EXECUTIVE SUMMARY**

Write the executive summary for the assessment report:
- Overall security posture rating (1-5 stars with justification)
- The single most important thing the CEO should know
- The top 3 priorities with business risk language (not technical language)
- Recommendation for next steps (reassessment timeline, penetration test?)
- Resources required for remediation (rough estimate of effort/cost)

---

**PART 5 — REMEDIATION ROADMAP**

Design a 90-day remediation roadmap for PolicyHub's development and security teams:
- Week 1-2: Critical immediate actions
- Weeks 3-6: High priority remediations
- Weeks 7-12: Medium priority and hardening
- Ongoing: Monitoring and process improvements''',
    },
    {
        'title': 'Question 11: Security Policies & Compliance',
        'description': 'Write real-world security policies aligned with GDPR, ISO 27001, and Cyber Essentials',
        'difficulty': 'advanced',
        'order': 11,
        'points': 35,
        'instructions': '''Security policies are the foundation of any security programme. Without clear policies, you can't consistently enforce controls, demonstrate compliance, or hold people accountable.

**What You'll Learn:**
- The major security frameworks and what they require
- How to write policies that are actually followed
- How to map controls to compliance requirements
- How AI helps accelerate policy development

**The Major Frameworks:**

**Cyber Essentials (UK Government):**
Five basic controls: firewalls, secure configuration, user access control, malware protection, patch management. Basic certification that many government contracts require.

**ISO 27001:**
International standard for Information Security Management Systems. Comprehensive, risk-based approach. Certification demonstrates serious security commitment.

**GDPR / UK GDPR:**
Data protection law. Requires appropriate technical and organisational measures to protect personal data. Non-compliance: up to £17.5m or 4% of global turnover.

**NIST Cybersecurity Framework:**
US framework widely used globally. Five functions: Identify, Protect, Detect, Respond, Recover.

**SOC 2:**
Service organisation security auditing standard. Type I (point in time) or Type II (over a period). Often required by enterprise customers.

**The Policy Writing Challenge:**
Most security policies are either (a) too long and never read, or (b) too vague to be actionable. The best policies are:
- Short enough to be read
- Clear enough to be followed
- Specific enough to be enforced

**Your Challenge:**
Write a complete Data Protection Policy aligned with UK GDPR requirements for a specific business scenario.''',
        'example_prompt': '''Write a complete, compliance-aligned Data Protection Policy for a small business. I want to understand the GDPR requirements AND produce a policy that people will actually follow.

**THE BUSINESS:**
"ClearPath Recruitment" — a 25-person recruitment agency specialising in technology sector placements. They process:
- Candidate personal data (CVs, contact details, employment history, references)
- Client company contact data (hiring managers, HR contacts)
- Financial data (payment details for invoicing)
- Sensitive data (some candidates have DBS checks processed)
- Communications data (email threads, meeting notes)

**CURRENT SITUATION:**
- No formal data protection policy exists
- They have a part-time "data protection contact" who is actually the operations manager
- They've never done a formal data audit
- They use: Gmail, Salesforce CRM, LinkedIn Recruiter, Dropbox for document storage
- No formal subject access request process
- Candidate data is kept indefinitely "in case they become useful again"

---

**PART 1 — GDPR FUNDAMENTALS FOR THIS CONTEXT**

Before writing the policy, explain the GDPR requirements most relevant to a recruitment agency:

1. **Lawful Basis for Processing:** Which lawful bases apply to a recruiter's data processing? (Legitimate interests, contract, consent — when is each appropriate?)

2. **Special Category Data:** What is special category data and does a recruitment agency handle it? What additional protections apply?

3. **Retention Periods:** How long can a recruiter legally retain candidate data? What does "as long as necessary" actually mean in practice?

4. **Subject Rights:** List all 8 data subject rights and which ones are most likely to be exercised by candidates (with realistic scenarios).

5. **ICO Registration:** Does ClearPath need to be registered with the ICO? What does this involve?

---

**PART 2 — THE DATA AUDIT**

Before writing a policy, you need to know what data you have. Design a data audit for ClearPath:

Create a "data register" (also called a Record of Processing Activities / ROPA) template:

| Data Category | Data Subjects | Data Types | Lawful Basis | Retention Period | Storage Location | Third Party Sharing | Risk Level |

Fill in 5 rows with realistic data for a recruitment agency.

---

**PART 3 — THE DATA PROTECTION POLICY**

Write the complete Data Protection Policy. It must be:
- Compliant with UK GDPR
- Readable by non-legal staff
- Under 1,000 words (concise policies get read)
- Signed off at board level (state who would sign)

**Sections to include:**
1. Policy Statement (why we care, what this commits us to)
2. Scope (who this applies to)
3. Our Data Protection Principles (the 6 GDPR principles, in plain English)
4. What Data We Collect and Why (summary for each data category)
5. How Long We Keep Data (clear retention periods)
6. Data Subject Rights (how people can exercise them)
7. Data Security (what controls we maintain)
8. Data Breaches (what to do when something goes wrong)
9. International Transfers (if applicable)
10. Questions and Reporting Concerns

---

**PART 4 — THE CANDIDATE PRIVACY NOTICE**

Write the privacy notice that ClearPath sends to every candidate:
- What data is collected
- Why it's collected and the lawful basis
- How long it's kept
- Who it's shared with
- Their rights and how to exercise them
- Contact details for questions

Keep it under 400 words. Make it genuinely readable — not legal boilerplate.

---

**PART 5 — DATA BREACH RESPONSE PROCEDURE**

Write a step-by-step data breach response procedure for ClearPath:

- How to recognise a data breach (it's not always obvious)
- The 72-hour ICO reporting rule (when does it apply? How to report?)
- Internal reporting chain
- Whether to notify affected individuals (and when it's required vs discretionary)
- Documentation requirements
- Post-breach review process

Make this practical enough that the operations manager could follow it at 11pm on a Friday.''',
    },
    {
        'title': 'Question 12: Secure Communication & Encryption',
        'description': 'Understand how encryption protects data and create secure communication guidelines',
        'difficulty': 'intermediate',
        'order': 12,
        'points': 30,
        'instructions': '''Encryption is the foundation of digital security. Understanding how it works — without needing to implement it yourself — is essential for security professionals.

**What You'll Learn:**
- How encryption works at a conceptual level
- The difference between symmetric and asymmetric encryption
- How HTTPS, email encryption, and VPNs protect data
- How to communicate encryption concepts to non-technical stakeholders

**Encryption Fundamentals:**

**Symmetric Encryption:**
The same key encrypts and decrypts. Fast, but the key must be shared securely. Used for: encrypting files, database encryption (AES-256 is the standard).

**Asymmetric Encryption:**
Two keys — a public key (share freely) and a private key (keep secret). What the public key encrypts, only the private key can decrypt. Used for: SSL/TLS certificates, digital signatures, key exchange.

**How HTTPS Works:**
1. Browser requests secure connection
2. Server sends its public key (in a certificate signed by a trusted authority)
3. Browser verifies the certificate
4. Browser uses the public key to securely exchange a session key
5. From this point, all traffic is encrypted with the session key

**Common Encryption Standards:**
- **AES-256:** Gold standard for data at rest
- **TLS 1.3:** Current standard for data in transit (HTTPS)
- **RSA-2048/4096:** Asymmetric, used in certificates
- **SHA-256:** Hashing (not encryption — one-way, for verifying integrity)

**Why Encryption Isn't Enough:**
- Encryption protects data in transit and at rest
- It does NOT protect against compromised endpoints
- It does NOT protect against users sharing their own credentials
- Key management is as important as the algorithm

**Your Challenge:**
Explain encryption to a non-technical manager, then create a "Secure Communication Checklist" for a small business.''',
        'example_prompt': '''Help me explain encryption to a non-technical audience and create practical secure communication guidance for a small business.

---

**PART 1 — EXPLAINING ENCRYPTION WITHOUT JARGON**

I need to explain HTTPS and email encryption to the board of a small business. They're intelligent but not technical.

**Section A: The Locked Box Analogy**
Create a clear, memorable analogy for how HTTPS works. The analogy should:
- Explain why a padlock icon in a browser matters
- Explain what it doesn't protect against
- Be under 200 words
- Not use any technical terms without explaining them

**Section B: The Three Questions They'll Ask**
Answer these questions in plain English:
1. "If our website has HTTPS, are we secure?"
2. "Our emails say they're encrypted — does that mean no one can read them?"
3. "We use a VPN — does that mean we're protected?"

For each: give the real answer (not just "yes, you're fine").

**Section C: Why Encryption Can Fail**
Explain the 3 most common ways encryption fails to protect people — without making it feel hopeless.

---

**PART 2 — SECURE EMAIL IN PRACTICE**

A common business question: how should we handle confidential information over email?

Explain:
1. What does "email is inherently insecure" actually mean? (What can go wrong with a normal email?)
2. What does encrypting email actually protect? (And what doesn't it protect?)
3. Tools for secure email: S/MIME vs PGP vs encrypted email services (ProtonMail, etc.)
4. For most small businesses: what's the PRACTICAL advice? (Sometimes the answer isn't "use PGP" — it's "use a secure file sharing portal instead")
5. When should a business use a secure document sharing platform instead of email?

---

**PART 3 — THE SECURE COMMUNICATION CHECKLIST**

Create a "Secure Communication Checklist" for "Harwood Legal LLP" — a 15-person law firm that regularly shares confidential client documents and legal advice.

**Section 1: Email Security**
- What to do before emailing confidential documents
- When NOT to use email
- How to verify you're emailing the right person
- What to include in every confidential email (classification marking, handling instructions)

**Section 2: Document Sharing**
- Approved methods for sharing confidential documents with clients
- Approved methods for sharing internally
- How to set document access permissions correctly
- What to do with documents when a matter concludes

**Section 3: Device Security**
- Requirements for any device used for work email and documents
- Remote wipe requirement
- Screen lock and timeout settings
- What to do if a device is lost or stolen

**Section 4: Video Calls and Meetings**
- Screen sharing precautions (closing background applications, notifications)
- Recording policy (when permitted, where stored, retention)
- What NOT to do on public WiFi

**Section 5: Physical Security**
- Clean desk policy
- Printer security (why picking up print jobs promptly matters)
- Screen privacy in public places

Format this as something a law firm could actually hand to all staff.

---

**PART 4 — THE CERTIFICATE EXPLAINED**

A client asks: "How do I know your website is secure?"

Write a 2-paragraph explanation a paralegal could give to a nervous client about:
1. What the padlock in the browser means
2. How to verify they're on the real law firm website (not a fake)
3. What to do if they see a certificate warning

---

**PART 5 — HASHING VS ENCRYPTION**

Explain to me (as a security student) the difference between:
- Encryption (reversible with the right key)
- Hashing (irreversible, one-way)
- Salting (why you add randomness to hashes)

Then explain: why would a website store a hash of your password rather than your actual password? Walk me through what happens when you log in — using a sequence diagram described in text.''',
    },
    {
        'title': 'Question 13: Mini Project — Security Audit Report',
        'description': 'Conduct a complete security audit of a fictional organisation and deliver a professional report',
        'difficulty': 'advanced',
        'order': 13,
        'points': 40,
        'instructions': '''You've learned the building blocks. Now put them together in your first complete security engagement — a comprehensive audit of a fictional small business.

**What You'll Produce:**
A complete security audit report covering:
- Scope and methodology
- Findings across multiple security domains
- Risk ratings and business impact
- Prioritised remediation recommendations
- An executive summary for non-technical leadership

**The Audit Domains to Cover:**
1. Physical security
2. Network and infrastructure security
3. Endpoint security (computers and devices)
4. Access control and authentication
5. Data protection and privacy
6. Staff awareness and culture
7. Business continuity and backup
8. Vendor and third-party risk

**Using AI Effectively in This Project:**
AI is your research partner, your writing assistant, and your structure guide. But the analysis — the judgment about what matters most for THIS specific organisation — is yours.

**This Mini Project Requirements:**
- Complete audit of all 8 domains
- Professional report format (technical and executive sections)
- Minimum 10 findings across domains
- Prioritised remediation roadmap
- Presentation-ready executive summary

**The test:** Could this report be submitted to a real client? That's your quality bar.''',
        'example_prompt': '''Conduct a complete security audit for a fictional startup and produce a professional report. This is my security mini project.

**THE CLIENT:**
"Veriflow Data" — a 12-person UK startup that provides data analytics software to NHS trusts and private healthcare providers. They process health data (special category under GDPR), have 3 NHS clients generating £400K/year revenue, and are pursuing Cyber Essentials Plus certification to win a larger NHS framework contract.

**AUDIT SCOPE:**
Full organisational security audit covering all 8 domains.

**KNOWN INFORMATION (gathered in initial interviews):**

*Physical:* Single open-plan office, code lock on main entrance, no CCTV, server room is actually a locked server cupboard

*Network:* Standard business broadband, consumer-grade router from ISP, one flat network (no segmentation), no firewall beyond router, all staff on same WiFi including visitors

*Endpoints:* Mix of MacBooks and Windows laptops, 2 staff using personal devices, no MDM (mobile device management), BitLocker enabled on some Windows machines, no antivirus policy

*Access Control:* Microsoft 365 with basic licensing, no MFA deployed, shared admin account for some systems, leavers' accounts not always disabled promptly

*Data Protection:* ICO registered, basic privacy notice on website, no formal data audit, client NHS data stored in Microsoft SharePoint with broad internal access permissions

*Awareness:* No formal security training, staff have received phishing emails (1 click recorded last year), no security reporting process

*Business Continuity:* Microsoft 365 cloud backup, critical code in GitHub, no tested recovery procedure, no business continuity plan

*Vendors:* 5 key SaaS tools, no formal vendor security assessments, some tools used before procurement review

---

**PART 1 — FINDINGS ACROSS ALL 8 DOMAINS**

For each domain, write 1-2 findings. Total: minimum 10 findings.

For each finding use this format:
- **ID:** [DOM-001 format]
- **Domain:** [Which domain]
- **Finding Title:** [Professional, specific]
- **Severity:** Critical/High/Medium/Low with CVSS score where applicable
- **Description:** What was found and why it matters
- **Business Risk:** Specific risk to Veriflow's business (NHS contract, GDPR, operations)
- **Recommendation:** Specific, actionable remediation
- **Effort:** Low (< 1 day) / Medium (1 week) / High (> 1 month)

---

**PART 2 — THE RISK REGISTER**

Compile all findings into a risk register (table format):
| ID | Finding | Domain | Severity | Likelihood | Impact | Priority | Owner | Target Date |

Sort by priority. Explain the prioritisation logic — not just by CVSS score, but by business context (NHS contract risk, GDPR exposure, operational risk).

---

**PART 3 — THE EXECUTIVE SUMMARY**

Write a 1-page executive summary for Veriflow's CEO and investors:
- Overall security rating (1-5 with brief justification)
- The 3 most critical issues in plain English
- The business risk if unaddressed (contracts, fines, reputation)
- The good news (what's working)
- The ask: resources and timeline needed
- The Cyber Essentials Plus path: can they achieve it, and what's needed?

---

**PART 4 — THE REMEDIATION ROADMAP**

Design a 90-day security improvement plan:

**Month 1: Critical (NHS contract risk items)**
What to fix immediately to protect existing client relationships.

**Month 2: Foundation Building**
Core security controls to implement.

**Month 3: Cyber Essentials Plus Preparation**
Specific controls for certification.

For each item: estimated cost (tools + staff time), who owns it, and success criteria.

---

**PART 5 — THE FINDINGS PRESENTATION**

Write the talking points for presenting this report to Veriflow's board (15-minute slot):
- Opening: Set the right tone (honest but constructive)
- The headline finding (what the board must understand immediately)
- The 3-part message: Where you are, what's at risk, what to do
- How to handle "are we going to lose our NHS contract?"
- The close: what you need them to decide today''',
    },
    {
        'title': 'Question 14: Mini Project — Incident Response Simulation',
        'description': 'Run a complete simulated incident response exercise from detection to post-incident report',
        'difficulty': 'advanced',
        'order': 14,
        'points': 40,
        'instructions': '''Incident response is a skill you build through practice. This mini project puts you in the lead responder role for a realistic ransomware attack — from the first alert to the final post-incident report.

**What This Project Tests:**
- Incident triage and severity assessment
- Containment decision-making under pressure
- Evidence collection and investigation thinking
- Stakeholder communication (technical and executive)
- Complete incident documentation
- Root cause analysis and lessons learned

**The Incident:**
A ransomware attack against a UK medical practice. This is high-stakes: patient safety could be affected, NHS reporting requirements apply, and the media could pick up the story.

**Your Role:**
You are the incident response lead brought in to manage this incident. You have a team of 2 analysts, access to the organisation's IT systems, and the authority to make containment decisions.

**Requirements for this project:**
- Complete incident timeline
- Decision log (every major decision with rationale)
- Stakeholder communications (3 different audiences)
- Full post-incident report (executive and technical sections)
- Lessons learned and prevention recommendations
- Minimum 1,500 words of substantive content

**This is your most realistic security exercise yet.** Make every decision as if it were real.''',
        'example_prompt': '''I'm running a complete incident response simulation. This is my security mini project — treat every decision as if the consequences are real.

**THE SCENARIO:**

**Day 1, 08:14 Tuesday morning:**
Dr. Sarah Chen, a GP at "Millbrook Surgery" (a 4-doctor, 12-staff NHS primary care practice with 6,200 patients), calls the practice manager in a panic. Her computer has displayed a ransom note. The note says all files have been encrypted. It demands £50,000 in Bitcoin within 72 hours. The note shows a countdown timer.

**Immediate context:**
- Patient appointment system is inaccessible
- Patient record system (EMIS Health — the NHS clinical software) appears down
- The practice is due to open to patients in 46 minutes
- 3 other staff computers are also displaying ransom notes
- The practice manager has already called IT support who said "reboot the computers"

**You arrive on-site at 08:32.**

---

**PHASE 1: FIRST 30 MINUTES (08:32 - 09:02)**

Walk me through your actions minute by minute.

For each decision, state:
- What you decide
- Why (the reasoning)
- What information you're trying to get
- What you tell (and don't tell) the staff

Key decisions to make and justify:
1. The IT support person wants to reboot the computers — do you allow this?
2. The practice is due to open in 28 minutes — do you open or close today?
3. The practice manager wants to call the police — do you advise them to? Now or later?
4. Someone suggests paying the ransom immediately — how do you respond?

---

**PHASE 2: CONTAINMENT AND SCOPING (09:00 - 12:00)**

You've made your immediate decisions. Now understand and contain the incident.

**The Investigation:**
What evidence do you need to collect? Create an evidence collection log with:
- What you're looking for
- Where to look
- What each piece of evidence would tell you
- Chain of custody requirements

**The Scope:**
Based on 4 encrypted machines found, design the investigation to determine:
- When did the initial infection occur?
- How did the attacker get in (the attack vector)?
- How many systems are affected?
- Is any data at risk of exfiltration (not just encryption)?
- Is the attacker still in the environment?

**The Decision Matrix:**
Create a containment decision framework. For each system:
- Patient record server: Isolate immediately or keep running?
- Appointment system: Isolate or keep running?
- Reception computers: Isolate or keep running?
- Dr. Chen's computer: Already isolated — what do you do with it?

---

**PHASE 3: COMMUNICATIONS (Ongoing throughout)**

Write three communications you'd actually send:

**Communication A: Staff Briefing (09:00am)**
What do you tell the 12 staff members gathered in reception?
- What happened (at the level they need to know)
- What they should and shouldn't do
- What's happening next
- How to handle patient calls and queries
- Tone: calm, in control, clear

**Communication B: ICO Notification (within 72 hours)**
Draft the notification to the Information Commissioner's Office.
Cover: the nature of the breach, data affected, number of individuals affected (estimate), likely consequences, measures taken, contact details.
This is a legal requirement — get the format right.

**Communication C: Patient Letter (to send after the incident)**
A letter to the 6,200 registered patients explaining what happened, whether their data was affected, and what they should do.
Tone: honest, reassuring, clear. This should prevent patient panic without minimising a real event.

---

**PHASE 4: RECOVERY AND ROOT CAUSE**

48 hours later: systems are being restored from backup. Investigation has revealed:

**Root cause findings:**
- Initial access: Phishing email to the practice manager 12 days ago
- The email contained a malicious Word document (invoice from a fake supplier)
- The attacker spent 12 days in the network before deploying ransomware
- 3 months of appointment data was successfully restored from backup
- Patient clinical records (EMIS) were not encrypted (EMIS was on isolated system)
- No evidence of data exfiltration, but cannot be 100% confirmed

Write the root cause analysis:
- What happened at each stage (timeline)
- Why each stage succeeded (the security failures)
- The "counterfactual" — where, if one thing had been different, this attack would have failed

---

**PHASE 5: POST-INCIDENT REPORT**

Write the complete post-incident report:

**Executive Summary (for NHS commissioners and practice partners):**
What happened, what the impact was, what was done, and what's changing.

**Full Incident Timeline:**
From initial phishing email to system restoration. Table format.

**Impact Assessment:**
- Clinical impact (patient care disruption)
- Data impact (what data was at risk, what was confirmed affected)
- Financial impact (lost revenue, recovery costs, potential fines)
- Reputational impact

**Lessons Learned (10 items):**
For each lesson: what happened, why it happened, and the specific change being made.

**Prevention Recommendations:**
10 security improvements in priority order. For each: what it addresses, rough cost, implementation timeline.

---

**REFLECTION:**
What's the single most important thing every small healthcare organisation should implement to prevent this type of attack?
Why is healthcare particularly targeted by ransomware attackers?
What does this incident teach us about the cost of not investing in security?''',
    },
    {
        'title': 'Question 15: Capstone — Full Security Assessment',
        'description': 'Deliver a comprehensive security assessment package for a realistic scenario — your portfolio piece',
        'difficulty': 'advanced',
        'order': 15,
        'points': 50,
        'instructions': '''This is your Track B Capstone. You've studied the threat landscape, network security, incident response, vulnerability assessment, compliance, and more. Now you bring it all together in one comprehensive security assessment.

**What This Capstone Demonstrates:**
- Strategic security thinking (not just technical knowledge)
- Professional communication across multiple audiences
- Ability to assess, prioritise, and communicate risk
- Understanding of the full security landscape
- Real-world applicability of everything learned

**The Capstone Deliverable:**
A complete Security Assessment Package for a realistic organisation — the kind of work a security consultant would charge thousands of pounds for.

**The Package Must Include:**
1. Threat analysis (who and what threatens this organisation)
2. Vulnerability assessment summary (simulated findings across key domains)
3. Policy recommendations (3 specific policy gaps to address)
4. Incident response readiness (gap analysis and improvement plan)
5. Executive briefing (for board-level decision making)
6. Remediation roadmap (prioritised, costed, timed)

**The Organisation:**
You choose — a sector that interests you, a realistic size, and a context with genuinely interesting security challenges.

**Make it genuinely yours.** This is your portfolio piece — the work you'd show a potential employer to demonstrate what you know.''',
        'example_prompt': '''This is my Track B Capstone — a complete security assessment package for a fictional organisation. I want this to be portfolio-ready.

**THE ORGANISATION I'VE CHOSEN:**
"LegalEdge" — a 40-person law firm specialising in corporate law and M&A (mergers and acquisitions). They handle highly confidential client information including pending deals, corporate strategies, and sensitive negotiations. A data breach could cost a client millions and end LegalEdge's reputation overnight.

**WHY THIS IS INTERESTING SECURITY-WISE:**
- Highly sensitive data (M&A targets are extremely valuable to threat actors)
- Client confidentiality is the core business value
- Regulatory requirements (Solicitors Regulation Authority + UK GDPR)
- Remote working (partners work from anywhere)
- Perception that "we're too small to be targeted" (they're not)

---

**SECTION 1 — THREAT ANALYSIS: WHO WANTS TO ATTACK LEGALEDGE?**

Write a comprehensive threat analysis:

**Threat Actor Profiles:**
For each relevant threat actor type:
- Identity and motivation
- Why LegalEdge is a target
- Specific attack scenarios relevant to a law firm
- Current threat level assessment
- Real examples of similar organisations being targeted (public knowledge)

Cover: organised crime, corporate espionage, nation-state, insider threat, opportunistic attackers.

**The Crown Jewels:**
What specific data would be most valuable to an attacker? Map LegalEdge's information assets by sensitivity and attack value.

**The Risk Landscape:**
What is the current UK legal sector threat environment? (Use publicly available knowledge — NCSC reports, SRA guidance)

---

**SECTION 2 — VULNERABILITY ASSESSMENT SUMMARY**

Based on a typical 40-person law firm's likely security posture, create a simulated vulnerability assessment summary.

**Assume these findings from assessment:**

Technical findings: Develop 8 realistic technical findings across: network security, email security, endpoint protection, cloud storage permissions, remote access, web presence.

Process/people findings: Develop 4 findings across: access control procedures, staff awareness, data handling practices, vendor management.

**For each of the 12 findings:**
- Title, domain, severity (Critical/High/Medium/Low)
- One paragraph description
- Business risk (specific to a law firm handling M&A)
- Remediation action

**Risk Summary Matrix:**
Present all 12 findings in a risk matrix table, sorted by priority.

---

**SECTION 3 — POLICY GAP ANALYSIS**

Identify the 3 most critical policy gaps at LegalEdge.

For each gap:
- What policy is missing or inadequate?
- What risk does the gap create?
- Write the core policy content (the actual policy text, 200-300 words each)
- Implementation approach (how do you roll this out to partners and staff?)

Consider: client data handling policy, remote working security policy, incident reporting policy, acceptable use policy, supplier security policy.

---

**SECTION 4 — INCIDENT RESPONSE READINESS**

Assess LegalEdge's incident response capability (assume they currently have none).

**Gap Analysis:**
| IR Capability | Current State | Target State | Gap |

Cover: detection capability, response team, escalation procedures, forensic capability, communication plan, legal/regulatory notification, recovery procedures.

**IR Improvement Plan:**
Design the 6-month plan to build incident response capability from zero. What do you build first? What can be done cheaply? What requires investment?

**The IR Playbook:**
Write the first page of LegalEdge's incident response playbook — specifically for the "suspected data breach of client M&A information" scenario (their highest risk incident type).

---

**SECTION 5 — EXECUTIVE BRIEFING**

Write the board-level briefing document.

**Format:**
One page (800 words max). Designed for senior partners who are intelligent, successful, and not technical.

Contents:
- The cyber threat facing LegalEdge in 2026 (plain English, compelling)
- The 3 findings that put the business at most risk
- The regulatory context (SRA requirements, GDPR exposure)
- The investment required (realistic, not alarming)
- The business case (why security investment makes commercial sense for a law firm)
- The ask: what the board needs to decide and approve today

---

**SECTION 6 — REMEDIATION ROADMAP**

Design the complete remediation roadmap:

**90-Day Priority Plan:**
Month 1: What MUST happen (highest risk, lowest effort)
Month 2: Foundation controls
Month 3: Advanced measures and policy implementation

**12-Month Roadmap:**
Quarters 2-4: Ongoing improvements and maturity development

For the full roadmap:
| Initiative | What It Addresses | Effort | Cost (estimate) | Owner | Target Date |

**The Investment Case:**
Total security investment required for year 1.
Return on investment framing — how do you justify this to cost-conscious partners?

---

**FINAL REFLECTION — THE SECURITY ASSESSMENT CRAFT**

Close your capstone with a reflection:

1. What did you learn that surprised you most about security assessment?
2. Where in this assessment did AI help most — and where did it fall short?
3. What's the hardest part of security consulting that this exercise taught you?
4. What would you do differently in a real engagement?
5. What's the one piece of advice you'd give to LegalEdge's managing partner about building a security-conscious culture — beyond technology?

Your capstone is your proof of capability. Present it with the confidence of someone who has genuinely grappled with a complex, real-world problem.''',
    },
]
