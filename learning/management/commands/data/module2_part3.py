"""
Module 2 Part 3: Power Features & Professional Workflows — "AI at Work"
Challenges 17-24: Combining tools and features for real professional workflows (4-5 hours)
"""

MODULE2_PART3_CHALLENGES = [
    {
        'title': 'Question 17: AI for Spreadsheets & Data',
        'description': 'Use AI to clean messy data, build formulas, and turn numbers into insights',
        'difficulty': 'intermediate',
        'order': 17,
        'points': 30,
        'instructions': '''Data doesn't have to be scary. AI can help you turn messy spreadsheets into clear insights — even if you're not a data person.

**What You'll Learn:**
- How AI helps with data cleaning and formatting
- How to generate Excel/Sheets formulas by describing what you want
- How to turn raw data into a meaningful narrative

**What AI Does Well with Data:**

**Data Cleaning:**
- Standardise inconsistent text (all caps, mixed case, extra spaces)
- Identify and suggest fixes for missing or suspect values
- Restructure data from one format to another

**Formula Generation:**
- Describe what you want in plain English → get the formula
- Explain what complex formulas actually do
- Debug formulas that aren't working

**Analysis and Storytelling:**
- Turn a dataset into a written summary with key insights
- Identify trends, outliers, and anomalies
- Create chart recommendations based on the data type

**Your Challenge:**
Work with a messy sales dataset and use AI to:
1. Clean and standardise the data
2. Generate useful formulas
3. Extract the 3 most important insights
4. Write an executive summary of the findings

**Include in your prompt:**
- A realistic messy dataset (you can invent the numbers)
- Specific data cleaning requests
- 3-4 formula requests described in plain English
- A request for insight extraction and storytelling

**The test:** Could a non-data person understand the output and act on it?''',
        'example_prompt': '''I have a messy monthly sales spreadsheet that needs cleaning, analysing, and turning into clear insights. Help me work through this systematically.

---

**THE MESSY DATA:**

Here's a sample of our online shop's sales data for January (it's been exported from 3 different systems and is a mess):

| Date | Sales Rep | Region | Product | Units | Revenue | Customer Type |
|------|-----------|--------|---------|-------|---------|---------------|
| 01/01/24 | sarah jones | London | Widget Pro | 12 | £1440 | New |
| 1st Jan | SARAH JONES | london | widget pro | - | 1440 | new customer |
| Jan 3 | Tom B | Manchester | Widget Lite | 8 | £560 | returning |
| 03-01-2024 | thomas brown | manch | Widget lite | 8 | 560.00 | Returning |
| 5/1/24 | Priya S | Birmingham | Widget Pro | 20 | £2400 | NEW |
| Jan 5 | priya sharma | bham | Widget Pro | 20 | 2400 | N |
| 7 Jan | tom | Mnchstr | Widget Plus | 5 | £875 | Existing |
| 07/01/24 | T. Brown | Manchester | Widget Plus | 5 | 875 | existing customer |

(The full dataset has 200 rows like this — some duplicates, some inconsistencies, some missing values)

---

**PART 1 — DATA CLEANING PLAN:**

Looking at this sample, identify:
1. Every inconsistency type present (list them all)
2. The standardisation rules I should apply to fix each type
3. For dates: what format should I standardise to?
4. For the "Customer Type" column: what are the distinct values and how should each be mapped to a clean standard?
5. How would I identify probable duplicate rows?

Write me a step-by-step data cleaning protocol I can follow.

---

**PART 2 — FORMULA GENERATION:**

Write the Excel/Google Sheets formula for each of these requests:

1. "Count the total number of transactions from the London region"
2. "Calculate the average revenue per sale, excluding any rows where revenue is blank or zero"
3. "Show me the top 3 sales reps by total revenue using a SUMIF approach"
4. "Flag any row where the Units column is blank or contains a dash as 'MISSING DATA'"
5. "Calculate what percentage of total revenue each region represents"

For each formula: write it out, explain what each part does in plain English, and note any assumptions you've made.

---

**PART 3 — INSIGHTS EXTRACTION:**

Assuming the full dataset is clean, here are the actual January summary numbers:
- Total revenue: £47,300
- Units sold: 412
- London: 45% of revenue
- Manchester: 30% of revenue
- Birmingham: 25% of revenue
- Widget Pro: 58% of revenue, 38% of units
- Widget Lite: 22% of revenue, 42% of units
- Widget Plus: 20% of revenue, 20% of units
- New customers: 62% of transactions
- Returning customers: 38% of transactions
- Top performer: Priya Sharma (£18,200 revenue, 38% of total)
- January vs December: +12% revenue, +8% units

Extract the 5 most important insights from this data. For each insight: state it clearly, explain why it matters, and suggest one action to take based on it.

---

**PART 4 — EXECUTIVE SUMMARY:**

Write a 150-word executive summary of January's sales performance that:
- Leads with the most important headline
- Covers: revenue, key product performance, regional trends, customer acquisition vs retention
- Flags the most important thing to investigate further
- Ends with a forward-looking statement for February

Professional tone — this goes to the company directors on Monday morning.''',
    },
    {
        'title': 'Question 18: AI Voice & Transcription',
        'description': 'Turn meetings, recordings, and audio into organised, actionable text',
        'difficulty': 'intermediate',
        'order': 18,
        'points': 30,
        'instructions': '''Every meeting, every call, every interview — what if you never missed an action item again?

**What You'll Learn:**
- The major AI transcription tools and what they do best
- How to prompt AI to extract maximum value from transcripts
- How to turn raw transcription into professional outputs

**The Key Tools:**

**Transcription:**
- **Otter.ai:** Real-time transcription, speaker identification, meeting summaries
- **Fireflies.ai:** Meeting recorder with CRM integration, searchable archive
- **Whisper (OpenAI):** Open source, highly accurate, good for sensitive content
- **Microsoft Teams / Google Meet:** Built-in transcription in enterprise plans

**What You Can Extract from a Transcript:**
- Key decisions made
- Action items with owners
- Open questions unresolved
- Tone and sentiment of the meeting
- A summary email for people who couldn't attend
- Follow-up questions to ask

**The AI Workflow:**
1. Record/transcribe the meeting
2. Paste transcript into AI chat
3. Extract specific outputs with targeted prompts

**Your Challenge:**
Work with a raw, messy meeting transcript and use AI to extract maximum value from it.

Write a prompt that takes a realistic meeting transcript and produces:
1. A clean summary of what was discussed
2. All decisions made
3. All action items in a table format
4. A follow-up email for absent team members
5. The top 3 unresolved questions that need answers

Make your prompt specific, structured, and produce outputs someone could act on immediately.''',
        'example_prompt': '''I have a raw meeting transcript that needs turning into professional, actionable outputs. Work through this systematically.

---

**RAW TRANSCRIPT:**
(This is a lightly edited auto-transcription — there are speaker mix-ups and run-on sentences)

"Rachel: okay I think we're all here, so let's get started, it's the weekly product review, so uh, Alex can you give us the update on the app redesign?

Alex: yeah sure so we finished the wireframes last Tuesday and Lisa has been reviewing them, Lisa do you want to jump in?

Lisa: yeah so I've looked through them and honestly I think the onboarding flow is still too complicated for new users, we did some user testing last week, only 3 people but all three of them got confused at the payment step, so I think we need to rethink that section before we move to development

Alex: ok that's fair, so should we delay the dev start date? it was meant to be the 20th

Rachel: how long would you need to rework the onboarding?

Lisa: I'd say at least a week, maybe ten days to do it properly and test again

Rachel: ok so let's push dev start to March 3rd, Alex can you update the project plan and send to the whole team by Thursday?

Alex: yep, will do

Rachel: what about the API issue Tom mentioned in the last meeting, is that resolved?

Tom: so sort of, the integration with Stripe is working now but we've hit a problem with the webhook timeouts, I'm working with the Stripe support team, they've been pretty slow to respond honestly, it might need to go to their tier two support

Rachel: how long could that take?

Tom: could be another week, could be two, hard to say

Rachel: ok that's a risk, um, Sam can you add a contingency for this in the risk register?

Sam: sure, I'll update it today

Rachel: good. The other thing I wanted to flag is the marketing timeline, Sophie, where are we with the launch campaign?

Sophie: so we have the copy ready and the social assets are being designed this week, we're still waiting on final brand approval from the client though, they said by Friday but I'm not confident

Rachel: that's concerning, if we don't have brand approval by Friday the whole launch timeline moves, Sophie can you follow up with the client today and escalate if you don't hear by end of tomorrow?

Sophie: yes absolutely

Rachel: ok I think that's everything, let's meet again next Wednesday same time, can everyone confirm they're free?

Everyone: yeah, sure, fine

Rachel: great, thanks all"

---

**WHAT I NEED:**

**1. MEETING SUMMARY** (5-7 sentences)
What was this meeting about, what was the mood/outcome, and what are the critical things to know?

**2. DECISIONS MADE**
List every decision made. Format: Decision | Who Decided | Impact

**3. ACTION ITEMS TABLE**
Extract every action item:
| Task | Owner | Deadline | Priority (H/M/L) | Notes |
If no deadline was stated, suggest a reasonable one based on context.

**4. FOLLOW-UP EMAIL**
Write a professional email from Rachel to the full product team (including people not in the meeting):
- Subject line that conveys urgency appropriately
- Quick context: what was covered
- Decisions made
- Actions required (with owners and deadlines)
- Risks flagged
- Next meeting details
- Max 250 words, professional but not stiff

**5. OPEN QUESTIONS THAT NEED ANSWERS**
List the unresolved issues that could affect the project if not answered quickly.

Format everything clearly with headers. This is going out to the team today.''',
    },
    {
        'title': 'Question 19: Notion AI & Smart Workspaces',
        'description': 'Build an AI-powered workspace that organises your work and thinks alongside you',
        'difficulty': 'intermediate',
        'order': 19,
        'points': 30,
        'instructions': '''Notion AI transforms a note-taking app into an intelligent workspace that actively helps you work.

**What You'll Learn:**
- How Notion AI differs from standalone AI tools
- How to design an AI-powered workspace for real projects
- How automated summaries, smart databases, and AI blocks work together

**What Notion AI Can Do:**
- **Write and edit** directly inside your documents
- **Summarise** long pages or databases
- **Auto-fill properties** in databases based on content
- **Generate** agendas, action items, and first drafts from bullet notes
- **Ask questions** about your workspace content
- **Create** complete project setups from a brief

**Why It's Different:**
Unlike general AI chat tools, Notion AI has context. It can see your notes, your projects, your meeting records. Every AI action is informed by what's already in your workspace.

**Smart Workspace Features:**
- Meeting notes database with auto-summaries
- Project tracker with AI-generated status updates
- Reading notes with auto-extracted key takeaways
- Goal tracker with AI-suggested next actions
- Client database with AI-generated briefings

**Your Challenge:**
Design a complete AI-powered project workspace for a specific real project.

**Your project:** Choose something you're actually working on (or invent a realistic one): launching a freelance business, running a personal project, organising a major event, building a side hustle.

Design the full workspace: all the pages, databases, AI automations, and templates you'd use — with the actual Notion AI prompts for each.''',
        'example_prompt': '''Design a complete AI-powered Notion workspace for managing my freelance social media consultancy. Include all the pages, databases, and AI prompts I'd use.

**MY FREELANCE BUSINESS:**
I run a freelance social media consultancy. I manage 6 ongoing clients, each with their own content calendar, monthly reporting, and strategy. I also do project-based work (audits, one-off campaigns). I'm a solo operator — no team.

My main frustrations:
- I lose track of what I've promised each client
- Monthly reports take 3 hours each (pulling data, writing insights, formatting)
- Client briefings are scattered across emails and notes
- I forget follow-ups and action items from client calls

**DESIGN MY WORKSPACE:**

---

**SECTION 1 — WORKSPACE ARCHITECTURE**

What are the main sections (pages/databases) I need? Give me:
- A complete workspace map (what pages exist and how they connect)
- Which parts should be databases (with filters/views) vs regular pages
- How information flows between sections

---

**SECTION 2 — KEY DATABASES WITH AI FEATURES**

Design these 4 databases in detail:

**A) Client Hub Database**
- Properties I need (columns): list them all
- Default views: (by client, by status, by next action)
- The Notion AI prompt I'd use to auto-generate a "Client Briefing" from the properties filled in
- The AI prompt for generating a monthly check-in agenda from the client's history

**B) Content Calendar Database**
- Properties needed for each content piece
- How it links to the Client Hub
- The AI prompt for generating a week's worth of post ideas from a client brief
- The AI prompt for turning "topic + platform" into a full draft post

**C) Meeting Notes Database**
- Template for a client call note
- The Notion AI prompt that turns rough bullet notes into:
  - A clean meeting summary
  - Action items extracted to my task list
  - A follow-up email draft

**D) Monthly Report Template**
- The full template structure for a client report
- The Notion AI prompt that turns raw data input into written insight paragraphs
- The prompt that generates the "key recommendations" section from performance data

---

**SECTION 3 — MY AI WORKFLOW**

Describe my typical Monday morning workspace routine using Notion AI:
- What I check, in what order
- Which AI prompts I'd use to set up the week
- How I'd use AI to prioritise my task list

---

**SECTION 4 — THE "NEW CLIENT" SETUP PROMPT**

Write the exact Notion AI prompt I'd use when onboarding a new client — to automatically generate:
- Their client page from a brief
- First month content calendar structure
- Onboarding checklist
- Welcome email draft

Make this practical enough that I could set it up this week.''',
    },
    {
        'title': 'Question 20: Automating Repetitive Tasks',
        'description': 'Design AI automation workflows that eliminate your most time-wasting repetitive work',
        'difficulty': 'advanced',
        'order': 20,
        'points': 35,
        'instructions': '''If you do the same task more than twice a week, AI can probably automate it — or at least cut the time in half.

**What You'll Learn:**
- How to identify tasks worth automating
- The "When X happens → AI does Y → Then Z" automation logic
- How tools like Zapier, Make, and n8n connect AI to your existing apps

**The Automation Logic:**
Every automation follows this pattern:
- **Trigger:** When X happens (new email, form submission, calendar event, new file)
- **Action:** AI does Y (summarises, drafts a reply, categorises, extracts data)
- **Output:** Then sends Z (posts to Slack, adds to spreadsheet, sends email, creates task)

**Tools for AI Automation:**
- **Zapier:** Most beginner-friendly, huge number of app integrations
- **Make (Integromat):** More powerful, visual workflow builder, better for complex flows
- **n8n:** Open source, self-hosted option for sensitive data
- **Notion AI / Zapier + Claude:** Custom AI workflows with your own prompts

**High-Value Automations to Know:**
- New email → AI summarises and routes → Creates task in project tool
- New form submission → AI drafts personalised response → Sends for approval
- Weekly data export → AI analyses → Summary sent to team Slack
- Social media mention → AI assesses sentiment → Alert if negative

**Your Challenge:**
Design 3 automation workflows for a specific person's work situation.

Write detailed workflow designs for each automation including: trigger, AI step (with actual prompt), output, and tools involved. Then show the first message you'd type in Zapier or Make to start building it.''',
        'example_prompt': '''Design 3 AI automation workflows that would save the most time in this work situation, then show me how to build the first one.

**THE PERSON:**
I'm an estate agent (property sales). My daily repetitive tasks:
- Responding to similar enquiry emails (viewing requests, price queries, property availability)
- Updating our CRM after each viewing with notes and next steps
- Sending weekly property market update emails to a list of 200+ prospective buyers
- Creating property listing descriptions from spec sheets sent by developers
- Following up with leads who haven't responded in 7 days

I use: Gmail, Salesforce CRM, Mailchimp, WhatsApp Business, and Google Sheets.

---

**PART 1 — AUTOMATION AUDIT**

First, help me think about this systematically:
1. Which of my tasks are most worth automating? (High frequency + consistent format = best candidates)
2. Which tasks are too nuanced or relationship-sensitive to automate fully?
3. What's the difference between "automate fully" vs "AI-assisted first draft"?

---

**PART 2 — DESIGN 3 AUTOMATION WORKFLOWS**

For each workflow, give me:
- **Workflow Name**
- **The Problem It Solves** (time saved, quality improvement, risk reduction)
- **Trigger:** What event starts this workflow?
- **AI Step:** What does AI actually do? Include the exact prompt text I'd use.
- **Output:** What gets produced and where does it go?
- **Tools Needed:** Which apps connect to make this work?
- **Limitations:** What can't this automation do that I still need to handle manually?

Design workflows for these 3 scenarios:

**Workflow 1:** New viewing enquiry email comes in via Gmail

**Workflow 2:** I finish a property viewing and need to update Salesforce and plan next steps

**Workflow 3:** Every Monday morning, generate and send weekly market update to the buyer mailing list

---

**PART 3 — BUILD THE FIRST WORKFLOW**

Take Workflow 1 (new viewing enquiry email) and show me exactly how to build it in Zapier:

1. Step-by-step Zapier setup instructions
2. The exact AI prompt I'd use in the Zapier + Claude/ChatGPT step
3. The decision logic (how does the automation know what type of enquiry it is?)
4. What the drafted reply would look like for a specific example email
5. How I review and approve it before it sends (keeping the human in the loop)

Make this specific enough that I could actually follow these steps and build it.''',
    },
    {
        'title': 'Question 21: Building Your Prompt Library',
        'description': 'Create a personal collection of go-to prompt templates for your most common work tasks',
        'difficulty': 'intermediate',
        'order': 21,
        'points': 30,
        'instructions': '''The most productive AI users don't start from scratch every time. They have a personal library of proven prompts they reuse.

**What You'll Learn:**
- How to design reusable prompt templates
- How to organise a prompt library for maximum usefulness
- How to build templates that work across different situations

**What Makes a Great Prompt Template:**
1. **Clear placeholders** in [SQUARE BRACKETS] for variable information
2. **Consistent structure** that works every time you use it
3. **Built-in quality controls** — format, tone, length, output structure
4. **A brief usage note** explaining when to use this template
5. **Short enough to paste quickly** — complex is useful, clunky is not

**Categories Worth Building:**
- Email templates (cold outreach, follow-up, apology, proposal, announcement)
- Content creation (social media, blog posts, product descriptions)
- Analysis (competitive research, decision frameworks, feedback)
- Meetings (agenda creation, notes to actions, follow-up emails)
- Personal (cover letters, LinkedIn profiles, personal statements)

**Your Challenge:**
Build a personal prompt library of 5 templates tailored to YOUR professional context.

For each template:
1. Give it a clear name and use-case description
2. Write the full template with [PLACEHOLDERS]
3. Include usage notes (when to use it, what to fill in)
4. Demonstrate it with a real filled-in example

Then: organise your 5 templates into a structure you'd actually use — a Notion page, a Google Doc, or even a saved notes format.

**Make these genuinely yours.** Think about the 5 tasks you do most often with AI, and build the templates you'd actually reach for.''',
        'example_prompt': '''Build a personal prompt library of 5 professional templates I'll actually use. Then show me how to organise them for quick access.

**MY WORK CONTEXT:**
I'm a mid-level operations manager at a logistics company. I use AI mainly for: writing internal communications, preparing reports for senior management, running supplier meetings, responding to complaints, and onboarding new team members.

---

**BUILD THESE 5 TEMPLATES:**

---

**TEMPLATE 1: Executive Update Email**
I send weekly update emails to the Operations Director summarising the week's performance.

Design a template for this that:
- Has placeholders for: week number, key metrics, what went well, challenges, upcoming risks, and requests/decisions needed
- Produces a professional, concise email (under 200 words)
- Structures information in a way executives appreciate (headlines first, detail below)
- Has the right tone: direct, factual, solution-focused

---

**TEMPLATE 2: Supplier Issue Response**
When a supplier fails to deliver on time or quality, I need to respond professionally.

Design a template that works whether I'm:
- Issuing a formal warning
- Requesting an explanation
- Negotiating a recovery plan

Include: [SEVERITY LEVEL], [SPECIFIC ISSUE], [IMPACT ON OUR BUSINESS], [WHAT I NEED FROM THEM], [DEADLINE FOR RESPONSE]

---

**TEMPLATE 3: New Team Member Onboarding Plan**
I onboard someone new to the team roughly once every 2 months.

Create a template that, when filled in with: [ROLE], [START DATE], [MAIN RESPONSIBILITIES], [KEY PEOPLE TO MEET], generates a 4-week onboarding plan with:
- Week-by-week goals
- Key introductions and meetings to schedule
- Milestones and check-in points
- Resources to share in the first week

---

**TEMPLATE 4: Meeting Agenda Generator**
I run 3-4 internal meetings per week and always need a structured agenda.

Create a template using: [MEETING PURPOSE], [ATTENDEES], [DURATION], [KEY TOPICS], [DECISIONS NEEDED] that produces:
- Pre-read list (what to prepare)
- Timed agenda with facilitator notes
- Decision slots clearly marked
- Action item format for the end

---

**TEMPLATE 5: Process Improvement Proposal**
When I want to propose a change to how we do something, I write a 1-page proposal.

Create a template using: [CURRENT PROCESS], [PROBLEM WITH IT], [PROPOSED CHANGE], [EXPECTED BENEFITS], [RESOURCES/COST NEEDED] that produces a concise proposal senior management will actually read.

---

**ORGANISE MY LIBRARY:**

After building all 5 templates, design a simple structure for my "Prompt Library" — how should I organise these so I can find and use them quickly? Include:
- A naming convention
- A category structure
- Where I should save them (tool recommendation)
- How to add new templates as I build more

Make this practical, not complex.''',
    },
    {
        'title': 'Question 22: AI Ethics, Hallucinations & Limitations',
        'description': 'Develop a personal fact-checking workflow and understand when not to trust AI',
        'difficulty': 'advanced',
        'order': 22,
        'points': 35,
        'instructions': '''AI can be confidently, convincingly wrong. Understanding this — and building habits to manage it — is essential for any professional AI user.

**What You'll Learn:**
- What AI hallucinations are and why they happen
- How to spot likely hallucinations before they cause problems
- A personal fact-checking workflow for professional AI use

**What is an AI Hallucination?**
When AI generates information that sounds completely plausible but is factually wrong — often with high confidence, no hesitation, and convincing detail. It's not lying; it's pattern-matching gone wrong.

**Common Hallucination Patterns:**
- **Invented statistics** ("Studies show that 67% of...") — numbers are often made up
- **Fake references** (books, papers, and websites that don't exist)
- **Outdated information** presented as current
- **Wrong names and dates** for real events
- **Confident answers to questions AI shouldn't be able to answer** (specific prices, current availability, local information)

**When AI is Most Likely to Hallucinate:**
- Specific statistics, figures, and percentages
- Recent events (past 6-12 months)
- Niche topics with limited training data
- Specific quotes attributed to real people
- Legal, medical, and financial specifics

**Your Challenge:**
Deliberately find AI hallucinations, then build a personal fact-checking workflow.

1. Ask AI 3 questions designed to trigger hallucinations (questions about specific facts, statistics, or references)
2. Identify what in the responses to check and why
3. Design a personal fact-checking protocol for professional AI use
4. Write a brief "AI Trust Guide" for your specific work context''',
        'example_prompt': '''I want to understand AI hallucinations by actively finding them, then build a proper fact-checking system for my work.

---

**PART 1 — HALLUCINATION HUNTING: Answer these 3 questions**

(I'll verify the answers independently — the goal is to see where you might be wrong)

**Question A:** What are the latest statistics on employee burnout rates in the UK in 2024? Include specific percentages and cite the studies.

**Question B:** Can you name 3 specific books published between 2022-2024 about AI in the workplace, with author names, publishers, and a brief description of each?

**Question C:** What was the exact UK National Living Wage rate on 1 April 2023, and what legislation governs it?

---

**PART 2 — HONEST SELF-ASSESSMENT**

After answering the 3 questions above, be honest with me:
1. For each answer, rate your confidence: High / Medium / Low
2. Where are you most likely to have generated incorrect information?
3. What specifically should I verify in each answer before using it professionally?
4. Which of the 3 types of questions are most dangerous to use AI for without fact-checking?

---

**PART 3 — MY FACT-CHECKING PROTOCOL**

Design a practical fact-checking protocol for my work context (I'm a communications manager who uses AI daily for: drafting press releases, writing reports with statistics, creating training materials, and drafting policy summaries).

The protocol should answer:
1. **What to ALWAYS verify** — categories of information I should never use from AI without checking
2. **What to spot-check** — information that's usually fine but worth a quick verify
3. **What to trust** — tasks where AI accuracy is generally reliable for my work
4. **My verification workflow** — step-by-step, what do I actually do to check something?
5. **Speed vs safety** — when is thorough fact-checking worth it, and when is a quick check enough?

---

**PART 4 — AI TRUST GUIDE**

Write a short "AI Trust Guide" (one page, bullet points) that I could share with my communications team — helping them understand what AI is reliable for, what needs checking, and our team's rules around AI use for professional communications.

Include: approved uses, required verification steps, red flag topics, and how to cite AI use if needed.''',
    },
    {
        'title': 'Question 23: Data Privacy & AI at Work',
        'description': 'Understand what you should and shouldn\'t share with AI — and write a workplace AI policy',
        'difficulty': 'advanced',
        'order': 23,
        'points': 35,
        'instructions': '''Using AI at work without thinking about data privacy is a serious risk — for you, your employer, and your clients.

**What You'll Learn:**
- What data should never go into AI tools
- How to understand what different AI tools do with your data
- How to write a practical AI usage policy for a team

**The Core Risk:**
When you paste information into an AI tool:
- Free tools may use your input to train future models
- Enterprise tools have data processing agreements — but vary
- Sensitive information entered now could surface in unexpected ways later

**What Should Never Go Into Free AI Tools:**
- Personal data of real customers or employees (GDPR applies)
- Confidential business strategies, financials, or IP
- Passwords, access credentials, or security information
- Client information covered by NDAs or contracts
- Anything your employer would consider proprietary

**What's Generally Fine:**
- Fictional or anonymised scenarios
- Your own personal writing or ideas
- General business questions with no sensitive specifics
- Public information you're reorganising

**The GDPR Angle:**
Under UK GDPR, inputting personal data about real people into AI tools without proper data processing agreements is likely a data protection breach. Many organisations are now creating specific AI policies.

**Your Challenge:**
Write a practical AI usage policy for a fictional company.

**The company:** A 50-person HR consultancy that uses AI tools across all teams — writing, research, client work, and administration.

Your policy should be practical, not just legal boilerplate — something employees would actually read and follow.''',
        'example_prompt': '''Write a practical AI Usage Policy for a fictional HR consultancy. This should be something employees actually read and understand — not legal jargon no one follows.

---

**THE COMPANY:**
"Meridian People" — a 50-person HR consultancy based in Birmingham. Services: HR strategy, recruitment support, training and development, employee relations, and compliance advice.

**Data profile:**
- Handles employee data for 30+ client companies
- Processes sensitive personal data: CVs, performance reviews, disciplinary records, salary information, health-related adjustments
- Subject to UK GDPR, Employment Law confidentiality, and client NDAs
- Teams use AI tools daily (currently ungoverned — different people use different tools)

**The Problem:**
The MD has heard from a client that their employee's CV was identifiable in an AI-generated output. They need a proper policy — quickly.

---

**WRITE THE POLICY:**

**Section 1 — Purpose (max 100 words)**
Why this policy exists, who it applies to, and what it covers. Write for a non-lawyer audience.

**Section 2 — Approved AI Tools**
Create a tiered table:
| Tool | Approved Use Cases | NOT Approved For | Notes |
Include: Claude/ChatGPT (free tier), Claude/ChatGPT (enterprise/paid), Microsoft Copilot (M365), Google Gemini (Workspace), Image AI tools, General web AI tools

**Section 3 — What You Must NEVER Input into AI**
A clear, specific list — not vague categories. Think like an employee reading this at their desk.

**Section 4 — What's Generally Safe to Use AI For**
Equally specific — help employees understand where AI genuinely helps without risk.

**Section 5 — The Anonymisation Rule**
Explain clearly: if you need to use real client situations as examples, how do you anonymise them properly? Give 3 before/after examples showing the right approach.

**Section 6 — If Something Goes Wrong**
What to do if an employee realises they've shared something they shouldn't have:
- Who to tell
- Within what timeframe
- What information to provide
- What happens next (non-punitive tone — encourage reporting)

**Section 7 — Getting Started Checklist**
A simple 5-item checklist employees complete before using AI on any client-related work.

---

**FORMATTING:**
- Plain English throughout
- Max 800 words total
- Use bullet points over paragraphs where possible
- Tone: Professional but human — like advice from a trusted colleague, not a legal document
- Include one memorable phrase that sums up the key principle (something people will actually remember)''',
    },
    {
        'title': 'Question 24: Module 2 Capstone — The AI-Powered Workday',
        'description': 'Simulate a complete professional workday using every AI skill from this module',
        'difficulty': 'advanced',
        'order': 24,
        'points': 50,
        'instructions': '''This is your Module 2 capstone — a full simulation of a professional workday using AI tools and features across every skill you've learned.

**What You'll Demonstrate:**
- Choosing the right AI tool for each task
- Managing a complex, multi-task workday efficiently
- Producing professional outputs across different formats
- Applying context management and quality control

**The Challenge:**
You'll simulate a full Tuesday at work for a specific professional persona. Across 5 work scenarios, you'll use AI for different types of tasks — and in each case, choose the right approach and produce a professional output.

**The Persona:**
You are a Marketing Manager at a mid-size UK software company. It's Tuesday morning. Your to-do list has 5 items to tackle with AI's help.

**For each task:**
1. Name the AI tool or approach you'd use (and why, not just what)
2. Write the actual prompt you'd use
3. Show what the output would look like
4. Note one thing you'd verify or refine before using it

**The 5 Tasks:**
1. Summarise and analyse a competitor's recent product announcement
2. Write a quarterly marketing report summary for the CEO
3. Create social media content for 3 platforms for a new feature launch
4. Respond to a negative press article about your industry
5. Plan next month's team priorities using data from this month's results

**This is your chance to demonstrate everything Module 2 has taught you.** Show strategic tool selection, professional output quality, and smart, efficient AI use.''',
        'example_prompt': '''I'm simulating a full AI-powered workday as a Marketing Manager at TechNova, a 200-person UK software company that sells project management software to SMEs. It's Tuesday morning. Here are my 5 tasks — I'll work through each one methodically.

---

**TASK 1 — COMPETITOR ANALYSIS**
*Scenario:* Our main competitor, ProjectFlow, just released a major product update announcement. I need to understand it quickly and brief my team.

**Tool choice and rationale:** [State which AI tool you'd use and why]

**My prompt:**
"Analyse this competitor product announcement and produce a structured competitive intelligence brief:

[Competitor announcement text:]
'ProjectFlow today launched ProjectFlow 3.0, featuring AI-powered task automation, real-time team sentiment tracking, and a new pricing model starting at £8/user/month (previously £14/user/month). The update targets SMEs under 50 employees. CEO Dana Park said: "We're making enterprise-grade AI accessible to every small team." Available from March 1st.'

I need:
1. What's actually new here (vs marketing spin)?
2. The most significant threat to our position — be specific
3. Our likely competitive vulnerabilities based on this
4. 3 immediate talking points for our sales team when clients ask about this
5. One strategic response option to consider"

**Expected output quality:** Professional enough to share with the Sales Director in a 2pm call.
**What I'd verify:** Any specific price comparisons or feature claims against their actual website.

---

**TASK 2 — QUARTERLY CEO REPORT**
*Scenario:* I need to write the marketing section of the CEO's quarterly board report. I have raw data, but need a compelling written summary.

**Tool choice and rationale:** [State which AI tool you'd use and why]

**My prompt:**
Write a 300-word executive marketing summary for the Q4 board report based on this data:

Raw Q4 numbers:
- Website traffic: 48,200 visits (+23% vs Q3)
- Qualified leads generated: 312 (+18% vs Q3)
- Cost per lead: £67 (Q3: £81) — significant improvement
- Email open rate: 31% (industry benchmark: 24%)
- 2 major pieces of press coverage (TechCrunch UK feature, SME Today profile)
- Launched new case study programme — 4 case studies published
- LinkedIn followers: 12,400 (grew 800 this quarter)
- Campaign that underperformed: Paid search — 60% of budget, 22% of leads

Structure the summary as:
- Headline Result (1 sentence)
- Key Wins (3 bullets with context)
- One Honest Challenge (what didn't work and what we're doing about it)
- Q1 Focus (what this means for next quarter)

Tone: Confident, honest, data-led. The CEO values directness — no padding.

**What I'd verify:** The actual accuracy of every number before it goes in the report.

---

**TASK 3 — SOCIAL MEDIA CONTENT**
*Scenario:* We're launching a new AI scheduling feature. I need content for LinkedIn, Twitter/X, and Instagram.

**Tool choice and rationale:** [State which AI tool you'd use and why]

**My prompt:**
Create launch content for our new "AutoSchedule AI" feature across 3 platforms.

Feature details: AutoSchedule AI looks at your team's workload and automatically suggests the best task schedule for the week. It learns from how your team works and gets smarter over time. Saves managers an average of 3 hours/week in planning time.

Target audience: Operations managers and team leads in companies of 10-50 people.

**LinkedIn Post:**
- Professional but conversational
- Leads with the problem, not the product
- 3 hours/week stat must be included
- Ends with a question driving comments
- 150-200 words + 3 relevant hashtags

**Twitter/X Thread:**
- Hook tweet (max 280 chars, stops the scroll)
- 3 supporting tweets explaining the feature benefit
- CTA tweet (link to learn more)
- Each tweet: self-contained but flows as a thread

**Instagram Caption:**
- Shorter and punchier than LinkedIn
- Visual description note: what image would pair with this?
- Max 100 words + 5 hashtags

**What I'd verify:** That the "3 hours/week" stat is approved by the product team for public use.

---

**TASK 4 — NEGATIVE PRESS RESPONSE**
*Scenario:* A journalist published an opinion piece saying "AI project management tools are making remote workers feel surveilled." Our product is name-dropped in the article.

**Tool choice and rationale:** [State which AI tool you'd use and why]

**My prompt:**
Help me respond to this situation. We need a response that:
1. Doesn't ignore a legitimate concern (AI surveillance is a real issue people worry about)
2. Differentiates our product (TechNova helps teams plan better — it doesn't monitor individuals)
3. Doesn't sound defensive or corporate

Please produce:
A) A short public statement (150 words max) we could post on our company blog
B) A proposed response to the journalist via email (we have their contact)
C) 3 internal talking points for our sales team who will get questions from prospects about this

Our values: We've always been anti-surveillance. Our product has no individual time-tracking or monitoring features.

**What I'd verify:** Run A and B past our legal team before any public posting.

---

**TASK 5 — TEAM PRIORITIES PLANNING**
*Scenario:* I need to plan next month's team priorities based on this month's results and a set of business goals.

**Tool choice and rationale:** [State which AI tool you'd use and why]

**My prompt:**
Based on this month's marketing performance and our Q1 business goals, help me build a prioritised plan for next month.

This month's context:
- Paid search underperforming (high spend, low lead quality)
- Case study programme working well — 4 published, clients love them
- Email marketing outperforming benchmarks
- Board wants 20% lead growth by end of Q1
- Team capacity: 4 people at 80% capacity (one team member on parental leave)

Create a prioritised action plan for next month:
1. Top 3 priorities with clear rationale (linked to the lead growth goal)
2. What to stop or reduce (based on what's not working)
3. Resource allocation recommendation across the 4 team members
4. One thing to test this month with a small experiment
5. How I'd know at month-end if we succeeded

Format as a planning document I can share with my team on Monday.

**What I'd refine:** Discuss the resource allocation with each team member before finalising.

---

**FINAL REFLECTION:**
Looking across all 5 tasks:
- Where did having the right tool make the biggest difference?
- Where was AI assistance most valuable vs where was human judgment irreplaceable?
- What's the most important thing I've learned about using AI in a professional workday?''',
    },
]
