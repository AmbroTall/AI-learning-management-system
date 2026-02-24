"""
Populate the free 'Introduction to AI' module (5 lessons).
Run this before populate_module1.

Usage:
    python manage.py populate_intro
"""

from django.core.management.base import BaseCommand
from learning.models import Module, Challenge

INTRO_LESSONS = [
    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 1 — The revolution
    # ─────────────────────────────────────────────────────────────────────────
    {
        'title': 'Lesson 1: The Biggest Shift in 100 Years',
        'description': 'AI isn\'t just another tech trend. Understand why this moment in history is genuinely unprecedented — and why it matters for you.',
        'difficulty': 'beginner',
        'order': 1,
        'points': 10,
        'instructions': '''## Something Extraordinary is Happening Right Now

Let's start with a story.

In 2022, Google's **DeepMind** released a system called **AlphaFold 2**. Scientists had been trying to figure out the 3D shape of proteins — the building blocks of all life — for over 50 years. It was considered one of biology's greatest unsolved problems. Individual research teams would spend months, sometimes years, figuring out the structure of a single protein.

AlphaFold solved **200 million of them.** In months.

That's more protein structures than all of human science had discovered in the previous half-century — combined.

---

## It's Not Just Science. Look Around You.

**ChatGPT** launched in November 2022. It reached **100 million users in 2 months** — faster than any product in history. For context, TikTok took 9 months. Instagram took 2.5 years.

People weren't just curious about it. They were using it. For work. For creativity. For learning.

Then came the results that turned heads even further:

- **GPT-4 scored in the top 10% of the Bar Exam** — the qualification test for lawyers
- An AI system **diagnosed a rare connective tissue disorder** in a boy who had seen 17 doctors over 3 years — none of them got it right
- GitHub Copilot (an AI coding tool) was shown to **increase developer productivity by 55%**
- In 2023, AI wrote a piece of music that moved listeners to tears. It also wrote a screenplay that placed in a professional competition. And it passed a **Master's level business school exam at Wharton**

This isn't science fiction. This is Tuesday.

---

## So What Actually *Is* AI?

There's a lot of hype around this word. Let's be precise.

**Artificial Intelligence** is the ability of a computer system to perform tasks that normally require human intelligence — things like understanding language, recognising patterns, solving problems, and generating new content.

The version of AI that's changing the world right now is called **Generative AI** — AI that doesn't just analyse things, but *creates* them. Text, images, code, audio, video.

> Think of it this way: previous software followed instructions. Generative AI can *write* the instructions — and then follow them.

The key breakthrough was **Large Language Models (LLMs)** — systems trained on essentially the entire written output of human civilisation. They read the internet. Books. Science. Literature. Code. Conversations. And they learned not just *facts*, but *how to think* in language.

The result? A system you can have a conversation with. Ask it anything. Ask it to write anything. Ask it to help you with any task.

And it's not just ChatGPT. There's **Claude** (Anthropic), **Gemini** (Google), **Llama** (Meta), **Copilot** (Microsoft) — an entire ecosystem of powerful AI tools, most of them free or cheap to access.

---

## What Changed? Why Now?

AI research has existed since the 1950s. So why is it only powerful now?

Three things converged at once:

**1. Scale of data** — The internet gave AI an almost unlimited supply of human-generated text, images, and knowledge to learn from.

**2. Computing power** — GPUs (originally built for video games) turned out to be perfect for training AI. The cost per computation dropped by 1,000× in 10 years.

**3. A breakthrough in architecture** — The "transformer" (the T in ChatGPT) was a 2017 research breakthrough that made language models dramatically more capable. Almost all modern AI is built on this foundation.

None of these on their own would have been enough. Together, they created a step-change — not gradual improvement, but a cliff edge.

---

## Why Does This Matter for *You*?

Because this technology is now in your hands.

Not in a lab. Not behind a corporate firewall. In your browser. For free.

The question isn't whether AI will change your industry, your profession, your job. **It already is.** The question is whether you'll be the person who *uses* it or the person who watches others use it.

This programme exists to make sure you're the former.

In the next four lessons, you'll see exactly what AI can do, where it's already transforming real jobs, what the career opportunity looks like, and how this programme will take you from curious to capable.

**Let's go.**
''',
        'example_prompt': '''## What to Take Away from Lesson 1

- **AlphaFold solved 200 million protein structures** — more than 50 years of human science combined. AI isn't hype. It's producing real results at unprecedented scale.
- ChatGPT hit 100 million users in 2 months. GPT-4 passed the Bar Exam in the top 10%. AI has crossed a threshold of *genuine usefulness*.
- **Generative AI** is the category that matters right now — AI that creates text, images, code, audio, and video on demand.
- The breakthrough happened because of **data + compute + transformers** — three things that converged around 2022.
- The technology is already in your hands. The only question is whether you use it.

**Next: What exactly can AI do? The capabilities will surprise you →**
''',
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 2 — What AI can do
    # ─────────────────────────────────────────────────────────────────────────
    {
        'title': 'Lesson 2: What AI Can Actually Do',
        'description': 'A tour of the genuinely astonishing things AI can do today — across writing, coding, research, creativity, and analysis.',
        'difficulty': 'beginner',
        'order': 2,
        'points': 10,
        'instructions': '''## The Capabilities That Will Change Your Mind

You might have tried an AI chatbot and thought: *"Okay, it's a fancy search engine."*

Stay with me. Because what AI can do in 2025 goes far beyond answering questions.

---

## Write Anything. Seriously, Anything.

Need a professional email declining a client? A detailed business proposal? A legal contract? A compelling job application? A speech for your friend's wedding?

Describe what you need. Give context. AI produces a high-quality first draft in seconds.

And not a generic template. A *good* draft. One that sounds like a professional wrote it, tailored to your specific situation.

Lawyers are using AI to draft contracts they used to spend hours on. Marketers are producing a month of social media content in an afternoon. Authors are using AI as a creative collaborator — bouncing ideas, exploring plot directions, overcoming writer's block.

> **Real example:** A solo consultant described the following to Claude: "I need a proposal for a retail client looking to reduce inventory costs by 15%. They're a mid-size fashion brand. Our solution involves AI-powered demand forecasting." Claude produced a 4-page professional proposal, complete with methodology, pricing structure, and projected ROI — in under 30 seconds.

---

## Write Code From a Description

You don't need to know how to code.

Describe what you want a programme to do, in plain English. AI writes the code.

"Write me a Python script that reads a spreadsheet of sales data and produces a weekly summary report, automatically emailed to me every Monday morning."

Done. Functional code. With explanations.

Experienced developers are using AI to code **twice as fast** — writing the skeleton of a feature and having AI flesh it out, generate test cases, find bugs, and write documentation. What used to take a day takes an hour.

For non-coders, AI has opened up an entirely new capability: the ability to automate things, build tools, and create digital products — without learning programming syntax.

---

## Research at Machine Speed

Imagine you need to understand a topic fast. A competitor's market position. A medical condition. A legal ruling. A technical concept.

Previously: hours of reading, synthesising, note-taking.

Now: paste in a document (or several), ask AI to summarise, extract key points, compare sources, and highlight implications.

**AI can read a 100-page report and give you a sharp, accurate executive summary in 30 seconds.**

Researchers are using AI to process hundreds of academic papers at once — synthesising findings that would have taken months to manually review. Journalists use it to analyse datasets. Consultants use it to prepare client briefings in a fraction of the time.

---

## Create Images, Music, and Video From Words

This is where people's jaws drop.

Type: *"A photorealistic image of a futuristic office overlooking a cityscape at sunset, with two people having a meeting."*

Midjourney, DALL-E, Adobe Firefly — any of these tools will produce a stunning, original image in seconds. Designers use this for concept mockups, marketing materials, product prototypes.

Now add music: **Suno** and **Udio** generate full songs — with vocals, instrumentation, production — from a text prompt. "An upbeat Afrobeat track with a positive message about technology."

Video is coming fast. **Sora** (OpenAI) can generate cinematic short videos from text descriptions. The quality will be indistinguishable from human-made footage within 2-3 years.

---

## Analyse Documents and Extract Insight

Upload a contract. Ask AI to highlight any unusual clauses, flag potential risks, and summarise the key obligations.

Upload a set of financial statements. Ask AI to identify trends, calculate ratios, and flag anything concerning.

Upload your CV and a job description. Ask AI what's missing, what to emphasise, and how to tailor it.

This is the kind of analysis that used to require a specialist, an hour, and a fee. Now it takes two minutes.

---

## Translate — And Communicate Across Languages

AI translation is no longer awkward or robotic. Modern AI translates with natural fluency, including idioms, tone, and cultural context.

But it goes further. You can give AI your content in English and ask it to adapt it for a German-speaking audience — not just translate the words, but adapt the references and examples to resonate culturally. That's a completely different capability.

---

## The Implication

Think about what you just read.

In a single afternoon, using free tools:
- You could draft a professional business proposal
- Create the images and branding for it
- Research your competitor landscape
- Build a data analysis tool (in code) to back up your numbers
- Translate everything into a second language

None of this required expertise in writing, design, research, coding, or translation.

**AI has democratised capability.** The skills that used to take years to develop — or thousands of pounds to hire — are now available to anyone who knows how to work with these tools.

Learning to work with them *well* is the skill this programme teaches.
''',
        'example_prompt': '''## What to Take Away from Lesson 2

- AI can **write anything** — proposals, contracts, emails, marketing copy, creative content — at professional quality, in seconds
- **Code from a description** — you don't need to be a developer to automate tasks and build tools
- **Research at machine speed** — AI can read and synthesise hundreds of documents faster than you can read one
- **Image, music, and video generation** — creative content that used to require specialists is now accessible to anyone
- **Document analysis** — upload a contract, financial report, or CV and get expert-level insight instantly
- AI has **democratised capability** — the question is who learns to use it well

**Next: Who's already winning with this? Real stories from real workplaces →**
''',
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 3 — AI transforming real jobs
    # ─────────────────────────────────────────────────────────────────────────
    {
        'title': 'Lesson 3: The People Already Winning',
        'description': 'Real stories of professionals who transformed their work with AI — and what it could look like in your field.',
        'difficulty': 'beginner',
        'order': 3,
        'points': 10,
        'instructions': '''## AI Isn't Changing the Future. It's Changing Right Now.

The people winning with AI aren't mostly engineers or tech founders. They're accountants, lawyers, marketers, healthcare workers, small business owners, and educators.

They didn't wait to see how things played out. They picked up the tools, learned to use them, and quietly got significantly better at their jobs.

Here's what that looks like in practice.

---

## The Paralegal Who Became 3× More Productive

A paralegal at a law firm in London used to spend 6-7 hours a day reviewing contracts — reading every clause, cross-referencing obligations, flagging anomalies.

She started using Claude (the AI used in this platform) to do the initial review. She'd upload the contract, ask it to:
- Summarise the key terms
- Highlight any unusual or potentially risky clauses
- Compare obligations against standard templates

The AI would return a detailed analysis in under a minute.

She still reviewed everything — the AI wasn't making the final call. But she was reviewing a *summary* and *flagging* rather than reading raw text from scratch. She went from reviewing 3 contracts a day to 9.

**Her billable hours didn't change. Her output tripled.**

---

## The Marketer Who Produces a Month of Content in a Day

A marketing manager at a mid-size ecommerce company was the sole content creator. Blog posts, email campaigns, social media, product descriptions — all of it on her shoulders. She was drowning.

She built a simple workflow:
1. Give AI a product, a target audience, and a brand tone of voice
2. AI generates 10 social media posts, 3 email subject lines, and a 500-word blog intro
3. She picks the best versions, edits for brand voice, and schedules

One afternoon per week now produces her entire month of content.

**She's not using AI to replace her creativity. She's using it to remove the blank page problem and the volume problem.**

---

## The Developer Who Ships Twice as Fast

A software developer at a fintech startup described his workflow: he writes the architecture and the logic, then uses AI (GitHub Copilot and Claude) to write the boilerplate code, generate test cases, write the documentation, and review his code for bugs.

"I spend my time thinking about the hard problems. AI handles the repetitive parts. I'm probably shipping features twice as fast as I was 18 months ago."

He noted something important: **AI makes mistakes. But it makes them fast, and you can correct them fast.** The net result is still dramatically faster than doing everything manually.

---

## The Small Business Owner Who Automated Her Admin

A hair salon owner in Manchester was spending Sunday evenings doing admin — booking confirmations, supplier emails, social media posts, accounting queries. 4 hours every week.

She used AI to:
- Write template responses for common client queries
- Draft supplier emails in seconds
- Create her monthly social content calendar
- Summarise her weekly financials from a spreadsheet

**She got her Sunday evenings back.** The business runs smoother. Her stress is down.

She has no tech background. She learned to use AI tools in a few hours. The return on that time investment is ongoing.

---

## The Healthcare Professional Who Caught What Others Missed

A nurse practitioner started using AI as a reference tool — not to diagnose patients, but to rapidly surface information. When a patient presented with a rare combination of symptoms, she described the case to an AI tool and asked it to suggest differential diagnoses.

The AI surfaced a rare autoimmune condition she hadn't considered. She raised it with the specialist. **The patient was correctly diagnosed after years of unexplained symptoms.**

The AI wasn't the doctor. She was. But AI gave her a resource that would have taken hours to research manually — in seconds.

---

## What These People Have In Common

They're not geniuses. They're not tech workers. They didn't spend a year learning complex systems.

They did one thing: **they learned to communicate effectively with AI.** They learned what to ask, how to provide context, how to get consistently useful output.

That's prompt engineering. That's what Module 1 of this programme teaches.

---

## What Does This Look Like in Your Field?

Almost every professional role has tasks AI can accelerate. Here are examples by sector:

**Healthcare:** Clinical notes, patient communication, research summaries, protocol drafting
**Legal:** Contract drafting and review, case research, regulatory compliance checks
**Finance:** Report generation, data analysis, client summaries, risk flagging
**Education:** Lesson planning, marking feedback, resource creation, differentiation
**Marketing:** Content creation, campaign briefs, competitor analysis, ad copy
**HR:** Job descriptions, interview questions, policy documents, onboarding materials
**Operations:** Process documentation, SOP writing, supplier emails, data summarisation

**The question isn't *whether* AI applies to your field. It's *which tasks* to start with.**

---

## The Productivity Gap is Growing

Workers using AI report completing tasks 40–60% faster on average. That's not a small improvement — that's the difference between being good at your job and being exceptional.

And as AI tools improve (which they're doing fast), that gap will grow.

The people building these skills now are not just more productive today. They're better positioned for everything that comes next.
''',
        'example_prompt': '''## What to Take Away from Lesson 3

- Real professionals — not just tech workers — are transforming their work with AI *right now*
- A paralegal tripled her contract review output. A marketer reduced a month of content work to one afternoon. A developer ships twice as fast.
- What they all have in common: **they learned to communicate effectively with AI** — that's the skill this programme teaches
- AI applies to almost every professional role — healthcare, legal, finance, education, marketing, HR, operations
- Workers using AI report **40–60% productivity improvement** — and the gap is growing
- The time to start is now, while the advantage is still real

**Next: What this means for your career — and the opportunity in front of you →**
''',
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 4 — Career opportunity
    # ─────────────────────────────────────────────────────────────────────────
    {
        'title': 'Lesson 4: Your Career in the AI Era',
        'description': 'The career opportunity is real and it\'s right now. Understand the salary premium, the new roles emerging, and why the timing matters.',
        'difficulty': 'beginner',
        'order': 4,
        'points': 10,
        'instructions': '''## There's a Window Open Right Now. Here's How Wide It Is.

Let's talk about the career reality of AI — not in abstract terms, but in specifics.

---

## The Numbers Are Real

Research firm **McKinsey** estimates AI could add **$4.4 trillion in annual value** to the global economy — most of it through productivity gains in professional work.

That value has to go somewhere. And a significant portion of it goes to the people who know how to capture it.

Here's what the data looks like on an individual level:

- Professionals with AI skills command on average a **40% salary premium** over comparable roles without AI proficiency
- **74% of companies** are actively seeking employees with AI skills — across *all* departments, not just tech
- AI-literate candidates are **3× more likely to be shortlisted** in competitive recruitment processes
- Workers using AI tools report productivity improvements of **40–60%** — which directly translates into faster career progression, higher output, and more value delivered

---

## New Jobs That Didn't Exist 3 Years Ago

An entirely new category of professional roles is being created:

**AI Prompt Engineer**
Designs the instructions and workflows that direct AI systems within organisations. Think of this as the person who makes AI useful at scale. Starting salaries range from £40,000 to £85,000 — and climbing.

**AI Operations Manager**
Manages the rollout and optimisation of AI tools across a business. Identifies where AI creates value, trains teams to use it, measures results. A hybrid of operations and technology.

**AI Content Strategist**
Creates, scales, and quality-controls content produced with AI tools. This is not just a marketer — it's someone who understands how to use generative AI for content while maintaining brand standards.

**AI-Augmented Analyst**
A data or business analyst who uses AI to process and synthesise information 5-10× faster than traditional methods. Produces insights that would have taken a team a week — alone, in a day.

**AI Security Specialist**
Uses AI to detect threats, analyse vulnerabilities, and automate security monitoring. Cybersecurity has become one of the fastest-growing intersections with AI.

These roles are live on LinkedIn and Indeed. They're not hypothetical.

---

## It's Not Just New Roles — Every Existing Role Is Changing

More importantly: **AI skills are becoming table stakes for existing jobs.**

Think about what happened with email in the 1990s. Being able to use email went from "impressive optional extra" to "of course you have email" in about 5 years.

The same trajectory is happening with AI. Right now, knowing how to use AI tools is a differentiator. In 3-5 years, it'll be an expectation.

The question is: do you build those skills now, when they make you stand out? Or do you build them later, when everyone else has them too?

---

## A Common Misconception

> *"AI skills are for tech people."*

This is wrong. And it's an important one to address.

The people capturing the most value from AI right now are overwhelmingly **not** software engineers or data scientists. They're:

- A lawyer who can review 9 contracts a day instead of 3
- A marketer who produces a month of content in an afternoon
- A nurse practitioner who surfaces rare conditions in minutes
- A small business owner who got her Sunday evenings back

**AI literacy is not about coding. It's not about machine learning. It's about knowing how to work *with* AI effectively** — which tasks to delegate to it, how to give it proper context, how to evaluate and refine its output.

That's a skill anyone can develop. This programme will take you from zero to competent — and beyond.

---

## What AI Literacy Actually Means

Being AI literate in 2025 means:

**1. Knowing which tool to use for which task**
ChatGPT vs Claude vs Gemini vs Midjourney — they're not interchangeable. Knowing the landscape lets you pick the right tool and get better results faster.

**2. Communicating clearly and precisely with AI**
This is prompt engineering. The difference between a mediocre result and an excellent one often comes down to how clearly you've explained the task, the context, and the expected output.

**3. Designing AI-powered workflows**
Not just using AI for one-off tasks, but building repeatable systems where AI handles predictable work automatically.

**4. Reviewing and refining AI output**
AI produces first drafts, not final products. Knowing how to evaluate quality, catch errors, and direct improvements is an essential part of the loop.

**5. Using AI responsibly**
Understanding the limits — hallucinations, bias, confidentiality — so you use it in ways that protect rather than expose you.

All five of these are covered in this programme, across four practical modules.

---

## The Window Is Open. For Now.

Here's the honest framing.

First-mover advantage in technology is real but time-limited. People who learned to build websites in the early 2000s had a decade of advantage. People who learned digital marketing in 2008 rode a wave that's still paying off. People who learned data analysis in 2012 are now in senior roles that pay extremely well.

AI is that moment, but bigger. And it's happening faster.

The people who will look back on 2025 and 2026 as a turning point in their career are the ones who didn't wait to "see how it all plays out" — they engaged, learned, and built.

That's what you're doing right now.
''',
        'example_prompt': '''## What to Take Away from Lesson 4

- AI-literate professionals earn on average a **40% salary premium** — and are 3× more likely to be shortlisted
- New roles like **AI Prompt Engineer**, **AI Operations Manager**, and **AI-Augmented Analyst** are live and paying well
- AI skills are becoming baseline expectations — the advantage window is real *right now*, and it won't stay open forever
- **AI literacy is not about coding** — it's about knowing how to work with AI effectively: choosing tools, crafting prompts, building workflows, reviewing output
- Every industry and every professional role is affected — healthcare, legal, marketing, finance, education, and more
- The pattern is consistent: people who build skills early in a technology shift come out significantly ahead

**Next: How this programme is structured — and what you're about to unlock →**
''',
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 5 — Programme orientation
    # ─────────────────────────────────────────────────────────────────────────
    {
        'title': 'Lesson 5: Your Programme — What\'s Coming',
        'description': 'Get excited about what comes next. A preview of all four modules, how the platform works, and how to make the most of every lesson.',
        'difficulty': 'beginner',
        'order': 5,
        'points': 10,
        'instructions': '''## You've Seen the Opportunity. Now Here's Your Roadmap.

You know what AI can do. You've seen who's winning with it. You understand the career stakes. Now let's talk about what *you're* going to build — and how.

---

## The Programme at a Glance

This programme is structured as four modules, each building on the last. Here's what's waiting for you:

---

### 🎯 Module 1 — AI Prompt Engineering Foundation
*15–20 hours · 30 challenges · Beginner → Intermediate*

This is where everything starts. **Prompt engineering** is the art and science of communicating with AI to get consistently excellent results.

You'll learn:
- The anatomy of a great prompt (context, tone, format, constraints)
- How to get professional-quality output every time
- Role-playing and persona techniques
- Chain-of-thought prompting for complex reasoning
- How to handle failures and iterate to improve results
- Real-world prompting for specific industries and tasks

By the end, you'll be getting results from AI that most people don't know are even possible. The gap between someone who "just uses ChatGPT" and someone who knows prompt engineering is enormous — and you'll feel that gap close lesson by lesson.

**This module unlocks everything else.**

---

### 🛠️ Module 2 — AI Tools & Platform Mastery
*15–20 hours · 24 challenges · Intermediate*

AI isn't one tool. It's an ecosystem. This module gives you the full map.

You'll work hands-on with:
- **ChatGPT, Claude, and Gemini** — the big three, their strengths, when to use each
- **Microsoft Copilot** — AI inside Word, Excel, PowerPoint, Teams, and Outlook
- **Image generation** — Midjourney, DALL-E, Adobe Firefly
- **AI for audio and video** — ElevenLabs, Runway, Sora
- **No-code automation** — Zapier, Make, and how to build AI-powered workflows
- **Specialist AI tools** for research, writing, coding, and analysis

By the end, you'll have a genuine mastery of the AI landscape. You'll know which tool to reach for in any situation — and how to use it to its full potential.

---

### 🤖 Module 3 — AI Agents & Automation
*15–20 hours · 22 challenges · Advanced*

This is where things get genuinely exciting.

An **AI agent** is an AI system that doesn't just respond to questions — it takes actions, makes decisions, and operates continuously on your behalf.

You'll learn:
- How AI agents work and why they're different from chatbots
- Building your first automated AI workflow
- Connecting AI to real-world data (emails, calendars, spreadsheets, APIs)
- Creating agents that monitor, research, and act — while you're doing something else
- Deploying AI systems that save you hours every week, automatically

Imagine: an AI that monitors your inbox, prioritises what needs your attention, drafts responses for routine messages, and flags urgent items — all without you touching it. That's what you'll build.

**You go from *using* AI to *deploying* AI.**

---

### 🏆 Module 4 — Your Capstone Project
*15–20 hours · 15 challenges · Expert*

You choose your specialisation:

**💻 Track A: Coding with AI**
Build a real, functional AI-powered Python application — guided by AI every step of the way. You don't need prior coding experience. AI is your co-developer, explainer, and debugging partner. By the end, you'll have deployed a working application and a portfolio piece that demonstrates real capability.

**🔒 Track B: Cybersecurity with AI**
Complete a professional defensive security assessment using AI as your analysis tool. You'll work through vulnerability scanning, threat modelling, incident response, and security policy writing — all with AI augmenting your capability. A portfolio of real security deliverables awaits.

**Both tracks create tangible work you can show a potential employer, client, or business.**

---

## How Each Lesson Works

Every lesson in this programme is a **hands-on challenge** — not a passive video to watch.

The flow for each lesson:

1. **Read the task** — understand what you're being asked to do and why it matters in a real context
2. **Attempt it yourself** — write the prompt, code the solution, build the workflow
3. **Submit for evaluation** — your work is evaluated by **Claude AI** in real time
4. **Receive your score and feedback** — specific, detailed feedback explaining what worked and how to improve
5. **Pass (70+ score) to unlock the next lesson**

You can retry as many times as you like. The feedback is specific enough to guide you to a pass if you engage with it seriously.

---

## Features Built Into the Platform

**📎 File Upload** — Upload PDFs, images, spreadsheets, or documents directly in the challenge. Work with real files, just like a real professional context.

**🎤 Voice Input** — Dictate your prompts with the microphone button. Think out loud. The platform transcribes in real time.

**💻 Code Editor** — Module 4A includes a full Python editor with syntax highlighting, code running (simulated), and AI code review.

**🆘 AI Help Mode** — Stuck? Ask AI for guidance without it affecting your scored submission. Use it to understand the task better, not to cheat.

**🏆 Points and Achievements** — Every challenge awards points. Achievements unlock at milestones. The leaderboard lets you see how you compare. The gamification isn't just for fun — it keeps you moving through 60+ hours of content.

---

## Three Tips to Get the Most Out of This

**1. Be consistent, not intense.**
The learners who complete this programme don't do it in marathon sessions. They do a lesson or two a day, consistently. Build a habit, not a sprint.

**2. Write your own prompts. Always.**
It's tempting to take a peek at what seems like the "right answer." Resist. The learning happens in the *attempt* — in the friction of figuring out what to say and seeing how AI responds. You can't fast-track that.

**3. Read the feedback as if it's personal coaching.**
Because it is. Claude's evaluation feedback is specific to your submission. It tells you exactly what worked, what didn't, and what to try differently. Use it.

---

## You're Genuinely Ready

Four lessons ago, you didn't know how this technology worked, what it could do, or what the opportunity looked like. Now you do.

**You know:**
- Why AI is the biggest technology shift in 100 years
- What it can actually do (and what's genuinely impressive)
- Who's already winning with it and how
- What the career opportunity looks like and why now is the time
- Exactly what's coming in this programme and how to get the most from it

The moment you click "Mark as Complete" and the next button appears, you'll be unlocking **Module 1 — AI Prompt Engineering Foundation** — where the real hands-on training begins.

**Welcome. Let's build something extraordinary.**
''',
        'example_prompt': '''## What to Take Away from Lesson 5

- **Module 1** (Prompt Engineering): the foundational skill — learn to communicate with AI like a professional
- **Module 2** (AI Tools): master the full ecosystem — ChatGPT, Claude, Copilot, image tools, automation platforms
- **Module 3** (Agents & Automation): go from *using* AI to *deploying* AI that works for you continuously
- **Module 4** (Capstone): choose Coding with AI or Cybersecurity with AI — produce real portfolio work
- Each lesson is a **hands-on challenge**, evaluated in real time by Claude AI, with specific feedback to guide improvement
- Features include: file upload, voice input, code editor, help mode, and a full achievements system
- **Best advice:** consistency beats intensity — write your own prompts — read the feedback carefully

**You're ready. Module 1 unlocks now. →**
''',
    },
]


class Command(BaseCommand):
    help = 'Populate the free Introduction to AI module (5 lessons)'

    def handle(self, *args, **options):
        self.stdout.write('Creating Introduction to AI module...\n')

        module, created = Module.objects.get_or_create(
            title='Introduction to AI',
            defaults={
                'description': (
                    'Five free lessons that will change how you see AI — and your career. '
                    'Discover what AI can truly do, who\'s already winning with it, and why '
                    'the skills you\'re about to build are among the most valuable of this decade. '
                    'No subscription required.'
                ),
                'order': 0,
                'icon': '🚀',
                'duration_hours': 2,
                'module_type': 'intro',
                'is_free': True,
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'✓ Created module: {module.title}'))
        else:
            self.stdout.write(f'→ Module already exists: {module.title}')
            if not module.is_free:
                module.is_free = True
                module.save()
                self.stdout.write(self.style.SUCCESS('  ✓ Marked as free'))

        created_count = 0
        for lesson_data in INTRO_LESSONS:
            lesson, lesson_created = Challenge.objects.get_or_create(
                module=module,
                title=lesson_data['title'],
                defaults=lesson_data,
            )
            if lesson_created:
                created_count += 1
                self.stdout.write(f'  ✓ Lesson {lesson.order}: {lesson.title}')
            else:
                # Update content for existing lessons
                for field, value in lesson_data.items():
                    setattr(lesson, field, value)
                lesson.save()
                self.stdout.write(f'  ↻ Updated: {lesson.title}')

        # Sequential prerequisites
        lessons = list(Challenge.objects.filter(module=module).order_by('order'))
        for i, lesson in enumerate(lessons):
            if i > 0:
                lesson.prerequisite_challenge = lessons[i - 1]
                lesson.save()

        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Introduction module ready ({len(lessons)} lessons, {created_count} newly created)'
        ))
        self.stdout.write('''
Programme structure:
  🚀 Introduction to AI     (5 free lessons — no subscription)
  🎯 Module 1 — Prompt Engineering   (30 lessons — subscription required)
  🛠️  Module 2 — AI Tools             (24 lessons — subscription required)
  🤖  Module 3 — Agents & Automation  (22 lessons — subscription required)
  🏆  Module 4 — Capstone Project     (15 lessons — subscription required)
''')
