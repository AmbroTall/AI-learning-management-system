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
You have an important job interview coming up. Give AI your COMPLETE context upfront to get the most personalised interview preparation help possible.

**Your prompt must include:**

**Context section:**
- The role you're applying for (job title, company, industry)
- Your relevant experience and background
- Your key strengths for this role
- Areas you're nervous about or find tricky
- The interview format (panel? one-to-one? competency-based? presentation?)

**Task section:**
- What specific help you need (preparing answers? researching the company? handling tricky questions?)

**Format section:**
- How to organise the response (sections, bullet points, priority order)

**Why This Works:**
When AI has full context from the start, it doesn't waste time on generic advice. Every suggestion is tailored to YOUR situation. This is the difference between "help me prepare for an interview" and "help me prepare for a panel interview for a Marketing Manager role at a sustainability brand, where I'm strong on campaigns but nervous about people-management questions."''',
        'example_prompt': '''I have an important job interview in 3 days and need to prepare thoroughly. Here's my complete situation:

**CONTEXT — About the Role:**
- Job title: Marketing Manager
- Company: A growing e-commerce brand (about 80 staff) that sells sustainable homeware
- What they're looking for: Someone to lead their social media and email marketing, manage a small team of 2, and drive revenue through digital channels
- Why I want this role: It's a step up from my current coordinator role, and I believe strongly in their sustainability mission

**CONTEXT — About Me:**
- Current role: Marketing Coordinator at a fashion retailer (2.5 years)
- Strengths: Very strong on content creation, social media strategy, and campaign management — I led a campaign that grew our Instagram following by 40% in 6 months
- Weaknesses: I haven't formally managed a team before (though I've mentored junior interns)
- Nervous about: Questions about managing people, questions about budget management, and the salary negotiation at the end

**CONTEXT — Interview Format:**
- Two-stage interview: First is a 45-minute panel with the Marketing Director and HR
- They'll use competency-based questions ("tell me about a time when...")
- I'll need to give a 5-minute presentation on "how you would approach your first 90 days in this role"

**TASK — What I Need:**
1. Help me prepare strong answers to the 5 most likely competency questions for this role
2. Structure my 5-minute 90-day plan presentation
3. Prepare me for the "people management" weakness — I need a confident answer that turns this into a positive
4. Suggest 3-4 smart questions I can ask them at the end
5. Advise on how to handle the salary conversation professionally

**FORMAT:**
- Number each section clearly (1–5 matching my requests above)
- For competency answers, use the STAR format (Situation, Task, Action, Result)
- Keep advice practical and specific to this company and role
- For the 90-day plan, give me a clear structure I can build into slides''',
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
Should you leave your job and go freelance, or stay in employment? This is one of the most common career crossroads people face.

**Your prompt must include:**
1. The decision with full context (your situation, financial position, priorities)
2. A request for step-by-step analysis (not just a recommendation)
3. Specific steps you want AI to follow (e.g., "evaluate financial readiness," "assess work-life balance," "consider career growth")
4. Ask AI to give a final recommendation WITH its reasoning

**The result should feel like a thoughtful conversation, not a snap judgement.**''',
        'example_prompt': '''I need help thinking through a big career decision. Don't just tell me what to do — walk me through your thinking step by step.

**THE DECISION:**
Should I leave my full-time job and go freelance as a graphic designer, or stay in my current employment?

**MY SITUATION:**
- Current role: In-house graphic designer at a marketing agency (3 years)
- What I like: Steady income, team environment, benefits (pension, 25 days holiday)
- What I don't like: Limited creative freedom, feel like I'm doing the same type of work repeatedly, no say in which clients we take on
- Freelance idea: I already have 3 regular clients I work with in evenings/weekends, earning about £800/month extra
- Financial situation: 4 months of living expenses saved, rent £700/month, no major debt
- Personal situation: No dependents, renting, flexible lifestyle
- Main goal: More creative control and the ability to choose my projects

**ANALYSE THIS STEP BY STEP:**

