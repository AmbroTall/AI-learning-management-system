"""
Module 1 Part 2: Levelling Up — "Conversations That Work Harder"
Challenges 9-16: Advanced techniques and conversation management (4-5 hours)
"""

MODULE1_PART2_CHALLENGES = [
    {
        'title': 'Question 9: Building on the Conversation',
        'description': 'Learn how to have multi-step conversations that build toward a goal',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 25,
        'instructions': '''Real-world tasks rarely fit in a single message. The best prompt engineers think in conversations.

**What You'll Learn:**
- How to plan multi-turn conversations
- How each message can build on the last
- How to reference previous context naturally

**The Concept:**
Instead of cramming everything into one mega-prompt, break your task into logical steps. Each message narrows the focus based on what AI gave you before.

Think of it like a brainstorming session with a colleague:
- "Here's my situation..." → "Interesting. Based on your ideas, I like option 2..." → "Great, now let's build a detailed plan for that..."

**Your Challenge:**
You want to plan a community event in your neighbourhood but don't know where to start. Have a **3-message conversation** with AI:

**Message 1:** Share details about your neighbourhood, available spaces, budget, and what kind of event you're thinking about. Ask for 3-5 event ideas.
**Message 2:** Pick the most interesting idea. Ask for a detailed breakdown: what it involves, how to organise it, potential costs, and biggest challenges.
**Message 3:** Ask for a concrete 2-week action plan to make it happen.

**Write all 3 messages in your prompt.** Use phrases like "Based on your suggestions..." or "Let's go deeper on idea #2..." to show you're building on context.

**Why This Matters:**
Complex problems need structured conversations. This technique works for event planning, research, creative projects, debugging code — anything that requires going deeper step by step.''',
        'example_prompt': '''I want to organise a community event in my neighbourhood. Let's work through this step by step.

---

**MESSAGE 1:**
Here's my situation:
- I live in a friendly neighbourhood in south Manchester with about 200 houses
- There's a community centre with a hall (seats 80), a local park, and a church with a car park
- Budget: I can probably raise £500 from the local residents' association
- Time of year: Early summer (June)
- The neighbourhood has a mix of young families, students, and retired people
- We don't currently have many community events — people want to connect more

Based on this, suggest 5 community event ideas that would bring people together. For each, give me a one-line description and why it would work for our neighbourhood.

---

**MESSAGE 2:**
I really like the idea of [pick whichever one resonates — let's say it's a summer street food festival in the park]. Let's go deeper on this one.

Tell me:
1. What would the event actually look like? (Layout, timing, activities)
2. How do I find local food vendors or get neighbours to contribute?
3. What permissions or insurance might I need?
4. What equipment and supplies do I need?
5. What's the biggest challenge I'll face in organising this?
6. How do I make sure ALL age groups enjoy it?

Be practical — I've never organised an event before.

---

**MESSAGE 3:**
I'm going for it. Let's make this happen.

Create a 2-week action plan:
- **Week 1:** Planning, permissions, and reaching out to people
- **Week 2:** Final preparations and promotion

For each day, give me:
- One main task (should take 1-2 hours)
- Why it matters
- What "done" looks like

Keep it realistic — I'm doing this in my spare time alongside a full-time job.''',
    },
    {
        'title': 'Question 10: The Perfect Briefing',
        'description': 'Master front-loading context so AI gives brilliant first responses',
        'difficulty': 'intermediate',
        'order': 10,
        'points': 25,
        'instructions': '''The best single technique for getting great AI responses: **front-load your context.**

**What You'll Learn:**
- How to write a comprehensive context block
- Why "priming" AI with your full situation works so well
- The CONTEXT → TASK → FORMAT framework

**The Framework:**
Structure every complex prompt in three parts:
1. **CONTEXT:** Everything AI needs to know about you and your situation
2. **TASK:** What you specifically need help with
3. **FORMAT:** How you want the answer structured

**Your Challenge:**
You're planning a big surprise birthday party for someone important to you. Give AI your COMPLETE context upfront to get the most personalised party planning help possible.

**Your prompt must include:**

**Context section:**
- Who the party is for (their personality, interests, age)
- Your relationship with them
- Budget and guest count
- Venue options you're considering
- Any constraints (dietary needs, accessibility, surprise element)

**Task section:**
- What specific help you need (theme ideas? timeline? food planning? entertainment?)

**Format section:**
- How to organise the response (sections, bullet points, priority order)

**Why This Works:**
When AI has full context from the start, it doesn't waste time on generic advice. Every suggestion is tailored to YOUR situation. This is the difference between "plan a birthday party" and "plan a surprise 60th for someone who loves gardening, hates fuss, and has 30 guests coming to a village hall on a £400 budget."''',
        'example_prompt': '''I need help planning a surprise birthday party. Here's my complete situation:

**CONTEXT — About the Birthday Person:**
- Who: My mum, turning 60
- Personality: Warm, social, loves being around family but hates being the centre of attention (ironic for a surprise party!)
- Interests: Gardening, baking, quiz nights, 80s music, her book club
- Important: She keeps saying "don't make a fuss" — but she'd secretly love it if we did something thoughtful
- She thinks we're just having "a quiet family dinner"

**CONTEXT — The Logistics:**
- Date: Saturday, April 12th (her actual birthday)
- Venue: We've booked the village hall near her house (capacity 60, basic kitchen, no decorations)
- Guest count: About 35 people (family, neighbours, book club friends, old school friends)
- Budget: £400 total (between me and my two siblings)
- Dietary: Mum is vegetarian, one guest is gluten-free, most people eat everything
- The surprise element: We need to get her there without suspicion. My brother will bring her "for a drink"

**TASK — What I Need:**
1. A theme that feels personal to mum (not generic "60th" banners)
2. Food plan for 35 people on a budget (mix of homemade and bought)
3. A timeline for the day (setup, surprise moment, activities)
4. 2-3 activity ideas that suit a mixed-age group (kids to 80-year-olds)
5. How to keep the surprise secret (communication plan with guests)
6. A decoration plan that's charming, not tacky

**FORMAT:**
- Use clear numbered sections matching my 6 requests
- Include a budget breakdown showing where the £400 goes
- Give me a week-by-week prep timeline (we have 4 weeks)
- Keep suggestions practical — I'm organising this while working full-time''',
    },
    {
        'title': 'Question 11: Role Play for Expert Advice',
        'description': 'Unlock expert-level responses by giving AI a specific role to play',
        'difficulty': 'intermediate',
        'order': 11,
        'points': 30,
        'instructions': '''Want advice from a financial advisor, career coach, or nutritionist? Just ask AI to become one.

**What You'll Learn:**
- How to assign AI a specific expert role
- Why role-playing produces deeper, more specialised responses
- How to set up the role with credentials and personality

**The Technique:**
When you say "Act as a certified financial advisor with 15 years of experience," AI shifts its response style. It uses industry terminology, gives more nuanced advice, and thinks from that expert's perspective.

**The Key Elements of a Great Role Assignment:**
1. **Who they are** — title, experience level, specialisation
2. **Their style** — how they communicate (direct? nurturing? no-nonsense?)
3. **Their constraints** — what they would and wouldn't recommend
4. **Your situation** — what you're coming to them for

**Your Challenge:**
Get personalised advice from a **personal finance advisor helping you budget and save.** Set up the role in detail, then present your financial situation and ask for a complete plan.

**Make the role detailed!** Don't just say "act as a finance advisor." Give them a background, a communication style, and expertise that matches what you need.

**Why This Matters:**
In real life, expert advice costs hundreds per hour. With the right prompt, you can get thoughtful, personalised guidance. The better you define the role, the better the advice.''',
        'example_prompt': '''I need help getting my finances in order. Please take on this role:

**YOUR ROLE:**
You are a friendly, no-nonsense personal finance advisor helping me budget and save. Specifically:
- You've helped hundreds of young professionals go from "where does my money go?" to having a clear financial plan
- You specialise in helping people in their 20s-30s who earn a decent salary but never seem to save
- Your approach: practical steps over theory, no judgement, celebrate small wins
- You DON'T recommend complex investments or risky strategies for beginners
- Your motto: "Pay yourself first, automate everything, then enjoy the rest guilt-free"

**MY SITUATION:**
- Age: 27, single, renting a flat with one flatmate
- Income: £32,000/year (about £2,100/month after tax)
- Current savings: £800 (that's it...)
- Monthly expenses I know about: Rent £650, phone £40, gym £30, streaming £25
- Where my money disappears: Eating out, online shopping, nights out
- I have no budget system — I just spend until the account looks scary
- No pension beyond the workplace default
- No debt (thankfully)
- Goal: I want to save £5,000 in 12 months for a holiday fund AND start feeling in control

**WHAT I NEED FROM YOU:**

As my finance advisor, give me:

1. **Honest Assessment** — Based on my numbers, where am I and how bad/good is it? Be real with me.

2. **Simple Budget** — Create a monthly budget that:
   - Puts savings FIRST (how much per month to hit £5,000 in 12 months?)
   - Is realistic (I'm not going to stop eating out entirely)
   - Includes a "fun money" category so I don't feel deprived
   - Shows me exactly where each pound goes

3. **3 Quick Wins** — Things I can do THIS WEEK to start saving immediately

4. **The One System** — One simple system or app I should set up to automate this so I don't have to think about it

5. **Monthly Check-In Questions** — 3 questions I should ask myself each month to stay on track

Talk to me like a coach, not a textbook. Be direct, practical, and encouraging.''',
    },
    {
        'title': 'Question 12: Think Step-by-Step',
        'description': 'Get smarter AI responses by asking it to show its reasoning',
        'difficulty': 'intermediate',
        'order': 12,
        'points': 30,
        'instructions': '''Here's a cheat code: when you ask AI to "think step by step," it gives significantly better answers.

**What You'll Learn:**
- What "chain-of-thought" prompting is and why it works
- How to request structured reasoning
- When to use this technique (decisions, analysis, complex problems)

**The Science:**
Research shows that when AI explains its reasoning step-by-step, it makes fewer errors and gives more thoughtful answers. It's the difference between asking someone to shout an answer vs. showing their working.

**When to Use This:**
- Making a big decision (career, purchase, life change)
- Analysing something with multiple factors
- When you need to understand WHY, not just WHAT
- Problem-solving complex situations

**Your Challenge:**
You're facing a real decision. Ask AI to help — but specifically request that it **shows its thinking at each step.**

**Your Decision:**
I am currently looking at a career change into the AI sector. What are the benefits of doing this over my current job working in the hospitality industry? Don't mention salaries. My main goal is to work remotely.

**Your prompt must include:**
1. The decision with full context (both options, your priorities)
2. A request for step-by-step analysis (not just a recommendation)
3. Specific steps you want AI to follow (e.g., "evaluate remote work potential," "consider transferable skills," "assess long-term growth")
4. Ask AI to give a final recommendation WITH its reasoning

**The result should feel like a thoughtful conversation, not a snap judgement.**''',
        'example_prompt': '''I need help thinking through a big career decision. Don't just tell me what to do — walk me through your thinking step by step.

**THE DECISION:**
I am currently looking at a career change into the AI sector. What are the benefits of doing this over my current job working in the hospitality industry? Don't mention salaries. My main goal is to work remotely.

**MY SITUATION:**
- Current: Working as a restaurant supervisor in a busy hotel (3 years in hospitality)
- Age: 29, based in Birmingham
- What I like about hospitality: Working with people, fast-paced problem-solving, teamwork
- What I don't like: Can't work remotely, long unsociable hours, physically exhausting, limited progression without relocating
- My main goal: I want to work remotely — flexibility to work from home or anywhere
- Tech skills: Comfortable with computers, use social media daily, have played around with AI tools like ChatGPT
- Interest in AI: Fascinated by how AI is changing every industry, completed this AI prompt engineering course
- Constraints: I need to keep earning while I transition — can't afford to stop working

**ANALYSE THIS STEP BY STEP (don't mention salaries):**

**Step 1:** What are the realistic remote work opportunities in the AI sector vs hospitality? (Be specific about AI roles that can be done remotely)
**Step 2:** What transferable skills do I already have from hospitality that are valuable in AI/tech? (Connect the dots for me)
**Step 3:** What would I need to learn to make this transition? (Specific skills, courses, timeframes)
**Step 4:** How does the AI sector compare for work-life balance and flexibility vs hospitality?
**Step 5:** What are the growth opportunities and job security like in AI compared to hospitality long-term?
**Step 6:** What are the biggest risks of making this change, and how can I reduce them?
**Step 7:** Give me your final recommendation with clear reasoning — should I make this move?

Show your working at every step. I want to understand HOW you reached your conclusion, not just what it is.''',
    },
    {
        'title': 'Question 13: Constraints Unlock Creativity',
        'description': 'Discover how adding restrictions actually produces better, more focused results',
        'difficulty': 'intermediate',
        'order': 13,
        'points': 30,
        'instructions': '''It sounds backwards, but: **more constraints = better output.**

**What You'll Learn:**
- Why restrictions force AI to be creative and specific
- How to use constraints strategically
- The types of constraints that work best

**The Paradox:**
"Write something about my business" → generic, bland
"Write a 150-word About page that avoids cliches, uses exactly 2 customer quotes, starts with a question, and must mention our founding story" → focused, interesting!

**Types of Constraints You Can Use:**
- **Length:** Exact word count or character limit
- **Style:** Must include/avoid specific words or phrases
- **Structure:** Specific format or sections required
- **Content:** Must reference certain topics, examples, or data
- **Tone:** Specific emotional register
- **Audience:** Who it's for (and who it's NOT for)

**Your Challenge:**
Write an "About Me" page for a professional website (yours, or a fictional one). But here's the key — include **at least 5 specific constraints** that force AI to produce something unique and compelling.

**Minimum constraints to include:**
1. Exact word count range
2. A tone described with 2-3 specific adjectives
3. Something it MUST include (a story, a number, a quote)
4. Something it must AVOID (cliches, jargon, specific phrases)
5. A structural requirement (how it starts, how it ends, number of paragraphs)

**The more creative and specific your constraints, the better the output. Push yourself!**''',
        'example_prompt': '''Write an "About Me" section for my freelance copywriting website.

**About Me:**
- Name: Jordan Lee
- Profession: Freelance copywriter, specialising in small businesses and startups
- Experience: 3 years freelance, before that 2 years in-house at an e-commerce company
- Personality: Down-to-earth, slightly funny, hates corporate waffle
- Clients: Local coffee shops, online stores, personal trainers, small tech startups
- What makes me different: I actually BUY from my clients. I only work with businesses I genuinely like.

**CONSTRAINTS (follow ALL of these):**

1. **Length:** Exactly 160-180 words. Not one word more.
2. **Tone:** Confident, warm, and a tiny bit cheeky. Like a smart friend you'd trust with your business.
3. **Must include:**
   - A specific number (e.g., "helped 40+ businesses" or reference a result)
   - The phrase "words that actually work" somewhere natural
   - ONE short sentence (under 5 words) for impact
4. **Must avoid:**
   - The words "passionate," "creative," "storyteller," "wordsmith," or "craft"
   - Starting with "Hi, I'm Jordan" or any version of introducing yourself first
   - Any sentence longer than 25 words
5. **Structure:**
   - Start with a bold statement or question (hook the reader immediately)
   - Second paragraph: what I do and who I help
   - Third paragraph: why I'm different (the "I only work with businesses I'd buy from" angle)
   - End with a call-to-action that doesn't say "get in touch" or "let's chat"
6. **Voice:** First person. No third person ("Jordan is a copywriter...").
7. **Feeling:** After reading it, someone should think "I like this person" — not "this person is trying to impress me."

Make every word count. This is a copywriter's website — the About page IS the audition.''',
    },
    {
        'title': 'Question 14: Your AI Learning Coach',
        'description': 'Set up AI as your personal tutor by establishing your learning style and preferences',
        'difficulty': 'intermediate',
        'order': 14,
        'points': 30,
        'instructions': '''One of the most powerful uses of AI: a personal tutor that adapts to exactly how YOU learn.

**What You'll Learn:**
- How to "train" AI on your learning preferences
- How to create a personalised learning experience
- The power of establishing preferences before asking for help

**The Technique:**
Before asking AI to teach you something, tell it HOW you learn best:
- Do you prefer examples or theory first?
- Do you learn by doing or by reading?
- Do you need analogies or straight facts?
- How much time do you have?

This is like telling a personal trainer about your fitness level before they design your programme.

**Your Challenge:**
Set up AI as your personal learning coach in a **two-part prompt:**

**Part 1 — Establish Your Learning Profile:**
Tell AI how you learn, your constraints, communication preferences, and goals.

**Part 2 — Request Help With a Topic:**
Pick any skill you genuinely want to learn (it doesn't have to be tech!) and ask for a personalised learning plan that matches your profile.

**Ideas for topics:**
- Public speaking
- Basic coding (Python, HTML)
- Graphic design
- Personal finance
- A new language
- Cooking a specific cuisine
- Data analysis

**Make sure Part 2 explicitly references your learning profile from Part 1.**''',
        'example_prompt': '''I want you to be my personal learning coach. First, let me tell you how I learn best, then help me learn something new.

---

**PART 1 — My Learning Profile:**

**How I Learn Best:**
- I'm a hands-on learner — I need to DO things, not just read about them
- I like structured sessions with clear goals (not "explore and see what happens")
- I need to understand the "why" before the "how" (don't just tell me steps — tell me why each step matters)
- Real-world examples stick much better than abstract theory
- I love analogies — connecting new concepts to things I already know

**My Constraints:**
- Available time: 2 hours per day (evenings, after work)
- Budget: Up to £40/month for tools or resources
- Currently working full-time so I need flexible learning
- I have a laptop and a smartphone

**My Communication Preferences:**
- Be direct — if I'm wrong or heading in the wrong direction, tell me immediately
- Use simple language first, introduce jargon only when necessary (and define it)
- Break big concepts into bite-sized pieces
- Celebrate progress but don't over-praise — I want honest feedback

**My Learning Goal:**
I want to learn graphic design so I can create professional-looking social media posts, presentations, and basic branding materials for my side business. I don't need to become a professional designer — I just want my business materials to look polished and consistent.

---

**PART 2 — Create My Learning Plan:**

Based on my learning profile above (hands-on, 2 hours/day, structured, "why before how"), create a 4-week learning plan for graphic design fundamentals.

**Week-by-week, I need:**
- What to learn each day (specific topic, max 45 min of learning)
- A daily practice task (a specific design to create with exact requirements)
- One resource to check out (free YouTube video, article, or tutorial)
- A "mini milestone" at the end of each week (something I can share to see my progress)

**Requirements:**
- Start with fundamentals (colour theory, typography, layout basics)
- Focus on social media graphics and simple brand materials
- Recommend 1-2 design tools (with free tiers) and teach me how to use them
- Include real design challenges (e.g., "design an Instagram post for a coffee shop sale")
- By week 4, I should be able to create a consistent set of branded templates for my business

Remember my profile: hands-on tasks over theory, explain WHY each design principle works, keep it to 2-hour daily sessions with clear structure.''',
    },
    {
        'title': 'Question 15: When to Start Fresh vs Continue',
        'description': 'A strategic skill: knowing when to build on context and when to reset',
        'difficulty': 'advanced',
        'order': 15,
        'points': 35,
        'instructions': '''Not every conversation should keep going. Sometimes starting fresh is smarter.

**What You'll Learn:**
- When to continue a conversation (and how)
- When to start a new conversation (and why)
- How to carry forward key context efficiently

**When to CONTINUE the same conversation:**
- You're iterating on the same topic (editing a document, refining an idea)
- AI needs to remember decisions you made together
- You're building something step-by-step (a plan, a project)

**When to START FRESH:**
- You're switching to a completely different topic
- The conversation has gotten long and confused
- You want AI to approach something without bias from earlier messages
- The previous conversation went in a wrong direction

**When starting fresh, SUMMARISE key context:** Don't make AI re-discover everything. Give it a brief summary of where you left off.

**Your Challenge:**
You have two scenarios. For each one, decide: **continue or start fresh?** Then write the appropriate prompt.

**Scenario A:** Yesterday you spent 30 minutes with AI designing a logo concept for your side business. Today you want to write the homepage copy for the same business.

**Scenario B:** You asked AI to help you plan a holiday itinerary and got great suggestions. Now you want to refine the plan and add specific restaurant recommendations.

**For each scenario:**
1. State your decision (continue or fresh) and explain WHY
2. Write the actual prompt you'd use
3. If starting fresh, show how you'd summarise the previous context efficiently''',
        'example_prompt': '''Here are my two scenarios. I'll decide whether to continue or start fresh, and write the right prompt for each.

---

**SCENARIO A: Logo design → Homepage copy**

**Decision: START FRESH**

**Why:** These are different tasks requiring different "thinking modes." The logo conversation would have AI focused on visual concepts, colours, and design language. Homepage copy needs a completely different focus — messaging, persuasion, and writing. Keeping the old context could actually pollute the new task with unnecessary visual design details.

**New Conversation Prompt:**
I'm building a website for my side business and need help writing the homepage copy.

Quick context from a previous session (so you're up to speed):
- Business: "GreenBox" — a subscription service delivering eco-friendly household products
- Brand personality: Friendly, honest, slightly playful (not preachy about sustainability)
- Target customer: Busy professionals aged 25-40 who want to be more eco-friendly but don't have time to research every product
- Visual style: Clean, modern, green and cream colour palette
- Tagline we developed: "Good stuff, delivered. No guilt required."

Now I need homepage copy with these sections:
1. Hero section (headline + subheadline + CTA button text)
2. "How it works" (3 simple steps)
3. "Why GreenBox?" (3 compelling benefits — not generic)
4. Social proof section (write 3 realistic-sounding customer testimonials)
5. Final CTA section (motivating close)

Tone: Match our brand — friendly, honest, a tiny bit cheeky. Like a smart friend who happens to know a lot about sustainability.
Length: Each section should be scannable (short sentences, bullet points where appropriate).

---

**SCENARIO B: Holiday itinerary → Refine with restaurants**

**Decision: CONTINUE**

**Why:** This is iterative work on the SAME topic. AI needs to remember which cities we chose, the travel dates, the accommodation, and the overall vibe of the trip. Starting fresh would mean re-explaining all the context and losing the specific suggestions it already tailored for us.

**Follow-up Prompt (in same conversation):**
Love the itinerary! Let's build on it. I want to add specific restaurant recommendations.

For each day of the trip, suggest:
- A lunch spot (casual, local favourite, under £15 per person)
- A dinner spot (can be a bit nicer, up to £30 per person)
- One "must-try" local food experience (street food, market, food tour, etc.)

For each restaurant:
1. Why you're recommending it (what makes it special)
2. What to order (their signature dish or best item)
3. Whether I need to book ahead

Remember our preferences from earlier: we love trying local food, one of us is vegetarian, and we prefer independent places over chains. Keep it consistent with the relaxed vibe we planned.''',
    },
    {
        'title': 'Question 16: Prompt Templates That Save Time',
        'description': 'Create reusable prompt templates you can use again and again',
        'difficulty': 'advanced',
        'order': 16,
        'points': 35,
        'instructions': '''Why write a great prompt once when you can use it forever?

**What You'll Learn:**
- How to create reusable prompt templates
- Using placeholders for variable information
- Building your own "prompt library"

**The Concept:**
A prompt template is like a fill-in-the-blanks version of a proven prompt. You create the structure once, then swap in new details each time.

**Example:**
Instead of writing a new meeting agenda prompt every week, create a template:
"Generate a meeting agenda for [MEETING TYPE] with [ATTENDEES]. Topics: [LIST]. Duration: [TIME]. Include: time allocation per topic, discussion questions, and action item slots."

**Your Challenge:**
Create a **reusable prompt template** for one of these common tasks:
- Generating meeting agendas from rough notes
- Writing professional emails (any type)
- Creating social media content for a brand
- Summarising long documents or articles
- Preparing for any type of meeting or conversation

**Your template must include:**
1. Clear placeholders in [BRACKETS] for variable information
2. Fixed structure that works every time
3. Built-in quality controls (format, tone, length)
4. Instructions at the top explaining how to use the template

**Then demonstrate the template** by filling it in with a real example.

**What to Submit:**
First, create your template with clear [PLACEHOLDER] fields. Then show the template filled in with a real example so we can see it in action. Your submission should include both the blank template AND the completed version.

**Real-World Value:**
Professionals who use AI daily have personal libraries of prompt templates. This saves enormous time and ensures consistent quality. You're building a tool you'll actually use.''',
        'example_prompt': '''I want to create a reusable prompt template for turning messy meeting notes into professional, actionable meeting summaries. First, build the template, then show it in action.

---

**THE TEMPLATE:**

Create a reusable template with this structure:

**Template Name:** Meeting Notes → Action Plan Converter

**How to use:** Replace everything in [BRACKETS] with your specific information. Keep everything else exactly as written.

**The Template:**
```
Transform these meeting notes into a professional summary and action plan.

MEETING DETAILS:
- Meeting name: [NAME OF MEETING]
- Date: [DATE]
- Attendees: [LIST OF PEOPLE AND THEIR ROLES]
- Duration: [HOW LONG]
- Meeting purpose: [WHY THIS MEETING HAPPENED]

RAW NOTES:
[PASTE YOUR MESSY NOTES HERE]

CREATE THIS OUTPUT:

1. MEETING SUMMARY (3-5 sentences)
   - What was the meeting about?
   - What were the main outcomes?

2. KEY DECISIONS MADE
   - List each decision with brief context
   - Note who approved/agreed

3. ACTION ITEMS TABLE
   Format: | Task | Owner | Deadline | Priority (High/Med/Low) |
   - Extract EVERY action item mentioned
   - If no deadline was stated, suggest a reasonable one
   - If no owner was assigned, flag it as "NEEDS OWNER"

4. OPEN QUESTIONS
   - Anything that was raised but not resolved
   - Anything that needs follow-up

5. NEXT MEETING
   - Suggested agenda items based on open items
   - Recommended date if discussed

Keep it professional, concise, and action-oriented.
```

---

**NOW DEMONSTRATE IT — Fill in the template with this real example:**

MEETING DETAILS:
- Meeting name: Q1 Marketing Planning
- Date: 15th January 2025
- Attendees: Lisa (Marketing Manager), Tom (Content Lead), Priya (Social Media), Jamie (Designer)
- Duration: 45 minutes
- Meeting purpose: Plan marketing activities for Q1

RAW NOTES:
"Lisa opened saying we need to focus on 3 channels this quarter — email, LinkedIn, and the blog. Tom said the blog has been getting good traffic and we should aim for 2 posts per week instead of 1. Priya asked who would write the extra posts — Tom said he'd do one if Priya handled social promotion. Jamie mentioned the website banner needs updating, it still shows Christmas stuff. Lisa agreed and said Jamie should do it by end of this week.

Big discussion about the email newsletter — open rates dropped to 15%. Priya suggested we A/B test subject lines. Lisa loved it, said let's start with the February newsletter. Tom volunteered to write 3 versions to test. Nobody brought up the budget yet — Lisa said she'll send it around by Friday and we can discuss async.

Priya asked about the product launch in March — needs assets 3 weeks early. Jamie said that's tight but doable if he gets the brief by Feb 1st. Lisa will send the brief. Quick chat about team social event — maybe bowling? No decision made, Priya will poll the team.

Lisa: let's meet again in 2 weeks to check progress."

Transform these notes using the template above.''',
    },
]
