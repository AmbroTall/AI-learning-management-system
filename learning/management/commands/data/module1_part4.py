"""
Module 1 Part 4: Mastery — "Putting It All Together"
Challenges 25-30: Capstone-level challenges combining multiple techniques (3-4 hours)
"""

MODULE1_PART4_CHALLENGES = [
    {
        'title': 'Question 25: Build a Business Plan',
        'description': 'Use AI to create a comprehensive mini business plan for a side hustle',
        'difficulty': 'advanced',
        'order': 25,
        'points': 40,
        'instructions': '''Time to combine everything you've learned into a real, complex project.

**What You'll Learn:**
- How to use AI for complex, multi-section document creation
- Applying context, structure, constraints, and iteration all at once
- Getting AI to produce professional-quality business documents

**The Challenge:**
Get AI to help you create a **mini business plan** for a side hustle or small business idea. This isn't a full 50-page plan — it's a practical, actionable plan you could actually use.

**Your prompt must combine these skills you've learned:**
- **Context** (Lesson 3): Full background on you and your idea
- **Structure** (Lesson 4): Clear sections with specific requirements
- **Constraints** (Lesson 13): Realistic constraints (budget, time, market)
- **Format** (Lesson 6): Professional, scannable output

**Business plan sections to request:**
1. Executive summary (what's the business?)
2. Problem & solution (what need does it fill?)
3. Target customer (who specifically?)
4. How it works (the business model)
5. Startup costs and ongoing expenses
6. Revenue projections (realistic, first 6 months)
7. Marketing strategy (how will people find you?)
8. Risks and challenges (honest assessment)
9. 90-day launch plan (specific action steps)

**Pick a real idea you're excited about** — or use one of these:
- Handmade products (candles, jewellery, art)
- Social media management for local businesses
- Personal fitness coaching
- Custom gift basket or hamper service
- Freelance photography or videography
- Event catering or baking for events

**Make it real and specific.** Generic plans are useless. The more details you give AI about YOUR situation, the more useful the plan.''',
        'example_prompt': '''I want to start a side business and need a practical mini business plan. Help me think through this properly.

**MY IDEA:** Social media management for local small businesses

**ABOUT ME:**
- I'm a 24-year-old working full-time in customer service at a retail company
- I run my own personal Instagram account (4,500 followers) and have always enjoyed creating content
- I've helped a friend promote their local café on social media informally — their following grew from 200 to 1,800 in 3 months
- Available: 10-12 hours per week (evenings and weekends)
- Budget to start: £150
- I have: Laptop, smartphone with a good camera, Canva (free plan), basic knowledge of Instagram and Facebook
- I've never run a business before

**CREATE A MINI BUSINESS PLAN WITH THESE SECTIONS:**

**1. Executive Summary (5 sentences max)**
- What's the business?
- Who's it for?
- Why will it succeed?

**2. The Problem I'm Solving**
- Why do local small businesses struggle with social media?
- What's wrong with existing options? (agencies too expensive? generic content? no local knowledge?)
- Why would a local business choose me over a big agency?

**3. Target Customer (Be Specific)**
- Exactly which types of businesses am I targeting? (restaurants? hair salons? independent shops?)
- What's their pain point?
- Where do I find them?
- What would they pay per month?

**4. Service Details**
- What exactly am I offering? (number of posts per week? content creation? community management?)
- What's included in the service vs. what's an add-on?
- What makes my service different from hiring a big agency?

**5. Pricing Strategy**
- What should I charge per month? (research the market for freelance social media managers)
- Starter packages vs. ongoing monthly retainers?
- Any introductory offers to land the first clients?

**6. Startup Costs**
- Everything I need to spend to get started (be specific, include amounts)
- Monthly running costs
- Keep total startup costs under my £150 budget

**7. Revenue Projections (First 6 Months)**
- Month 1: How many clients, how much revenue (be realistic — this is a side hustle!)
- Month 3: Growth target
- Month 6: Where I want to be
- Show the maths (clients x monthly rate)

**8. Marketing Plan (How to Get My First 3 Clients)**
- 5 specific actions I can take in the first month to find clients
- Free strategies AND any paid options worth trying
- How to approach a local business owner without feeling awkward about it

**9. Risks & Honest Challenges**
- Top 5 things that could go wrong
- For each risk, what's my backup plan?
- Biggest challenge I'll face running this alongside a full-time job

**10. 90-Day Launch Plan**
- Week 1-2: Setup (exactly what to do)
- Week 3-4: First outreach and marketing push
- Month 2: First clients and refining the service
- Month 3: Growth and building a portfolio

**REQUIREMENTS:**
- Be realistic, not optimistic. I'd rather know the truth.
- Include specific numbers (not just "charge a competitive rate" — tell me what that means in pounds)
- Make it actionable — I should be able to start executing next week
- Total length: Scannable. Use bullet points, tables, and bold headers.
- At the end, give me a GO/NO-GO assessment: is this idea worth pursuing given my situation?''',
    },
    {
        'title': 'Question 26: The Technical Communication Toolkit',
        'description': 'Communicate a technical project consistently across five different professional formats',
        'difficulty': 'advanced',
        'order': 26,
        'points': 40,
        'instructions': '''In IT and tech, the ability to communicate the same solution clearly to completely different audiences is a critical professional skill. This challenge puts that to the test.

**What You'll Learn:**
- How to use AI to create consistent messaging across multiple formats
- Adapting the same core technical content for completely different readers
- Building a professional communication package for a real project

**The Challenge:**
You have a technical project, solution, or IT system. Create a **complete communication package** — the same core information presented in 5 completely different formats for 5 different audiences.

**You'll create ALL of these in a single, well-structured prompt:**
1. **Technical overview** (for your development team or technical colleagues)
2. **Executive briefing** (for management who need to make a decision)
3. **Client-facing proposal section** (for a potential client or end user)
4. **Training module introduction** (for learners who need to understand and use it)
5. **Professional social media post** (for a company or organisation page)

**The key constraint: CONSISTENCY.** All 5 must clearly be about the same project with the same core message — just adapted for the format and reader.

**Your prompt must include:**
- Your project or solution details (what it is, what problem it solves, how it works)
- What makes it effective or valuable
- Your target reader for each piece and what they care about
- Specific format constraints for each piece

**Use a real IT project you've worked on, or a realistic fictional one.** These are the types of communications you'll produce in professional settings.''',
        'example_prompt': '''Create a complete communication package for my IT project. All 5 pieces should clearly be about the same solution, adapted for each specific audience.

**ABOUT THE PROJECT:**
- What it is: A web-based IT helpdesk ticketing system I built for a small business (50 employees)
- The problem it solves: Staff were reporting IT issues by walking over, calling, or emailing the IT person directly — there was no tracking, no prioritisation, and issues were constantly getting lost
- How it works: Staff submit tickets through a simple web form, IT staff see a prioritised dashboard with status updates, automated emails keep users informed, and monthly reports show resolution times
- Built with: Python (Django), SQLite database, deployed on a local server
- Results: Average response time improved from "whenever IT gets to it" to 2.3 hours for standard issues; no reported lost tickets since launch

**CREATE THESE 5 PIECES:**

**1. Technical Overview (for IT colleagues or a development team)**
- Length: 200-250 words
- Audience: People who understand technical terminology
- Focus: Architecture, tech stack, how it works under the hood
- Include: Database structure overview, key technical features, deployment approach
- Tone: Precise, technically accurate, professional peer-to-peer

**2. Executive Briefing (for a non-technical manager or director)**
- Length: 120-150 words
- Audience: Decision-maker who doesn't want technical details
- Focus: The problem, the solution, and the measurable business impact
- Must include: A clear before/after comparison and what it means for the business
- Tone: Clear, business-focused, no jargon

**3. Client-Facing Proposal Section (for a potential client considering this solution)**
- Length: 150-200 words
- Audience: A business owner or IT manager at a similar-sized company
- Focus: Benefits, reliability, and ease of adoption
- Must include: A specific outcome they can expect
- Tone: Professional, benefit-focused, confidence-building

**4. Training Module Introduction (for employees who will use the system)**
- Length: 100-130 words
- Audience: Non-technical office workers
- Focus: What they need to do, why it's easy, and how it helps them get IT issues resolved faster
- Must include: Simple steps for what to do when they have an IT problem
- Tone: Friendly, reassuring, clear

**5. Professional Social Media Post (for a company or organisation page)**
- Length: 120-150 words
- Audience: Professional network — other IT professionals and businesses
- Focus: The problem solved and the approach taken
- Must include: Something that sparks interest or useful discussion
- Tone: Confident, professional, slightly conversational

**CRITICAL:** All 5 must feel like they're about the same project. The core message — "we replaced IT chaos with a clean, trackable, faster system" — must come through in each piece, just framed for that specific reader. Read them side by side: is the project identity consistent? Does the value come through in every version?

After all 5, write a brief note (2-3 sentences) explaining how you adjusted the technical detail and focus for each audience.''',
    },
    {
        'title': 'Question 27: Event Planning Pro',
        'description': 'Plan a complete event or workshop with AI handling all the complex coordination',
        'difficulty': 'intermediate',
        'order': 27,
        'points': 35,
        'instructions': '''Event planning is multi-step, multi-stakeholder, and full of things that can go wrong. Perfect for AI.

**What You'll Learn:**
- Using AI for complex project planning with many moving parts
- Thinking about dependencies (what has to happen before what?)
- Building contingency plans

**Your Challenge:**
Plan a complete event from start to finish. This could be:
- A team workshop or training day
- A networking event or meetup
- A product launch event
- A charity fundraiser
- A conference talk or presentation
- A company away day

**Your prompt must include:**
1. Event details (type, size, purpose, date, budget)
2. Audience (who's attending and what they expect)
3. A request for a detailed timeline (before, during, and after the event)
4. Budget breakdown
5. Task list with owners and deadlines
6. Contingency plans (what could go wrong?)

**Make it detailed enough that someone could hand this plan to an event coordinator and they'd know exactly what to do.**''',
        'example_prompt': '''I've been asked to organise a team-building workshop for my department. I've never planned an event before — help me create a complete plan.

**EVENT DETAILS:**
- What: Half-day team-building workshop (morning only, 9am-1pm)
- Why: Our team has grown from 8 to 15 people in 6 months. Half the team has never met in person (we're hybrid). Morale is okay but collaboration could be better.
- When: Saturday, March 8th (4 weeks away)
- Where: Need a venue — somewhere in central London. We have a £1,500 total budget.
- Attendees: 15 people (mix of ages 23-52, some introverts, one person uses a wheelchair)
- My boss's one request: "Make it fun, not cringy. No trust falls."

**CREATE A COMPLETE EVENT PLAN:**

**1. Venue Recommendations**
- What type of venue should I look for?
- Key requirements (accessibility, size, AV equipment, catering option)
- Estimated cost range
- When to book by

**2. Workshop Agenda (9am-1pm)**
- Detailed schedule with timings
- Mix of activities (icebreakers, team challenges, discussion, fun)
- Nothing that would make introverts want to hide
- Activities that ACTUALLY help people bond (not forced fun)
- Include a break!

**3. Pre-Event Timeline (4 weeks out)**
- Week-by-week checklist of what to do and when
- What to communicate to the team (and when)
- What to order or book

**4. Budget Breakdown**
- How to spend the £1,500 wisely
- Venue: £[amount]
- Food/drinks: £[amount]
- Materials/supplies: £[amount]
- Buffer for unexpected costs
- Where to save money vs where to spend

**5. Logistics Checklist (Day-Of)**
- What to bring
- What to set up before people arrive
- Timeline for the day (including setup and cleanup)
- Who does what (I'll need to assign helpers)

**6. Communication Plan**
- Email to send the team (when and what to include)
- What information people need (address, parking, what to wear)
- How to build excitement without being annoying

**7. Contingency Plans**
- What if someone cancels last minute?
- What if an activity bombs? (backup plan)
- What if we go over time?
- What if the venue has issues?

**8. Post-Event**
- How to get feedback (without a boring survey)
- Follow-up message to the team
- How to measure if it was successful

**TONE:** Make this feel achievable. I'm nervous about organising this and I need a plan I can follow step by step.''',
    },
    {
        'title': 'Question 28: The Learning Scenario Designer',
        'description': 'Design realistic learning scenarios and practice exercises that develop genuine understanding',
        'difficulty': 'intermediate',
        'order': 28,
        'points': 35,
        'instructions': '''One of the most valuable skills in any professional field: the ability to DESIGN learning experiences — not just complete them.

**What You'll Learn:**
- How to use AI to create realistic, effective learning scenarios
- Designing questions and exercises that build genuine understanding
- Thinking about common mistakes and misconceptions — and how to address them

**Why This Matters:**
Whether you're training a colleague, creating study materials, writing assessments, or helping someone understand a topic — being able to design good learning scenarios is a superpower.

**The Difference Between a Weak and a Strong Scenario:**
- **Weak:** "A company experiences a data breach. What should they do?"
- **Strong:** "At 9pm on a Friday, the IT manager of a 30-person marketing agency receives an alert that an unknown IP address has been accessing the shared cloud storage for the past 6 hours. Two senior staff are on holiday. The office is closed and there's no on-call policy. What are the first 3 actions to take, and why does the ORDER matter?"

The second one is specific, pressured, and forces genuine thinking — not just reciting knowledge.

**Your Challenge:**
Pick a technical or professional topic you know well (or want to explore). Use AI to design a **complete learning scenario package** around it.

**Your prompt must request:**
1. A realistic, detailed scenario (a specific situation someone could actually face)
2. A set of guided questions that lead learners through the scenario step by step
3. The "expert answer" for each question (what a knowledgeable person would say)
4. Three common mistakes beginners make — and what each mistake reveals about their thinking
5. A practical follow-up challenge (something learners can DO after working through the scenario)

**Topic ideas:**
- Network security incident response
- Troubleshooting a slow or failing web application
- Designing a database schema for a new project
- Managing a software project that's falling behind schedule
- Responding to a customer data protection request
- Setting up IT systems for a newly onboarded team''',
        'example_prompt': '''Design a complete learning scenario package for IT students learning about cybersecurity incident response.

**TOPIC:** Responding to a suspected phishing attack in a small business

**Target learners:** IT students who understand what phishing is conceptually but have never practised the response process in a realistic, pressured context.

**Learning goal:** By the end of this scenario, learners should be able to identify the correct immediate steps in an incident response, explain WHY those steps come in a specific order, and recognise the reactive mistakes that make things worse.

---

**CREATE THE FOLLOWING:**

**1. The Scenario (realistic and specific)**
Write a detailed scenario description that:
- Has a specific time, place, and context (not just "a company was attacked")
- Involves real decisions with no single obvious "right" answer on the surface
- Includes enough detail to feel immersive but not overwhelming
- Creates a sense of pressure — time, available resources, or ambiguity
- Is 150-200 words in length

**2. Guided Questions (6-8 questions)**
Design questions that:
- Build on each other (each answer sets up the next question)
- Progress from "what happened?" to "why does this matter?" to "what should you do and why?"
- Include at least one question that challenges a common assumption
- Are specific to THIS scenario, not generic cybersecurity questions
- For each question, also include: "What a strong answer looks like" (the expert model answer, 2-4 sentences)

**3. The Expert Walkthrough**
Write a model response showing how an experienced IT professional would work through this scenario:
- What they notice first and why
- Their decision-making process (including what they rule out)
- Why they prioritise steps in a specific order
- What they document and when
(250-300 words, written in narrative form)

**4. Common Mistakes (three beginner mistakes)**
For each mistake:
- Describe exactly what the learner does wrong
- Explain WHY this is wrong (what assumption or knowledge gap it reveals)
- Give the correct approach and explain why it matters

**5. Practical Follow-Up Challenge**
A hands-on task the learner can complete after working through the scenario:
- Something active (not just further reading)
- Directly builds on what the scenario taught
- Completable in 20-30 minutes
- Includes clear success criteria (how the learner knows they've done it well)

---

**Quality check:** After generating everything, review the scenario and questions together. Would a motivated IT student genuinely learn something? Would it feel like a situation they could actually face?''',
    },
    {
        'title': 'Question 29: The Multi-Agent Thinker',
        'description': 'Simulate multiple expert perspectives to get well-rounded advice',
        'difficulty': 'advanced',
        'order': 29,
        'points': 45,
        'instructions': '''The smartest decisions come from considering multiple perspectives. AI can simulate an entire advisory board.

**What You'll Learn:**
- How to get AI to argue multiple sides of an issue
- Simulating different expert perspectives
- Making better decisions by seeing blind spots

**The Concept:**
Instead of getting one opinion from AI, ask it to role-play as 3 different experts who each bring a different lens to the same problem. They might agree, disagree, or see things the others miss.

This is how real advisory boards work — a finance person, a creative person, and a strategist will all see the same opportunity differently.

**Your Challenge:**
You have an idea, project, or decision. Get AI to evaluate it from **3 different expert perspectives.**

**Pick a scenario:**
- A new product idea you want to launch
- A business pivot you're considering
- A marketing strategy for a new brand
- A career decision with multiple factors
- A community project or event concept

**Your prompt must include:**
1. The idea/situation in detail
2. Three specific expert roles (not just "expert 1, 2, 3" — give them specialities and personalities)
3. What each expert should focus on (their lens)
4. A request for each expert's honest opinion (including criticism)
5. A final "consensus" section — where do they agree and disagree?

**The power move:** Ask the experts to respond to EACH OTHER's points, not just give isolated opinions.''',
        'example_prompt': '''I have a business idea and I want to stress-test it by getting 3 different expert perspectives. Each expert should give their honest opinion — including criticism.

**THE IDEA:**
A subscription box for people learning to cook. Each month, subscribers get:
- A themed recipe card set (e.g., "Italian basics" or "30-minute weeknight meals")
- The exact spices and specialty ingredients needed (not common stuff like salt or oil)
- A QR code linking to step-by-step video tutorials
- A beginner-friendly difficulty rating (1-5 stars)
- Price: £24.99/month, commitment-free

Target: Young adults (22-35) who want to cook more but find it overwhelming to know where to start.

**THE THREE EXPERTS:**

---

**EXPERT 1: Maya — The Marketing Strategist**
- Background: 12 years in direct-to-consumer brand marketing, launched 3 successful subscription boxes
- Her lens: Market fit, customer acquisition, branding, competition
- Personality: Enthusiastic but data-driven. Will tell you if the market is too crowded.
- She should evaluate:
  - Is there real demand for this? (Who's the competition?)
  - How would she position this brand?
  - What's the customer acquisition strategy?
  - What's the biggest marketing challenge?
  - Her honest prediction: will this work?

---

**EXPERT 2: James — The Finance & Operations Guy**
- Background: CFO of an e-commerce company, previously ran a food subscription startup
- His lens: Numbers, logistics, margins, scalability
- Personality: Pragmatic, no-nonsense. Loves spreadsheets. Will poke holes in your financial model.
- He should evaluate:
  - Are the margins viable at £24.99? (Cost of ingredients, packaging, shipping?)
  - What's the break-even point?
  - Operational challenges (sourcing, spoilage, shipping food items)
  - What's the churn risk? (Subscription fatigue)
  - His honest prediction: financially viable?

---

**EXPERT 3: Aisha — The Customer Experience Designer**
- Background: UX researcher who specialises in subscription products and food tech
- Her lens: Will customers actually love this? Will they stick around?
- Personality: Empathetic, obsessed with user behaviour. Thinks about the unboxing moment.
- She should evaluate:
  - Would the target customer actually want this? (Or will they buy once and forget?)
  - What would make the unboxing experience memorable?
  - How to reduce churn (keep people subscribed)
  - What's missing from my concept that customers would expect?
  - Her honest prediction: will customers love this?

---

**FORMAT:**

For each expert:
1. **Initial Reaction** (2 sentences: gut feeling)
2. **Detailed Analysis** (their evaluation using their specific lens)
3. **Biggest Concern** (the one thing that worries them most)
4. **One Suggestion** (what would they change or add?)
5. **Verdict:** Green light / Yellow light (proceed with caution) / Red light

**THEN — The Advisory Board Discussion:**
After all 3 have spoken, write a brief "discussion" where:
- Where do all 3 agree?
- Where do they disagree? (And who has the stronger argument?)
- What's the consensus recommendation?
- Top 3 things I should do before investing any money

Make the experts feel like real people with real opinions — not just generic positive/negative takes.''',
    },
    {
        'title': 'Question 30: Prompt Engineering Foundation Challenge',
        'description': 'The final challenge: apply every technique to your own real-world scenario',
        'difficulty': 'advanced',
        'order': 30,
        'points': 50,
        'instructions': '''Congratulations — you've reached the final challenge! Time to prove you've mastered prompt engineering.

**What This Challenge Tests:**
Every technique you've learned across all 29 lessons:
- Specificity and context (Lessons 1-3)
- Structure and formatting (Lessons 4, 6)
- Examples and tone control (Lessons 5, 7)
- Iteration and refinement (Lesson 8)
- Multi-turn conversations (Lesson 9)
- Front-loading context (Lesson 10)
- Role assignment (Lesson 11)
- Chain-of-thought reasoning (Lesson 12)
- Constraints (Lesson 13)
- Templates and personalisation (Lessons 14, 16)
- Real-world application (Lessons 17-29)

**Your Final Challenge:**
Choose a real scenario from YOUR life — something you actually need help with — and demonstrate mastery by writing a **series of 3-4 connected prompts** that build on each other.

**Pick your own scenario, or use one of these:**
- Planning and launching a personal IT project (app, tool, or portfolio piece)
- Preparing for a major certification or assessment (study plan → practice → review → execute)
- Launching a side hustle or creative project (idea → plan → marketing → first steps)
- Solving a real problem in your community or organisation (diagnose → analyse → plan → communicate)
- Creating a personal development plan for a specific skill (assess → plan → track → adjust)

**YOUR SERIES OF PROMPTS MUST DEMONSTRATE:**

1. **Prompt 1 — Setup & Analysis:**
   - Rich context (your full situation)
   - Clear structure with sections
   - Specific requests with format requirements
   - Role assignment (if appropriate)

2. **Prompt 2 — Go Deeper:**
   - Build on Prompt 1's response
   - Use chain-of-thought ("based on your analysis, now...")
   - Add constraints to focus the output
   - Request a specific deliverable

3. **Prompt 3 — Make It Actionable:**
   - Reference both previous responses
   - Create something concrete (a plan, a document, a strategy)
   - Include timeline, owners, and specific next steps
   - Apply iteration ("improve this by...")

4. **Prompt 4 (Optional but impressive) — Communicate It:**
   - Take what you've built and adapt it for a specific audience
   - Different tone/format for a different reader
   - Show audience adaptation skills

**Grading Criteria:**
- Did you provide rich, relevant context?
- Did you use clear structure and formatting?
- Did each prompt build meaningfully on the previous one?
- Did you use constraints, roles, or reasoning techniques?
- Is the final output genuinely useful for your scenario?
- Would someone else find this impressive and practical?

**This is YOUR moment. Show what you've learned. Make it real, make it useful, and make it yours.**''',
        'example_prompt': '''I'm using all my prompt engineering skills to tackle a real challenge: I'm planning to build and launch a personal IT portfolio project over the next 10 weeks. Here's my full series:

---

**PROMPT 1 — ANALYSIS & RESEARCH**

Act as a senior software developer who mentors students building their first portfolio projects. You've seen hundreds of student projects — you know exactly what makes them impressive and what makes them forgettable.

**My Context:**
- I'm an IT student with 8 months of learning behind me (HTML, CSS, basic Python, intro to databases)
- My goal: Build one solid portfolio project that demonstrates real skills and solves a genuine problem
- Available time: 10-12 hours per week for the next 10 weeks
- Tools I have: VS Code, GitHub (basic), Python, SQLite, basic knowledge of Flask
- What I want to avoid: Building something nobody would actually use, or copying a tutorial without understanding it
- End goal: Have something I'm proud to show and talk about in detail

Based on your experience, give me:
1. The 5 most common mistakes students make when building portfolio projects (so I can avoid them)
2. The qualities that make a portfolio project genuinely impressive vs. forgettable
3. 5 project ideas well-suited to my skill level that solve a real problem (not just another to-do app)
4. A framework for the 10 weeks: Plan → Build → Test → Document → Present

Be honest — I want something I'm actually capable of building well, not something impressive on paper that I can't explain.

---

**PROMPT 2 — CHOOSE AND PLAN**

Based on your suggestions, I've chosen to build a **personal expense tracker web app** — a simple tool where users can log expenses, set monthly budgets, and see simple visual summaries of their spending.

Now let's build a detailed development plan for the first 4 weeks (the foundation phase).

For each week, create:
- **Main goal** (what I should have working by Sunday)
- **Daily tasks** (specific, achievable tasks for 1.5-2 hours each evening)
- **One technical concept to learn** (link to what I'm building that week)
- **Weekly checkpoint** (how I know the week was successful — a specific, testable outcome)
- **Common mistake to avoid** (one thing that trips students up at this stage)

**Constraints:**
- Each daily task must be completable in 1.5-2 hours
- I shouldn't skip ahead — each week must build on the previous one
- Include time for research, not just coding
- Keep it realistic (I have coursework too)

Also: create a "Project Setup Checklist" — everything I need to do before writing a single line of code.

---

**PROMPT 3 — DOCUMENTATION PLAN**

Now help me think about how to document and present this project professionally.

Create:

1. **README Structure:**
   A template for my GitHub README that:
   - Explains what the project does and who it's for (in plain English)
   - Shows how to install and run it (step-by-step)
   - Includes a screenshot section placeholder
   - Explains the technical choices I made (and why)
   - Shows what I learned from building it

2. **Project Writeup (for a portfolio or presentation):**
   A 250-word narrative explaining the project as if presenting it to someone who hasn't seen it:
   - The problem it solves
   - How I approached building it
   - The biggest technical challenge and how I solved it
   - What I'd improve if I had more time

3. **5 Questions I Should Be Able to Answer:**
   The questions someone knowledgeable would ask when reviewing this project — with guidance on how to prepare strong answers for each one.

Keep it professional but authentic — this should sound like a student who genuinely built something, not a marketing brochure.

---

**PROMPT 4 — THE PITCH VERSION**

Final piece: I want to be able to talk about this project confidently in different situations.

Create 3 versions of how I'd describe it:

1. **The 60-second verbal explanation** (for when someone asks "what did you build?"):
   Engaging, clear, avoids jargon — makes the listener understand the value immediately

2. **The technical deep-dive (2-3 minutes):**
   For a technical audience — covers the architecture, key decisions, and challenges overcome

3. **The one-sentence version:**
   For a social media post, profile bio, or casual introduction — punchy and memorable

For each: write the actual words, not just a description. Make them feel natural and confident.

---

This is my actual plan. Make it genuinely useful — I'll be following this for the next 10 weeks.''',
    },
]
