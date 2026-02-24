"""
Module 3 Part 3: Advanced Applications & Future Skills — "Where AI is Heading"
Challenges 17-22: Looking ahead and applying AI agents at the frontier (3-4 hours)
"""

MODULE3_PART3_CHALLENGES = [
    {
        'title': 'Question 17: AI Coding Assistants — An Overview',
        'description': 'Understand what AI coding tools can do — even if you\'ve never written code',
        'difficulty': 'intermediate',
        'order': 17,
        'points': 30,
        'instructions': '''AI has made coding more accessible than ever — and understanding coding assistants is valuable even if you never intend to code.

**What You'll Learn:**
- What GitHub Copilot, Cursor, and Claude Code do
- How AI coding assistants change the software development process
- How non-coders can direct AI coding assistants to build useful things

**The Major AI Coding Tools:**

**GitHub Copilot:**
- Autocompletes code as you type in your editor
- Suggests entire functions based on comments
- Integrated into VS Code, JetBrains, and other editors
- Best for developers already writing code

**Cursor:**
- AI-first code editor — the entire interface is built around AI
- Chat with your codebase: "what does this file do?"
- Make changes by describing what you want in English
- Good for both developers and people learning to code

**Claude Code / Claude in API:**
- Excellent at understanding and explaining existing code
- Strong at writing complex functions, debugging, and refactoring
- Best for step-by-step coding guidance with explanations

**What This Means for Non-Coders:**
- You can direct an AI to build small scripts and tools
- You can understand code without being able to write it
- You can be a "technical enough" manager or collaborator with dev teams
- You can build simple automations that previously required a developer

**Your Challenge:**
Explore what you could actually build with AI coding assistance — without writing any code yourself.

Watch AI write and explain real code, then direct it to build something useful for your work or life. The goal is confidence and understanding — not memorising syntax.''',
        'example_prompt': '''I want to understand what AI coding assistants can actually do — by exploring what I could build with their help, even with no coding experience.

**MY SITUATION:**
I work in sales operations and would benefit from simple tools to automate repetitive tasks. I've never written code, but I'm comfortable with computers, spreadsheets, and AI tools. I want to understand what's possible.

---

**PART 1 — WHAT AI CAN BUILD FOR ME**

Without me writing any code, what could an AI coding assistant realistically help me build?

Give me 10 specific examples of tools a sales ops person could build with AI assistance — ranging from "very simple" to "ambitious but achievable."

For each example:
- What the tool does
- What problem it solves
- How difficult it is (1-5 scale)
- What it would look like when done (a script? a web page? a spreadsheet add-on?)

---

**PART 2 — BUILD SOMETHING REAL**

Let's actually build something useful. I need a Python script that:
- Reads a CSV file of customer data (columns: Company Name, Contact Name, Email, Last Contact Date, Revenue, Stage)
- Identifies all customers who haven't been contacted in more than 30 days AND whose revenue is over £5,000
- Creates a prioritised follow-up list sorted by revenue (highest first)
- Outputs this as a new CSV file called "follow_up_priority.csv"
- Also prints a summary: how many customers need follow-up, total revenue at risk

**Do two things:**
1. Write the complete script
2. Explain EVERY line in plain English — as if you're teaching me, not just showing me the code

I should understand what each line does even if I couldn't write it myself.

---

**PART 3 — LEARNING TO DIRECT AI CODE**

Now that you've written the script, I want to modify it. I'll direct you in plain English and you'll write the code changes:

**Change 1:** "Also highlight customers who are marked as 'Proposal Sent' in the Stage column AND haven't been contacted in 14+ days — these are even more urgent."

**Change 2:** "Add a column to the output CSV called 'Urgency Score' that scores each customer from 1-10 based on days since contact and revenue size."

**Change 3:** "Add a 'today's date' header to the output CSV so I know when the list was generated."

For each change:
- Write the updated code
- Explain what changed and why
- Point out any potential issues or edge cases I should know about

---

**PART 4 — THE BIGGER PICTURE**

Based on what we just did together:

1. What can a non-coder realistically build with AI coding assistance in 2025?

2. What are the limits — what still requires a real developer?

3. How should a business person think about AI coding tools in their work? What's the right level of engagement?

4. If I wanted to go further and learn the basics of Python, what's the smartest path — given that AI is available to help me learn?

5. What's the one coding skill that would give a non-technical professional the highest return on investment?''',
    },
    {
        'title': 'Question 18: AI for Team Collaboration',
        'description': 'Design AI-assisted team workflows that improve how groups work together',
        'difficulty': 'intermediate',
        'order': 18,
        'points': 30,
        'instructions': '''AI isn't just a personal productivity tool — it can transform how entire teams collaborate, communicate, and work together.

**What You'll Learn:**
- How AI enhances shared workspaces and collaborative editing
- How to design team workflows that incorporate AI sensibly
- The management challenges of AI adoption in a team

**How AI Changes Team Collaboration:**

**Shared Documents:**
- AI that everyone can ask questions of your shared knowledge base
- Auto-summaries when you open a document you haven't read
- AI-assisted editing that tracks and explains changes

**Meetings:**
- AI notetakers that produce consistent summaries
- Automated action item distribution
- Pre-meeting briefings for all attendees

**Communication:**
- AI-assisted writing that maintains a consistent team voice
- Translation and accessibility tools
- Sentiment monitoring in team communications (for distributed teams)

**Project Management:**
- AI that predicts project risks based on progress patterns
- Automatic status updates generated from completed tasks
- Intelligent task prioritisation suggestions

**The Human Challenge:**
AI in teams creates real challenges:
- Who is responsible when AI makes a mistake?
- How do you maintain authentic relationships when AI assists communication?
- How do you onboard new team members into an AI-assisted culture?

**Your Challenge:**
Design a complete AI-assisted team workflow for a fictional project — showing how AI supports (not replaces) human collaboration at every stage.''',
        'example_prompt': '''Design a complete AI-assisted team workflow for a product launch project. Show how AI supports collaboration at every stage without replacing human judgment.

**THE PROJECT:**
A 6-person product team at a mid-size SaaS company is launching a new feature: an AI-powered reporting dashboard. Timeline: 8 weeks to launch. The team: 1 Product Manager, 2 Developers, 1 Designer, 1 Marketing Manager, 1 Customer Success Manager.

**THE CHALLENGE:**
The team is distributed — 3 in London, 2 remote in Manchester, 1 in Berlin. They use Slack, Notion, Figma, GitHub, and Google Meet. The project has a history of miscommunication and things "falling through the cracks."

---

**PART 1 — AI ACROSS THE PROJECT PHASES**

Design how AI assists the team in each of the 4 project phases:

**Phase 1: Kick-off and Planning (Week 1)**
- What AI tools and features are used?
- What specifically does AI do in the kick-off meeting?
- How does AI help create and maintain the project plan?
- What human decisions can't be delegated to AI?

**Phase 2: Design and Build (Weeks 2-6)**
- How does AI support the design review process?
- How does AI assist development (code review, documentation, testing)?
- How does AI help the team stay aligned across locations?
- What's the "daily AI check-in" for the project?

**Phase 3: Pre-Launch (Week 7)**
- How does AI assist with testing and quality assurance?
- How does AI help prepare launch communications?
- How does AI support risk assessment?

**Phase 4: Launch Week (Week 8)**
- Real-time AI monitoring and alerting
- AI-assisted customer response during launch
- Post-launch performance summary generation

---

**PART 2 — THE SHARED AI WORKSPACE**

Design the team's Notion or Confluence workspace with AI built in.

For the main project hub, show:
- Page structure (what pages exist)
- Where AI summaries auto-generate
- Where AI can be queried ("ask the project" feature)
- How meeting notes automatically flow into action items
- How decisions are recorded and made searchable

---

**PART 3 — THE DAILY AI STANDUP**

Design an AI-powered async standup system that replaces the 15-minute daily team call.

Show:
- The 3 questions each team member answers (in Slack/Notion)
- How AI consolidates the answers into a summary
- How AI identifies blockers and flags them to the PM
- How AI surfaces patterns ("Tom has flagged the same blocker 3 days in a row")
- What the AI-generated daily brief looks like

---

**PART 4 — THE WEEKLY STATUS REPORT**

Design the automatic weekly status report that AI generates from project activity.

Write the AI prompt that produces this report from:
- Task completion data
- Meeting summaries
- Blockers logged
- Code commits and PR activity
- Risk register

Show what the generated report looks like for Week 3 of the project (invent realistic project status data).

---

**PART 5 — THE HUMAN GUARDRAILS**

Where should the team explicitly NOT use AI, and why?

Design the team's "AI Use Charter" — a simple document that answers:
- What AI is approved for in this project
- What decisions must be made by humans
- How to handle disagreements that arise from AI suggestions
- Who is accountable when AI assists a decision that goes wrong
- How new team members learn the team's AI norms

---

**PART 6 — MANAGEMENT PERSPECTIVE**

You're the PM. After this 8-week project, write a short retrospective reflection:
- What worked well about AI-assisted collaboration?
- What created friction or problems?
- What would you change in the next project?
- One recommendation for other teams adopting AI collaboration tools''',
    },
    {
        'title': 'Question 19: AI in Different Industries',
        'description': 'Research how AI agents are transforming your target industry and present your findings',
        'difficulty': 'intermediate',
        'order': 19,
        'points': 30,
        'instructions': '''AI is transforming every industry — but the way it's transforming healthcare looks nothing like how it's transforming retail. Understanding your specific industry's AI trajectory is a genuine career advantage.

**What You'll Learn:**
- How AI is being applied across different industries
- What's hype vs what's genuinely transformative
- How to position yourself as AI changes your industry

**Industries Being Reshaped by AI:**

**Healthcare:** Diagnostic imaging AI, drug discovery, clinical documentation automation, patient communication
**Finance:** Fraud detection, credit risk assessment, algorithmic trading, customer service automation
**Education:** Personalised learning, automated grading, content generation, tutoring AI
**Legal:** Contract review, legal research, document drafting, compliance monitoring
**Retail:** Demand forecasting, personalised recommendations, inventory management, customer service
**Manufacturing:** Predictive maintenance, quality control, supply chain optimisation
**Marketing:** Content generation at scale, audience segmentation, campaign optimisation
**Recruitment:** CV screening, interview scheduling, candidate matching

**The Framework for Analysing AI in Any Industry:**
1. What repetitive tasks are being automated?
2. What decisions are being AI-assisted (not fully automated)?
3. What new roles are being created because of AI?
4. What existing roles are declining?
5. What human skills are becoming MORE valuable?

**Your Challenge:**
Pick the industry that interests you most (yours, a target industry, or one you're curious about) and present a thorough 5-minute briefing on how AI is changing it — including what it means for someone entering or working in that industry today.''',
        'example_prompt': '''Research and present a thorough briefing on how AI is transforming the recruitment and HR industry. I'm interested in this industry as a career path.

---

**THE BRIEFING FORMAT:**
I need a "5-minute briefing" — detailed enough to be genuinely informative, concise enough to be absorbed quickly. Imagine presenting this to a group of career-changers thinking about moving into HR and recruitment.

---

**SECTION 1 — THE LANDSCAPE (60 seconds)**

Set the scene:
- How big is the UK HR/recruitment industry?
- What were the main challenges BEFORE AI?
- What changed that made AI adoption accelerate recently?
- One statistic or insight that captures the scale of AI adoption in this industry

---

**SECTION 2 — WHAT'S ACTUALLY BEING AUTOMATED NOW (90 seconds)**

What AI is doing TODAY in recruitment and HR — not future predictions, real current applications:

For each application:
- What it does
- Which companies are using it (name real tools/vendors)
- How much of the task it handles vs what humans still do
- Any concerns or controversies around it

Cover at least:
- CV/resume screening
- Interview scheduling
- Candidate sourcing
- Employee onboarding
- Performance management
- Compliance and reporting

---

**SECTION 3 — THE JOBS PICTURE (60 seconds)**

Be honest about what's changing:
- What recruitment roles are declining or changing significantly?
- What new roles are being created by AI adoption?
- What skills are becoming MORE valuable as AI handles the routine work?
- What does a strong recruitment professional look like in 2027?

---

**SECTION 4 — THE ETHICAL CHALLENGES (30 seconds)**

What are the most significant concerns around AI in recruitment?
- Bias in AI screening tools (give a specific example)
- Data privacy and GDPR implications
- The candidate experience debate
- One regulation or legal development affecting AI hiring

---

**SECTION 5 — WHAT THIS MEANS FOR ME (60 seconds)**

Practical advice for someone considering a career in HR/recruitment in 2025:
- The skills to prioritise (be specific — not just "learn AI")
- The tools to learn to use
- The type of company to target (early AI adopters vs traditional)
- The career path that has the most growth potential given AI trends
- One thing most people get wrong about AI's impact on this industry

---

**CLOSING: Your Assessment**
If you were advising someone passionate about people and HR, would you tell them to go into recruitment now?
Be honest — what's exciting, what's uncertain, and what's the smart play?''',
    },
    {
        'title': 'Question 20: The Future of AI Agents',
        'description': 'Think critically about where AI agents are heading and what it means for your career',
        'difficulty': 'advanced',
        'order': 20,
        'points': 35,
        'instructions': '''AI agents are advancing fast. Understanding where they're heading — and what that means for how you work — is one of the most valuable things you can do for your career right now.

**What You'll Learn:**
- The key developments driving AI agent capability growth
- What "autonomous agents," "computer use," and "agentic AI" mean in practice
- How to position yourself for a future where AI agents do more

**Where AI Agents Are Heading:**

**Today (2025):**
- Agents follow instructions, use defined tools, mostly run single tasks
- Humans supervise most agent actions
- Best at well-defined, repetitive workflows

**Near Future (2026-2027):**
- Agents that can operate computers autonomously (browse web, use apps, manage files)
- Multi-agent coordination (networks of agents working together)
- Agents with long-term memory across projects
- More reliable reasoning on complex, ambiguous tasks

**Medium Term (2027-2030):**
- "Computer use" AI that acts as a digital employee
- Agents that manage other agents (hierarchical AI teams)
- Personalised AI that knows your entire professional history
- Agents that can execute weeks-long projects with minimal supervision

**The Career Reality:**
The jobs that survive and thrive are those where humans add value that agents can't:
- Novel judgment in unprecedented situations
- Deep client/stakeholder relationships
- Creative direction and taste
- Ethical oversight and accountability
- Cross-domain synthesis that requires life experience

**Your Challenge:**
Write a "Future of My Career" brief — a thoughtful analysis of how AI agents will change your specific target role over the next 3 years, and how you'll position yourself to thrive.''',
        'example_prompt': '''Write a "Future of My Career" analysis — a thoughtful, honest assessment of how AI agents will change my target role over the next 3 years and how I should position myself.

**MY SITUATION:**
I'm 27, working in digital marketing (social media and content). I've been in the field for 3 years. I want to grow into a senior marketing manager or head of marketing role within the next 4-5 years. I've been learning about AI throughout this programme.

---

**PART 1 — WHAT MY JOB LOOKS LIKE TODAY**

Before looking ahead, let's be honest about my current role:

Describe a typical week for a digital marketing specialist in 2025:
- The tasks that take most of my time
- Which of these are already partially automated or AI-assisted
- Which require genuine human creativity or judgment
- Where I currently add the most irreplaceable value

---

**PART 2 — THE 12-MONTH VIEW (2025-2026)**

What will AI agents change in my role in the next 12 months?

Be specific:
- Which current tasks will AI handle almost entirely?
- Which tasks will shift from "doing" to "directing and reviewing"?
- What new skills will I need to do my job well?
- What will my job description look like differently?

Include: concrete AI tools that will drive these changes, and one prediction that might surprise me.

---

**PART 3 — THE 3-YEAR VIEW (2025-2028)**

Project forward 3 years — what does a senior marketing role look like?

- What does "good at marketing" mean when AI handles most content creation?
- What human skills will command the highest salary premium?
- What's the career path that leads to strategic leadership rather than being displaced?
- What new types of marketing roles are emerging?

---

**PART 4 — THE RISKS TO BE HONEST ABOUT**

Don't just tell me what I want to hear:

- What's the honest risk to my specific career trajectory from AI agents?
- Are there parts of digital marketing that could be heavily commoditised?
- What would a career that relies too heavily on AI-replaceable skills look like by 2028?
- One uncomfortable truth about where AI is heading in my field

---

**PART 5 — MY ACTION PLAN**

Given this analysis, what should I do in the next 12 months to position myself well?

Give me:
- 3 skills to develop that will be MORE valuable as AI handles more (specific, not generic)
- 2 things to stop spending time on (that AI will do anyway)
- The type of experience to seek out (what does "great" look like on my CV in 3 years?)
- One unconventional move that most people in my field won't make but could pay off significantly

---

**PART 6 — THE GROWTH SCENARIO**

Paint the picture of the best-case scenario: what does my career look like at 30 if I make the right moves over the next 3 years?

What's the role, what's the title, what am I actually doing day to day — in a world where AI agents are handling most content creation?

Make this inspiring but honest.''',
    },
    {
        'title': 'Question 21: AI Safety & Responsible Automation',
        'description': 'Design safety checks, human oversight, and ethical guardrails for AI automation systems',
        'difficulty': 'advanced',
        'order': 21,
        'points': 35,
        'instructions': '''Powerful automation without proper safety thinking is genuinely risky. Responsible AI practitioners design systems that can fail gracefully.

**What You'll Learn:**
- The key failure modes in AI automation systems
- How to design human oversight that's meaningful (not just performative)
- The ethical considerations that should shape every automation you build

**Why AI Safety Matters in Automation:**

**The risks in agentic AI systems:**
- **Cascade failures:** One wrong AI decision triggers a chain of wrong actions
- **Scope creep:** Agent does more than intended — deletes files, sends emails, spends money
- **Prompt injection:** Malicious content in the data manipulates the agent's behaviour
- **Confirmation bias:** Agent optimises for what it thinks you want, not what you actually need
- **No off switch:** Automation running when it should have stopped

**What Can Go Wrong in Real Scenarios:**
- Email automation sends 1,000 emails with a factual error
- Content pipeline publishes AI-generated misinformation
- Customer service bot promises something the business can't deliver
- Data automation overwrites important files without backup
- AI agent spends beyond its authorised budget

**The SAFE Framework for Responsible Automation:**
- **S — Scope:** Define exactly what the system can and can't do
- **A — Accountability:** Make it clear who owns every automated decision
- **F — Failsafes:** What happens when something goes wrong?
- **E — Escalation:** When and how does a human take over?

**Your Challenge:**
Design a complete AI safety framework for a real automation system.

**The system:** A sales outreach automation that identifies prospects, personalises emails, sends sequences, and updates the CRM — running largely autonomously.''',
        'example_prompt': '''Design a complete AI safety and responsible automation framework for an outbound sales outreach system. This needs to be genuinely safe, not just checkbox compliance.

**THE AUTOMATION SYSTEM:**
A B2B software company wants to build an AI sales outreach system that:
- Identifies potential prospects from LinkedIn and company databases
- Researches each prospect and personalises outreach messages
- Sends initial outreach emails (Day 1)
- Sends follow-up emails (Day 4, Day 8)
- Updates CRM with all activity
- Flags positive responses for human sales team follow-up
- Runs autonomously on a defined prospecting list of 500 companies/month

**THE RISKS:**
The company knows this is powerful but potentially risky. They've had bad experiences with email automation before — spam complaints, incorrect personalisation ("Hi [First Name]"), embarrassing factual errors about the prospect's company.

---

**PART 1 — FAILURE MODE ANALYSIS**

Before designing safeguards, map every way this system could go wrong.

For each failure mode:
- What triggers it?
- What's the worst-case outcome?
- How likely is it? (High / Medium / Low probability)
- How severe is it? (Annoying / Damaging / Catastrophic)

Cover at least:
- Personalisation errors (wrong details, offensive mistakes)
- Volume errors (sending to wrong people, too frequently)
- Content errors (hallucinated "facts" about the prospect)
- Tone/compliance errors (regulatory issues, inappropriate content)
- Data errors (wrong CRM updates, duplicate outreach)
- Security errors (prospect data exposure, prompt injection)

---

**PART 2 — THE SCOPE DEFINITION**

Write the formal "Scope Document" for this automation. This document:
- Defines exactly what the system IS authorised to do
- Defines exactly what it is NOT authorised to do
- Sets hard limits (max emails per day, no sending between 8pm-8am, etc.)
- Defines the "blast radius" — what's the maximum damage if everything goes wrong?

Make this specific enough that an engineer could implement it as hard constraints.

---

**PART 3 — THE HUMAN OVERSIGHT ARCHITECTURE**

Design the human oversight system — making it meaningful, not bureaucratic.

Answer:
- What does a human review before anything gets sent? (The minimum effective review)
- What is reviewed by exception only (too much to check everything)?
- Who is accountable for automated decisions in this system?
- How do you prevent the oversight from becoming a rubber-stamp?
- What's the "emergency stop" procedure?

---

**PART 4 — THE QUALITY GATE PROMPTS**

Write the AI evaluation prompts that check each email BEFORE it's sent:

**Quality Gate 1 — Accuracy Check:**
A prompt that reviews the personalisation elements and flags anything that looks wrong, uncertain, or potentially offensive.

**Quality Gate 2 — Compliance Check:**
A prompt that reviews the email for spam law compliance (GDPR, CAN-SPAM), excessive claims, and anything that could create legal risk.

**Quality Gate 3 — Tone Check:**
A prompt that evaluates whether the email is appropriate for a cold professional outreach — flagging anything too casual, too pushy, or too generic.

---

**PART 5 — THE INCIDENT RESPONSE PLAN**

Design what happens when something goes wrong:

**Scenario A:** You realise the system sent 200 emails with incorrect company names in the personalisation (called "Apex Ltd" instead of "Alpine Ltd").
- What do you do in the first 30 minutes?
- What do you communicate to affected prospects?
- How do you prevent this recurring?

**Scenario B:** A prospect replies angrily, saying they're marking you as spam and considering legal action because of persistent AI-generated emails.
- Immediate response procedure
- Escalation path
- What changes to the system?

---

**PART 6 — THE ETHICS CHECKLIST**

Write a pre-launch ethics checklist for this automation. This is the document the business signs off before going live.

Cover:
- Consent and data ethics
- Transparency (should recipients know they're in an AI outreach sequence?)
- Impact on the prospects being targeted
- The team's genuine accountability for automated decisions
- Your honest assessment: is this system ethical? What conditions make it acceptable vs unacceptable?''',
    },
    {
        'title': 'Question 22: Module 3 Capstone — Your AI Agent System',
        'description': 'Design and present a complete AI agent and automation system for a real-world scenario',
        'difficulty': 'advanced',
        'order': 22,
        'points': 50,
        'instructions': '''This is your Module 3 capstone. Design a complete AI agent and automation system for a real-world scenario — demonstrating everything you've learned.

**What You'll Demonstrate:**
- Agent design and persona specification
- Multi-step workflow design with AI at multiple stages
- Tool selection and integration thinking
- Human oversight and safety design
- Strategic thinking about where AI adds genuine value

**The Capstone Challenge:**
Design a complete AI agent system that solves a significant, real-world problem for a specific organisation. Your system must be:
- Detailed enough that a technical team could start building it
- Safety-conscious with human checkpoints built in
- Practically achievable (not science fiction)
- Clearly valuable — you can articulate the ROI

**Minimum Requirements:**
- At least 3 distinct AI agent roles (with persona specifications)
- At least 4 automation workflows
- At least 2 integration points with existing tools
- A clear human oversight architecture
- Success metrics and implementation roadmap

**The Scenario:**
Choose a real organisation type (a school, a charity, a small business, a healthcare practice, a law firm, an estate agency) and design a system that would genuinely transform how they operate.

This is your showcase — make it thorough, thoughtful, and impressive.''',
        'example_prompt': '''Design a complete AI agent and automation system for a GP (General Practice) medical surgery. This is my Module 3 capstone.

**THE ORGANISATION:**
"Millfield Surgery" — a busy GP practice with 4 GPs, 2 nurses, 2 receptionists, and a practice manager. 5,500 registered patients. The surgery struggles with: high call volumes for appointments, administrative overload, repeat prescription management, and patient communication.

**IMPORTANT CONSTRAINT:**
This is healthcare — patient safety and clinical judgment stay with humans. The AI system must support and reduce administrative burden, NEVER make clinical decisions.

---

**SECTION 1 — SYSTEM OVERVIEW**

Write a compelling one-page executive summary of the AI agent system:
- The problem it solves
- The 3 main components
- The expected impact (time saved, patient experience improvement, cost reduction)
- The implementation approach (phased, starting small)
- The safety philosophy

---

**SECTION 2 — THE THREE AI AGENTS**

Define 3 distinct AI agents, each with a full persona specification:

**Agent 1: "Grace" — Patient Communication Agent**
- Role and purpose (what does Grace do?)
- Full system prompt (what are her instructions, personality, rules?)
- What she can do and what she CANNOT do
- How she interacts with patients (by phone? text? email? web chat?)
- Handoff rules (when does she immediately transfer to a human?)

**Agent 2: "Admin" — Administrative Automation Agent**
- Role and purpose
- System prompt
- Specific tasks it handles (be precise about which admin tasks)
- Integration points with the surgery's existing systems (booking system, patient records)
- Human oversight requirement

**Agent 3: "Rex" — Repeat Prescription Processing Agent**
- Role and purpose
- System prompt
- The exact workflow for processing a repeat prescription request
- Safety gates (what triggers a pharmacist/GP review instead of automatic processing?)
- Audit trail requirements

---

**SECTION 3 — FOUR AUTOMATION WORKFLOWS**

Design 4 complete workflows:

**Workflow 1: Appointment Booking**
Full flow from "patient calls/contacts" to "appointment booked" — using Grace as the patient-facing agent.

**Workflow 2: Repeat Prescription Processing**
Full flow from "patient requests repeat prescription" to "prescription ready" — with the appropriate safety gates.

**Workflow 3: Post-Appointment Follow-Up**
Automated check-in 48 hours after appointments for non-urgent cases — and routing based on patient response.

**Workflow 4: Daily Admin Digest**
Automated morning briefing for the practice manager — consolidating overnight messages, today's appointments, outstanding tasks, and flags needing attention.

---

**SECTION 4 — PATIENT SAFETY ARCHITECTURE**

This is healthcare — design the safety architecture:

- Every point where AI stops and waits for human review
- The "never AI" list (what absolutely cannot be automated)
- How the system handles a patient expressing distress or urgency
- Audit trail and documentation requirements
- What happens if the system fails (backup procedures)
- Compliance with NHS data standards and GDPR

---

**SECTION 5 — IMPLEMENTATION ROADMAP**

Design a 6-month phased implementation:

**Phase 1 (Month 1-2): Foundation**
What gets built and deployed first? (Start with lowest risk, highest impact)

**Phase 2 (Month 3-4): Core Automations**
What goes live in this phase?

**Phase 3 (Month 5-6): Full System**
Final components and integration

For each phase: what's being launched, how it's tested, what success looks like, and what the rollback plan is if something goes wrong.

---

**SECTION 6 — SUCCESS METRICS**

After 6 months of full operation, how will Millfield Surgery know this system is working?

Define:
- 5 measurable outcomes and how to track them
- The patient satisfaction metrics to monitor
- The staff experience metrics (did this actually reduce burden?)
- Any red flags that would trigger a system review
- The annual review process for the AI system

---

**SECTION 7 — WHAT MAKES THIS DIFFERENT**

Finish with a reflection:
- What's genuinely innovative about this approach?
- What's the hardest part to get right?
- If you were implementing this tomorrow, what would you do first and why?
- What would you NOT automate, and what does that tell us about where human healthcare professionals are irreplaceable?''',
    },
]
