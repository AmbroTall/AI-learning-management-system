"""
Module 3 Part 2: Automation & Workflows — "Making AI Work for You"
Challenges 9-16: Building automations and connecting AI to real workflows (4-5 hours)
"""

MODULE3_PART2_CHALLENGES = [
    {
        'title': 'Question 9: Why Automation Matters',
        'description': 'Audit your own work to identify the 5 tasks AI could automate or dramatically speed up',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 25,
        'instructions': '''The most valuable automation skill isn't technical. It's being able to spot which tasks in your own life are worth automating.

**What You'll Learn:**
- How to identify automation-worthy tasks (frequency × effort × consistency = automation priority)
- The difference between "fully automate," "AI-assist," and "keep manual"
- How to calculate the real time value of automating a task

**The Automation Priority Framework:**

High-priority automation candidates:
- ✅ Repetitive (done weekly or more often)
- ✅ Consistent format (same structure each time)
- ✅ Rules-based (a human could write the rules)
- ✅ Time-consuming (takes 30+ minutes when done manually)
- ✅ Low creativity required (following a process, not making unique decisions)

Keep manual (for now):
- ❌ Rare or unique tasks
- ❌ Requires significant human judgment
- ❌ High-stakes decisions where errors are costly
- ❌ Relationship-dependent (needs personal touch)

**Your Challenge:**
Audit your own weekly routine and identify your top 5 automation opportunities.

For each task, complete the full analysis:
1. Describe the task (what you do, how often, how long it takes)
2. Score it on the automation priority criteria
3. Classify it: fully automate, AI-assist, or keep manual
4. Estimate the time savings per week
5. Describe what the automated version would look like

Then calculate: if you implemented all 5 automations, how many hours per month would you save?

**Be honest about your actual work** — the more specific you are, the more useful this exercise is.''',
        'example_prompt': '''Conduct a personal automation audit for my weekly work routine. Help me identify my top 5 automation opportunities with full analysis.

**MY WORK CONTEXT:**
I'm an account manager at a digital marketing agency. My typical week involves:

**Daily tasks:**
- Check client campaign performance dashboards (15 min/day across 8 clients)
- Reply to client emails with performance updates and queries (1-2 hours/day)
- Update our internal CRM with call notes after client conversations (20 min/day)

**Weekly tasks:**
- Write 8 client weekly performance reports (same format every time, 30 min each = 4 hours)
- Prepare agendas for the following week's client calls (15 min per client = 2 hours)
- Internal status update to my line manager (summary of all accounts, 45 min)
- Monitor competitor activity for 3 key clients (30 min)

**Monthly tasks:**
- Monthly invoicing summary (tracking billable hours and expenses, 2 hours)
- Client satisfaction check-ins (brief emails to each client, 1 hour)
- Prepare end-of-month reports for senior clients (2-3 hours each, 4 clients)

---

**AUTOMATION AUDIT:**

For each of the following 5 tasks, complete a full analysis:

**TASK 1: Weekly Client Performance Reports**
**TASK 2: Client Call Agendas**
**TASK 3: CRM Updates After Calls**
**TASK 4: Internal Weekly Status Update**
**TASK 5: Monthly End-of-Month Reports**

For EACH task, tell me:

1. **Automation Score** (rate 1-5 on each criterion):
   - Repetitiveness (how often, how consistent)
   - Rules-based nature (could a new person follow written rules?)
   - Time cost (how long does manual take?)
   - Error risk (how bad is a mistake here?)
   - Creativity required (purely mechanical vs genuine thinking)

2. **Classification:** Fully automate / AI-assist (human reviews) / Keep manual?

3. **Why:** Explain your classification decision

4. **What Automation Looks Like:** Describe specifically how this task would work if automated. What triggers it? What does AI do? What does a human still review?

5. **Tools That Could Power This:** Which specific tool(s) would you use?

6. **Time Saved Per Week:** Realistic estimate

---

**SUMMARY:**
- Total hours currently spent on these 5 tasks per week
- Total hours after automation
- Hours saved per week and per month
- What would I do with that time that would create more value?

---

**PRIORITY ORDER:**
Given limited time to implement, which automation should I build first and why?''',
    },
    {
        'title': 'Question 10: Zapier + AI',
        'description': 'Build your first AI-powered automation connecting apps with triggered AI actions',
        'difficulty': 'intermediate',
        'order': 10,
        'points': 30,
        'instructions': '''Zapier is the glue that connects thousands of apps — and with AI actions built in, it becomes a powerful automation engine.

**What You'll Learn:**
- How Zapier's trigger → action logic works
- How to add AI steps that process and transform information
- How to design a practical Zapier + AI workflow from scratch

**Zapier Basics:**
Every Zap follows this pattern:
- **Trigger:** An event in App A (new email, new form submission, new row in sheet)
- **Action(s):** Things that happen in App B, C, D as a result
- **AI Step:** In between, AI processes/transforms the data

**Zapier AI Capabilities:**
- Summarise text content
- Classify or categorise items
- Draft response text based on input
- Extract specific information from unstructured content
- Translate content
- Score or evaluate content

**Common Powerful Combinations:**
- New form submission → AI classifies and summarises → Creates task in Asana/Notion
- New email → AI drafts reply → Saves to drafts for review
- New social mention → AI scores sentiment → Alerts if negative
- New invoice → AI extracts key fields → Adds to tracking sheet
- New review → AI analyses and categorises → Weekly digest to Slack

**Your Challenge:**
Design a complete Zapier + AI workflow for a real business use case.

**Choose one scenario:**
1. Automate the intake and triage of customer support emails
2. Automate the tracking and summarising of competitor social media mentions
3. Automate the conversion of sales call notes into CRM entries and follow-up tasks
4. Automate a weekly content digest from multiple sources

For your chosen scenario: design the complete workflow with every step, the AI prompt, and what the final output looks like.''',
        'example_prompt': '''Design a complete Zapier + AI workflow to automate customer support email intake and triage for a small software company.

**THE BUSINESS:**
"TaskMate" — a 15-person SaaS company with 2,000 customers. They receive 40-80 support emails per day through support@taskmate.io. Currently, one person manually reads every email, categorises it, and assigns it to the right team member. This takes 2 hours/day.

**THE PROBLEM:**
- Emails aren't categorised consistently
- Urgent issues sometimes get missed in the volume
- The wrong person often gets assigned (tech support vs billing vs features)
- Response time is inconsistent

**THE GOAL:**
Build a Zapier automation that: reads every incoming support email, categorises it, assesses urgency, drafts a first response, creates a ticket in their helpdesk, and alerts the right team member — before any human touches it.

---

**PART 1 — THE FULL WORKFLOW DESIGN**

Design the complete Zap. For each step:
- Step number and name
- What app/tool is used
- What specifically happens
- What data passes from this step to the next

The workflow should cover:
- Trigger: New email arrives in Gmail (support@taskmate.io)
- Step 1: [What happens first?]
- Step 2: [What happens next?]
- ... continue until the human sees an actionable, organised ticket

---

**PART 2 — THE AI CLASSIFICATION PROMPT**

Write the exact prompt that runs in Zapier's AI step to classify and analyse each email.

The AI needs to output (in a structured format):
1. **Category:** Bug Report / Billing Query / Feature Request / Account Issue / General Question
2. **Urgency:** P1 Critical / P2 High / P3 Normal / P4 Low (with criteria for each level)
3. **Assign to:** Technical Team / Billing Team / Customer Success / General Support
4. **Summary:** One-sentence description of the issue
5. **Sentiment:** Frustrated / Neutral / Positive
6. **Suggested response approach:** (Brief note on how to handle this)

Write the prompt so it outputs structured data (JSON or a clear format Zapier can parse).

---

**PART 3 — THE AUTO-DRAFT RESPONSE**

Write the prompt for a second AI step that drafts a personalised initial response email.

The draft should:
- Acknowledge the specific issue (using the summary from Step 2)
- Match the tone to the sentiment score (frustrated = more empathy, neutral = professional)
- Give a realistic response time estimate based on urgency level
- For P1/Critical: escalate language, immediate acknowledgment
- For routine questions: direct, friendly, efficient

Show me an example draft response for 3 different email types.

---

**PART 4 — THE HELPDESK TICKET**

What information should the auto-created helpdesk ticket contain?
Design the ticket template with all fields populated from the automation.

---

**PART 5 — ALERTS AND NOTIFICATIONS**

Design the alert system:
- P1 Critical: What alert goes out? To whom? How? (SMS? Slack? Phone call?)
- P2 High: What notification?
- P3/P4: What, if anything?

---

**PART 6 — MEASURING SUCCESS**

How would TaskMate know if this automation is working well?
- What metrics would they track?
- What does "success" look like after 30 days?
- What human review process should still exist?''',
    },
    {
        'title': 'Question 11: Make (Integromat)',
        'description': 'Build advanced visual AI workflows with Make\'s powerful multi-step automation',
        'difficulty': 'advanced',
        'order': 11,
        'points': 35,
        'instructions': '''Make (formerly Integromat) takes automation further than Zapier — with visual workflow building, advanced logic, and more complex multi-step processes.

**What You'll Learn:**
- How Make's visual workflow approach differs from Zapier
- Building multi-branch automations with conditional logic
- When to choose Make over Zapier for complex AI workflows

**Make vs Zapier:**

**Zapier:**
- Best for simple A→B automations
- Easier to get started
- Better app coverage for common tools
- Costs more at scale

**Make:**
- Better for complex, multi-step workflows
- Conditional branches (if/then logic)
- Better for loops and data transformation
- Visual workflow builder (see the whole flow)
- More cost-effective for high-volume automations

**Make's Unique Power:**
- **Routers:** Split workflow into multiple branches based on conditions
- **Iterators:** Process each item in a list separately
- **Aggregators:** Combine multiple items into one output
- **Error handling:** Sophisticated fallback logic

**Your Challenge:**
Design a complex Make workflow that processes form submissions, enriches the data with AI, and routes to different outcomes based on AI analysis.

**The scenario:** A consultancy runs a "Business Health Check" form. Visitors fill in 10 questions about their business. Make should: collect the response, have AI analyse it, score it, write a personalised report, and route to different follow-up sequences based on the score.

Design the complete workflow including conditional logic and multiple outputs.''',
        'example_prompt': '''Design a complex Make automation workflow that processes Business Health Check form submissions with AI and routes to different follow-up sequences.

**THE BUSINESS:**
"Venture Advisory" — a small business consultancy. They run a free "Business Health Check" where SME owners fill in a 10-question assessment on their website. Based on the results, they want to:
- Send a personalised, AI-generated report to the business owner
- Route the lead to different follow-up sequences based on their score
- Create a CRM contact with enriched profile
- Alert the relevant consultant team

**THE FORM (10 questions with scoring logic):**
1. How long have you been in business? (<1yr / 1-3yrs / 3+yrs)
2. What's your approximate annual revenue? (<£50K / £50K-£250K / £250K+)
3. Do you have a documented business strategy? (No / Informal / Formal written)
4. How would you rate your cash flow situation? (Crisis / Tight / Stable / Strong)
5. Do you have a clear sales process? (No process / Ad hoc / Defined process)
6. How reliant are you on one or two key clients? (Very / Somewhat / Not reliant)
7. Do you have any systems or processes documented? (None / Some / Comprehensive)
8. How confident are you in your team's ability to run things without you? (Not confident / Somewhat / Very confident)
9. Are you hitting your growth targets? (No and behind / Mixed / Yes consistently)
10. What's your biggest challenge? (Free text)

---

**PART 1 — THE SCORING SYSTEM**

Design a scoring algorithm:
- How many points does each answer get?
- What are the score ranges and what do they mean?
  - "Emergency" tier (needs urgent help)
  - "Foundations" tier (building basics)
  - "Growth" tier (ready to scale)
  - "Optimise" tier (fine-tuning a strong business)

---

**PART 2 — THE MAKE WORKFLOW MAP**

Design the full workflow as you'd build it in Make. For each module:
- Module name and app
- What it does
- What data it receives and sends forward

The workflow should include:
- Trigger: Typeform submission
- Data parsing and scoring calculation
- AI analysis module (what prompt? what output?)
- Router (branching into 4 different paths based on score tier)
- Different outcomes for each path
- CRM contact creation
- Consultant alert
- Confirmation email to the form submitter

Draw this as a text-based workflow diagram showing the branches.

---

**PART 3 — THE AI ANALYSIS PROMPT**

Write the Make AI module prompt that analyses the form responses and produces:
1. The business health score (calculated from the answers)
2. The tier classification
3. Top 3 strengths (based on their answers)
4. Top 3 most urgent areas to address
5. The personalised report intro paragraph (tailored to their specific situation)
6. The recommended next step (specific to their tier)

---

**PART 4 — THE FOUR PERSONALISED EMAILS**

Write the personalised email that goes out for each tier:

**Emergency tier email:** Empathetic, urgent, clear call-to-action (free 30-min call)
**Foundations tier email:** Encouraging, practical, resource-focused
**Growth tier email:** Energetic, forward-looking, coaching-focused
**Optimise tier email:** Peer-level, sophisticated, premium service focus

Each email: 150 words, personalised using the AI analysis output, specific to their answers.

---

**PART 5 — ERROR HANDLING**

What happens when something goes wrong?
- The AI step fails (timeout or error)
- The CRM rejects the contact creation (duplicate)
- The email fails to send
- The form response is missing critical fields

Design Make's error handling for each scenario.''',
    },
    {
        'title': 'Question 12: Email & Calendar Automation',
        'description': 'Use AI to draft replies, categorise emails, schedule meetings, and manage your inbox',
        'difficulty': 'intermediate',
        'order': 12,
        'points': 30,
        'instructions': '''Email is where most professionals spend 2-3 hours every day. AI can dramatically reduce that.

**What You'll Learn:**
- How to use AI to draft, categorise, and manage email
- How to automate calendar scheduling and meeting prep
- Building an AI-powered inbox management system

**The Email AI Toolkit:**

**Drafting:**
- Draft replies based on email context and your preferences
- Generate personalised outreach at scale
- Write follow-up sequences

**Categorisation:**
- Automatically sort emails by type, urgency, sender
- Flag emails requiring a decision vs just information
- Identify which emails an AI could draft a reply for

**Calendar:**
- Draft meeting request emails with clear agendas
- Create meeting summaries from notes
- Schedule follow-up meetings based on conversation context
- Prepare briefing documents before important calls

**The "Zero Inbox" AI System:**
1. Email arrives → AI categorises and prioritises
2. Routine emails → AI drafts reply for approval
3. Important emails → AI summarises and flags key decision
4. Meeting requests → AI checks calendar and suggests times
5. End of day → AI digest of outstanding items

**Your Challenge:**
Design a complete AI email management system for a specific professional's inbox — showing how AI handles different email types and reduces the manual workload.

Pick a professional role (sales executive, operations manager, freelancer, etc.) and design the full system.''',
        'example_prompt': '''Design a complete AI email management system for a busy sales executive. Show me how AI handles each type of email and what the system looks like in practice.

**THE PERSON:**
James — a Senior Sales Executive at a cloud software company. He manages 40 active sales opportunities at various stages and receives 80-120 emails per day. His email is a mix of:
- Prospect enquiries and cold inbound (25% of emails)
- Active deal communications (35% of emails)
- Internal communications from colleagues and managers (25% of emails)
- Newsletters, marketing, admin (15% of emails)

His biggest pain points:
- Missing follow-ups because emails get buried
- Spending 45 minutes each morning just triaging
- Writing similar "check-in" emails repeatedly
- Not having context ready before important calls

---

**PART 1 — THE CATEGORISATION SYSTEM**

Design how AI would automatically categorise every email James receives.

Create a categorisation matrix with:
- Category names (at least 8 specific categories for his work)
- What makes an email belong to each category
- The priority level for each (respond today / respond this week / no response needed)
- The default action for each category (draft reply / forward / file / flag for attention)

---

**PART 2 — SIX EMAIL TYPES: AI DRAFT PROMPTS**

Write the AI drafting prompt for each of these 6 common email types James sends:

**Type 1: Response to a prospect who filled in the "request a demo" form**
What info does the AI need? Write the exact prompt James would use to auto-draft this.

**Type 2: Follow-up after a discovery call where the prospect seemed interested**
Context needed + the draft prompt.

**Type 3: Chasing a proposal that's been out for 2 weeks with no response**
Context needed + the draft prompt (polite but persistent).

**Type 4: Declining a meeting request professionally (not a fit)**
Context needed + the draft prompt.

**Type 5: Requesting a reference call with an existing happy customer, for a new prospect**
Context needed + the draft prompt.

**Type 6: Weekly pipeline update to his sales manager**
Data inputs needed + the draft prompt.

---

**PART 3 — THE PRE-CALL BRIEFING AUTOMATION**

James has an important discovery call every day. Design an automation that:

**30 minutes before each calendar event:**
- Pulls any email thread with that company/contact from the past 90 days
- Summarises the relationship history and key conversation points
- Lists any open questions or commitments from previous conversations
- Pulls the company's recent news (if web access available)
- Creates a one-page briefing document in his Notion or Google Docs

Show the complete automation design and the AI prompt that generates the briefing.

---

**PART 4 — THE WEEKLY EMAIL DIGEST**

Every Friday at 4pm, James wants an automated digest. Design what it contains:
- Emails that need a response this week and haven't been replied to
- Open follow-ups that are overdue
- Deal activity summary (which prospects have been engaged, which have gone quiet)
- Suggested priority actions for next Monday

Write the prompt that generates this digest from his email and calendar data.

---

**PART 5 — ROI CALCULATION**

If this system works as designed:
- Time spent on email management before: X hours/week
- Time spent after: Y hours/week
- What would James do with the hours saved?
- What's the business value of faster, more consistent follow-up?''',
    },
    {
        'title': 'Question 13: Content Pipelines',
        'description': 'Build an automated content creation pipeline from idea to published post',
        'difficulty': 'advanced',
        'order': 13,
        'points': 35,
        'instructions': '''Content creation is one of the highest-ROI areas for AI automation — especially for businesses that need consistent output across multiple platforms.

**What You'll Learn:**
- How to design an end-to-end content pipeline
- How AI handles each stage (ideation → drafting → editing → formatting → scheduling)
- How to maintain quality and brand voice at scale

**The Content Pipeline Stages:**

1. **Ideation:** Topic generation based on trends, keywords, audience questions
2. **Brief Creation:** From topic to detailed content brief
3. **First Draft:** AI writes based on brief
4. **SEO/Platform Optimisation:** Adapts for search or specific platforms
5. **Human Review:** Quality gate — catch errors, inject personality
6. **Multi-Platform Formatting:** Blog → LinkedIn → Twitter → Email → Instagram
7. **Scheduling:** Auto-schedule to publishing tools
8. **Performance Tracking:** Monitor and feed back into ideation

**Tools in a Content Pipeline:**
- Idea generation: Perplexity, ChatGPT, Ahrefs/SEMrush
- Drafting: Claude, ChatGPT, Jasper
- SEO: Surfer SEO, Clearscope
- Scheduling: Buffer, Hootsuite, Later
- Automation glue: Zapier, Make
- Storage: Notion, Airtable, Google Sheets

**Your Challenge:**
Design a complete automated content pipeline for a specific business.

**The business:** A UK-based personal finance blog targeting millennials (25-40) working through "adulting" financial decisions — home buying, savings, investing, debt management.

Design the full pipeline: from idea generation to published content across 3 platforms.''',
        'example_prompt': '''Design a complete automated content pipeline for "MoneyMature" — a UK personal finance blog targeting millennials navigating adult financial decisions.

**THE BRAND:**
MoneyMature covers: first-time home buying, ISAs and savings, debt management, starting to invest, and managing money as a couple or new parent. Tone: friendly, honest, non-judgmental, and practical. We don't talk down to readers. No financial jargon without explanation.

**TARGET PLATFORMS:**
1. Blog (WordPress) — 2 long-form posts per week
2. LinkedIn — 3 posts per week
3. Email newsletter — 1 per week (Monday morning)

**CURRENT SITUATION:**
One part-time writer produces 2 posts/week maximum. They want to scale to 2 blog posts + 3 LinkedIn posts + 1 email per week without hiring.

---

**PART 1 — TOPIC IDEATION SYSTEM**

Design the weekly topic generation process:

**A) Automated Idea Sources:**
What data sources should feed the ideation process? (Where do good money content ideas come from?)

**B) The Ideation AI Prompt:**
Write the weekly prompt that generates 10 blog topic ideas. It should:
- Reference current financial news/events (via web search)
- Consider seasonal relevance (e.g., ISA season, tax year end)
- Match the audience's life stage (first home, starting investing)
- Score each idea on: audience relevance, search potential, competition, freshness

**C) Topic Approval Step:**
How does the human quickly review and approve ideas? Design the lightweight approval interface.

---

**PART 2 — THE CONTENT BRIEF GENERATOR**

Once a topic is approved, design the automation that creates a full content brief.

The brief should automatically include:
- Target keyword and 5 secondary keywords
- Recommended article structure (H2 headers)
- What the article must cover
- What competing articles are missing (the angle to differentiate)
- Recommended word count
- Tone guidance specific to this topic
- 3 specific examples or case studies to include

Write the AI prompt that generates this brief from just the approved topic.

---

**PART 3 — THE FIRST DRAFT PIPELINE**

Design the complete drafting process:

**A) Blog Post Drafting Prompt:**
Write the AI prompt that takes the brief and produces a first draft. Include in the prompt:
- MoneyMature's specific style rules
- UK-specific requirements (ISAs not 401Ks, pounds not dollars)
- How to handle financial advice disclaimers appropriately
- Word count and structure requirements

**B) From Blog to LinkedIn (Repurposing Prompt):**
Write the prompt that takes the finished blog post and creates 3 LinkedIn posts from it:
- Post 1: The key insight/lesson (hook + value)
- Post 2: A contrarian or surprising angle from the post
- Post 3: A personal finance question inspired by the post (drives comments)

**C) From Blog to Email Newsletter:**
Write the prompt that creates the Monday email from that week's content:
- Subject line (3 options to test)
- Personal intro (2-3 sentences from the "editor")
- Summary of the week's 2 blog posts
- "This week's money tip" (standalone value)
- CTA

---

**PART 4 — THE QUALITY GATE**

What should the human editor review before anything is published?

Design the review checklist:
- Factual accuracy checks (what specifically to verify?)
- Brand voice check (what are the red flags?)
- UK compliance/disclaimer check
- SEO check (is the keyword used naturally?)
- Readability check (what's the standard?)

How long should a proper review take if AI did its job well? What's the target?

---

**PART 5 — PERFORMANCE FEEDBACK LOOP**

How does content performance data feed back into the next cycle of ideation?

Design the monthly performance review process:
- What metrics to track
- How to identify what topics/formats work best
- How to update the AI prompts based on what's working
- How to evolve the pipeline as you learn more about the audience''',
    },
    {
        'title': 'Question 14: Data Collection & Automated Reporting',
        'description': 'Build automated data gathering and AI-generated reporting workflows',
        'difficulty': 'advanced',
        'order': 14,
        'points': 35,
        'instructions': '''Pulling together data from multiple sources and writing reports is one of the biggest time sinks in professional life. AI can automate most of it.

**What You'll Learn:**
- How to build automated data collection flows
- How AI turns raw data into written insights and narratives
- How to create reporting systems that run themselves

**The Data-to-Report Pipeline:**
1. **Collection:** Pull data automatically from multiple sources
2. **Consolidation:** Merge into a single, clean dataset
3. **Analysis:** AI identifies trends, outliers, and key insights
4. **Narrative:** AI writes the report text based on the data
5. **Formatting:** Convert to professional document/presentation
6. **Distribution:** Auto-send to relevant recipients

**Tools That Power This:**
- Data collection: Zapier, Make, Google Apps Script
- Storage: Google Sheets, Airtable, Notion databases
- Analysis: Claude, ChatGPT, Python (with AI assistance)
- Report creation: Google Docs API, Notion, Gamma
- Distribution: Gmail, Slack, Microsoft Teams

**Your Challenge:**
Design a complete automated reporting system for a real business scenario.

**The scenario:** A marketing agency needs to deliver weekly performance reports to 8 different clients. Each report pulls data from Google Analytics, social media platforms, and ad spend tracking. Currently, the team spends 6 hours every Friday producing these reports manually.

Design the automation that makes this nearly zero effort — from data collection to client inbox.''',
        'example_prompt': '''Design a complete automated weekly client reporting system for a digital marketing agency. This should eliminate 80% of the manual work currently taking 6 hours every Friday.

**THE AGENCY:**
"Beacon Digital" — a 20-person digital marketing agency. They have 8 clients, each receiving a weekly performance report every Friday by 5pm. Currently the process: account managers pull data from multiple platforms, paste it into a Word template, write insight paragraphs, format everything, then email it. Takes 45 min per client × 8 clients = 6 hours of senior account manager time every Friday.

**DATA SOURCES PER CLIENT:**
- Google Analytics 4: website traffic, conversions, source breakdown
- Google Ads: spend, impressions, clicks, conversions, ROAS
- Meta Ads Manager: spend, reach, engagement, conversions
- Instagram Insights: follower growth, post performance
- Email platform (Mailchimp): open rates, clicks, list growth

**REPORT STRUCTURE (currently in the Word template):**
1. Executive Summary (200 words — the most important this week)
2. Performance Scorecard (table: KPIs vs targets, colour-coded RAG)
3. Top Wins This Week (3 bullet points)
4. Areas of Concern (2-3 bullets + recommended actions)
5. Campaign Spotlight (1 campaign with detailed breakdown)
6. Next Week's Focus (3 planned activities)

---

**PART 1 — DATA COLLECTION ARCHITECTURE**

Design how data gets collected automatically every Thursday night (ready for Friday delivery):

For each data source:
- What API or connection method to use
- What specific data fields to pull
- Where the data gets stored (what tool/format)
- How to handle when data isn't available (API errors, platform outages)

Show the data flow diagram (text-based).

---

**PART 2 — THE DATA CONSOLIDATION SHEET**

Design the master Google Sheet structure that holds all client data:

- What are the tabs/sheets?
- What columns exist in the main data sheet?
- How is client data separated from each other?
- How are week-over-week and month-over-month comparisons calculated automatically?

---

**PART 3 — THE AI REPORT GENERATION PROMPT**

Write the core AI prompt that generates each client's report from their consolidated data.

The prompt should:
- Receive the client's data as structured input
- Know the client's context (industry, goals, what they care about)
- Generate all 6 report sections
- Write insights that explain WHY metrics moved, not just that they moved
- Match Beacon Digital's professional but accessible report tone
- Flag anomalies and patterns a human might miss

Show the prompt template with [PLACEHOLDERS] for the data inputs.

---

**PART 4 — SAMPLE REPORT OUTPUT**

Using fictional data for Client 1 ("Oakfield Furniture" — an e-commerce furniture retailer), show what the AI-generated report would look like:

Fictional data to use:
- Website sessions: 12,400 (↑18% vs last week)
- Conversions: 89 (↑5% vs last week)
- Google Ads spend: £2,100 (conversion rate dropped from 3.2% to 2.8%)
- Meta Ads: £800 spend, reach 45,000 (↑30%), but ROAS dropped to 1.4 (was 2.1)
- Email: 32% open rate (↑4pts), 8 sales attributable

Generate the full 6-section report from this data.

---

**PART 5 — AUTO-FORMATTING AND DISTRIBUTION**

Design the final stage:
- How the AI output gets formatted into the branded Word/PDF report
- How client reports are automatically named and saved
- How each report gets emailed to the right client at the right time
- How to handle customisation per client (different KPIs, different benchmarks)

---

**PART 6 — QUALITY CONTROL**

What's the minimum human review process that should always happen?
- What does the account manager check in 5 minutes?
- What are the red flags that mean "don't send this automatically"?
- How do you ensure a client never sees a report with obvious AI errors?''',
    },
    {
        'title': 'Question 15: No-Code AI App Building',
        'description': 'Build a simple AI-powered application without writing any code',
        'difficulty': 'advanced',
        'order': 15,
        'points': 40,
        'instructions': '''You don't need to be a developer to build AI-powered applications. No-code tools let anyone create useful apps in hours.

**What You'll Learn:**
- The major no-code AI app building platforms
- How to think like an app designer without coding skills
- How to build and deploy a simple AI-powered tool

**The Key No-Code AI Platforms:**

**Softr:** Build web apps from databases (Airtable, Google Sheets) — portals, directories, tools
**Glide:** Turn spreadsheets into polished mobile apps with AI features
**Bubble:** More powerful no-code builder with complex logic
**Typeform + AI:** Smart forms that adapt based on answers
**Notion + Make:** Workflows that feel like apps without being apps
**Pory:** Build portals from Airtable/Notion data

**Types of Apps You Can Build Without Code:**
- Customer FAQ bots (answer questions from your documentation)
- Feedback collection and analysis tools
- Internal knowledge bases with AI search
- Client intake and onboarding forms with personalised responses
- Quote calculators with AI recommendations
- Content generators with your brand voice

**Your Challenge:**
Design and spec a complete no-code AI-powered application.

**Choose one:**
- A customer FAQ bot for a specific business
- A feedback analyser that collects and categorises customer responses
- A content generator tool for a specific type of content
- An AI job matching tool (for a recruitment niche)

Design the full application: user journey, AI components, data structure, and how to build it with no-code tools.''',
        'example_prompt': '''Design a complete no-code AI-powered application: a "Customer FAQ Bot" for a small e-commerce business. I want a full spec I could actually build.

**THE BUSINESS:**
"Petal & Stem" — an online flower subscription service. Customers can subscribe to weekly, fortnightly, or monthly fresh flower deliveries. They receive 30-50 customer service messages per day via their website chat, mostly asking the same 20 questions.

**THE GOAL:**
Build an AI FAQ bot that: answers 80% of questions automatically, collects contact info and escalates the other 20% to a human, and works 24/7 — reducing Petal & Stem's customer service workload by 3 hours per day.

**TOOLS TO USE:**
Budget: Free or under £30/month. No technical staff.

---

**PART 1 — THE APPLICATION DESIGN**

**A) User Journey Map**
Walk me through the complete customer experience:
- How do they find and open the bot?
- What happens in the first message?
- How does the conversation flow for the 5 most common question types?
- How does the bot hand off to a human when it can't help?
- What happens after the conversation ends?

**B) The Knowledge Base**
Design the FAQ document that powers the bot. Write all 20 Q&As the bot needs to know:

Include the 20 most common questions for a flower subscription service — covering: subscription management, delivery, quality issues, gifting, pricing, and account management.

For each Q&A: write it in a natural conversational format the bot will use, not formal FAQ style.

**C) Bot Personality**
Define the bot's persona: name, personality, tone, and 3 sample responses that capture the brand voice.

---

**PART 2 — THE TECH STACK**

Given the budget and no-code constraint, recommend the specific tools to build this:

For each component:
- Which tool to use and why
- Free vs paid? What's the cost?
- How it connects to the other tools
- How long it takes to set up

Components needed:
- The bot interface (where does it live on the website?)
- The AI model powering it (which AI and how to connect it)
- The knowledge base storage
- The escalation/handoff system
- The conversation history log
- The reporting (how many questions answered, escalation rate)

---

**PART 3 — THE AI PROMPT**

Write the system prompt that defines how the bot behaves:
- Its identity and personality
- How it greets customers
- How it uses the FAQ knowledge base
- When to escalate (be specific — what situations?)
- What to do when it doesn't know the answer
- Response length and format rules
- What it should NEVER say

---

**PART 4 — THE ESCALATION FLOW**

Design what happens when the bot can't help (the 20% escalation):
- How does it recognise it's out of its depth?
- What does it say to the customer?
- What information does it collect? (Name, email, order number, issue summary)
- Where does this information go? (Email, Slack, Airtable?)
- What does the human agent see when they pick up the conversation?

---

**PART 5 — BUILD PLAN**

Give me a step-by-step plan to build this in one weekend:

Saturday: [What to do]
Sunday: [What to do]
Monday morning: [Testing and launch]

Include: exact tools to sign up for, what to build first, how to test it, and how to launch it on the website.

---

**PART 6 — SUCCESS METRICS**

After 30 days, how would Petal & Stem know if this bot is working?
- What to measure
- What "good" looks like
- What would trigger a redesign or improvement
- The most important single metric''',
    },
    {
        'title': 'Question 16: Building Your First Full Workflow',
        'description': 'Design and document a complete end-to-end AI automation that solves a real problem',
        'difficulty': 'advanced',
        'order': 16,
        'points': 40,
        'instructions': '''You've learned all the building blocks. Now it's time to design a complete, sophisticated workflow that solves a real business problem end-to-end.

**What You'll Demonstrate:**
- Multi-step workflow design with AI at multiple stages
- Integration of different tools and platforms
- Error handling and quality control
- Documentation professional enough for someone else to build from

**What "Full Workflow" Means:**
A complete workflow has:
- **A clear problem** it solves with measurable impact
- **A defined trigger** that starts the process
- **Multiple steps** including at least 2 AI stages
- **Conditional logic** (different paths for different inputs)
- **A human checkpoint** at the right moment (not too early, not too late)
- **A defined output** that creates real value
- **Error handling** for when things go wrong
- **Metrics** to measure if it's working

**Your Challenge:**
Design a complete, documented automation workflow that solves a real problem in your professional or personal life.

This is your Module 3 Part 2 capstone — show everything you've learned about automation.

**Requirements:**
- Solves a real, high-value problem (not trivial)
- Uses at least 3 different apps/tools
- Includes at least 2 AI steps with actual prompts
- Has conditional logic (branches)
- Includes a human review checkpoint
- Comes with a full implementation guide
- Includes success metrics''',
        'example_prompt': '''I'm designing a complete end-to-end workflow to solve a real business problem. This is my automation capstone.

**THE PROBLEM:**
I run a freelance copywriting business. Every new client enquiry goes through a chaotic, manual process: they email me, I spend 20-30 minutes reading through their brief (if they send one), I ask 5-10 clarifying questions over multiple emails, I research their company and competitors, then I send a proposal. The whole intake process takes 2-4 days and 90 minutes of my time per lead — and I miss 30% of enquiries because I forget to follow up.

**THE SOLUTION:**
A fully automated client intake and proposal workflow that: captures enquiries, qualifies and scores them, gathers all the information I need, researches the client, generates a first-draft proposal for my review, and follows up automatically if they don't respond.

---

**SECTION 1 — WORKFLOW OVERVIEW**

Write a one-paragraph description of this workflow that explains:
- What it does
- What triggers it
- The main stages
- What it produces
- The estimated time it saves me per month

---

**SECTION 2 — THE COMPLETE WORKFLOW MAP**

Map every step of the workflow. For each step:

| Step # | Step Name | Tool/App | What Happens | Input | Output | Notes |

Include every step from "enquiry arrives" to "proposal in client's inbox."

---

**SECTION 3 — THE SMART INTAKE FORM**

Design the intake form that replaces the chaotic email back-and-forth.

What questions does it ask? (Design 10 questions that give me everything I need for a proposal)

For each question:
- The question text
- Answer type (dropdown, free text, multiple choice, etc.)
- Why this question matters
- How the answer will be used downstream in the workflow

---

**SECTION 4 — THE TWO AI STEPS**

**AI Step 1 — Client Research and Scoring:**
Write the prompt that:
- Receives the intake form answers
- Researches the company (using web search if available)
- Scores the lead (A/B/C based on fit and value)
- Produces a "client briefing" document I can read in 2 minutes

**AI Step 2 — Proposal First Draft:**
Write the prompt that:
- Takes the brief and research
- Generates a professional proposal draft in my voice
- Includes: project scope, my approach, timeline, and pricing structure (with [PRICE TO FILL IN] placeholder)
- Flags 3 things I should verify or personalise before sending

---

**SECTION 5 — CONDITIONAL LOGIC**

Design the branching logic:

**If lead score = A (high value):**
→ What happens? (Different urgency, different proposal, different follow-up)

**If lead score = B (medium value):**
→ Standard process

**If lead score = C (low fit):**
→ Polite decline template, or redirect to lower-cost option

**If form submitted but I don't respond within 48 hours:**
→ Automatic follow-up sequence

---

**SECTION 6 — THE HUMAN CHECKPOINT**

At what exact point do I step in?

- What do I see when I review? (What does my "review dashboard" look like?)
- What decisions do I make?
- What does "approve and send" trigger?
- What does "send back for revision" trigger?

---

**SECTION 7 — IMPLEMENTATION GUIDE**

Write a step-by-step guide to build this workflow:
- Tools to use (with free tier options where possible)
- Order to build the steps (start with the highest-value parts)
- How to test before going live
- What to launch first (minimum viable version) vs what to add later

---

**SECTION 8 — SUCCESS METRICS**

After 60 days, how will I know if this workflow is working?

Define:
- 3 metrics to track
- What "success" looks like for each
- What would signal a problem with the workflow
- One thing I'd do to improve it after the first 30 days''',
    },
]
