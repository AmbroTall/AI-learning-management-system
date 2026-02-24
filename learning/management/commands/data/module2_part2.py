"""
Module 2 Part 2: The AI Tool Ecosystem — "Right Tool, Right Job"
Challenges 9-16: Exploring the major AI tools and knowing when to use each (4-5 hours)
"""

MODULE2_PART2_CHALLENGES = [
    {
        'title': 'Question 9: ChatGPT in Practice',
        'description': 'Explore ChatGPT\'s strengths through 3 real tasks and evaluate its performance',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 25,
        'instructions': '''ChatGPT is the most widely used AI tool in the world. But what is it actually good at — and where are its limits?

**What You'll Learn:**
- ChatGPT's core strengths: conversational flexibility, creative tasks, GPT plugins, and custom GPTs
- How to evaluate AI output quality critically
- How to write tasks that test a tool's real capabilities

**ChatGPT's Strengths:**
- Broad general knowledge and conversational fluency
- Strong at creative writing, brainstorming, and ideation
- Custom GPTs for specialised tasks
- Plugins and integrations with other apps
- DALL-E image generation built in
- Browsing capability for current information

**ChatGPT's Limitations:**
- Can hallucinate confidently (make up facts)
- Long documents and deep analysis can drift
- Less focused on reasoning transparency than some alternatives
- Quality varies across different models and settings

**Your Challenge:**
Complete 3 different tasks that test ChatGPT's range, then evaluate the performance:

**Task 1 — Creative Writing:** Ask for a short, engaging story or piece of content for a specific purpose (social media post, product description, email campaign)

**Task 2 — Research & Explanation:** Ask it to explain a complex concept in your field, with examples, in accessible language

**Task 3 — Structured Analysis:** Ask it to evaluate something with pros, cons, and a recommendation

**After each task, write a brief evaluation:**
- What worked well?
- Where did it fall short?
- What would you verify or fact-check?
- Would you use it for this task in real life?''',
        'example_prompt': '''I'm going to complete 3 tasks that test ChatGPT's capabilities, then evaluate each response honestly.

---

**TASK 1 — Creative Writing Test**

I run a small independent bookshop called "The Last Chapter" in Edinburgh. Write 3 Instagram captions for these posts:

Post A: We just received a special limited edition Harry Potter anniversary box set
Post B: Our cosy reading corner has just been refurbished with new armchairs
Post C: We're hosting a free children's storytime event this Saturday at 11am

Requirements for each:
- Max 150 words
- Warm, bookish personality — literary references welcome
- Relevant hashtags (5-7)
- An engaging question or call-to-action
- Should feel like a real independent bookshop, not a corporate account

---

**TASK 2 — Research & Explanation Test**

Explain "machine learning" to someone who runs a small business and has never studied technology.
- No jargon unless defined
- Use a real-world analogy they'd immediately understand
- Include 3 concrete examples of how machine learning already affects their daily business life (whether they know it or not)
- End with one practical way they could use ML tools in their business today
- Max 300 words

---

**TASK 3 — Structured Analysis Test**

A small business owner is deciding whether to invest in paid social media advertising (Facebook/Instagram ads) or search engine optimisation (SEO) with a budget of £500/month.

Analyse this decision:
1. Pros and cons of paid social ads for a small business
2. Pros and cons of SEO for a small business
3. How the right answer depends on their specific situation (what questions should they ask themselves?)
4. Your recommendation for a business that sells handmade jewellery online, targeting women aged 30-55 in the UK

---

**After all 3 tasks, give me a brief evaluation:**
For each task: what did you handle well, where did you have limitations, and what should a user verify before relying on this output?

Be honest — I'm learning how to use AI critically.''',
    },
    {
        'title': 'Question 10: Claude for Deep Work',
        'description': 'Discover Claude\'s strengths — long documents, careful reasoning, and structured analysis',
        'difficulty': 'intermediate',
        'order': 10,
        'points': 25,
        'instructions': '''Claude (the AI you're using right now) has distinct strengths that make it particularly powerful for certain types of work.

**What You'll Learn:**
- Where Claude excels compared to other AI tools
- How to use Claude for long-document work and deep analysis
- How to leverage Claude's reasoning strengths in professional contexts

**Claude's Core Strengths:**
- **Long document handling:** Can read, analyse, and reason across very long texts
- **Careful reasoning:** Less likely to rush to wrong conclusions on complex problems
- **Nuanced analysis:** Handles ambiguity and trade-offs thoughtfully
- **Professional writing:** Formal documents, reports, careful prose
- **Instruction-following:** Precise adherence to formatting and structural requirements
- **Honest uncertainty:** More likely to acknowledge when it doesn't know something

**Ideal Use Cases for Claude:**
- Analysing long research papers or reports
- Complex decision analysis with multiple considerations
- Drafting professional documents (proposals, policies, reports)
- Reasoning through ethical or nuanced situations
- Detailed feedback on long pieces of writing
- Any task where accuracy matters more than speed

**Your Challenge:**
Use Claude to analyse a detailed business case study and produce a structured recommendation.

**The Case Study:**
A fictional mid-size company is facing a strategic decision about remote work policy following post-pandemic hybrid working.

Write a prompt that:
1. Gives Claude a rich, detailed scenario to analyse
2. Requests systematic reasoning through multiple angles
3. Asks for a structured report format with clear sections
4. Requires a final, defensible recommendation with reasoning

This tests Claude's ability to reason carefully and produce professional analytical output.''',
        'example_prompt': '''Analyse the following business case study and produce a structured strategic recommendation report.

---

**CASE STUDY: Meridian Consulting — Remote Work Policy Decision**

**Background:**
Meridian Consulting is a 120-person management consultancy based in London. Before 2020, all staff worked in the office 5 days/week. During the pandemic, they shifted to fully remote. Since 2022, they've operated a voluntary hybrid model — no mandated office days.

**Current Situation:**
- 40% of staff come in 0-1 days/week (primarily senior staff and parents)
- 35% come in 2-3 days/week (mostly junior and mid-level consultants)
- 25% come in 4-5 days/week (mostly new graduates and client-facing partners)
- Office costs: £85,000/month for a 3-floor building they're now under-utilising
- Client satisfaction scores: consistently high (NPS of 67)
- Staff satisfaction: mixed — 68% say current flexibility is important to them; 22% say they feel isolated

**Business Pressures:**
- Two senior partners have left for competitors with fully flexible policies
- Three junior consultants quit in the last year citing "lack of mentorship and connection"
- The board is considering two options: mandate 3 days/week in office, or go fully remote and drop the lease
- New CEO wants a decision within 30 days

**Stakeholder Positions:**
- Senior partners (65+): favour more office presence for client relationships and mentoring
- Mid-level consultants (30-50): split opinion; many value flexibility highly
- Junior staff (22-29): divided — some want mentorship and connection, others prefer remote flexibility
- HR Director: worried about culture erosion and onboarding quality
- Finance Director: sees fully remote as a £1M/year saving opportunity

---

**I NEED A STRUCTURED ANALYSIS REPORT:**

**Section 1 — Situation Assessment**
What are the core tensions in this decision? What is Meridian really deciding between?

**Section 2 — Stakeholder Analysis**
How does each group's interests differ? Where are the genuine conflicts?

**Section 3 — Option Analysis**
Evaluate each of the two options the board is considering:
- Mandate 3 days/week in office
- Go fully remote and drop the lease
- AND identify if there's a better third option they haven't considered

For each option: business impact, talent implications, financial impact, cultural risk, and feasibility.

**Section 4 — Recommendation**
Make a clear, justified recommendation. Not "it depends" — make a call.
Include: what you recommend, the reasoning, key risks to manage, and 3 conditions that would change your recommendation.

**Section 5 — Implementation Plan**
If the board accepts your recommendation, what are the first 5 actions in the first 30 days?

---

Format this as a professional consulting report. Be direct, well-reasoned, and willing to take a position.''',
    },
    {
        'title': 'Question 11: Google Gemini & the Google Ecosystem',
        'description': 'Learn how Gemini works with Google tools to supercharge your existing workspace',
        'difficulty': 'intermediate',
        'order': 11,
        'points': 25,
        'instructions': '''Google Gemini is Google's AI — and its superpower is how deeply it integrates with tools most people already use every day.

**What You'll Learn:**
- What makes Gemini different from standalone AI tools
- How Gemini works with Google Docs, Sheets, Gmail, Search, and Meet
- How to design workflows that use Gemini's integration strengths

**Gemini's Key Strengths:**
- **Google Workspace integration:** Works directly inside Docs, Sheets, Slides, Gmail, and Meet
- **Real-time information:** Connected to Google Search for current information
- **Multimodal:** Can work with text, images, audio, and video
- **Google Meet summaries:** Summarises meetings and extracts action items
- **NotebookLM integration:** Deep research and document synthesis

**Ideal Use Cases:**
- Drafting and editing directly inside Google Docs
- Building formulas and summaries in Google Sheets
- Summarising long email threads in Gmail
- Creating first-draft presentations in Google Slides
- Generating meeting summaries from Google Meet recordings
- Research projects that benefit from current web information

**Your Challenge:**
Design a complete research project plan that uses Gemini's Google ecosystem integration across multiple tools.

**The Project:** You're researching a potential career change into UX Design and need to use multiple Google tools to organise your findings.

Write a prompt that:
1. Plans the full research process using Gemini + Google tools
2. Shows exactly which Google tool you'd use for each part
3. Demonstrates how the tools would work together
4. Produces a structured research output ready to act on''',
        'example_prompt': '''Help me design a career research project using Gemini's Google ecosystem integration. I want a complete plan showing which Google tool to use at each stage.

**MY SITUATION:**
I'm a 28-year-old currently working as a project coordinator in a marketing agency. I'm considering a career change into UX Design. I have no formal UX training, but I have strong communication skills, enjoy problem-solving, and have always been interested in how products work. I use Google Workspace daily.

**THE RESEARCH PROJECT:**
I want to thoroughly research UX Design as a career path and create an action plan. I want to use Gemini alongside Google tools to do this properly.

---

**PART 1 — Research Architecture**

Design a complete research plan for this career exploration using Google tools. For each stage, specify:
- Which Google tool to use (Docs, Sheets, Search/Gemini, Gmail, Slides, NotebookLM, etc.)
- What task Gemini or that tool helps accomplish
- What the output of that stage looks like

Stages to cover:
1. Initial broad research (what is UX Design? What do UX designers actually do?)
2. Market research (demand, salaries, growth, specialisations)
3. Skills gap analysis (what do I already have vs what I need?)
4. Learning pathway research (courses, bootcamps, self-study resources)
5. Portfolio and experience building plan
6. Network and community identification
7. Decision document (should I make this change?)

**PART 2 — Sample Prompts for Each Stage**

For each stage above, write the specific Gemini prompt I would actually type into that Google tool. Show me what real, effective prompts look like for this research.

**PART 3 — The Synthesis Document**

Describe what a completed Google Doc would look like at the end of this research — the structure of my "Career Research Report" that pulls together everything I've found. Give me the full document outline with section headers and what goes in each section.

**PART 4 — Decision Framework**

Create a simple decision framework (Google Sheets format — table/matrix) that helps me make the final go/no-go decision on the career change. What criteria matter? How would I score each one?''',
    },
    {
        'title': 'Question 12: Microsoft Copilot at Work',
        'description': 'Discover how AI built into Microsoft 365 transforms everyday office work',
        'difficulty': 'intermediate',
        'order': 12,
        'points': 30,
        'instructions': '''Microsoft Copilot is AI built directly into the tools millions of people use every day — Word, Excel, PowerPoint, Outlook, and Teams.

**What You'll Learn:**
- How Copilot works differently from standalone AI tools
- The specific superpowers Copilot has in each Microsoft 365 app
- How to write the kinds of prompts that work well in office contexts

**Copilot's App-by-App Strengths:**

**Word:** Draft, rewrite, summarise, change tone — directly in your document
**Excel:** Generate formulas, analyse data, create charts from descriptions
**PowerPoint:** Generate entire presentations from a brief, reformat slides, create speaker notes
**Outlook:** Summarise long email threads, draft replies, prepare for meetings
**Teams:** Summarise meeting recordings, list action items, catch up on missed conversations

**What Makes Copilot Different:**
Unlike starting from scratch, Copilot works with your existing content. It can see your meeting notes, your emails, your documents — and use that context to produce better, more relevant outputs.

**Your Challenge:**
Demonstrate how Copilot would transform a typical office scenario:

**The scenario:** You've just attended a long, somewhat chaotic project meeting. You have 4 pages of rough notes. You need to turn them into (a) professional meeting minutes, (b) a polished status update email, and (c) a 5-slide executive summary presentation.

Write the prompts you would use in each Microsoft app, plus a brief explanation of why you'd use that specific app for that task.''',
        'example_prompt': '''Show me how Microsoft Copilot would transform these rough meeting notes across different Office apps. Write the actual prompts I'd use in each tool.

---

**THE RAW MEETING NOTES:**

Q2 product planning mtg — 14 people, 90 mins

Sarah opened — stressed we need to hit 3 new features by end of Q2. Currently tracking at 2.
Tom from dev — said the API integration is behind because of dependency on the payments team. Could be 2 weeks late. Asked for a decision on whether to deprioritise the new reporting dashboard.
Lisa (product) said clients are asking about the dashboard constantly. Can't deprioritise it.
Tom said they're at capacity. Can we bring in contractor? Budget conversation needed.
Finance rep (Mark) wasn't in the room — someone needs to get sign-off on contractor budget (approx £8k for 3 weeks).
Design team (Nina) — mobile redesign is on track for March 15th. Needs dev to confirm integration date by Monday or it slips.
Customer success raised that 3 enterprise clients have mentioned the slow load times. Tech debt issue apparently flagged 6 months ago but not resolved.
Sarah said load time fix needs to be prioritised — "this is a client retention risk"
Decision made: Dashboard deprioritised until Q3, API integration prioritised. Dev to give new delivery date by Thursday.
Load time fix escalated — James to assess next week, present options to Sarah by following Friday.
Mobile redesign — dev to confirm integration by Monday (Nina's hard deadline).
Mark needs to be emailed about contractor budget urgently.
Next meeting: 3 weeks. Sarah to send calendar invite.

General vibe: stressed, running behind, but recoverable.

---

**PROMPT 1 — In Microsoft Word:**
Write the exact prompt I'd type into Word's Copilot to turn these notes into professional meeting minutes.

Format the prompt so it produces:
- Meeting header (date, attendees, purpose)
- Key Discussion Points (3-4 bullet points)
- Decisions Made
- Action Items table: | Task | Owner | Deadline |
- Next Meeting details

---

**PROMPT 2 — In Outlook:**
Write the exact prompt I'd type into Outlook's Copilot to draft a status update email.

The email should go to the wider product team (20 people) who weren't in the meeting.
- Professional but not overly formal
- Clear summary of where things stand
- Specific actions people need to take
- Positive/solution-focused tone (not alarm-raising)
- Max 200 words

---

**PROMPT 3 — In PowerPoint:**
Write the exact prompt I'd type into PowerPoint's Copilot to create a 5-slide executive summary.

Structure the slides as:
- Slide 1: Current Status (project health, key metrics)
- Slide 2: What's Going Well
- Slide 3: Current Blockers and Risks
- Slide 4: Decisions Made and Rationale
- Slide 5: Next Steps and Timeline

Each prompt should be something I could actually type — not a description of what to do, but the real Copilot instruction.

---

**Finally — explain:** Why is using the dedicated app (Word, Outlook, PowerPoint) better than asking a standalone AI tool to produce the same outputs?''',
    },
    {
        'title': 'Question 13: AI Image Generation',
        'description': 'Master the art of writing prompts that create powerful, professional visuals',
        'difficulty': 'intermediate',
        'order': 13,
        'points': 30,
        'instructions': '''AI can now generate stunning images from text descriptions — and writing a good image prompt is its own creative skill.

**What You'll Learn:**
- How AI image generation works (DALL-E, Midjourney, Adobe Firefly)
- The anatomy of an effective image prompt
- How to use AI images for real professional purposes

**The Major Image AI Tools:**
- **DALL-E (ChatGPT):** Good for realistic images, product mockups, and quick illustrations
- **Midjourney:** Known for artistic, photorealistic, and cinematic quality
- **Adobe Firefly:** Safe for commercial use, integrates with Adobe products
- **Stable Diffusion:** Open source, highly customisable

**Anatomy of a Great Image Prompt:**

1. **Subject:** What is in the image?
2. **Style:** Photography? Illustration? Watercolour? 3D render?
3. **Mood/Lighting:** Warm, dramatic, minimalist, vibrant?
4. **Composition:** Close-up, wide shot, overhead view?
5. **Colour palette:** Specific colours or overall tone?
6. **Additional details:** Time of day, setting, texture, context

**Your Challenge:**
Design a complete brand visual identity for a fictional small business using AI image prompts.

**The Business:** Choose one:
- A boutique yoga and wellness studio
- A specialty coffee roaster
- A children's book illustration studio
- A sustainable fashion brand

Write detailed image prompts for:
1. A logo concept
2. A hero banner for the website
3. A social media post visual
4. A product mockup or service image

For each prompt, also explain your creative choices — why these elements support the brand identity.''',
        'example_prompt': '''I'm creating a complete visual brand identity for a boutique wellness studio using AI image generation. Write detailed image prompts for each asset, and explain the creative choices behind each one.

**THE BRAND:**
"Stillwater Studio" — a boutique yoga, meditation, and breathwork studio in a converted Victorian building in Bristol. Target client: professional women aged 28-45 who are stressed, time-poor, and seeking real wellbeing (not Instagram wellness). Brand personality: Calm, honest, grounded. Not spiritual-lite or overly aesthetic. Real, quiet, restorative.

Colour palette we're working with: Deep slate blue, warm off-white, terracotta, natural linen.

---

**ASSET 1 — LOGO CONCEPT**

Write an AI image prompt for a logo concept that captures the brand.

Requirements:
- Minimal and sophisticated — not literal or clipart-y
- Should work in black and white AND in the brand palette
- Timeless, not trendy
- Suggests calm water, stillness, or breath without being obvious

Your prompt: [Write the full detailed image generation prompt]
Your creative rationale: [Explain why these elements serve the brand]

---

**ASSET 2 — WEBSITE HERO BANNER**

Write an AI image prompt for the main hero banner image on the homepage.

Requirements:
- Photorealistic style
- Should evoke how a client FEELS after a session — not during (so not straining in a yoga pose)
- Natural light, probably morning
- Human but not posed/stock-photo-y
- Horizontal format, space for text overlay on left side

Your prompt: [Write the full detailed image generation prompt]
Your creative rationale: [Explain the mood, composition, and lighting choices]

---

**ASSET 3 — INSTAGRAM POST VISUAL**

Write an AI image prompt for a social media post promoting a "Monday Morning Reset" class.

Requirements:
- Square format
- Warm and inviting — feels like an invitation, not a hard sell
- Minimal text space needed (text will be added separately)
- Could be: a detail shot, a mood board, a texture, or an abstract composition
- Should stop a scroll without being loud

Your prompt: [Write the full detailed image generation prompt]
Your creative rationale: [Why this works for Instagram's visual language]

---

**ASSET 4 — STUDIO ATMOSPHERE IMAGE**

Write an AI image prompt for an interior photo showing the studio space.

Requirements:
- Should feel like the actual converted Victorian space
- Morning light, natural materials, quiet
- No people — the space itself is the subject
- High-end but not intimidating
- Magazine editorial quality

Your prompt: [Write the full detailed image generation prompt]
Your creative rationale: [Explain how this image communicates the studio's identity]

---

Finally: what are the 3 most important principles of writing effective image prompts that you've demonstrated across these 4 examples?''',
    },
    {
        'title': 'Question 14: AI for Presentations & Video',
        'description': 'Use AI tools to create polished presentations and video content faster than ever',
        'difficulty': 'intermediate',
        'order': 14,
        'points': 30,
        'instructions': '''Creating compelling presentations used to take hours. AI tools like Gamma, Beautiful.ai, Tome, and Synthesia can produce polished decks and videos from a brief in minutes.

**What You'll Learn:**
- The major AI presentation and video tools and what they do best
- How to write a brief that produces a genuinely good AI-generated deck
- What to do with AI-generated slides (it's always a starting point, not the end)

**The Key Tools:**

**Presentation AI:**
- **Gamma:** Generates beautiful, structured decks from a prompt or outline
- **Beautiful.ai:** Intelligent layouts that adjust as you add content
- **Tome:** Strong for narrative-driven, story-based presentations
- **Microsoft Designer:** Creates polished slides integrated with Office

**Video AI:**
- **Synthesia:** Creates presenter videos with AI avatars (no camera needed)
- **Descript:** Edits video by editing the transcript
- **Runway:** AI video generation and editing
- **HeyGen:** Personalised AI video messages at scale

**When to Use These Tools:**
- Sales decks and proposals (quick turnaround)
- Training materials (consistent, professional)
- Internal updates (fast, clear)
- Explainer videos (no production crew needed)

**Your Challenge:**
Create a complete brief for a 10-slide pitch deck using AI presentation tools.

**The Pitch:** Choose a business, project, or idea to pitch to an investor, partner, or senior stakeholder. Write the detailed brief you would give to an AI presentation tool — and produce the slide-by-slide content that would go into each slide.''',
        'example_prompt': '''Create a complete 10-slide pitch deck for an AI presentation tool like Gamma or Tome. Write both the brief AND the full slide-by-slide content.

**THE PITCH:**
"MindBridge" — an AI-powered mental health check-in app for small and medium businesses. Designed for HR teams to monitor team wellbeing at scale, identify early warning signs, and connect employees with the right support.

**AUDIENCE:** Angel investors and seed-stage VCs at a pitch event in London. 8-minute presentation slot.

**BRAND FEEL:** Professional but human. Clean, trustworthy. Not cold or clinical. Calm blues and greens.

---

**PART 1 — THE BRIEF (what I'd type into Gamma/Tome):**

Write a concise 200-word brief I would paste into an AI presentation tool to generate the initial deck. Include:
- The product and its purpose
- The audience for this specific presentation
- The visual style and tone
- The key message I want to leave investors with
- Any constraints (slide count, time, colours)

---

**PART 2 — SLIDE BY SLIDE CONTENT:**

Write the detailed content for all 10 slides:

**Slide 1 — Opening/Hook:** A single powerful statement or question that grabs attention immediately

**Slide 2 — The Problem:** The workplace mental health crisis — statistics, human cost, why existing solutions fail. (Include real-ish stats)

**Slide 3 — Our Solution:** What MindBridge does, in clear, simple language. Lead with outcome, not features.

**Slide 4 — How It Works:** 3-step process diagram content (what the employee sees, what HR sees, what happens next)

**Slide 5 — Market Opportunity:** TAM/SAM/SOM for UK employee wellbeing market. Why NOW?

**Slide 6 — Traction:** Early metrics, pilot customers, key partnerships, waitlist size (make these realistic and compelling)

**Slide 7 — Business Model:** How we make money (SaaS pricing tiers), unit economics, expansion potential

**Slide 8 — Competition:** Competitive landscape — what's out there, and why we win in our specific niche

**Slide 9 — The Team:** 3 founders with complementary skills — write compelling bios that build credibility

**Slide 10 — The Ask:** How much we're raising, what it's for, and what we'll achieve with it

For each slide: headline text, 3-4 bullet points of key content, and a note on what visual would work best.

---

What are the 3 most important principles of a compelling investor pitch, based on the structure above?''',
    },
    {
        'title': 'Question 15: AI Writing & Editing Tools',
        'description': 'Compare AI writing assistants and know when to use each type for different tasks',
        'difficulty': 'intermediate',
        'order': 15,
        'points': 30,
        'instructions': '''There's a whole category of AI tools specifically designed for writing — and they work very differently from general AI chat tools.

**What You'll Learn:**
- The difference between AI writing assistants and AI chat tools
- When to use Grammarly, Hemingway, Jasper, or a general AI chat tool
- How to combine tools for maximum writing quality

**The Key Tools:**

**Grammar and Style:**
- **Grammarly:** Grammar, spelling, tone analysis, clarity suggestions, plagiarism check
- **Hemingway Editor:** Readability scoring, highlights complex sentences, passive voice detection
- **ProWritingAid:** Deep grammar + style analysis for longer documents

**AI-Powered Writing:**
- **Jasper:** Marketing copy, long-form content, trained on marketing frameworks
- **Copy.ai:** Quick marketing copy — product descriptions, ads, social media
- **Notion AI:** Writing within your project notes (context-aware)

**When to Use What:**
- Editing and polishing existing work → Grammarly, Hemingway
- Marketing copy at scale → Jasper, Copy.ai
- Drafting from scratch → General AI chat (Claude, ChatGPT)
- Everything in a notes/project context → Notion AI

**Your Challenge:**
Take a rough draft and improve it using multiple approaches — demonstrating you know when each tool type adds the most value.

**The draft:** A product description for an eco-friendly water bottle. Write it in rough form, then show how you'd improve it using (a) a Grammarly-style edit, (b) a Hemingway-style readability fix, and (c) a full rewrite using AI chat. Compare all three outputs.''',
        'example_prompt': '''I want to improve a rough product description using different AI writing approaches. Show me what each approach does and when to use it.

---

**THE ROUGH DRAFT:**

"The EcoFlow water bottle is really great for people who care about the environment. It is made from stainless steel which means it is very durable and will last you a long time unlike plastic bottles which are bad for the environment. It can keep your drinks cold for up to 24 hours and hot drinks hot for 12 hours. The bottle is 500ml which is a good size for most people. It comes in lots of different colours. The lid is leak proof so you don't have to worry about spills in your bag. We think it's really important to reduce plastic waste and that's why we made this bottle. You can buy it on our website."

---

**APPROACH A — Grammarly-Style Grammar and Clarity Edit:**

Edit this draft for:
1. Grammar and spelling errors
2. Sentence structure improvements
3. Removing redundant phrases
4. Improving word choice
5. Fixing passive voice where it weakens the sentence

Show me the edited version with brief annotations explaining the key changes.

---

**APPROACH B — Hemingway-Style Readability Fix:**

Now take the original rough draft and:
1. Identify every sentence that is too long or complex (flag with why)
2. Identify every word that could be simpler (flag with a simpler alternative)
3. Calculate the approximate reading grade level of the original
4. Rewrite it to a grade 6-7 reading level (clear, direct, easy to scan)
5. Show the before and after Flesch-Kincaid score improvement

---

**APPROACH C — Full AI Chat Rewrite:**

Forget both edits above. Start from scratch with a proper copywriting brief:

Write a compelling product description for the EcoFlow bottle that:
- Opens with the customer's benefit, not the product feature
- Uses the "so what?" technique: every feature is followed by its real-world benefit
- Targets eco-conscious millennials aged 25-35 who are practical, not preachy
- Includes social proof signal (used by X people, or a credible stat)
- Ends with a clear, confident CTA
- Length: 80-100 words
- No clichés ("game-changer," "eco-warrior," "sustainable future")

---

**COMPARISON:**
After showing all three outputs, give me a side-by-side analysis:
- Which approach produced the strongest result?
- What did each approach do that the others couldn't?
- For a small e-commerce business with limited time and budget, what's the most practical workflow combining these approaches?''',
    },
    {
        'title': 'Question 16: Choosing the Right Tool for the Job',
        'description': 'Build a practical decision framework for matching AI tools to real tasks',
        'difficulty': 'advanced',
        'order': 16,
        'points': 35,
        'instructions': '''You now know about a wide range of AI tools. The real skill? Knowing exactly which one to reach for and why.

**What You'll Learn:**
- A practical decision framework for AI tool selection
- How to evaluate tools based on task requirements, not hype
- How to justify your tool choices to colleagues and clients

**The Decision Factors:**

When choosing an AI tool, consider:
1. **Task type:** Creative? Analytical? Editing? Visual? Automated?
2. **Output format:** Text, image, presentation, code, video?
3. **Quality requirements:** Quick draft vs polished professional output?
4. **Integration:** Does it need to work inside an existing tool (Google/Microsoft)?
5. **Speed vs depth:** Do you need it in 2 minutes or is careful analysis worth the time?
6. **Cost:** Free tier sufficient, or worth paying?
7. **Privacy:** Is the content sensitive? (Don't put confidential data in free tools)

**The Tools to Know:**
- General AI chat: Claude, ChatGPT, Gemini
- Office integration: Copilot (Microsoft), Gemini (Google Workspace)
- Images: DALL-E, Midjourney, Firefly
- Presentations: Gamma, Tome, Beautiful.ai
- Writing: Grammarly, Hemingway, Jasper
- Automation: Zapier, Make, n8n
- Research/documents: NotebookLM, Perplexity

**Your Challenge:**
Given 6 real work scenarios, choose the best AI tool for each and write a clear, specific justification.

Make your answers specific — "use AI" is not an answer. Which tool, why that tool, and what specifically you'd ask it to do.''',
        'example_prompt': '''I need to build my AI tool selection instincts. For each of these 6 scenarios, tell me: which AI tool to use, why, and the specific first prompt I'd type.

---

**SCENARIO 1:**
I'm a solo consultant. A client just sent me 47 pages of their company strategy document and financial reports. They're paying me to give them a concise analysis with recommendations within 24 hours.

- Which tool? Why this tool over alternatives?
- What's the first prompt I'd type?

---

**SCENARIO 2:**
I'm a marketing manager. My team needs to produce 30 product descriptions for a new clothing line by end of week. The brief is ready. I have one junior writer and a budget of £0 for new tools.

- Which tool? Why this tool over alternatives?
- What's the first prompt I'd type?

---

**SCENARIO 3:**
I'm an HR director preparing for a quarterly all-hands presentation to 200 employees. I have rough notes on key themes (wellbeing, new office policy, Q3 results), but I'm not a confident PowerPoint designer.

- Which tool? Why this tool over alternatives?
- What's the first prompt I'd type?

---

**SCENARIO 4:**
I'm a small business owner. I just had a 60-minute strategy meeting with my business coach on Zoom. I want the key decisions, action items, and quotes turned into a professional summary I can share with my co-founder.

- Which tool? Why this tool over alternatives?
- What's the first prompt I'd type?

---

**SCENARIO 5:**
I'm a freelance graphic designer pitching a new brand identity to a client. I want to show them 4 different visual concepts in a mood board before doing the real design work — without spending 3 hours in Photoshop first.

- Which tool? Why this tool over alternatives?
- What's the first prompt I'd type?

---

**SCENARIO 6:**
I'm a sales manager. Every Monday I manually compile data from 3 different spreadsheets to create a team performance report. It takes 2 hours and involves copy-pasting the same information in the same format every week.

- Which tool? Why this tool over alternatives?
- What's the first prompt or workflow I'd set up?

---

**After all 6 scenarios, give me:**
A one-page "AI Tool Selection Cheat Sheet" — a simple reference guide I could share with my team to help them choose the right AI tool quickly for common work tasks.''',
    },
]