**Step 1:** Assess my financial readiness — am I in a safe enough position to go freelance?
**Step 2:** Evaluate my existing freelance foundation — what do my current 3 clients tell us about my potential?
**Step 3:** What are the realistic income scenarios in year 1 of freelancing? (Best case, likely case, worst case)
**Step 4:** How does work-life balance and wellbeing compare between the two options?
**Step 5:** What am I giving up by leaving employment? (Consider benefits, stability, professional development, team connection)
**Step 6:** What do I gain by going freelance that I can't get in my current role?
**Step 7:** What are the biggest risks of making this change, and how can I reduce them?
**Step 8:** Give me your final recommendation with clear reasoning — should I make this move, and if so, when and how?

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
"Write me a cover letter" → generic, forgettable
"Write a 200-word opening paragraph that avoids clichés, opens with a story, uses exactly one specific achievement, and never uses the word 'passionate'" → focused, memorable!

**Types of Constraints You Can Use:**
- **Length:** Exact word count or character limit
- **Style:** Must include/avoid specific words or phrases
- **Structure:** Specific format or sections required
- **Content:** Must reference certain topics, examples, or data
- **Tone:** Specific emotional register
- **Audience:** Who it's for (and who it's NOT for)

**Your Challenge:**
Write the opening section of a **job application cover letter** for a role you'd genuinely want. But here's the key — include **at least 5 specific constraints** that force AI to produce something unique and compelling.

**Minimum constraints to include:**
1. Exact word count range
2. A tone described with 2-3 specific adjectives
3. Something it MUST include (a specific achievement, a number, or a personal connection to the role)
4. Something it must AVOID (clichés, specific overused words, generic phrases)
5. A structural requirement (how it starts, what the final sentence achieves)

**The more creative and specific your constraints, the better the output. Push yourself!**''',
        'example_prompt': '''Write the opening section of a cover letter for a job application.

**About Me and the Role:**
- My name: Alex Sharma
- Role I'm applying for: Social Media Manager at a mental health charity
- My background: 2 years managing social media for a retail brand, grew TikTok from 0 to 22,000 followers in 8 months
- What makes me different: I volunteer at a youth mental health group on weekends — this role genuinely means something to me personally
- Key strength: I create content that feels human, not corporate

**CONSTRAINTS (follow ALL of these):**

1. **Length:** Exactly 150-170 words. Not a word more.
2. **Tone:** Warm, purposeful, and quietly confident — like someone who genuinely cares about the cause, not someone who's just job-hunting.
3. **Must include:**
   - My TikTok achievement (22,000 followers) mentioned naturally, not as a brag
   - A hint at my personal connection to mental health (without oversharing)
   - One sentence that shows I've researched this specific charity
4. **Must avoid:**
   - The words "passionate," "excited," "thrilled," or "opportunity"
   - Starting with "I am writing to apply for..."
   - Any sentence that could work for ANY cover letter (be specific to this role and charity)
5. **Structure:**
   - Open with something that shows you understand what this charity does and why it matters
   - Middle: who I am and why I'm the right fit (lead with the human connection, then the skills)
   - Close with something that invites a conversation, not a generic sign-off
6. **Voice:** First person. Direct. No passive voice.
7. **Feeling:** After reading it, the hiring manager should think "I want to meet this person" — not "this is a well-written letter."

