"""
Module 1 Part 2: Levelling Up — "Conversations That Work Harder"
Challenges 9-16: Advanced techniques and conversation management (4-5 hours)
"""

MODULE1_PART2_CHALLENGES = [
    {
        'title': 'Building on the Conversation',
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
You want to start a side business but don't know what. Have a **3-message conversation** with AI:

**Message 1:** Share your skills, interests, available time, and budget. Ask for 3-5 side business ideas.
**Message 2:** Pick the most interesting idea. Ask for a detailed breakdown: what it involves, first steps, potential earnings, and biggest challenges.
**Message 3:** Ask for a concrete 2-week action plan to get started.

**Write all 3 messages in your prompt.** Use phrases like "Based on your suggestions..." or "Let's go deeper on idea #2..." to show you're building on context.

**Why This Matters:**
Complex problems need structured conversations. This technique works for business planning, research, creative projects, debugging code — anything that requires going deeper step by step.''',
        'example_prompt': '''I want to brainstorm a side business. Let's work through this step by step.

---

**MESSAGE 1:**
Here's my situation:
- Skills: I'm good at writing, social media, and basic graphic design (Canva)
- Interests: Fitness, cooking, helping small businesses
- Available time: 10-15 hours per week (evenings and weekends)
- Budget to start: £300 maximum
- I have a laptop, phone, and decent internet

Based on this, suggest 5 side business ideas I could realistically start within 2 weeks. For each, give me a one-line description and why it fits my skills.

---

**MESSAGE 2:**
I really like the idea of [pick whichever one resonates — let's say it's social media management for local businesses]. Let's go deeper on this one.

Tell me:
1. What would I actually do day-to-day?
2. How do I find my first 3 clients?
3. What should I charge as a beginner?
4. What tools do I need (free or cheap)?
5. What's the biggest challenge I'll face in the first month?
6. Realistic income after 3 months?

Be honest — I want the real picture, not just the optimistic version.

---

**MESSAGE 3:**
I'm convinced. Let's make this happen.

Create a detailed 2-week action plan:
- **Week 1:** What to set up, learn, and prepare (day by day)
- **Week 2:** How to get my first client (specific outreach steps)

For each day, give me:
- One main task (should take 1-2 hours)
- Why it matters
- What "done" looks like

Make it specific enough that I can just follow the plan without thinking too hard. I want to take action, not just plan forever.''',
    },
    {
        'title': 'The Perfect Briefing',
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
You have a job interview coming up. Give AI your COMPLETE context upfront to get the most personalised interview prep possible.

**Your prompt must include:**

**Context section:**
- Your background (current role, experience, education)
- The job you're interviewing for (title, company, industry)
- Your strengths (what you're confident about)
- Your weaknesses (what worries you about this interview)
- Interview details (format, who you'll meet, when)

**Task section:**
- What specific help you need (practice questions? answers? confidence tips?)

**Format section:**
- How to organise the response (sections, bullet points, priority order)

**Why This Works:**
When AI has full context from the start, it doesn't waste time on generic advice. Every suggestion is tailored to YOUR situation. This is the difference between "prepare for behavioural questions" and "given your transition from teaching to UX design, here's how to frame your classroom experience as user research."''',
        'example_prompt': '''I need help preparing for a job interview. Here's my complete situation:

**CONTEXT — About Me:**
- Currently: Teaching assistant at a primary school (3 years)
- Before that: Worked in retail for 2 years after university
- Education: English Literature degree
- Recently completed: Google UX Design Certificate (online, took 6 months)
- Portfolio: 3 UX case studies (school app redesign, local bakery website, fitness tracker)
- Strongest skills: Communication, understanding user needs (from working with kids and customers), writing, research
- Weakest areas: Never used Figma professionally, no experience with dev handoff, never done a design sprint

**CONTEXT — The Interview:**
- Role: Junior UX Designer at a digital agency (they build websites and apps for clients)
- Company size: 30 people, creative culture, work with clients like restaurants and charities
- Interview format: 30-min call with the Head of Design + a portfolio review
- Interview is in 5 days
- Job posting mentioned: "We value empathy, curiosity, and someone who asks great questions"

**TASK — What I Need:**
1. Top 5 questions they're likely to ask (with suggested answer structures using MY background)
2. How to explain my career change as a strength, not a weakness
3. How to present my case studies confidently (they're student projects, not real client work)
4. 3 great questions I should ask them (that show I'm thoughtful)
5. One-day interview prep schedule I can follow for the next 5 days

**FORMAT:**
- Use clear numbered sections matching my 5 requests
- For interview questions, give me the question AND a bullet-point answer framework (not full scripts — I want to sound natural)
- Keep the prep schedule actionable (specific tasks, not vague "review your portfolio")''',
    },
    {
        'title': 'Role Play for Expert Advice',
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
Pick ONE expert role and get personalised advice:
- A career coach helping you plan your next career move
- A personal finance advisor helping you budget and save
- A fitness coach designing a realistic workout plan
- A life coach helping you set and achieve goals
- A public speaking coach helping you prepare for a presentation

**Make the role detailed!** Don't just say "act as a coach." Give them a background, a communication style, and expertise that matches what you need.

**Why This Matters:**
In real life, expert advice costs hundreds per hour. With the right prompt, you can get thoughtful, personalised guidance. The better you define the role, the better the advice.''',
        'example_prompt': '''I need help getting my finances in order. Please take on this role:

**YOUR ROLE:**
You are a friendly, no-nonsense personal finance coach who:
- Has helped hundreds of young professionals go from "where does my money go?" to having a clear financial plan
- Specialises in helping people in their 20s-30s who earn a decent salary but never seem to save
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

As my finance coach, give me:

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
        'title': 'Think Step-by-Step',
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

**Pick a decision:**
- Should I go back to university or do a bootcamp?
- Should I accept this job offer or stay in my current role?
- Should I move to a new city or stay where I am?
- Should I start freelancing or stay employed?

**Your prompt must include:**
1. The decision with full context (both options, your priorities)
2. A request for step-by-step analysis (not just a recommendation)
3. Specific steps you want AI to follow (e.g., "evaluate against each priority," "consider 1-year and 5-year impact")
4. Ask AI to give a final recommendation WITH its reasoning

**The result should feel like a thoughtful conversation, not a snap judgement.**''',
        'example_prompt': '''I need help making a big career decision. Don't just tell me what to do — walk me through your thinking step by step.

**THE DECISION:**
I've been offered a new job but I'm unsure whether to take it or stay where I am.

**Option A — Stay at current job (Marketing Assistant, small agency):**
- Salary: £28,000
- Been here 2 years, comfortable and liked by the team
- Learning has slowed down — doing the same tasks every week
- 10-minute walk from home
- Good work-life balance, leave by 5:30pm
- No clear promotion path (it's a 6-person company)
- Boss is lovely but the company isn't growing

**Option B — New job offer (Marketing Executive, mid-size tech company):**
- Salary: £35,000 (25% raise)
- Bigger team (20 in marketing), more structured career path
- Would learn SEO, paid ads, and data analytics (skills I don't have yet)
- 45-minute commute by train
- Fast-paced environment, might mean longer hours
- 3-month probation period
- Company is growing quickly, potential to move up

**MY PRIORITIES (ranked):**
1. Career growth and learning new skills
2. Financial stability
3. Work-life balance
4. Job security
5. Enjoying my day-to-day work

**ANALYSE THIS STEP BY STEP:**

**Step 1:** Evaluate each option against each of my 5 priorities (which option wins on each?)
**Step 2:** Identify what I'd be giving up with each choice (trade-offs)
**Step 3:** Consider the 1-year impact (where would I be in 12 months with each option?)
**Step 4:** Consider the 3-year impact (which option puts me in a better position long-term?)
**Step 5:** Factor in risk (what's the worst that could happen with each choice?)
**Step 6:** Give me your final recommendation with clear reasoning

Show your working at every step. I want to understand HOW you reached your conclusion, not just what it is.''',
    },
    {
        'title': 'Constraints Unlock Creativity',
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
        'title': 'Your AI Learning Coach',
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
- Photography
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
- Short sessions work better for me (30-45 minutes max before I lose focus)
- I need to understand the "why" before the "how" (don't just tell me steps — tell me why each step matters)
- Real-world examples stick much better than abstract theory
- I love analogies — connecting new concepts to things I already know

**My Constraints:**
- Available time: 1 hour per day (mornings, 7-8am before work)
- Budget: Free or under £15/month for tools/resources
- Currently working full-time so no courses that require daytime attendance
- I learn on my laptop (no tablet or special equipment)

**My Communication Preferences:**
- Be direct — if I'm wrong or heading in the wrong direction, tell me immediately
- Use simple language first, introduce jargon only when necessary (and define it)
- Break big concepts into bite-sized pieces
- Celebrate progress but don't over-praise — I want honest feedback

**My Learning Goal:**
I want to learn basic photography so I can take good photos for social media (for a small business I'm starting). I don't want to become a professional photographer — I just want my product photos and behind-the-scenes content to look polished and not "amateur."

---

**PART 2 — Create My Learning Plan:**

Based on my learning profile above (hands-on, 1 hour/day, budget-friendly, "why before how"), create a 3-week learning plan for smartphone photography.

**Week-by-week, I need:**
- What to learn each day (specific topic, max 30 min of learning)
- A daily practice task (specific photo to take with exact requirements)
- One resource to check out (free YouTube video, article, or app)
- A "mini milestone" at the end of each week (something I can share to see my progress)

**Requirements:**
- Use only a smartphone (no fancy camera)
- Focus on: lighting, composition, and editing
- Include product photography tips (I'll be photographing handmade candles)
- Recommend 1-2 free editing apps
- By week 3, I should be able to take a product photo that looks professional enough for Instagram

Remember my profile: hands-on tasks over theory, explain WHY each technique works, keep it to 1-hour daily sessions.''',
    },
    {
        'title': 'When to Start Fresh vs Continue',
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

**Scenario B:** You asked AI to review your CV and got great feedback. Now you want to implement those changes and get a second review of the updated version.

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

**SCENARIO B: CV feedback → Updated CV review**

**Decision: CONTINUE**

**Why:** This is iterative work on the SAME document. AI needs to remember what feedback it gave me so it can check whether I implemented it correctly. Starting fresh would mean re-explaining all the context and losing the specific suggestions it made.

**Follow-up Prompt (in same conversation):**
I've implemented your feedback on my CV! Here's what I changed:

- Rewrote all bullet points to start with strong action verbs ✅
- Added specific metrics to 4 achievements (revenue, percentage improvements, team sizes) ✅
- Removed the "Objective" section as you suggested ✅
- Condensed from 2 pages to 1 page ✅
- Reorganised skills section by category ✅

**Still working on:**
- The "Professional Summary" at the top — I couldn't get it right

Here's my updated CV: [paste updated CV]

Please review it again and:
1. Rate my changes (did I implement your feedback well?)
2. Help me write the Professional Summary (3 lines max, punchy, highlights my unique value)
3. Any final tweaks before I start applying?

Be as critical as last time — I want this to be strong before I send it out.''',
    },
    {
        'title': 'Prompt Templates That Save Time',
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
