"""
Module 1 Part 1: Foundations — "Your AI Superpowers"
Challenges 1-8: Core prompt engineering skills through fun, real-world scenarios (3-4 hours)
"""

MODULE1_PART1_CHALLENGES = [
    {
        'title': 'Question 1: Your First AI Conversation',
        'description': 'Learn the basics of talking to AI and getting useful responses',
        'difficulty': 'beginner',
        'order': 1,
        'points': 10,
        'instructions': '''Welcome to AI Prompt Engineering! Let's start with your very first conversation.

**What You'll Learn:**
- How to talk to AI naturally
- Why clear communication matters
- How to get useful, actionable responses

**Your Challenge:**
You're planning a weekend trip and need AI's help. Ask AI to help you plan a 2-day weekend getaway.

**What to include in your prompt:**
1. Where you want to go (pick a real city or region!)
2. Your budget
3. What kind of activities you enjoy
4. Any constraints (travelling solo? with family? dietary needs?)

**Why This Matters:**
This is exactly how people use AI in real life — to plan, brainstorm, and get personalised advice. The better you communicate what you want, the more useful the response.

**Tips for Success:**
- Write naturally, like you're asking a knowledgeable friend
- Include enough detail so AI understands YOUR situation
- Don't be afraid to be specific — "I like hiking" is good, "I like easy coastal hikes with ocean views" is better!''',
        'example_prompt': '''I'm planning a weekend trip to Brighton for 2 days next month. My budget is around £200 for activities and food (accommodation is sorted).

I enjoy:
- Walking along the coast and easy hikes
- Trying local food spots (I'm vegetarian)
- Quirky independent shops and markets
- Live music or comedy if anything's on

I'll be going with a friend who's never been to Brighton before.

Can you plan out a fun 2-day itinerary? Include specific places to eat and things to do, with rough timing so we make the most of it.''',
    },
    {
        'title': 'Question 2: Be Specific, Get Better Results',
        'description': 'Discover why vague prompts get vague answers — and how to fix that',
        'difficulty': 'beginner',
        'order': 2,
        'points': 15,
        'instructions': '''The #1 rule of prompt engineering: **Specificity is your superpower.**

**What You'll Learn:**
- The difference between a vague and a specific prompt
- How to add the right details without overloading
- Why specific prompts save you time (fewer back-and-forths!)

**The Problem:**
Compare these two prompts:
- Vague: "Help me write a birthday speech"
- Specific: Includes who the speech is for, your relationship, key memories, the tone, and the length

The vague version gives a generic template. The specific version gives something heartfelt and personal.

**Your Challenge:**
Get AI to write a personalised birthday speech or toast for someone you care about (real or imagined).

**Your prompt MUST include:**
1. Who the speech is for and your relationship with them
2. The occasion (milestone birthday? surprise party? intimate dinner?)
3. 2-3 specific memories or inside jokes to reference
4. The tone you want (funny? heartfelt? a mix?)
5. Any specific things to mention or avoid
6. Length preference

**Pro Tip:**
Think of it like ordering food. "Give me something good" vs "I'd like a medium veggie pizza with extra mushrooms, light on the cheese" — which one gets you what you actually want?''',
        'example_prompt': '''Write a birthday speech for me to give at my best friend Sam's 30th birthday party.

**About Sam and our friendship:**
- We've been best friends since university (met in freshers' week when we both got lost looking for the same lecture hall)
- Sam is the person who convinced me to start running — we did a half marathon together last year (both nearly died but finished!)
- Known for being hilariously bad at cooking but insists on hosting dinner parties anyway
- Recently got promoted to team lead at work and I'm incredibly proud

**The occasion:**
- Surprise party at a pub, about 40 guests (mix of friends, family, and work colleagues)
- Sam's parents will be there, so nothing too embarrassing!
- I'm giving the speech right after the cake

**Tone:** Warm and funny — make people laugh AND get a little emotional. The perfect balance of roasting Sam gently and showing how much they mean to me.

**Length:** 2-3 minutes when spoken (roughly 300-400 words)

**Must include:** The half marathon story and the cooking joke. End on something genuinely heartfelt.

**Must avoid:** Anything about Sam's ex, or the holiday in Ibiza (Sam's mum doesn't know about that one).''',
    },
    {
        'title': 'Question 3: The Magic of Context',
        'description': 'Learn how giving AI the right background transforms its responses',
        'difficulty': 'beginner',
        'order': 3,
        'points': 15,
        'instructions': '''Context is the secret ingredient that turns generic AI responses into genuinely useful ones.

**What You'll Learn:**
- Why AI gives better answers when it knows your situation
- How to provide context efficiently (not a life story!)
- The difference context makes in response quality

**The Concept:**
AI doesn't know anything about you unless you tell it. When you say "explain machine learning," AI doesn't know if you're a professor or a 10-year-old. Context fills that gap.

**Your Challenge:**
Pick ONE concept from this list (or choose your own):
- How the stock market works
- What AI actually is
- How a business makes money
- What blockchain is
- How social media algorithms work

Now get AI to explain it to **three different people:**
1. A curious 10-year-old
2. Your grandparent who's never used a computer
3. A job interviewer who asked "tell me what you know about this"

**What makes this powerful:**
Same topic, completely different explanations — all because you changed the context. This is a skill you'll use constantly: adjusting AI's output by telling it WHO the audience is.

**Tips:**
- For each version, tell AI exactly who they're talking to
- Mention what language/analogies would work for each person
- Give a word limit to keep each version focused''',
        'example_prompt': '''Explain "how social media algorithms work" in 3 completely different ways:

**Version 1 — For a curious 10-year-old:**
- Use a fun analogy they'd understand (like a school cafeteria, a librarian, or a DJ)
- Keep it under 60 words
- Make it sound exciting, not scary
- No technical words at all

**Version 2 — For my 75-year-old grandma who uses Facebook but doesn't understand why she sees certain posts:**
- Use her experience as the starting point ("You know how you see some friends' posts more than others?")
- Explain it practically — what does it mean for HER
- Reassuring tone, under 80 words
- Avoid words like "algorithm" — use plain English

**Version 3 — For a job interviewer who asked "What do you know about social media algorithms?"**
- Professional and knowledgeable tone
- Show understanding of key concepts (engagement, ranking signals, personalisation)
- Mention a real example (Instagram, TikTok, or LinkedIn)
- About 100 words
- End with an insight that shows I think critically about it

Label each version clearly.''',
    },
    {
        'title': 'Question 4: Structuring Your Requests',
        'description': 'Learn to break big, messy requests into clear, organised prompts',
        'difficulty': 'beginner',
        'order': 4,
        'points': 20,
        'instructions': '''Big tasks need structure. A wall of text confuses both humans AND AI.

**What You'll Learn:**
- How to break complex requests into clear sections
- Using bullet points, numbering, and headers to organise prompts
- Why structured prompts get dramatically better results

**The Problem:**
Imagine asking a chef: "Make me food for the week, I'm busy, I like healthy stuff but also pasta, oh and I can't eat dairy, and Tuesdays I get home late so something quick, and I meal prep on Sundays."

vs. giving them a clear brief with sections. Same information, completely different result.

**Your Challenge:**
Ask AI to create a **weekly meal plan** for you. But here's the twist — you need to structure your request clearly with specific sections.

**Your prompt must include these sections:**
1. **About me** — dietary preferences, allergies, cooking skill level
2. **Constraints** — budget per week, time available to cook, kitchen equipment
3. **Preferences** — cuisines you love, foods you hate, comfort foods
4. **Schedule** — which days you're busy (need quick meals) vs free (can cook longer)
5. **Output format** — how you want the plan organised (by day? with shopping list? with prep times?)

**Real-World Application:**
This structure works for ANY complex request — project plans, travel itineraries, study schedules, event planning. Master it once, use it everywhere.''',
        'example_prompt': '''Create a weekly meal plan for me. Here's everything you need:

**About Me:**
- Cooking skill: Intermediate (comfortable with most things, but nothing that takes 15 steps)
- Diet: No specific diet, but trying to eat more vegetables and less processed food
- Allergies: None, but I really dislike olives and aubergine

**Constraints:**
- Budget: About £50 for the week (for one person)
- Time: Weekday dinners need to be under 30 minutes
- I have a basic kitchen — oven, hob, one good pan, a baking tray, blender
- I meal prep on Sunday afternoon (2 hours max)

**Preferences:**
- Love: Mexican, Thai, Italian, and anything with rice
- Comfort foods: Pasta, stir-fry, soup
- I like variety — don't repeat the same meal twice in a week
- Breakfast can be simple (I'm not a morning cook)

**Weekly Schedule:**
- Monday–Wednesday: Home by 6pm, can cook 30 min
- Thursday: Late day, need something I prepped earlier or 15-min max
- Friday: Takeaway night (skip this)
- Saturday: Free to cook something fun (up to 1 hour)
- Sunday: Meal prep day + a nice brunch

**Format I Want:**
- Day-by-day breakdown (breakfast, lunch, dinner)
- Sunday prep list (what to make ahead)
- Full shopping list organised by supermarket section (produce, dairy, etc.)
- Estimated cost per meal

Keep it practical and realistic — I actually want to follow this!''',
    },
    {
        'title': 'Question 5: Show, Don\'t Just Tell',
        'description': 'Use examples to show AI exactly what style and quality you want',
        'difficulty': 'beginner',
        'order': 5,
        'points': 20,
        'instructions': '''One of the most powerful prompt engineering techniques: **give AI examples of what you want.**

**What You'll Learn:**
- How "few-shot prompting" works (giving examples before your request)
- Why examples are worth a thousand words of explanation
- How to use examples to control tone, style, and format

**The Concept:**
Instead of trying to describe the exact style you want (which is hard!), just SHOW it. Give AI 1-2 examples and say "more like this."

Think of it like showing a hairdresser a photo vs trying to describe the haircut in words. The photo wins every time.

**Your Challenge:**
You're helping a small business with their social media. They have a specific voice and style.

**What to do:**
1. Write (or copy) 2 example social media posts that have the tone/style you want
2. Explain what makes these examples good (this helps AI understand the pattern)
3. Ask AI to create 3 NEW posts in the same style about different topics

**Topics for the new posts:**
- Announcing a new product or service
- A behind-the-scenes or "day in the life" post
- A customer appreciation or thank-you post

**Why This Works:**
When you show AI a pattern, it picks up on things you might not even be able to articulate — sentence length, emoji usage, vocabulary level, humour style. It's like giving AI a style guide in seconds.''',
        'example_prompt': '''I run a small plant shop called "Leaf It To Us" and I need more social media posts. Here's our style:

**Example Post 1:**
"Monday morning rescue mission: grabbed this sad little fern from the clearance shelf. Two weeks of love and good light, and look at her now! Never give up on a plant (or a Monday). Who else is a plant rescuer? Show us your glow-ups!"

**Example Post 2:**
"Real talk: we killed our first three succulents before figuring it out. Overwatering is NOT love, people. Now we've got 200+ happy plants in the shop and we're here to save you from our mistakes. Drop your plant questions below — no judgement, only soil and sunshine."

**What I love about these:**
- Conversational and warm, like talking to a friend
- A bit cheeky/humorous
- Personal stories make it relatable
- Always ends with a question or call-to-action
- Uses emojis sparingly (1-2 max)
- Short sentences, easy to read on a phone

**Now create 3 new posts in this exact style for:**

1. **New arrival post:** We just got a shipment of rare Monstera Thai Constellation plants (they're gorgeous and sell out fast)

2. **Behind-the-scenes:** What our Sunday plant care routine looks like at the shop (watering 200+ plants, checking for pests, playing music for them)

3. **Customer appreciation:** A regular customer named Dave brings us homemade biscuits every Friday and we want to celebrate him

Match our voice exactly!''',
    },
    {
        'title': 'Question 6: Choosing the Right Format',
        'description': 'Control HOW AI presents information — tables, lists, comparisons, and more',
        'difficulty': 'intermediate',
        'order': 6,
        'points': 20,
        'instructions': '''The same information can be useless or incredibly useful depending on how it's formatted.

**What You'll Learn:**
- How to request specific output formats (tables, bullet points, pros/cons, etc.)
- When to use which format
- How format requests dramatically improve usability

**Why Format Matters:**
Imagine getting a restaurant recommendation as:
- A 500-word essay (hard to scan)
- A comparison table with ratings (easy to compare!)

Same info, but the table is actually useful when you're making a decision.

**Your Challenge:**
You're thinking about moving to a new city and need AI to help you compare your options in a **structured format.**

Compare these 3 UK cities: **London, Manchester, and Glasgow.**

**Your prompt must request:**
1. A comparison table with at least 5 criteria
2. A "quick verdict" section (2-3 sentences per option)
3. A final recommendation based on a specific need you state
4. A clear format that's easy to scan quickly

**Pro Tip:**
Tell AI exactly what columns you want in the table. Don't just say "compare them" — say "compare on: cost of living, job opportunities, nightlife, transport, and friendliness."''',
        'example_prompt': '''I'm considering moving to a new city for work and lifestyle. Compare these 3 UK cities for me:

1. **London**
2. **Manchester**
3. **Glasgow**

**Create a comparison table with these columns:**
- City name
- Average rent for a 1-bed flat (city centre)
- Job market strength (particularly for marketing/creative roles)
- Cost of living (rate 1-5, where 1 is cheapest)
- Nightlife and social scene (rate 1-5 with a brief note)
- Public transport quality (rate 1-5 with a brief note)
- Friendliness / ease of making friends (rate 1-5 with a brief note)
- Green spaces and outdoor activities nearby

**After the table, add:**

**Quick Verdict (2-3 sentences each):**
- Best thing about each city
- Biggest drawback of each city
- Who it's perfect for

**My Recommendation:**
Based on my situation:
- I'm 26 and single, looking for a social city with lots to do
- Working in digital marketing, need decent job opportunities
- Budget: Can spend max £900/month on rent
- I love live music, food scenes, and being able to walk/cycle places
- Coming from a small town, so I want somewhere exciting but not overwhelming

Which city should I pick and why? Be direct — I need a clear answer, not "it depends."''',
    },
    {
        'title': 'Question 7: Tone and Audience',
        'description': 'Master how to control the voice, tone, and style of AI responses',
        'difficulty': 'intermediate',
        'order': 7,
        'points': 20,
        'instructions': '''The same message, delivered in the wrong tone, can fall completely flat. Tone control is a superpower.

**What You'll Learn:**
- How to specify tone precisely (not just "professional" or "casual")
- How to adapt the same content for different audiences
- Real-world applications: emails, posts, announcements

**The Concept:**
"We're changing the office layout" can be:
- An exciting announcement: "Big news! We're upgrading our workspace..."
- A formal memo: "Please be advised that office restructuring will commence..."
- A casual Slack: "Heads up team — we're shuffling desks next week!"

Same information. Completely different impact.

**Your Challenge:**
You have a piece of news to share: **Your company is switching to a 4-day work week starting next month.**

Get AI to write this announcement in 3 completely different formats and tones:

1. **Formal company email** — from the CEO to all employees. Professional, clear, addresses potential concerns.
2. **Casual Slack message** — from a team lead to their team. Excited, brief, conversational.
3. **Social media post (LinkedIn)** — from the company's brand account. Inspiring, attracts talent, shareable.

**For each version, specify:**
- Who's writing it
- Who's reading it
- The exact tone (give AI 2-3 adjectives)
- Word count or length
- What to include or emphasise
- What to avoid

**Why This Matters:**
In any job, you'll communicate the same information to different audiences constantly. This skill translates directly to workplace communication, marketing, and leadership.''',
        'example_prompt': '''Our company "BrightPath" (a 50-person tech startup) is switching to a 4-day work week starting March 1st. Write 3 versions of this announcement:

---

**VERSION 1: Formal Company Email**
- From: CEO (Sarah Mitchell)
- To: All employees
- Tone: Warm but professional, confident, reassuring
- Length: 200-250 words
- Must address:
  - Why we're doing this (employee wellbeing + productivity research)
  - How it works (Fridays off, same salary, trial period of 3 months)
  - What's expected (maintain quality of work, some teams may need to coordinate)
  - Who to ask questions (HR)
- Avoid: Making it sound like a test they could fail, or being too stiff/corporate

---

**VERSION 2: Casual Slack Message**
- From: Team lead (you) to your team of 8
- Tone: Excited, genuine, light-hearted
- Length: 60-80 words max
- Must include: The key facts (when it starts, how it works)
- Can include: An emoji or two, a bit of humour
- Avoid: Being so casual that important details get lost

---

**VERSION 3: LinkedIn Post**
- From: BrightPath's company page
- Tone: Inspiring, forward-thinking, authentic (not braggy)
- Length: 150-200 words
- Must include: Why this matters for the industry, a human touch
- Should: Make talented people want to work here
- End with: A question or call-to-action to drive engagement
- Avoid: Sounding like every other corporate "we care about our people" post

Label each version clearly and make them feel genuinely different — not just the same text with different word choices.''',
    },
    {
        'title': 'Question 8: The Art of Iteration',
        'description': 'Learn the most practical skill: making AI responses better through refinement',
        'difficulty': 'intermediate',
        'order': 8,
        'points': 25,
        'instructions': '''Here's a secret: professionals almost never use the first AI response. They iterate.

**What You'll Learn:**
- The draft → feedback → refine workflow
- How to give AI specific improvement instructions
- Why iteration beats trying to write the "perfect" first prompt

**The Concept:**
Think of AI like a talented but mind-reading-impaired assistant. The first draft gets you 70% there. Your feedback gets you to 95%. This is normal and efficient!

**The Workflow:**
1. **First request:** Get the initial draft
2. **Review:** What's good? What's not right?
3. **Refine:** Give specific feedback and ask for improvements
4. **Polish:** Fine-tune the final version

**Your Challenge:**
Get AI to help you write an engaging "About Us" section for a small business website — but do it in **stages within a single prompt.**

**Stage 1:** Ask AI to write a first draft based on the business details
**Stage 2:** Tell AI what to improve (e.g., "make the opening more attention-grabbing," "add a personal story," "cut the jargon")
**Stage 3:** Ask AI to polish the final version with specific constraints

**You must show all 3 stages in your prompt** — this teaches AI (and you!) the iteration mindset.

**Real-World Value:**
This is how professionals use AI for writing, coding, design briefs, presentations — everything. The skill isn't writing one perfect prompt. It's knowing how to guide AI from "okay" to "excellent."''',
        'example_prompt': '''Help me create an "About Us" section for a small business website. We'll do this in 3 stages — draft, improve, and polish.

---

**STAGE 1 — First Draft**

Write an About Us section based on this:
- Business: "The Bake House" — a small family-run bakery in Bristol
- Founded: 2019 by married couple Tom and Hana
- Story: They started baking sourdough during lockdown, friends kept asking to buy loaves, and it grew from there
- What they sell: Artisan bread, pastries, and celebration cakes
- What makes them different: Everything is made fresh daily, they use local suppliers, and they're known for their community spirit (they donate unsold bread to a local shelter every evening)
- Vibe: Warm, welcoming, the smell of fresh bread, regulars who come every morning

Write a first draft (150-200 words, friendly and warm).

---

**STAGE 2 — Improve It**

Now take your draft and make these specific improvements:
1. The opening line is probably generic ("Welcome to The Bake House...") — make it a hook that captures the feeling of walking into the shop.
2. The lockdown origin story is our best asset — make it more vivid and personal. Include a small detail that makes it feel real (the first loaf was terrible? Hana's mum gave them the recipe?)
3. Remove any words like "passionate," "artisan," or "crafted with love" — these are overused. Show the quality through specifics instead.
4. Add something about the community donations — but naturally, not as a brag.
5. End with something inviting, not just "visit us today."

Show me the improved version.

---

**STAGE 3 — Final Polish**

Now apply these final constraints:
- Exactly 150-175 words (tighten it up)
- Every sentence must earn its place — cut anything fluffy
- Tone: Warm and genuine, like the bakery itself
- Must include at least one specific detail that makes us memorable
- The first line should make someone hungry or nostalgic

Show me the final polished version, and briefly explain what changed at each stage so I learn from the process.''',
    },
]
