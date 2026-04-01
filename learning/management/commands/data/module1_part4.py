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
        'title': 'Question 26: The Professional Communication Toolkit',
        'description': 'Communicate a project or initiative consistently across five different professional formats',
        'difficulty': 'advanced',
        'order': 26,
        'points': 40,
        'instructions': '''The ability to communicate the same information clearly to completely different audiences is one of the most valuable skills you can develop. This challenge puts that to the test.

**What You'll Learn:**
- How to use AI to create consistent messaging across multiple formats
- Adapting the same core information for completely different readers
- Building a complete communication package around a single project or event

**The Challenge:**
You have a project, event, or idea. Create a **complete communication package** — the same core information presented in 5 completely different formats for 5 different audiences.

**You'll create ALL of these in a single, well-structured prompt:**
1. **Organiser's briefing** (for the people helping you make it happen)
2. **Decision-maker summary** (for someone whose approval or support you need)
3. **Participant invitation** (for the people you want to attend or get involved)
4. **How-it-works explainer** (for someone who knows nothing about it)
5. **Social media post** (to build interest and awareness publicly)

**The key constraint: CONSISTENCY.** All 5 must clearly be about the same project with the same core message — just adapted for the format and reader.

**Your prompt must include:**
- What the project or event is (what it is, what it's for, why it matters)
- Who each piece is for and what they care about
- Specific format and length constraints for each piece

**Use something real from your life, or a realistic fictional idea.** It could be a community event, a family celebration, a fundraiser, a club or group activity — anything you'd actually need to communicate about.''',
        'example_prompt': '''Create a complete communication package for a community charity fundraiser. All 5 pieces should clearly be about the same event, adapted for each specific audience.

**ABOUT THE EVENT:**
- What it is: A sponsored 5km walk through the local park to raise money for a local food bank
- Why it exists: The food bank supported over 800 local families last year but is running low on funding — they need new donations to stay open through winter
- How it works: Participants sign up, collect sponsorship from friends and family, complete the walk together on a Sunday morning, and all funds raised go directly to the food bank
- Details: Sunday 14th September, 9am start, local park, free to enter, all fitness levels welcome, family-friendly
- Target: Raise £3,000 and get at least 80 participants

**CREATE THESE 5 PIECES:**

**1. Volunteer Organiser Briefing (for the 8 people helping run the event)**
- Length: 200-250 words
- Audience: Friends and community members who've agreed to help on the day
- Focus: Their specific roles, what happens when, and what to do if things go wrong
- Include: A simple timeline for the morning (7:30am setup → 9am walkers arrive → 10:30am finish → 11am pack up)
- Tone: Friendly, clear, practical — these are volunteers, not employees

**2. Sponsorship Request (for local businesses being asked to donate prizes or funding)**
- Length: 120-150 words
- Audience: Local business owners who receive dozens of requests like this
- Focus: The cause, the community impact, what's in it for them (logo on materials, goodwill, local visibility)
- Must include: One specific, compelling fact about the food bank's impact
- Tone: Respectful, grateful, concise — they're busy

**3. Participant Invitation (for local residents being invited to sign up and walk)**
- Length: 150-180 words
- Audience: People who might want to take part but aren't sure if it's for them
- Focus: Making it feel easy, inclusive, and worth their Sunday morning
- Must include: A clear answer to "but I'm not very fit — can I still do it?"
- Tone: Warm, encouraging, community-spirited

**4. How-It-Works Explainer (for someone who's heard about it but doesn't know the details)**
- Length: 100-130 words
- Audience: Someone who's asked "so how does a sponsored walk actually work?"
- Focus: Simple, clear explanation — registration, sponsorship, the walk itself, where the money goes
- Must include: What happens if someone can't get any sponsors
- Tone: Friendly, clear, no assumptions about what they already know

**5. Social Media Post (for the local community's public page)**
- Length: 100-130 words
- Audience: Local residents scrolling past — you have 3 seconds to catch their attention
- Focus: Hook, key details, call to action
- Must include: One detail that makes this feel urgent or personally meaningful
- Tone: Upbeat, community-focused, direct

**CRITICAL:** All 5 must feel like they're about the same event. The core message — "a friendly, inclusive walk that raises real money for a cause the local community genuinely needs" — must come through in every piece. Read them side by side: does the event feel consistent? Does the emotional hook land in every version?

After all 5, write 2-3 sentences explaining how you adjusted the tone and focus for each reader.''',
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
- Planning a major family celebration or milestone event (concept → logistics → coordinate → execute)
- Organising a home renovation or significant personal project (assess → plan → manage → complete)
- Planning an extended trip or adventure (research → prepare → organise → go)
- Making a meaningful personal change — health, fitness, or a new habit (assess → plan → track → adjust)
- Starting a creative personal project like writing, gardening, or a community initiative (idea → plan → develop → share)

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
        'example_prompt': '''I'm using everything I've learned about prompt engineering to plan something I've been putting off for years: a 6-week family road trip through Europe this summer. Four adults, one car, a rough idea of where we want to go — and no real plan yet. Here's my full series of connected prompts:

---

**PROMPT 1 — RESEARCH & ROUTE OPTIONS**

Act as an experienced travel planner who specialises in road trips across Europe. You've planned dozens of these — you know the routes that look great on paper but are exhausting in reality, and the hidden gems that make a trip genuinely memorable.

**Our Situation:**
- Who's going: Me and my partner (both mid-30s), and two friends who'll join for the first 3 weeks. The four of us travel well together but have different priorities — my partner wants slow, relaxed stops; our friends want to cover more ground and see big landmarks.
- Duration: 6 weeks total, leaving late June
- Starting and ending point: UK (driving through the Channel Tunnel)
- Rough wish list: France, Spain, and either Portugal or Italy — we can't do everything
- Budget: Around £4,500 for all four people for the full trip (excluding the car, which we own)
- Non-negotiables: At least one week somewhere coastal with good swimming; good food throughout; no more than 4 hours driving on any single day
- What I want to avoid: Over-scheduling. Previous holidays have been ruined by trying to fit too much in.

Give me:
1. The honest trade-offs of each route option — France/Spain/Portugal vs France/Spain/Italy. What do we gain and lose with each?
2. A recommended route with a rough week-by-week structure that balances both travel styles
3. The 5 decisions we need to make before we can book anything
4. A planning framework: Research → Book → Prepare → Pack → Go

Be direct. If our budget or timeline is unrealistic for what we want, say so.

---

**PROMPT 2 — BUILD THE ITINERARY**

Based on your advice, we've chosen France → Spain → Portugal. The rough shape: 10 days in France, 10 days in Spain, 10 days in Portugal, with 2 days of driving buffer built in.

Now build me a detailed week-by-week itinerary.

For each week, give me:
- **Where we are** (specific region or cities, not just countries)
- **Daily structure** (what type of day: driving day, base-camp day, or exploration day)
- **2-3 highlights** (specific places, experiences, or food worth going out of our way for)
- **One thing to watch out for** (a common mistake travellers make in this area)
- **Accommodation type** (hotel, gîte, Airbnb, campsite — what makes sense here and why)

**Constraints:**
- No more than 4 hours driving on any day
- At least 3 nights in each major stopping point — no one-night stays
- The coastal week must be in the itinerary by week 4
- Keep it realistic for people who also want to sit in a café for 2 hours doing nothing

Also: flag any weeks where the budget will be under the most pressure, and suggest where we could save without ruining the experience.

---

**PROMPT 3 — THE PRACTICAL DETAILS**

The itinerary is taking shape. Now help me get the practical side sorted — the stuff that falls apart if you don't think about it in advance.

Create:

1. **The Booking Order:**
   What to book first, second, and third — and how far in advance. Flag anything that will sell out or get significantly more expensive if we leave it too late.

2. **The Car Packing Strategy:**
   We're four adults in one car for 6 weeks. Help us think through what to bring and what to leave behind:
   - The essentials most people forget
   - The things people always overpack
   - How to organise the boot so we're not unpacking everything every night
   - What to buy when we arrive rather than bringing from home

3. **The "What If" Plan:**
   Five things that could genuinely go wrong on a trip like this — and for each, the practical steps to handle it quickly so it doesn't derail the whole trip.

---

**PROMPT 4 — COMMUNICATE IT**

Before we go, I need to get a few things sorted with the people around us.

Write me these three real pieces of communication:

1. **The message to our friends confirming the plan:**
   We need to give them enough detail to book their time off and feel genuinely excited — without overwhelming them with logistics they don't need yet. Warm, clear, and specific about the dates, the rough route, and what they need to sort on their end. 150-200 words.

2. **The house and pet checklist message (for the neighbour who's helping while we're away):**
   Clear, practical, and not too long. Covers: key handover, post, bins, the one plant that needs watering, and how to reach us in an emergency.

3. **The one-paragraph trip summary:**
   Something I can share with family who'll ask "so where are you going?" — engaging enough that they actually understand what we're doing, short enough that I'm not explaining it for 10 minutes.

---

This is my actual plan. Make every part genuinely useful — we're booking this in the next few weeks.''',
    },
]
