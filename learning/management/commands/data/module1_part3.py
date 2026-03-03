"""
Module 1 Part 3: Real-World Power — "AI at Work and Life"
Challenges 17-24: Professional and personal applications of prompt engineering (4-5 hours)
"""

MODULE1_PART3_CHALLENGES = [
    {
        'title': 'Question 17: The Email Wizard',
        'description': 'Master professional email writing for any situation',
        'difficulty': 'intermediate',
        'order': 17,
        'points': 35,
        'instructions': '''Email is still the #1 professional communication tool. AI can make you brilliant at it.

**What You'll Learn:**
- How to get AI to draft emails that match the right tone for any situation
- Adapting email style based on the relationship and context
- Handling tricky email situations (complaints, negotiations, awkward requests)

**The Reality:**
Most people spend 2+ hours a day on email. With the right prompts, AI can draft emails in seconds that would take you 20 minutes — and often better than what you'd write under pressure.

**Your Challenge:**
Draft a **tricky professional email** that requires careful tone management. Pick one of these scenarios:

1. **Following up after being ghosted** — You had a great interview 2 weeks ago, they said they'd get back in a week, and you've heard nothing.
2. **Pushing back on a deadline** — Your manager asked for a report by Friday but you realistically need until next Wednesday.
3. **Asking for a raise** — You've been in your role for a year, taken on extra responsibilities, and want to discuss compensation.
4. **Apologising professionally** — You missed an important deadline and need to address it with a client.

**Your prompt must include:**
- The full context (who you're emailing, your relationship, the situation)
- The tone you need (this is the hard part — these are all delicate situations!)
- What you want to achieve (the email's goal)
- Any specific things to include or avoid
- Length constraint

**Why This Matters:**
The difference between a good and bad email in these situations can affect your career, relationships, and reputation. AI helps you write when emotions might cloud your judgement.''',
        'example_prompt': '''I need to write a delicate email. Here's the situation:

**SCENARIO:** I had a fantastic job interview 2 weeks ago. The hiring manager (Rachel) said she'd let me know within a week. It's now been 2 weeks and I've heard nothing. I want to follow up without seeming desperate.

**CONTEXT:**
- Company: A design agency I really want to work at
- The interview: 45 minutes, we had great chemistry, she showed me around the office
- Rachel's last words: "We'll be in touch by end of next week!"
- I've already waited an extra week beyond her timeline
- I have another offer with a deadline in 5 days (this is true, not a bluff)
- I genuinely prefer this company over the other offer

**THE EMAIL MUST:**
- Sound confident and professional, NOT desperate or passive-aggressive
- Reiterate my interest without gushing
- Mention the other offer tactfully (as a genuine time constraint, not a threat)
- Give her a specific timeline (I need to respond to the other offer by Friday)
- Be warm — reference something specific from our conversation to remind her why I'm a good fit
- Leave the door open even if the timing doesn't work out

**THE EMAIL MUST NOT:**
- Start with "Just checking in" or "Just following up" (these sound weak)
- Sound like a ultimatum
- Be longer than 150 words
- Use corporate jargon or sound like a template
- Seem like I'm complaining about the delay

**TONE:** Confident, warm, professional. Like someone who knows their worth but is also genuinely nice.

Draft the email with a subject line.''',
    },
    {
        'title': 'Question 18: Meeting Notes to Action Plans',
        'description': 'Transform chaotic meeting notes into clear, actionable summaries',
        'difficulty': 'intermediate',
        'order': 18,
        'points': 35,
        'instructions': '''Meetings generate ideas. Prompt engineering turns those ideas into action.

**What You'll Learn:**
- How to use AI to extract structure from unstructured information
- Turning vague discussions into specific action items
- A skill every manager and team member needs

**The Problem:**
After most meetings, people walk away with different ideas about what was decided and who's doing what. Sound familiar? AI can solve this by turning messy notes into crystal-clear action plans.

**Your Challenge:**
You just came out of a team meeting and have rough, messy notes. Transform them into a professional summary with clear action items.

**What to include in your prompt:**
1. The raw meeting notes (make them realistic — incomplete sentences, tangents, side conversations)
2. Meeting context (who was there, what it was about)
3. Specific output format you want (summary, decisions, action items with owners and deadlines)
4. Instructions for handling ambiguity (e.g., "If no deadline was mentioned, suggest one")

**Make the notes REALISTIC** — real meeting notes aren't neat. They're messy, have tangents, missing context, and half-finished thoughts. The messier they are, the more impressive the AI transformation.

**Real-World Value:**
This is one of the most immediately useful prompt engineering skills. You can use this after every meeting starting today.''',
        'example_prompt': '''I just left a team meeting and my notes are a mess. Transform them into something I can send to the whole team.

**MEETING DETAILS:**
- Meeting: Weekly product team sync
- Date: Tuesday, 21st January 2025
- Attendees: Sam (Product Manager), Nina (Designer), Chris (Developer), Me (Marketing)
- Duration: 35 minutes (was supposed to be 30!)

**MY MESSY NOTES:**
"Sam started with app launch update — we're aiming for March 15th but Chris says maybe push to March 22nd because of the payment integration bug. Sam not happy but agreed if Chris confirms by Friday whether the bug is fixable this sprint.

Nina showed new onboarding screens — everyone loved them. But Chris pointed out the animation might be slow on older phones. Nina will test on her old phone this week. If it's laggy she'll simplify the animation.

I brought up the launch marketing plan — need final app screenshots from Nina by Feb 1st for the press kit. Sam wants a landing page live by Feb 15th. I said I need Chris to add the email signup form first. Chris said he can do it next week if I send him the design. I haven't made the design yet... need to do that.

Side conversation about the team offsite — Sam suggested escape rooms, Nina wants bowling. Nobody decided. Sam said he'll send a poll.

Budget discussion — Sam mentioned we got approval for £2,000 marketing budget for launch. I need to propose how to spend it by next meeting. Sam also said we should think about influencer partnerships — maybe reach out to 3-5 tech reviewers?

Oh and Chris mentioned he's on holiday the first week of March. That's right before launch... Sam said we need to make sure everything is code-complete by Feb 28th then.

Nina asked about app store listing — who's writing the description? I volunteered. Sam wants a first draft by Feb 10th.

Next meeting: same time next Tuesday."

**TRANSFORM THIS INTO:**

1. **Meeting Summary** (3-4 sentences — what was this meeting actually about?)

2. **Key Decisions Made** (list each decision clearly)

3. **Action Items Table:**
   | Task | Owner | Deadline | Priority |
   - Extract every single action item from the notes
   - If a deadline wasn't specified, suggest a reasonable one based on context
   - Flag anything that's BLOCKING someone else

4. **Risks & Dependencies**
   - What could go wrong?
   - What's dependent on what?

5. **Next Meeting Agenda** (what should we cover next Tuesday?)

Make it professional enough to share in Slack but concise enough that people actually read it.''',
    },
    {
        'title': 'Question 19: Research Like a Pro',
        'description': 'Use AI to research topics thoroughly and get structured, actionable insights',
        'difficulty': 'advanced',
        'order': 19,
        'points': 40,
        'instructions': '''AI is an incredible research partner when you ask the right questions.

**What You'll Learn:**
- How to structure research requests for comprehensive results
- Getting balanced analysis (not just one-sided cheerleading)
- Turning research into an actionable decision

**The Key:**
Most people ask AI "tell me about X." That's like going to a library and saying "give me books." Instead, tell AI exactly what you need to know, why, and how to structure the findings.

**Your Challenge:**
You're considering a major life decision: **starting a business vs staying employed.** You need thorough research to make an informed decision.

**Your prompt must include:**
1. Your specific situation (don't make AI guess)
2. What research areas you need covered (at least 4 sections)
3. A request for HONEST analysis (pros AND cons, not just encouragement)
4. A request for a specific action plan based on the research
5. How you want the output formatted

**Ask AI to be realistic.** The value of good research is honesty, not hype.''',
        'example_prompt': '''I'm seriously considering leaving my job to start my own business. I need thorough research to make a smart decision — not just encouragement.

**MY SITUATION:**
- Current: Office administrator at a medium-sized accounting firm, 5 years experience
- Age: 31, living with partner (they have a stable income), no kids
- Location: Leeds, UK
- Savings: About £15,000
- Business idea: Starting a virtual assistant / admin support service for small businesses
- What I like about my job: Stability, decent colleagues, predictable income
- What I don't like: Boredom, no growth, feeling like I'm building someone else's dream
- Skills: Organisation, spreadsheets, email management, diary management, basic bookkeeping, customer service
- I've been doing freelance VA work on weekends for 3 months and have 2 regular clients already

**RESEARCH I NEED:**

**1. Reality Check (Is this viable?)**
- How realistic is it to replace my salary with a VA business?
- What does the UK market look like for virtual assistants?
- What's the typical timeline from launch to full-time income?
- What do successful VA businesses actually look like after 1-2 years?

**2. Financial Analysis (Can I afford to do this?)**
- What are the startup costs for a VA business? (Be specific)
- How long should I expect before I'm earning consistently?
- Should I save more before leaving, or is £15,000 enough of a runway?
- What's the realistic income progression (month 1, 3, 6, 12)?

**3. Risk Assessment (What could go wrong?)**
- Top 5 risks of leaving employment to start this business
- For each risk: how likely is it, and what's the mitigation plan?
- What would "failing" look like, and could I recover?
- At what point should I go back to employment if it's not working?

**4. Starting While Employed vs Quitting First**
- Pros and cons of each approach for MY situation
- Could I realistically grow this while still working full-time?
- What's the tipping point where I should make the jump?

**5. Honest Recommendation**
Based on ALL of the above:
- Given my specific situation, should I start this business?
- What should I do in the next 60 days before making a final decision?
- What's the one thing that would make or break this plan?

**FORMAT:**
- Use clear headers for each section
- Include specific numbers where possible (costs, timelines, income ranges)
- Be direct — I want the honest truth, not a motivational speech
- End with a clear "Next 60 Days" action plan

This is a big decision. Help me make it with open eyes.''',
    },
    {
        'title': 'Question 20: Content Creator\'s Toolkit',
        'description': 'Generate a complete content plan with posts, ideas, and scheduling',
        'difficulty': 'advanced',
        'order': 20,
        'points': 35,
        'instructions': '''Content creation is one of the most popular real-world uses of AI. Let's master it.

**What You'll Learn:**
- How to use AI as a content planning partner
- Creating consistent content across platforms
- Maintaining a brand voice while scaling output

**The Reality:**
Small businesses, freelancers, and side hustlers spend hours every week creating content. With the right prompts, you can plan a full week of content in minutes.

**Your Challenge:**
Create a **complete 1-week social media content plan** (Monday to Sunday) for a real or fictional brand.

**Your prompt must include:**
1. Brand details (what it is, who it's for, the brand voice)
2. Which platforms you're posting on
3. Content goals (awareness? engagement? sales?)
4. Content pillars or themes to rotate through
5. Specific post requirements (copy, hashtags, posting times, content type)

**IMPORTANT:** Make sure your plan covers every day from **Monday through to Sunday** — a full 7-day week.

**Make it actionable** — someone should be able to take your output and schedule all the posts immediately, without any additional thinking.

**Bonus points for:**
- Including different content types (educational, entertaining, promotional, behind-the-scenes)
- Requesting specific hashtag strategies
- Asking for content that builds on itself through the week''',
        'example_prompt': '''Create a complete 1-week social media content plan for my business. I need posts for EVERY day from Monday to Sunday.

**THE BRAND:**
- Business: "FitKit" — a small UK business selling at-home workout equipment (resistance bands, yoga mats, dumbbells)
- Target audience: Women aged 25-40 who want to work out at home, busy with work/kids, not gym-goers
- Brand voice: Motivating but real (not "CRUSH IT!" — more like "you've got 20 minutes? That's enough.")
- What makes us different: Affordable, no-nonsense equipment. We don't sell the dream body, we sell the habit.
- Current following: 2,400 on Instagram, 800 on TikTok (still growing)

**PLATFORMS:** Instagram (feed + Stories) and TikTok

**CONTENT GOALS THIS WEEK:**
- Primary: Engagement (comments, saves, shares)
- Secondary: Drive traffic to our website (we have a January sale ending Sunday)

**CONTENT PILLARS (rotate through these):**
1. Quick workout tips (educational)
2. Customer stories/transformations (social proof)
3. Behind-the-scenes (building connection)
4. Product showcases (promotional — but soft sell)
5. Motivation/mindset (but REAL, not cheesy)

**CREATE FOR EACH DAY (Monday through Sunday — all 7 days):**

For each day, provide:
- **Platform:** Instagram, TikTok, or both
- **Content type:** Reel, carousel, static post, Story, or TikTok
- **Caption:** Full written caption (not just "write something about X" — give me the actual words!)
- **Visual description:** What the image/video should look like (I'll create it)
- **Hashtags:** 5-8 relevant hashtags per post (mix of popular and niche)
- **Best time to post:** Specific time and why
- **CTA:** What action we want people to take

**RULES:**
- Only 2 out of 7 posts should be directly promotional (the rest should provide value)
- At least one post should reference the January sale (ending Sunday)
- Captions should be under 150 words each
- Include at least 2 posts that encourage saves or shares (algorithm boost)
- One post should be designed to go viral (controversial take, relatable truth, or trend)
- No generic motivational quotes — everything should be specific to at-home fitness
- Cover ALL 7 days — Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, AND Sunday

Make it ready to execute. I want to schedule everything in one sitting.''',
    },
    {
        'title': 'Question 21: Data Storytelling',
        'description': 'Turn raw numbers into compelling narratives that drive decisions',
        'difficulty': 'advanced',
        'order': 21,
        'points': 40,
        'instructions': '''Numbers don't speak for themselves. Your job is to make them tell a story.

**What You'll Learn:**
- How to use AI to interpret and narrate data
- Turning raw numbers into insights that drive action
- Presenting data to non-technical audiences

**The Problem:**
"Sales were £45,000 this quarter" means nothing without context. Is that good? Bad? Getting better? Worse than competitors? Data storytelling adds that context.

**Your Challenge:**
You have raw data (numbers, survey results, or metrics) and need to transform it into a compelling **monthly business performance report for your boss.**

**Your prompt must include:**
1. The raw data (actual numbers — make them up if needed, but make them realistic)
2. Who will read this (their role and what they care about)
3. What story you want the data to tell (or ask AI to find the story)
4. The format you need (executive summary, presentation slides, email)
5. What decisions should result from this data

**The key: data without context is just noise. Data with a story drives action.**''',
        'example_prompt': '''I need to turn this raw data into a compelling monthly business performance report for my boss. She's not technical — she cares about "what does this mean and what should we do?"

**THE RAW DATA — Our Online Shop Performance (October vs September):**

- Website visitors: 12,400 (Sept) → 18,600 (Oct)
- Conversion rate: 3.2% (Sept) → 2.1% (Oct)
- Total orders: 397 (Sept) → 391 (Oct)
- Average order value: £42 (Sept) → £38 (Oct)
- Revenue: £16,674 (Sept) → £14,858 (Oct)
- Email subscribers: +340 (Sept) → +890 (Oct)
- Top traffic source change: Instagram went from 15% to 35% of traffic
- Return rate: 5% (Sept) → 12% (Oct)
- Customer reviews: 4.6 stars (Sept) → 4.2 stars (Oct)
- Best seller: Product A still #1, but Product C jumped from #8 to #2
- Cart abandonment: 65% (Sept) → 78% (Oct)

**AUDIENCE:** My boss (Marketing Director). She has a meeting with the CEO tomorrow and needs to explain our numbers.

**WHAT SHE NEEDS TO KNOW:**
1. Are we doing well or not? (The numbers tell a mixed story)
2. What's actually happening? (What's the underlying story?)
3. What should we do about it?

**CREATE THIS REPORT:**

**1. Executive Summary (3-4 sentences)**
- The headline: what's the most important thing to know?
- Is this good news, bad news, or mixed?

**2. The Good News**
- What's going well? Use the data to support it.
- Make it specific (not just "traffic is up" — explain WHY it matters)

**3. The Warning Signs**
- What's concerning? Connect the dots between different metrics.
- Don't just list problems — explain what they might mean

**4. The Story (What's Actually Happening)**
- Help me see the PATTERN in this data
- Why might traffic be up but revenue down?
- What does the Instagram traffic shift + lower conversion suggest?

**5. Recommended Actions (Top 3)**
- What should we do THIS WEEK?
- What should we investigate further?
- What should we change for next month?

**TONE:** Professional but accessible. Use the actual numbers but explain them like you're talking to a smart person who isn't a data analyst. No jargon.

**LENGTH:** Fits on one page. Use bullet points, bold key numbers, make it scannable.''',
    },
    {
        'title': 'Question 22: Problem-Solving Partner',
        'description': 'Use AI to systematically diagnose and solve complex problems',
        'difficulty': 'advanced',
        'order': 22,
        'points': 40,
        'instructions': '''AI isn't just for writing — it's a powerful thinking partner for solving real problems.

**What You'll Learn:**
- How to present a problem to AI for systematic analysis
- Using structured frameworks for problem-solving
- Getting AI to think critically, not just optimistically

**The Technique:**
Instead of asking "what should I do about X?", give AI a structured framework to follow. This forces deeper analysis and produces more actionable solutions.

**Your Challenge:**
You have a real problem that needs diagnosing and solving. Present it to AI with enough context and ask for systematic analysis.

**Pick a scenario:**
- Your small business sales have dropped significantly
- Your team's productivity has fallen and morale is low
- A project is behind schedule and over budget
- Your marketing campaigns aren't converting
- Your customer satisfaction scores have declined

**Your prompt must include:**
1. Clear problem statement with data/evidence
2. Context (when it started, what's changed, what you've noticed)
3. A specific problem-solving framework for AI to follow
4. A request for both diagnosis AND solutions
5. Prioritised action plan at the end

**Ask AI to be thorough** — surface-level advice like "try harder" isn't useful. You want root cause analysis.''',
        'example_prompt': '''I run a small online shop selling handmade candles and I have a serious problem. Help me diagnose it and figure out what to do.

**THE PROBLEM:**
Sales dropped 40% over the last 2 months (from about £6,000/month to £3,500/month).

**WHAT I KNOW:**
- Website traffic is actually UP 25% (so people ARE coming to the site)
- Social media engagement seems normal — likes, comments, shares are steady
- Email open rates haven't changed (22%, which is decent)
- Cart abandonment rate jumped from 55% to 82% (people add to cart but don't buy)
- I haven't changed my prices
- I haven't changed my products
- Customer complaints: Only 2, both about slow delivery (carrier issue, now resolved)
- A competitor launched a similar product line 6 weeks ago at 20% lower prices
- I recently redesigned my checkout page (4 weeks ago) — made it "cleaner"
- Returning customers are buying less frequently too (used to be every 6 weeks, now every 10+)

**ANALYSE THIS USING THIS FRAMEWORK:**

**Step 1 — Define the Real Problem:**
- What's the CORE issue here? (Not just "sales are down" — go deeper)
- What are symptoms vs root causes?

**Step 2 — Analyse the Data:**
- What story do these numbers tell when you connect the dots?
- What's the most important metric to focus on and why?
- What data am I MISSING that I should collect?

**Step 3 — Generate Hypotheses:**
- List 5 possible causes for the sales drop, ranked by likelihood
- For each, explain your reasoning using my data

**Step 4 — Test the Hypotheses:**
- For the top 3 most likely causes, how can I test whether each is actually the problem?
- What would I see if that hypothesis is correct?

**Step 5 — Solutions:**
- For each likely cause, give me 2-3 specific solutions
- Separate into: Quick wins (this week) vs Medium-term fixes (this month) vs Long-term strategy

**Step 6 — Action Plan:**
- What should I do TOMORROW? (The single most impactful action)
- What should I do this week? (Top 3 priorities)
- How will I know if my fixes are working? (What metrics to watch)

Be analytical and thorough. I need to understand WHY this is happening before I can fix it.''',
    },
    {
        'title': 'Question 23: Learning Accelerator',
        'description': 'Get AI to design a complete, personalised learning plan for any skill',
        'difficulty': 'intermediate',
        'order': 23,
        'points': 35,
        'instructions': '''AI can be the best personal tutor you've ever had — if you prompt it right.

**What You'll Learn:**
- How to get AI to create structured, personalised learning paths
- Including resources, projects, and milestones in learning plans
- Making self-directed learning actually stick

**Why This Works:**
Generic learning advice is everywhere. "Learn Python" has a million results on Google. But a personalised plan that accounts for YOUR schedule, YOUR learning style, and YOUR goals? That's rare and valuable.

**Your Challenge:**
Pick a skill you genuinely want to learn and get AI to create a **complete 4-week learning plan.**

**Ideas (pick anything!):**
- Public speaking or presentation skills
- A new language (basics)
- Excel or Google Sheets (intermediate level)
- Basic video editing
- Writing (blogging, copywriting, creative)
- Cooking a specific cuisine
- Personal finance and investing basics
- Graphic design fundamentals

**Your prompt must include:**
1. The skill and your specific goal (not just "learn cooking" — "be able to cook 10 impressive dinners for date night")
2. Your current level (total beginner? some knowledge?)
3. Your available time and preferred learning format
4. Constraints (budget, tools you have, scheduling)
5. How you want the plan structured (daily? weekly? milestone-based?)
6. A request for specific resources, practice tasks, and a way to measure progress

**Make it something you'd actually follow!**''',
        'example_prompt': '''I want to learn public speaking — I'm terrified of it but I need it for my career. Create a complete 4-week plan.

**MY SITUATION:**
- Current level: I freeze up when speaking in front of more than 3 people. My voice shakes, I talk too fast, and I forget what I was saying.
- Why I need this: I was just promoted to team lead and now have to present at weekly team meetings (10 people) and monthly department updates (30 people).
- First big presentation: 5 weeks from now (department update, 10-minute presentation)
- Available time: 30-45 minutes per day (evenings) + I can practice during my commute (30 min each way)
- Budget: Under £20 total
- What I do have: My phone (for recording practice), a mirror, and a supportive partner who'll be my practice audience

**MY SPECIFIC GOAL:**
In 4 weeks, I want to be able to give a 10-minute presentation to 30 people without:
- Freezing up or going blank
- Rushing through it at double speed
- Avoiding eye contact the entire time
- Reading every word from my notes

I don't need to be a TED Talk speaker. I just need to be calm, clear, and competent.

**CREATE MY 4-WEEK PLAN:**

**For each week, include:**
- **Theme:** What this week focuses on
- **Daily tasks** (Monday-Friday, 30-45 min each):
  - What to learn (specific technique or concept)
  - A practice exercise (specific, not vague — tell me exactly what to do)
  - A mini-challenge to push my comfort zone slightly
- **Weekend task:** A bigger practice session (1 hour)
- **Week milestone:** How I know I've progressed (specific measurable thing)

**ALSO INCLUDE:**
- 3-5 free resources (YouTube videos, articles, podcasts) — specific ones, not just "search YouTube"
- Quick techniques for managing nerves (that actually work, not just "breathe deeply")
- How to structure my 10-minute department presentation (a template I can fill in)
- What to do if I freeze during the actual presentation (a recovery plan)

**APPROACH:**
- Start very small (talking to myself in a mirror) and gradually build
- Make it feel achievable — I'm genuinely scared, so don't throw me into deep end on day 1
- Include some fun elements so it's not pure anxiety training
- Build real skills, not just confidence tricks

Remember: I'm not trying to become a professional speaker. I just need to stop being terrified and start being competent.''',
    },
    {
        'title': 'Question 24: The Negotiation Coach',
        'description': 'Prepare for any negotiation with scripts, strategies, and practice scenarios',
        'difficulty': 'advanced',
        'order': 24,
        'points': 40,
        'instructions': '''Negotiation is a life skill. AI can help you prepare like a pro.

**What You'll Learn:**
- How to use AI to prepare negotiation strategies
- Getting scripts for difficult conversations
- Practising counterarguments before the real conversation

**Where You'll Use This:**
- Salary negotiations
- Asking for a promotion
- Negotiating a better deal (rent, contracts, services)
- Handling difficult conversations at work
- Freelance rate discussions

**Your Challenge:**
Prepare for a real negotiation or difficult conversation using AI as your strategy coach.

**Your prompt must include:**
1. The full situation (what you're negotiating, with whom, what's at stake)
2. Your goal (what you ideally want, what you'd accept, your walk-away point)
3. The other person's likely perspective (what do THEY want? what are their concerns?)
4. A request for strategy (how to approach it) AND scripts (what to actually say)
5. Common pushbacks and how to handle each one
6. A request for practice scenarios

**Think about it from both sides** — the best negotiations happen when you understand the other person's position, not just your own.''',
        'example_prompt': '''I need to negotiate a salary raise and I'm nervous. Be my negotiation coach.

**THE SITUATION:**
- I've been at my company for 14 months as a Marketing Coordinator
- Current salary: £28,000
- I want to ask for: £33,000 (that's a ~18% raise)
- I'd accept: £31,000 minimum
- Annual review: In 2 weeks (perfect timing)
- My manager: David — fair, busy, doesn't like surprises. We have a good relationship but have never discussed salary.

**WHY I DESERVE A RAISE:**
- I was hired to manage social media only. I now also handle:
  - Email marketing (took it over when the person left, never got a pay bump)
  - Content writing for the blog (2 posts/week)
  - Monthly analytics reporting for the leadership team
- Results:
  - Grew Instagram following from 2,000 to 8,500 in 14 months
  - Email click-through rate improved from 1.8% to 4.2%
  - Blog traffic up 60%
- I haven't missed a deadline in 14 months
- Market rate for my ACTUAL role (Marketing Executive): £30,000-£35,000 in my area

**DAVID'S LIKELY PERSPECTIVE:**
- Budget is probably tight (it's a small company, 25 people)
- He values me — he's said "I don't know what we'd do without you" twice
- He might argue it's "not in the budget" or "let's revisit in 6 months"
- He might offer a small raise (2-3%) and think that's generous
- He doesn't know I've researched market rates

**COACH ME ON:**

**1. Strategy — Before the Meeting:**
- When and how to bring this up (email first? Direct ask in our 1:1?)
- How to frame it (not "I want more money" — what's the right angle?)
- What to prepare and bring to the meeting

**2. The Script — What to Actually Say:**
- Opening line (how to start this conversation naturally)
- My pitch (30 seconds — clear, confident, not apologetic)
- How to state my number (should I say £33K or let him make the first offer?)

**3. Handling Pushback:**
For each common objection, give me a specific response:
- "The budget is tight right now"
- "Let's revisit in 6 months"
- "We can offer 3% — that's what everyone gets"
- "You're already paid fairly for your title"
- "We value you in other ways (culture, flexibility, etc.)"

**4. If They Say No:**
- What to ask for instead (non-salary benefits, title change, development budget?)
- How to leave the conversation on good terms
- When to follow up

**5. Practice Scenario:**
Write a short roleplay dialogue between me and David where he pushes back and I handle it well. Show me what confident-but-respectful sounds like.

Make me feel prepared, not scripted. I want to walk in confident.''',
    },
]
