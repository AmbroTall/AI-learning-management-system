# Module 2: Build AI-Powered Tools - Task Automation & Productivity Section
# 7 challenges teaching students to build real automation tools

TASK_AUTOMATION_CHALLENGES = [
    {
        'title': 'Project 1: Smart Task Manager with AI',
        'description': 'Build an intelligent task manager that prioritizes and organizes work',
        'difficulty': 'beginner',
        'order': 1,
        'points': 30,
        'instructions': '''Welcome to Module 2 - Building Real Tools! 🚀

In Module 1, you learned to PROMPT AI. Now you'll BUILD TOOLS with AI!

**Your First Project:**
Create a smart task manager that uses AI to:
- Categorize tasks automatically
- Suggest priorities based on urgency/importance
- Break down complex tasks into steps
- Estimate time requirements

**What You'll Build:**
A prompt-based system where users input tasks, and AI:
1. Analyzes the task
2. Categorizes it (Work/Personal/Urgent/etc.)
3. Assigns priority (High/Medium/Low)
4. Breaks it into subtasks if complex
5. Estimates completion time

**The Challenge:**
Design the AI prompts that power this system. You need:
- A task analysis prompt
- A categorization prompt
- A priority scoring prompt
- A task breakdown prompt

**Real-World Use:**
Security teams use this for incident prioritization, project management, and workload balancing.

**Your Task:**
Create the complete prompt system for a smart task manager. Show how each component works together.''',
        'example_prompt': '''I'm building a Smart Task Manager for a SOC team. Here's the system design:

TASK INPUT EXAMPLE:
"Investigate the ransomware alert on SALES-PC-15, determine if it's real, contain if needed, and document findings"

PROMPT SYSTEM NEEDED:

1. TASK ANALYZER PROMPT:
Create a prompt that analyzes any task and returns:
- Task type (Incident Response, Vulnerability Management, Compliance, Admin, etc.)
- Complexity (Simple/Medium/Complex)
- Dependencies (what else needs to happen first)
- Skills required
- Estimated duration

2. PRIORITY SCORER PROMPT:
Create a prompt that scores tasks 1-10 based on:
- Urgency (time-sensitive?)
- Impact (how critical?)
- Effort required
- Risk if delayed
Output: Priority score with justification

3. TASK BREAKDOWN PROMPT:
For complex tasks, create a prompt that breaks them into:
- Sequential steps (must be done in order)
- Parallel steps (can do simultaneously)
- Each step with estimated time
- Required resources per step

4. TIME ESTIMATOR PROMPT:
Create a prompt that estimates realistic completion time considering:
- Task complexity
- Interruptions (SOC environment)
- Documentation time
- Review/approval time

5. INTEGRATION:
Show how these prompts work together in a workflow:
Task Input → Analysis → Priority Scoring → Breakdown (if needed) → Time Estimate → Final Output

Design this prompt system to be:
- Consistent in output format
- Easy to parse programmatically
- Realistic for SOC environment
- Helpful for actual prioritization

Provide example outputs for each prompt using the ransomware task above.''',
    },
    {
        'title': 'Project 2: Automated Email Response System',
        'description': 'Build an AI system that drafts professional email responses',
        'difficulty': 'beginner',
        'order': 2,
        'points': 30,
        'instructions': '''Build an AI-powered email assistant! 📧

**The Challenge:**
Security teams get tons of emails - user questions, vendor inquiries, incident notifications. Create an AI system that drafts appropriate responses.

**What You'll Build:**
A prompt system that:
1. Analyzes incoming email (type, urgency, sentiment)
2. Determines appropriate response type
3. Generates professional reply
4. Adapts tone to situation
5. Includes relevant security guidance

**Email Types to Handle:**
- User reporting potential phishing
- Vendor security questionnaire
- Management asking for status update
- User requesting security exception
- Partner asking about incident

**Your Task:**
Create prompts that can:
- Classify email type
- Extract key information
- Generate appropriate response
- Maintain professional tone
- Include security best practices

**Real-World Application:**
Speeds up response times, ensures consistency, reduces analyst workload for routine communications.''',
        'example_prompt': '''I'm building an Automated Email Response System for our security team.

INCOMING EMAIL EXAMPLE:
From: user@company.com
Subject: Suspicious email in my inbox
Body: "Hi security team, I got an email from 'IT Support' asking me to verify my password by clicking a link. It looks legit but something feels off. Should I click it? Thanks, Sarah"

BUILD THIS SYSTEM:

1. EMAIL CLASSIFIER PROMPT:
Create a prompt that classifies emails into:
- Phishing Report (user reporting suspicious email)
- Security Question (general security inquiry)
- Incident Report (user reporting security issue)
- Request (asking for access, exception, etc.)
- Status Query (asking about incident/ticket)
Output: Category + Urgency Level + Key Details Extracted

2. CONTEXT ANALYZER PROMPT:
Extract important information:
- User's security awareness level (novice/intermediate/advanced)
- Emotional state (worried, frustrated, urgent, casual)
- Required response type (immediate, informational, reassuring)
- Follow-up actions needed

3. RESPONSE GENERATOR PROMPT:
Generate appropriate response including:
- Thank them for reporting (always!)
- Answer their specific question
- Provide next steps
- Include relevant security tip
- Set expectations (when will they hear back?)
- Professional but friendly tone

4. TONE ADAPTER PROMPT:
Adjust response based on:
- Audience (user, management, vendor, partner)
- Situation urgency
- Emotional context
- Technical level of recipient

5. SECURITY GUIDANCE INJECTOR:
Add relevant security tips like:
- How to verify legitimate emails
- What makes this email suspicious
- What to do with similar emails
- Reporting mechanism reminder

For the phishing report example above, show:
- Classification output
- Context analysis
- Generated response
- Why this response is appropriate

Make responses:
- Clear and actionable
- Reassuring (not condescending)
- Educational (teach, don't just answer)
- Professional but warm
- Under 200 words typically''',
    },
    {
        'title': 'Project 3: Meeting Notes & Action Item Extractor',
        'description': 'Transform messy meeting notes into organized summaries with action items',
        'difficulty': 'intermediate',
        'order': 3,
        'points': 35,
        'instructions': '''Build a meeting notes processor! 📝

**The Problem:**
Security meetings generate lots of notes, but they're often messy. Action items get lost. Follow-ups are missed.

**Your Solution:**
An AI system that transforms raw meeting notes into:
- Clean executive summary
- Key decisions made
- Action items with owners and deadlines
- Risks identified
- Follow-up items
- Next meeting agenda suggestions

**What You'll Build:**
Prompts that can:
1. Parse unstructured notes
2. Identify action items
3. Extract decisions
4. Assign ownership
5. Flag risks/concerns
6. Generate follow-up tasks

**Real-World Use:**
After security review meetings, incident post-mortems, project planning sessions, vendor meetings, compliance reviews.

**Your Task:**
Create a comprehensive meeting notes processing system.''',
        'example_prompt': '''I'm building a Meeting Notes & Action Item Extractor for security team meetings.

RAW MEETING NOTES EXAMPLE:
```
Security Review Meeting - Dec 18, 2024
Present: John (CISO), Sarah (SOC Lead), Mike (Eng), Lisa (Compliance)

- Discussed Q4 security metrics - phishing clicks down 40% (good!)
- But ransomware attempts up 3x (concerning)
- Need to update IR playbook - current one is from 2022
- Sarah mentioned we're short-staffed, can't cover all shifts
- Mike said firewall upgrade is delayed, vendor issues
- Compliance audit in Feb - Lisa needs updated policies
- John approved $15K for new EDR tool
- Someone needs to schedule pen test - maybe Q1?
- Sarah: "Can we get a junior analyst hired?"
- John: "I'll talk to HR but no promises"
- Mike offered to help with documentation
- Next meeting: Jan 15
```

BUILD THIS EXTRACTOR SYSTEM:

1. SUMMARY GENERATOR PROMPT:
Create 3-5 bullet executive summary covering:
- Meeting purpose
- Key topics discussed
- Major outcomes
- Critical concerns raised

2. DECISION EXTRACTOR PROMPT:
Identify all decisions made:
Format: [Decision] - [Who decided] - [Impact]
Example: "Approved $15K for EDR tool - John (CISO) - Will improve endpoint protection"

3. ACTION ITEM IDENTIFIER PROMPT:
Extract all action items, even implicit ones:
Format for each:
- Action: [what needs to be done]
- Owner: [who's responsible]
- Deadline: [when or "TBD"]
- Priority: [High/Medium/Low]
- Dependencies: [what needs to happen first]

In the example, find actions like:
- Update IR playbook
- Schedule penetration test
- Update compliance policies
- Talk to HR about hiring
- Assist with documentation

4. RISK FLAGGING PROMPT:
Identify risks and concerns:
- Short-staffing issues
- Delayed firewall upgrade
- Upcoming compliance audit with gaps
- Increasing ransomware attempts
Rate each risk and suggest mitigation

5. FOLLOW-UP GENERATOR PROMPT:
Create next meeting agenda:
- Items to revisit
- Status updates needed
- New topics from this meeting
- Recurring items

6. ATTENDEE ACTION SUMMARY:
For each person, summarize:
- Their action items
- Deadlines they committed to
- What they need from others

Provide complete output for the example meeting notes above. Show how messy notes become organized, actionable documentation.

Make it:
- Clear and scannable
- Action-oriented
- Accountable (who owns what)
- Time-bound (deadlines explicit)
- Risk-aware (flags concerns)''',
    },
    {
        'title': 'Project 4: Smart Calendar Assistant',
        'description': 'Build an AI assistant that optimizes schedules and meetings',
        'difficulty': 'intermediate',
        'order': 4,
        'points': 35,
        'instructions': '''Create an intelligent calendar assistant! 📅

**The Challenge:**
Security professionals juggle incidents, meetings, projects, and on-call duties. Build an AI assistant that helps optimize time.

**What You'll Build:**
A system that:
1. Analyzes meeting requests
2. Suggests optimal timing
3. Identifies conflicts (not just time, but priority conflicts)
4. Recommends which meetings to attend/skip/delegate
5. Blocks focus time for important work
6. Balances reactive (incidents) vs proactive (projects) work

**Prompts Needed:**
- Meeting importance scorer
- Schedule optimizer
- Conflict resolver
- Focus time protector
- Meeting necessity evaluator

**Real-World Application:**
Helps security leaders manage time effectively, ensures critical work gets done, prevents burnout from meeting overload.

**Your Task:**
Design an AI-powered calendar management system.''',
        'example_prompt': '''I'm building a Smart Calendar Assistant for a busy SOC Manager.

CURRENT SITUATION:
Role: SOC Manager, 50+ hours/week
Responsibilities: Team leadership, incident oversight, project management, compliance
Calendar: Back-to-back meetings most days, little focus time
Problem: Important projects stall, always in reactive mode

MEETING REQUEST EXAMPLE:
From: vendor@security-tools.com
Subject: Product Demo - Next-Gen SIEM Solution
Proposed: Thursday 2-3pm
Attendees: You, your team (optional)
Details: "30-min demo of our new SIEM platform, addressing the pain points you mentioned. Can bring technical architect if needed."

BUILD THIS CALENDAR ASSISTANT:

1. MEETING IMPORTANCE SCORER PROMPT:
Evaluate meeting requests on:
- Alignment with strategic goals
- Urgency vs importance
- Value of attendance (could delegate? async instead?)
- Preparation time required
- Opportunity cost (what else could you do?)
Score 1-10 with reasoning

2. CALENDAR ANALYZER PROMPT:
Review current calendar and identify:
- Over-scheduled days (>6 hours meetings)
- No focus time blocks
- Back-to-back meetings (no breaks)
- Conflicting priorities
- Patterns (too many vendor calls, not enough team time)

3. OPTIMAL TIMING SUGGESTER PROMPT:
For approved meetings, suggest best time considering:
- Energy levels (morning for complex, afternoon for routine)
- Related meetings (cluster similar topics)
- Team availability
- Focus time protection (no meetings certain hours)
- Day of week patterns

4. MEETING NECESSITY EVALUATOR PROMPT:
For each meeting, determine:
- Must attend personally? (decision-making required)
- Could send delegate? (information gathering)
- Could be async? (email/doc instead)
- Could skip? (low value, optional)
Provide recommendation with reasoning

5. FOCUS TIME PROTECTOR PROMPT:
Identify time blocks needed for:
- Deep work (project planning, documentation)
- Incident response buffer (unexpected issues)
- Strategic thinking (not just tactical firefighting)
- Team 1-on-1s (recurring, important)
Suggest when to block calendar

6. CONFLICT RESOLVER PROMPT:
When multiple high-priority items conflict:
- Analyze tradeoffs
- Suggest delegation options
- Recommend reschedule strategy
- Identify what's truly urgent vs important

For the vendor SIEM demo meeting, provide:
- Importance score with reasoning
- Should attend? If not, who should?
- If yes, best timing this week?
- Preparation needed?
- Follow-up actions?

Then analyze a sample full week and suggest optimization:
MONDAY: 4 meetings, 2 incidents handled
TUESDAY: 7 meetings back-to-back, no lunch
WEDNESDAY: 5 meetings, compliance report due
THURSDAY: 3 meetings, team 1-on-1s
FRIDAY: 6 meetings, trying to finish project plan

Optimize this week considering:
- Meeting necessity
- Focus time needs
- Team needs
- Incident response capacity
- Work-life balance

Make recommendations:
- Specific (which meetings to move/cancel/delegate)
- Reasoning (why this helps)
- Balanced (not just "cancel everything")
- Realistic (acknowledging constraints)''',
    },
    {
        'title': 'Project 5: Knowledge Base Builder',
        'description': 'Create a system that builds searchable knowledge bases from security docs',
        'difficulty': 'intermediate',
        'order': 5,
        'points': 35,
        'instructions': '''Build an AI-powered knowledge management system! 📚

**The Problem:**
Security teams accumulate tons of documentation - runbooks, policies, incident reports, lessons learned. Finding information is hard.

**Your Solution:**
An AI system that:
1. Takes various documents (policies, runbooks, reports)
2. Extracts key information
3. Creates structured knowledge entries
4. Generates tags and categories
5. Creates searchable summaries
6. Links related content

**What You'll Build:**
Prompts that transform unstructured docs into organized, searchable knowledge base entries.

**Real-World Use:**
Onboarding new team members, quick reference during incidents, compliance documentation, building institutional knowledge.

**Your Task:**
Design a knowledge base builder system that processes security documents.''',
        'example_prompt': '''I'm building a Knowledge Base Builder for our security documentation.

DOCUMENT EXAMPLE:
```
Incident Response Playbook: Ransomware

Last Updated: Oct 2024

When ransomware is detected:

1. IMMEDIATE (First 15 min):
   - Isolate affected systems from network
   - Identify patient zero
   - Check backup status
   - Alert CISO and legal

2. CONTAINMENT (15-60 min):
   - Block C2 domains at firewall
   - Disable compromised accounts
   - Snapshot affected systems for forensics
   - Assess spread to other systems

3. ERADICATION (1-4 hours):
   - Identify all compromised systems
   - Remove malware
   - Patch vulnerabilities exploited
   - Reset all potentially compromised credentials

4. RECOVERY (4-24 hours):
   - Restore from clean backups
   - Verify system integrity
   - Monitor for re-infection
   - Gradual return to production

KEY CONTACTS:
- CISO: John Smith (555-0100)
- Legal: Sarah Jones (555-0101)
- Backup Admin: Mike Wilson (555-0102)

NEVER:
- Don't pay ransom without legal approval
- Don't turn systems back on without clean scan
- Don't skip documentation

LESSONS LEARNED:
- Most ransomware enters via phishing
- Quick isolation limits damage
- Tested backups are critical
```

BUILD THIS KNOWLEDGE BASE SYSTEM:

1. DOCUMENT ANALYZER PROMPT:
Extract from any document:
- Document type (playbook, policy, report, guide)
- Main topic/purpose
- Target audience (analysts, managers, all staff)
- Criticality (must-know, should-know, reference)
- Last updated date
- Status (current, needs review, outdated)

2. KEY INFORMATION EXTRACTOR PROMPT:
Pull out:
- Step-by-step procedures
- Critical contacts
- Important warnings/never do
- Required tools/access
- Time estimates
- Dependencies
- Related documents

3. SUMMARY GENERATOR PROMPT:
Create multiple summary levels:
- One-sentence: Ultra-quick reference
- One-paragraph: Quick overview
- Detailed: Comprehensive but organized
Each optimized for different use cases

4. TAG & CATEGORIZER PROMPT:
Generate:
- Primary category (Incident Response, Policy, Tool Guide)
- Tags (ransomware, malware, containment, recovery)
- Related topics (phishing, backups, forensics)
- Skill level required (basic, intermediate, advanced)
- When to use (during incident, planning, training)

5. Q&A GENERATOR PROMPT:
From the document, create common questions and answers:
- "What do I do first when ransomware is detected?"
- "Who do I contact for ransomware incidents?"
- "How long does ransomware recovery take?"
Makes knowledge base more searchable

6. RELATIONSHIP MAPPER PROMPT:
Identify connections to other knowledge:
- Prerequisites (what to read first)
- Related procedures (what else might help)
- Upstream/downstream processes
- Training materials needed

For the ransomware playbook example, provide:
- Complete knowledge base entry
- All tags and categories
- Summary at each level
- 10 Q&A pairs
- 5 related topics/documents

Make it:
- Highly searchable
- Quick to scan
- Actionable (steps clear)
- Connected (links to related info)
- Maintainable (easy to update)

Show how this becomes a searchable knowledge base entry that helps analysts find info fast during high-pressure situations.''',
    },
    {
        'title': 'Project 6: Automated Report Generator',
        'description': 'Build a system that creates professional security reports from data',
        'difficulty': 'advanced',
        'order': 6,
        'points': 40,
        'instructions': '''Create an automated reporting system! 📊

**The Challenge:**
Security teams need reports for management, compliance, board meetings. Writing them manually takes hours.

**Your Solution:**
An AI system that:
1. Takes raw data (metrics, incidents, scans)
2. Analyzes trends and patterns
3. Generates executive summaries
4. Creates detailed findings
5. Provides recommendations
6. Formats professionally

**Report Types:**
- Weekly security operations summary
- Monthly metrics report
- Quarterly board report
- Incident post-mortem
- Compliance status report

**Your Task:**
Design a comprehensive automated reporting system that produces publication-ready reports.

**Real-World Value:**
Saves 5-10 hours/week on reporting, ensures consistency, allows more time for actual security work.''',
        'example_prompt': '''I'm building an Automated Report Generator for security reporting.

DATA INPUT EXAMPLE:
```
WEEKLY DATA (Dec 11-17, 2024):
Alerts: 1,247 (up from 1,089 last week)
- Critical: 15 (5 real threats, 10 false positives)
- High: 234 (89 investigated, 145 auto-resolved)
- Medium: 687
- Low: 311

Incidents: 7 total
- Phishing: 3 (all contained, no data loss)
- Malware: 2 (both workstations, cleaned)
- Policy Violation: 2 (user education provided)

Vulnerabilities:
- New: 45 discovered
- Patched: 52
- Critical open: 8 (down from 12)
- Patch compliance: 91%

Notable Events:
- New firewall rules deployed Tuesday
- One analyst on vacation
- Planned maintenance caused alert spike Wednesday
- Successful phishing simulation: 82% pass rate (up from 67%)

Metrics vs Goals:
- MTTD: 15 minutes (goal: 20 min) ✓
- MTTR: 45 minutes (goal: 60 min) ✓
- False positive rate: 31% (goal: <25%) ✗
- Critical patches within 7 days: 87% (goal: 95%) ✗
```

BUILD THIS REPORT GENERATOR:

1. EXECUTIVE SUMMARY GENERATOR PROMPT:
Create 3-4 bullet executive summary:
- Overall security posture (improving/stable/declining)
- Key wins this week
- Areas of concern
- Critical action items
Write for C-level: no jargon, business impact focus

2. TREND ANALYZER PROMPT:
Identify and explain trends:
- Week-over-week changes
- Emerging patterns
- Anomalies vs normal
- Seasonal factors
- Whether trends are concerning
Support with data, explain significance

3. METRIC INTERPRETER PROMPT:
For each metric, provide:
- Current value vs goal
- Trend (improving/declining)
- Context (why this number?)
- So what? (why it matters)
- Action needed? (if any)

4. INCIDENT NARRATIVE GENERATOR PROMPT:
Transform incident list into story:
- What happened (concisely)
- How we responded
- Current status
- Lessons learned
- Preventive actions taken
Make it narrative, not just bullets

5. RISK HIGHLIGHTER PROMPT:
Identify and prioritize risks:
- What's getting worse?
- What could become critical?
- Resource constraints impacting security?
- Upcoming challenges?
Rate each risk, suggest mitigation

6. RECOMMENDATION GENERATOR PROMPT:
Based on data, suggest:
- Immediate actions (this week)
- Short-term improvements (this month)
- Strategic changes (this quarter)
- Resource needs
Each with justification and expected impact

7. FORMATTING OPTIMIZER PROMPT:
Structure the report:
- Sections in logical order
- Data visualizations suggested
- Key points highlighted
- Appendix for detailed data
- Professional language throughout

For the example data, generate:
- Complete weekly report (all sections)
- Formatted for email to CISO
- 2-page max, scannable
- Data-driven but readable
- Action-oriented

Additionally, show how to adapt this for:
- Monthly board report (higher level)
- Quarterly compliance report (audit focus)
- Incident post-mortem (deep dive)

Make reports:
- Consistent format (predictable structure)
- Data-driven (numbers tell the story)
- Actionable (clear next steps)
- Honest (acknowledge problems)
- Forward-looking (not just backwards)
- Appropriate detail for audience''',
    },
    {
        'title': 'Project 7: Personal Productivity Dashboard',
        'description': 'Build an AI system that tracks and optimizes personal productivity',
        'difficulty': 'advanced',
        'order': 7,
        'points': 40,
        'instructions': '''Create a personal productivity analyzer! 📈

**The Challenge:**
Security professionals are constantly interrupted, context-switching, and fighting fires. Build an AI system that helps optimize personal productivity.

**Your Solution:**
A system that:
1. Analyzes how time is spent
2. Identifies productivity patterns
3. Suggests optimizations
4. Tracks progress on goals
5. Identifies energy patterns
6. Recommends focus strategies

**What You'll Build:**
Prompts that turn productivity data into actionable insights and recommendations.

**Your Task:**
Design a comprehensive personal productivity analysis and optimization system.

**Real-World Value:**
Helps security professionals work smarter, prevent burnout, achieve goals, balance reactive and proactive work.''',
        'example_prompt': '''I'm building a Personal Productivity Dashboard for security professionals.

WEEKLY DATA INPUT:
```
TIME TRACKING (40 hours logged):
Meetings: 18 hours (45%)
Incident Response: 10 hours (25%)
Project Work: 6 hours (15%)
Email/Slack: 4 hours (10%)
Training/Learning: 2 hours (5%)

INTERRUPTIONS:
- Average: 8 per day
- Longest focus block: 45 minutes
- Context switches: 32 per day

ENERGY LEVELS (self-reported 1-10):
Mon AM: 8, PM: 5
Tue AM: 7, PM: 4
Wed AM: 6, PM: 3
Thu AM: 7, PM: 5
Fri AM: 5, PM: 6

GOALS THIS WEEK:
- Complete incident response playbook update (planned: 4hrs, actual: 1hr) ✗
- Review 20 security alerts (planned: 2hrs, actual: 3hrs) ✓
- Finish compliance documentation (planned: 3hrs, actual: 0hrs) ✗
- Team 1-on-1s (planned: 2hrs, actual: 2hrs) ✓

INCIDENTS:
- 3 high-priority incidents (unplanned, took 6 hours)
- 2 on-call escalations at night (impacted sleep)

NOTES:
- Wednesday afternoon completely lost to emergency meeting
- Friday more productive (fewer interruptions)
- Struggling to find time for strategic work
```

BUILD THIS PRODUCTIVITY SYSTEM:

1. TIME ANALYSIS PROMPT:
Analyze time allocation:
- Is distribution healthy? (too much reactive vs proactive?)
- Hidden time sinks (where is time disappearing?)
- Efficiency by time block (AM vs PM)
- Comparison to ideal distribution
- Impact of interruptions

2. PATTERN IDENTIFIER PROMPT:
Find patterns in:
- Energy levels throughout week
- Productive vs unproductive times
- Interruption patterns
- Meeting density impact
- Goal achievement correlation with time blocks

3. GOAL TRACKER PROMPT:
Analyze goal achievement:
- Why did some goals fail? (time estimation? interruptions? priorities?)
- Which goals actually mattered?
- Were goals realistic?
- What got in the way?
- How to adjust next week?

4. OPTIMIZATION SUGGESTER PROMPT:
Based on data, recommend:
- Best times for focus work (based on energy + interruptions)
- Meeting consolidation strategies
- Buffer time for incidents
- Goal adjustment for realism
- Time blocking strategies
- Communication boundaries

5. ENERGY OPTIMIZER PROMPT:
Analyze energy patterns:
- Peak performance times
- Energy drains (what depletes energy most?)
- Recovery strategies needed
- Burnout risk indicators
- Work-life balance assessment

6. WEEKLY PLAN GENERATOR PROMPT:
Create next week's optimized plan:
- Time block recommendations
- Goal priorities (what to tackle when)
- Buffer allocations (planned slack)
- Focus time protection
- Meeting optimization
- Realistic expectations

7. PROGRESS TRACKER PROMPT:
Track over multiple weeks:
- Are optimizations working?
- Productivity trends
- Goal achievement rate
- Burnout indicators
- Areas still struggling

For the example data, provide:

A. WEEKLY INSIGHTS:
- Top 3 productivity wins
- Top 3 challenges
- Biggest time wasters
- Energy pattern analysis

B. SPECIFIC RECOMMENDATIONS:
- When to schedule focus work
- Which meetings to decline/delegate
- How to handle interruptions
- Goal adjustments for realism

C. NEXT WEEK PLAN:
- Optimized time blocks
- Revised goals
- Protection strategies
- Success metrics

D. LONG-TERM SUGGESTIONS:
- Systemic changes needed
- Skills to develop
- Boundaries to set
- Process improvements

Make it:
- Honest (acknowledge struggles)
- Actionable (specific changes)
- Sustainable (not just "work harder")
- Personalized (based on patterns)
- Compassionate (recognize burnout risks)
- Data-driven (not just generic advice)

Show how this helps a burnt-out SOC analyst work smarter, not harder.''',
    },
]