Make every word count.''',
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
Pick any skill you genuinely want to learn and ask for a personalised learning plan that matches your profile.

**Ideas for topics:**
- Public speaking and presenting
- Cooking a specific cuisine
- A new language (Spanish, French, Arabic, etc.)
- Mindfulness and stress management
- Photography and composition
- Personal finance and budgeting
- Fitness and healthy habits

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
- Available time: 1 hour per day (evenings, after work)
- Budget: Up to £30/month for ingredients and basic equipment
- Currently working full-time so I need flexible, manageable sessions
- I have a standard home kitchen with basic equipment

**My Communication Preferences:**
- Be direct — if I'm doing something wrong, tell me immediately
- Use simple language first, introduce technical terms only when necessary (and define them)
- Break big concepts into bite-sized pieces
- Give me honest feedback — I want to genuinely improve, not just feel good

**My Learning Goal:**
I want to learn to cook Japanese food at home — specifically sushi, ramen, and a few popular side dishes. I don't need to become a professional chef — I just want to confidently cook authentic-tasting Japanese meals for friends and family.

---

**PART 2 — Create My Learning Plan:**

Based on my learning profile above (hands-on, 1 hour/day, structured, "why before how"), create a 4-week learning plan for Japanese cooking fundamentals.

**Week-by-week, I need:**
- What to learn each day (specific technique or dish, max 1 hour)
- A daily cooking task (a specific recipe or technique with exact requirements)
- One resource to check out (free YouTube video, article, or technique guide)
- A "mini milestone" at the end of each week (a dish I can cook for someone)

**Requirements:**
- Start with fundamentals (knife skills, rice cooking, basic stocks and sauces)
- Progress toward sushi, ramen, and side dishes by week 4
- Recommend essential Japanese pantry ingredients to buy in week 1
- Include real cooking challenges (e.g., "make a perfect bowl of miso soup from scratch")
- By week 4, I should be able to cook a full Japanese meal for 2 people

Remember my profile: hands-on tasks over theory, explain WHY each technique matters, keep it to 1-hour daily sessions with a clear focus.''',
    },
    {
        'title': 'Question 15: Challenge Your Own Thinking',
        'description': 'Use AI to stress-test your ideas and spot the flaws before they become problems',
        'difficulty': 'advanced',
        'order': 15,
        'points': 35,
        'instructions': '''The most dangerous plans are the ones that only sound good in your head. AI can be your strongest critic.

**What You'll Learn:**
- How to use AI as a "devil's advocate" to find weaknesses in your thinking
- Why challenging your own plans makes them stronger
- How to separate good ideas from ones that just feel good

**The Technique:**
Most people ask AI to SUPPORT their ideas. The smarter move is to ask AI to CHALLENGE them.

Say: "I'm planning to do X. I think it's a good idea because of Y and Z. Now argue against it. Find every flaw, risk, and blind spot."

**When This Is Powerful:**
- Before starting a business or side project
- Before making a big financial decision
- Before committing to a plan at work
- Before having an important conversation you've already mentally "planned out"

**Your Challenge:**
Think of a plan or decision you're genuinely considering (or use the scenario below). Ask AI to be your devil's advocate.

**Your prompt must include:**
1. Your plan or idea, explained clearly
2. The reasons WHY you think it's a good idea (be honest — this is exactly what AI will challenge)
3. A specific instruction to argue against it, find the risks, and challenge your assumptions
4. Ask AI to end with a verdict: is this plan worth pursuing, and what would make it stronger?

**Scenario to use if you don't have your own:**
You want to leave your flat-share and rent your own place for the first time. You think you can afford it and you're ready for the independence.''',
        'example_prompt': '''I have a plan and I want you to challenge it — not support it.

**MY PLAN:**
I want to leave my flat-share (where I currently split costs with 2 housemates) and rent a one-bedroom flat on my own starting next month.

**WHY I THINK IT'S A GOOD IDEA:**
- I earn £2,400/month take-home. A 1-bed flat near me costs around £850/month — that's 35% of my income, which I've read is the "acceptable" limit
- I've been in a flat-share for 3 years and I'm ready for my own space and independence
- I work from home 3 days a week and having a quiet, dedicated workspace would genuinely improve my productivity
- I have £2,000 saved which would cover the deposit and first month's rent
- My lease ends in 8 weeks — the timing feels right

**NOW CHALLENGE THIS:**
Act as a brutally honest financial advisor and life planner. Your job is NOT to encourage me — it's to find every weakness in my reasoning.

Specifically:
1. **Challenge my affordability calculation** — What costs am I not accounting for beyond rent?
2. **Challenge my savings situation** — Is £2,000 really enough of a safety net? What could go wrong?
3. **Challenge my timing** — Is "my lease is ending" actually a good reason to make a major financial decision?
4. **Challenge my "I'm ready" assumption** — What would someone NOT ready for this look like? Do any of those signs apply to me?
5. **Find the emotional reasoning** — Where in my plan am I deciding based on feelings rather than facts?
6. **Worst-case scenarios** — Walk me through 3 realistic things that could go wrong in the first 6 months

**VERDICT:**
After challenging everything, give me your honest verdict: Is this plan solid, risky, or reckless? And what would need to be true for this to be a genuinely good decision?

Be direct. I'd rather hear the hard truth now than learn it the hard way.''',
    },
    {
        'title': 'Question 16: Preparing for Difficult Conversations',
        'description': "Use AI to prepare for conversations you're nervous about — at work or in life",
        'difficulty': 'advanced',
        'order': 16,
        'points': 35,
        'instructions': '''Some of the most important moments in life happen in conversations. AI can help you prepare for them.

**What You'll Learn:**
- How to use AI to plan what to say before a difficult conversation
- How to anticipate what the other person might say — and how to respond
- How to stay calm, clear, and confident when it matters most

**The Reality:**
Most of us go into difficult conversations underprepared. We know what we want to say, but:
- We freeze when challenged
- We haven't thought through how the other person will react
- We say something we regret because we're nervous

AI can help you plan what to say, roleplay the other person's responses, and stress-test your approach before the real thing.

**When This Helps:**
- Asking for a pay rise or better working conditions
- Addressing a conflict with a colleague or friend
- Giving difficult feedback to someone
- Asking for something you feel nervous about requesting

**Your Challenge:**
Prepare for a real (or realistic) difficult conversation using AI.

**Your prompt must include:**
1. The situation — who you're talking to and what the conversation is about
2. What you want to achieve from the conversation
3. What you're nervous about (what might go wrong?)
4. A request for: how to open, what to say, and how to handle pushback
5. Ask AI to show you the other person's likely responses so you can prepare replies

**Use the scenario below, or your own:**
You want to ask your manager if you can work from home one day per week. Your manager generally prefers the team to be in the office.''',
        'example_prompt': '''I need to prepare for an important work conversation. Help me plan what to say and prepare for the responses I might face.

**THE SITUATION:**
I want to ask my manager (David) if I can work from home one day per week — ideally Fridays. Our company doesn't have a formal remote working policy, and David generally prefers the team in the office. He values "team presence" and has mentioned before that he thinks people are more productive face-to-face.

**WHAT I WANT TO ACHIEVE:**
- Get agreement (or at least a trial period) for one day working from home per week
- Keep my relationship with David positive — I don't want this to come across as a complaint
- Understand his concerns so I can address them properly

**WHAT I'M NERVOUS ABOUT:**
- He'll just say "no" without really considering it
- He'll think I'm not committed to the team
- I'll get flustered and back down if he pushes back
- He'll bring up someone else who was refused a similar request

**WHAT I NEED FROM YOU:**

1. **Opening Statement:** Write the first 3-4 sentences I should use to start this conversation — confident, professional, not apologetic

2. **My Case:** Give me 3 strong, specific reasons to present (focused on productivity and results, not "I'd prefer it")

3. **Handling Pushback:** For each of these responses from David, give me a calm, confident reply:
   - "I just think people are more productive when they're in the office"
   - "If I let you do it, everyone will want the same"
   - "I'm not sure it's something we can accommodate right now"
   - "Let's revisit this in 6 months"

4. **A Compromise I Can Offer:** What's a reasonable middle ground if he's reluctant? (e.g., a trial period, checking in more regularly, specific conditions)

5. **Closing the Conversation:** How should I end the conversation — whether he says yes, maybe, or no — while keeping the relationship positive and the door open?

I want to walk into this meeting feeling prepared and calm, not like I'm asking for a favour.''',
    },
]
