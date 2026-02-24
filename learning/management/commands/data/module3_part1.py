"""
Module 3 Part 1: Meet Your AI Agents — "From Chat to Action"
Challenges 1-8: Understanding AI agents and building your first custom assistants (3-4 hours)
"""

MODULE3_PART1_CHALLENGES = [
    {
        'title': 'Question 1: From Chat to Agents — What\'s the Difference?',
        'description': 'Understand how AI agents go beyond conversation to plan and execute tasks',
        'difficulty': 'beginner',
        'order': 1,
        'points': 20,
        'instructions': '''You've mastered AI chat. Now it's time to understand the next level: AI agents.

**What You'll Learn:**
- What makes an AI agent different from an AI chatbot
- How agents plan, use tools, and take actions — not just respond
- Why the shift from "asking AI" to "deploying AI" changes everything

**Chat AI vs Agent AI:**

**Chat AI (what you've been doing):**
- You ask → AI responds → Done
- Single message, single response
- AI is passive — it waits for your instructions
- Output is text you act on

**Agent AI (what's next):**
- You give a goal → AI plans how to achieve it
- Breaks tasks into sub-steps and executes each one
- Uses tools (search, code execution, file reading, API calls)
- Can take actions: send emails, update databases, schedule tasks
- Loops until the goal is completed

**A Simple Example:**

Chat: "Research the best laptops under £800" → AI gives you a text list
Agent: "Research the best laptops under £800, compare them in a table, check current prices on three websites, and email me a summary" → AI does all of this, not just the text

**Your Challenge:**
Compare how a chat AI and an agent AI would handle the same business task — showing what makes agents genuinely different.

**The task:** Your manager asks you to "find out what our competitors are doing on social media and summarise it in a report."

Write:
1. How you'd currently handle this with chat AI (step-by-step, multiple prompts)
2. How an AI agent would handle the same task (what steps it would autonomously take)
3. What the agent can do that chat AI can't — and what would still need a human''',
        'example_prompt': '''Help me understand the practical difference between AI chat and AI agents through a real work scenario.

**THE TASK:**
My manager has asked me to: "Research what our top 3 competitors are doing on social media and create a summary report I can share with the team."

Competitors: Apex Solutions, BlueLine Tech, and Momentum Digital (fictional B2B software companies)

---

**PART 1 — THE CHAT AI APPROACH (current way)**

Walk me through exactly how I'd do this using standard AI chat. Show each individual prompt I'd need to type, in order:

Step 1: [What prompt would I type first?]
Step 2: [What would I ask next?]
...and so on until the report is done

Be realistic — show all the manual steps including things I'd have to do myself (like actually looking at their social media pages).

Estimate: How many separate AI interactions would this take? How much of my time would be needed?

---

**PART 2 — THE AGENT APPROACH (what AI agents can do)**

Now describe how an AI agent (with access to web browsing, data processing, and document creation tools) would handle the exact same task.

Show:
- What goal I'd give the agent (my single input)
- Each step the agent would autonomously plan and execute
- What tools it would use at each step (web search, data extraction, writing, formatting)
- What the final output would look like
- What it would take to go from "I give the goal" to "report is ready"

---

**PART 3 — WHAT AGENTS CAN AND CAN'T DO**

Be honest with me:
1. What can an AI agent do in this scenario that chat AI genuinely cannot?
2. What would still require human judgment or decision-making even with an agent?
3. What's the risk of letting an agent run this task unsupervised?
4. For THIS specific task — would you use an agent or chat AI in 2025/2026? Why?

---

**PART 4 — THE SHIFT IN THINKING**

How should someone change how they think about AI once they start using agents?
- What new mental models are needed?
- What habits from chat AI need updating?
- What's the one most important thing to understand about working with agents?''',
    },
    {
        'title': 'Question 2: How AI Agents Think',
        'description': 'Understand task decomposition and how agents plan and execute complex goals',
        'difficulty': 'beginner',
        'order': 2,
        'points': 20,
        'instructions': '''AI agents don't just answer questions. They plan. They break goals into steps, execute each one, and adapt based on what they find.

**What You'll Learn:**
- How agents decompose complex goals into sub-tasks
- The "plan → execute → review → adapt" cycle
- How to give an agent a goal it can actually execute

**The Agent Thinking Process:**
When you give an agent a goal, it typically:
1. **Analyses** the goal — what does "done" look like?
2. **Decomposes** it — what sub-tasks need to happen?
3. **Sequences** them — in what order? What depends on what?
4. **Executes** each step using available tools
5. **Reviews** the output — did this step work?
6. **Adapts** — if something went wrong, how to recover?

**This is called "ReAct" thinking** (Reason + Act) and it's why agents can handle tasks that would break a simple chatbot.

**What Agents Need to Know:**
- A clear goal (not a vague task)
- What "done" looks like (success criteria)
- What tools are available to use
- What constraints to stay within (budget, time, permissions)

**Your Challenge:**
Give an AI agent a complex goal and map out the full execution plan.

**The goal:** "Create a 4-week content plan for our company LinkedIn page, including research on the best-performing content types in our industry, 20 draft posts, a posting schedule, and a simple tracker I can use."

Your task:
1. Write the goal as you'd give it to an agent (clear, complete, with success criteria)
2. Map out every sub-task the agent would need to execute
3. Identify the dependencies between sub-tasks
4. Show what the completed output would look like step by step''',
        'example_prompt': '''I want to understand how an AI agent would think through and execute a complex content planning task. Help me map the full agent execution plan.

**THE GOAL I'M GIVING THE AGENT:**

"Create a complete 4-week LinkedIn content plan for TechNova, a B2B project management software company targeting operations managers in SMEs (10-200 employees). The plan should include: research on what content performs best in our industry, 20 ready-to-post drafts, a publication schedule, and a tracking template. The company's brand voice is: professional but approachable, insight-led, never salesy."

---

**PART 1 — REFINING THE GOAL**

Before the agent starts, what clarifying questions should it ask me to ensure it can succeed?

List every ambiguity in my goal that could cause the agent to produce the wrong output if left unclear. Then suggest the improved, complete goal brief that includes all the necessary information.

---

**PART 2 — THE FULL TASK DECOMPOSITION**

Map out every sub-task the agent would need to complete to achieve this goal.

For each sub-task:
- Task name and description
- What tool would the agent use? (web search, AI writing, data analysis, document creation, etc.)
- What input does this task need?
- What output does this task produce?
- Which tasks must happen before this one? (dependencies)

Present this as a structured execution plan showing the logical order.

---

**PART 3 — THE EXECUTE → REVIEW → ADAPT CYCLE**

Pick 2 of the sub-tasks from Part 2 and show what the "execute → review → adapt" cycle would look like in practice:

**For each task:**
- What would a successful execution look like?
- What could go wrong or produce an unexpected result?
- How would the agent detect that something went wrong?
- What would it do to adapt and recover?

---

**PART 4 — THE FULL OUTPUT**

Show me what the complete agent output would look like when done:
- The research findings (key insights, not a long report — just the most actionable points)
- 5 sample post drafts from the 20 (enough to show quality and variety)
- The 4-week publication schedule (as a table)
- The tracking template (columns and structure)

Make the 5 sample posts genuinely good — something I'd actually post.

---

**PART 5 — HUMAN OVERSIGHT CHECK**

What decisions in this entire process should NOT be left to an agent alone?
Where would I, as the human, need to review and approve before the agent continues?

Design a simple "human checkpoint" system for this workflow.''',
    },
    {
        'title': 'Question 3: Build a Custom GPT',
        'description': 'Design a personalised AI assistant with specific skills, knowledge, and personality',
        'difficulty': 'intermediate',
        'order': 3,
        'points': 25,
        'instructions': '''Custom GPTs (and similar custom AI assistants) let you build a specialised AI tool tailored to a specific role, domain, or audience.

**What You'll Learn:**
- What a Custom GPT is and how it differs from a general AI
- How to write system instructions that create the right AI persona
- Real use cases where a specialised assistant outperforms a general one

**What is a Custom GPT?**
A Custom GPT is a version of ChatGPT that you configure with:
- **A specific role and purpose** — who is this AI and what does it do?
- **Custom instructions** — how should it behave, respond, and communicate?
- **Knowledge files** — documents it should know and reference
- **Capabilities** — can it search the web, generate images, run code?
- **Conversation starters** — suggested prompts to guide users

**When Custom GPTs Excel:**
- A role-specific assistant (interview coach, writing coach, customer service rep)
- A company-specific tool (knows your products, your policies, your voice)
- A teaching tool (explains things in a specific way to a specific audience)
- A workflow tool (always produces a specific output format)

**Your Challenge:**
Build a complete Custom GPT specification for a specific use case.

**Choose one:**
- "My Interview Coach" — a custom AI that helps people prepare for job interviews
- "Social Media Manager" — creates on-brand content for a specific business
- "Learning Companion" — helps someone study a specific topic they're learning
- Your own idea (describe it clearly)

Write the full specification: name, purpose, system instructions, knowledge overview, example interactions, and conversation starters.''',
        'example_prompt': '''I want to design a complete Custom GPT specification. I'm building "Interview Ace" — a personalised interview coaching assistant.

---

**CUSTOM GPT: "Interview Ace"**

**Purpose:** Help job seekers prepare for job interviews — from understanding the role to practising answers to building confidence.

**Target User:** Someone who has an interview coming up and wants focused, practical help to prepare.

---

**PART 1 — THE SYSTEM INSTRUCTIONS**

Write the full system instructions for Interview Ace. This is what gets entered into the Custom GPT's "Instructions" field. It should define:

1. **Role and Identity:** Who is Interview Ace? (Give it a professional identity — not just "an AI assistant")

2. **Core Mission:** What is it fundamentally trying to achieve for each user?

3. **Behaviour Rules:** How does it conduct itself?
   - How does it gather information at the start of a conversation?
   - How does it structure its coaching?
   - When does it push back vs encourage?
   - What does it never do?

4. **The Coaching Framework:** Interview Ace should use a specific approach — design one:
   - How does it diagnose what the user needs?
   - How does it structure a practice session?
   - How does it give feedback on practice answers?
   - How does it build on progress across the conversation?

5. **Output Format Rules:** How should responses look?
   - Length guidelines
   - Whether to use bullet points vs narrative
   - How to present feedback (sandwich method? Direct critique?)

Write these as actual instructions I'd paste into the Custom GPT settings — not a description of what the instructions should cover.

---

**PART 2 — KNOWLEDGE OVERVIEW**

What knowledge files should Interview Ace have access to?

Design 3 knowledge documents it should contain:
- Document name and purpose
- What information it should include
- How it should use this information in conversations

Examples to consider: interview techniques guide, common interview questions bank, body language and confidence tips, STAR method framework, industry-specific vocabulary guide.

---

**PART 3 — CONVERSATION STARTERS**

Write 5 conversation starter suggestions that appear when someone opens Interview Ace — prompts that immediately help users get started.

Make them specific and varied — covering different types of interview prep needs.

---

**PART 4 — EXAMPLE INTERACTIONS**

Show me 2 example conversations that demonstrate Interview Ace working at its best:

**Example A:** A nervous first-time job seeker preparing for their first professional interview
**Example B:** An experienced professional preparing for a senior leadership role interview

For each: show the opening question/message and Interview Ace's ideal first response.

---

**PART 5 — WHAT MAKES THIS BETTER THAN A GENERAL AI**

Compare: If someone asked a standard AI chat tool to help them prepare for an interview vs using Interview Ace — what specifically would be different?

List 5 concrete differences in the experience.''',
    },
    {
        'title': 'Question 4: Claude Projects & Persistent Workspaces',
        'description': 'Set up a persistent AI workspace with documents, context, and reusable outputs',
        'difficulty': 'intermediate',
        'order': 4,
        'points': 25,
        'instructions': '''Claude Projects (and similar features in other AI tools) let you create persistent workspaces where AI always has access to your documents, context, and past work.

**What You'll Learn:**
- What makes Projects different from regular conversations
- How to set up a Project for maximum productivity
- The types of work that benefit most from persistent workspaces

**What is a Claude Project?**
A Project is a dedicated AI workspace where you can:
- **Upload documents** that Claude always has access to (briefs, guidelines, templates)
- **Set project instructions** that apply to every conversation in the project
- **Maintain context** across multiple sessions — without re-explaining everything
- **Produce consistent outputs** that match your established formats and style

**When Projects Transform Your Work:**
- Long-running client work (always has the client brief available)
- Consistent content creation (always knows your brand voice)
- Research projects (always has access to your gathered sources)
- Team documentation (always aligned to company style guide)

**The Key Difference:**
Without Projects: Every conversation starts cold — you re-explain who you are, what the project is, what format you want.
With Projects: Every conversation starts informed — Claude knows the context, the documents, and the standards.

**Your Challenge:**
Design a complete Claude Project for a real ongoing work scenario.

**Choose a scenario:**
- A content marketing project for a specific client
- A long-running research project on a topic you're studying
- A product development project with brief, requirements, and brand guidelines
- A personal career development project

For your chosen scenario: define the project setup, write the project instructions, specify the documents to upload, and demonstrate what a productive Project session would look like.''',
        'example_prompt': '''Design a complete Claude Project for managing an ongoing content marketing client account. I'll use this as a template for all my client projects.

**THE CLIENT:**
"GreenPath" — a UK-based sustainable packaging company selling to food & beverage businesses. Target audience: procurement managers and sustainability leads at food brands with 50+ employees. Key messaging: cost-competitive sustainable packaging that helps brands meet their ESG targets.

**MY ROLE:**
Freelance content marketing consultant managing GreenPath's content strategy. I produce: monthly blog posts (2), LinkedIn content (12 posts/month), email newsletter (monthly), and quarterly case studies.

---

**PART 1 — PROJECT SETUP**

**A) Project Name and Description**
What should I name this project and write as the brief 2-sentence description?

**B) Project Instructions**
Write the full project instructions I'd set — the persistent context Claude has in every conversation in this project.

Cover:
- Client overview (who they are, what they do, who they sell to)
- Brand voice and tone guidelines (specific and detailed — not just "professional")
- What content I produce and at what frequency
- My role and what I need help with
- Non-negotiables: things the content must always/never do
- Output format preferences

Make these instructions comprehensive enough that a new session starts with Claude already knowing everything it needs.

**C) Documents to Upload**
List the 6 most important documents I should upload to this project. For each:
- Document name
- What it contains
- How Claude should use it

---

**PART 2 — FOUR SESSIONS IN ACTION**

Show me 4 different conversations I'd have inside this project — demonstrating the value of persistent context:

**Session 1: Monthly Blog Post**
Opening prompt + what Claude would produce (show the first 200 words of the blog post)

**Session 2: LinkedIn Content Week**
Opening prompt + what 3 posts would look like

**Session 3: Case Study First Draft**
Opening prompt + the case study outline Claude would produce

**Session 4: Strategy Review**
Opening prompt + what a strategic content review would look like

For each session: show how the project context (the instructions and documents) changes the output compared to starting from scratch.

---

**PART 3 — PROJECT MAINTENANCE**

How should I maintain this project over time?
- When to update the project instructions
- How to handle it when the client's focus shifts
- What to do when I've built up lots of past sessions
- How to use projects for multiple clients without mixing them up

---

**PART 4 — REUSABLE PROJECT TEMPLATE**

Based on this GreenPath example, create a generic "Client Content Project" template I can adapt for any new client. Give me the template with [PLACEHOLDERS] I fill in for each new client.''',
    },
    {
        'title': 'Question 5: Google NotebookLM',
        'description': 'Use AI to synthesise multiple documents into insights, briefings, and Q&A',
        'difficulty': 'intermediate',
        'order': 5,
        'points': 25,
        'instructions': '''Google NotebookLM is a specialised AI research tool that turns your own documents into a personal expert system.

**What You'll Learn:**
- What NotebookLM does and how it differs from general AI tools
- How to build a powerful research notebook from multiple sources
- How to use AI to synthesise, question, and extract from a document set

**What is NotebookLM?**
NotebookLM lets you upload multiple sources (PDFs, Google Docs, websites, audio files) and then:
- Ask questions about the combined content of all sources
- Generate briefing documents and summaries
- Create FAQ documents from your materials
- Explore connections between different sources
- Produce a podcast-style audio summary (Audio Overview)

**Why It's Different from General AI:**
Regular AI knows general things but might hallucinate specifics.
NotebookLM ONLY uses the documents you've provided — every answer is grounded in your specific sources, with citations.

**Ideal Use Cases:**
- Research projects with multiple papers and articles
- Competitive intelligence (collect competitor content, ask questions)
- Study and exam prep (upload your notes and textbooks)
- Legal/policy review (multiple documents, need to find specific clauses)
- Due diligence (company reports, news, filings in one place)

**Your Challenge:**
Design a NotebookLM research project on a topic that genuinely interests you.

Specify:
1. The topic and research goal
2. The 5-7 sources you'd upload (describe them realistically)
3. The 10 questions you'd ask across your document set
4. What outputs you'd generate (briefing doc, FAQ, summary)
5. How you'd use the finished research

Make this a real research scenario you'd actually find useful.''',
        'example_prompt': '''Design a complete NotebookLM research project. I'm researching whether to transition my small business from a sole trader to a limited company structure.

**THE RESEARCH GOAL:**
I've been running a freelance UX design business for 3 years as a sole trader. My revenue has grown to £75,000/year and I'm wondering if I should become a limited company for tax efficiency, credibility, and growth. I want to do proper research before I make this decision.

---

**PART 1 — MY SOURCE DOCUMENTS**

I'm going to upload these 7 sources to NotebookLM:

1. HMRC guidance: "Set up a private limited company" (gov.uk)
2. HMRC guidance: "Running a limited company" (gov.uk)
3. An accountant's blog: "Sole trader vs limited company: the complete 2025 guide" (fictional)
4. A freelancer community article: "When I switched to Ltd — the real pros and cons" (fictional)
5. HMRC: "Self Assessment tax returns" guidance
6. Companies House: "Company formation" guidance
7. My own notes document: "Current finances, clients, and business situation"

For each of these sources, tell me:
- What type of information it contains
- The most important questions I should extract from it
- One specific thing I should look for that often gets overlooked

---

**PART 2 — MY 10 RESEARCH QUESTIONS**

I'll ask NotebookLM these 10 questions across my document set. For each question, tell me:
- Which sources it would draw on to answer
- What a good answer would include
- Any limitations (what the documents might not cover)

**My questions:**
1. At what revenue level does it typically become tax-advantageous to switch to a limited company?
2. What are the ongoing compliance requirements and costs of running a limited company?
3. How does IR35 affect me if I'm doing mostly single-client work?
4. What happens to my existing contracts if I change my business structure?
5. Can I switch back to sole trader if limited company doesn't work out?
6. What are the differences in how I pay myself (salary vs dividends)?
7. What are the liability protections of a limited company actually worth in practice?
8. What do I need to do in terms of accounting and record-keeping?
9. How does a limited company structure affect my ability to take on employees later?
10. What are the practical steps and timeline to make the switch?

---

**PART 3 — THE OUTPUTS I'D GENERATE**

Using NotebookLM, I'd create these 3 outputs:

**A) Research Briefing Document**
What structure and sections should this briefing have? What information from my sources goes in each section?

**B) Decision FAQ**
Write 10 Q&A pairs that answer the most practical questions for someone in my exact situation — drawing from the sources I've described.

**C) Comparison Table**
Design a comparison table: Sole Trader vs Limited Company across the dimensions that matter most for my decision.

---

**PART 4 — THE DECISION**

Based on the research context I've described (£75K revenue, 3-year freelancer, UX design, considering growth):
What would well-rounded research likely conclude? What's the honest answer to my question?

And: What would a good accountant add that no amount of document research can tell me?''',
    },
    {
        'title': 'Question 6: Crafting Agent Personas',
        'description': 'Write system prompts that turn AI into specialist agents with distinct personalities and skills',
        'difficulty': 'intermediate',
        'order': 6,
        'points': 30,
        'instructions': '''The secret to specialised AI agents is the system prompt — the instructions that define who the agent is, how it thinks, and how it responds.

**What You'll Learn:**
- What makes a great agent persona specification
- How to create agents with distinct personalities and expertise
- How different agent personas produce genuinely different outputs

**The Elements of a Great Agent Persona:**

1. **Identity and Role:** Who is this agent? What is their professional background?
2. **Expertise:** What are they expert at? What are they NOT expert at?
3. **Personality and Communication Style:** How do they speak? Direct or nurturing? Formal or casual?
4. **Behavioural Rules:** What do they always/never do?
5. **Thinking Framework:** How do they approach problems in their domain?
6. **Output Preferences:** How do they structure their responses?

**Why Different Personas Matter:**
The same question asked to a "strict editor" persona vs a "enthusiastic coach" persona will produce fundamentally different outputs — not just in tone but in what they notice, what they prioritise, and what they recommend.

**Your Challenge:**
Create 3 distinct agent personas for the SAME underlying task: reviewing a piece of written content.

**The 3 Personas:**
1. **The Ruthless Editor** — high standards, direct, focused on professional quality
2. **The Encouraging Coach** — supportive, growth-focused, builds confidence
3. **The Audience Analyst** — data-minded, focused on reader response and effectiveness

For each persona: write the full system prompt, then show how they'd each respond to the same piece of writing. The difference between them should be immediately obvious.''',
        'example_prompt': '''Create 3 completely different agent personas for reviewing writing, then demonstrate each one on the same content sample.

**THE CONTENT SAMPLE TO REVIEW:**
(This is a draft "About Us" section for a startup's website)

"Welcome to BrightStart! We're a passionate team of innovators who are dedicated to revolutionising the way businesses approach their digital transformation journey. Our cutting-edge solutions leverage the latest technology to deliver exceptional value to our clients. With years of experience and a commitment to excellence, we're here to help your business thrive in today's competitive landscape.

Founded in 2021, BrightStart has grown from a small startup to a thriving company with clients across the UK and Europe. Our team of experts bring a wealth of knowledge and expertise to every project, ensuring that we consistently exceed expectations and deliver results that make a real difference.

We believe that success is a partnership, and we work closely with each client to understand their unique needs and goals. Our bespoke approach means that every solution we create is tailored specifically to you. Get in touch today to find out how BrightStart can help transform your business."

---

**PERSONA 1 — THE RUTHLESS EDITOR**

Write the full system prompt for this persona:
- Professional background and credentials (make them credible and specific)
- Communication style (how direct? what do they refuse to tolerate?)
- Their editing philosophy and framework
- What they always look for in writing (their specific checklist)
- What they will never do (false praise, vague feedback, etc.)
- Their output format

Then: Show this persona's review of the BrightStart copy above.

---

**PERSONA 2 — THE ENCOURAGING COACH**

Write the full system prompt for this persona:
- Professional background (different from the editor — perhaps a writing mentor or communications coach)
- Communication approach (what makes their encouragement genuine rather than hollow?)
- How they structure feedback to build confidence AND improve quality
- What they always acknowledge first
- How they frame criticism constructively
- Their belief about the relationship between writer and writing

Then: Show this persona's review of the same BrightStart copy.

---

**PERSONA 3 — THE AUDIENCE ANALYST**

Write the full system prompt for this persona:
- Professional background (maybe UX/conversion copywriting, marketing data, audience research)
- Their framework: they see writing through the eyes of the reader
- How they evaluate effectiveness vs quality
- The questions they always ask (who is reading this? what do they want? what will they do next?)
- Their metrics-minded approach to writing
- What they ignore (style preferences) vs prioritise (reader response)

Then: Show this persona's review of the same BrightStart copy.

---

**COMPARISON:**

After all 3 reviews:
1. What did each persona notice that the others didn't?
2. Whose feedback would be most useful for a first draft? An almost-finished draft?
3. If you could only use one of these personas for all your writing feedback, which would you choose and why?
4. When might it be valuable to use all three on the same piece?''',
    },
    {
        'title': 'Question 7: Giving Agents Knowledge',
        'description': 'Learn how to feed AI agents context, documents, and expertise so they become specialists',
        'difficulty': 'intermediate',
        'order': 7,
        'points': 30,
        'instructions': '''An AI agent is only as good as the knowledge it has access to. Learn how to turn a general AI into a genuine expert on your specific domain.

**What You'll Learn:**
- How to provide context documents that make AI a domain expert
- How to structure knowledge handoffs efficiently
- What "knowledge-rich agents" can do that "knowledge-poor agents" can't

**Types of Knowledge You Can Give AI Agents:**

**Reference Documents:**
- Company policies, FAQs, product specs, brand guidelines
- Technical documentation, process guides, SOPs
- Previous examples of good work (as style references)

**Context Information:**
- About your company, your customers, your industry
- Current projects, active decisions, recent history
- Constraints and non-negotiables

**Expertise Frameworks:**
- How to think about specific types of problems
- Decision criteria for common choices
- Industry-specific knowledge gaps to watch for

**The Result:**
Without knowledge: Generic advice that could apply to any company
With knowledge: Specific, actionable advice that knows YOUR business

**Your Challenge:**
Build a "company expert" agent — an AI that knows your fictional company inside and out, and can answer employee questions with real specificity.

**Create a fictional company** (50-100 employees, industry of your choice). Then:
1. Write the company knowledge document (the content you'd give the agent)
2. Write the agent instructions for a "Company Knowledge Expert" assistant
3. Show 5 questions an employee might ask and how the expert agent answers them differently from a general AI''',
        'example_prompt': '''Build a "Company Knowledge Expert" agent for a fictional company. I want to see the full knowledge setup and how the agent uses it.

**THE FICTIONAL COMPANY:**
"Brightfield Property Management" — a 65-person UK property management company that manages 1,200 residential properties on behalf of landlords in the Midlands. Services: tenant finding, property maintenance coordination, rent collection, compliance management.

---

**PART 1 — THE COMPANY KNOWLEDGE DOCUMENT**

Write a comprehensive company knowledge document that an AI agent would be given. This should include:

**A) Company Overview**
- What we do, who we serve, our service model
- How we're different from other property managers
- Our values and what they mean in practice (not just words)

**B) Key Policies and Processes**
- How we handle maintenance requests (the full process)
- Our late rent payment process (steps, timelines, communication)
- How we handle tenant complaints
- Our landlord communication standards

**C) Products and Services**
- Full service tiers and what each includes
- Pricing structure (invent realistic figures)
- What's included vs what costs extra

**D) Team Structure**
- Departments and their responsibilities
- Who to go to for what (referral guide)
- Escalation pathways

**E) Common Questions and Answers**
- 10 most common questions from tenants
- 10 most common questions from landlords
- The "tricky" situations and how we handle them

---

**PART 2 — AGENT INSTRUCTIONS**

Write the system prompt for a "Brightfield Expert" agent — an AI assistant that all staff can consult for answers to policy and process questions.

The agent should:
- Always answer based on Brightfield's specific policies (not generic property management practice)
- Know when to escalate vs handle itself
- Be helpful but accurate — no guessing
- Match Brightfield's professional but friendly tone
- Tell staff when to consult a human manager

---

**PART 3 — KNOWLEDGE-RICH VS KNOWLEDGE-POOR COMPARISON**

Show me the same question answered twice:

**Question from a new staff member:**
"A tenant has reported a leaking pipe. The landlord isn't responding to my calls. What do I do?"

**Answer A — Without company knowledge:** (What a generic AI would say)
**Answer B — Brightfield Expert with full knowledge:** (What the knowledge-rich agent says using the company's specific processes)

Show 5 such questions total, demonstrating how the knowledge transforms each answer.

---

**PART 4 — KNOWLEDGE MAINTENANCE**

How should Brightfield keep this agent's knowledge up to date?
- When does the knowledge document need updating?
- Who owns this process?
- How do you prevent an agent giving outdated information?
- What's the risk of an under-maintained knowledge base?''',
    },
    {
        'title': 'Question 8: Multi-Agent Thinking',
        'description': 'Simulate a panel of expert agents debating a real business decision from different angles',
        'difficulty': 'advanced',
        'order': 8,
        'points': 35,
        'instructions': '''One agent is powerful. A panel of agents with different expertise and perspectives is a decision-making superpower.

**What You'll Learn:**
- How multi-agent systems simulate diverse expert perspectives
- When getting multiple "AI experts" to debate produces better decisions
- How to structure a multi-agent consultation effectively

**The Multi-Agent Concept:**
Instead of asking one AI for advice, you set up multiple agents with different roles, expertise, and even personalities — then have them all analyse the same problem.

This works because:
- Different expertise catches different risks
- Disagreement reveals trade-offs you'd otherwise miss
- Advocacy for different positions forces you to think harder
- The "argument" between agents surfaces the real tension in the decision

**Example Setup for a Business Decision:**
- Agent 1: The CFO perspective — financial risk, cash flow, ROI
- Agent 2: The HR perspective — people impact, culture, capability
- Agent 3: The Customer perspective — client experience, reputation
- Agent 4: The Devil's Advocate — argues against whatever seems obvious

**Your Challenge:**
Set up a 3-agent advisory panel to evaluate a significant business decision.

**The Decision:** A growing 30-person digital marketing agency is deciding whether to launch a new service line: AI consultancy for non-tech SMEs. They'd need to hire 2 specialists, build a new sales process, and invest ~£40,000 in year one.

Run the full multi-agent panel:
1. Define each agent's role, expertise, and biases
2. Have each agent analyse the decision from their perspective
3. Show where they agree and disagree
4. Produce a synthesis: what does the combined analysis recommend?''',
        'example_prompt': '''Set up a 3-agent advisory panel to evaluate a major business decision. Show the full deliberation, including where the agents agree and disagree.

**THE DECISION:**
"Apex Digital" — a 30-person digital marketing agency in Bristol — is deciding whether to launch a new AI consultancy service. They'd advise non-tech SMEs on how to adopt AI tools across their operations. Investment required: 2 specialist hires (£45,000 each), 6 months to first revenue, £40,000 in setup costs. Potential upside: £200,000+ additional revenue by year 2.

**Current agency situation:**
- £2.8M annual revenue, profitable at 12% margin
- Strong client relationships but facing pricing pressure from competitors
- No current AI service offering — seeing client demand but not meeting it
- The two potential hires are known individuals who'd bring existing clients

---

**THE PANEL:**

**AGENT 1 — SARAH, THE FINANCIAL STRATEGIST**
Define: expertise, communication style, what she cares about most, her inherent biases, and her analytical framework for evaluating business investments.

**AGENT 2 — MARCUS, THE GROWTH DIRECTOR**
Define: expertise, communication style, what drives his thinking, where his biases lie, and how he evaluates strategic opportunities.

**AGENT 3 — PRIYA, THE RISK ANALYST**
Define: expertise, communication style, what keeps her up at night, her natural scepticism, and her framework for evaluating risk.

---

**THE DELIBERATION:**

**Round 1 — Initial Positions (150 words each agent):**
Each agent gives their initial reaction to the proposal. What do they immediately like or dislike?

**Round 2 — Cross-Examination (responding to each other):**
- Sarah responds to what Marcus said (what did he get wrong or underweight?)
- Marcus responds to Priya's concerns (which does he accept? Which does he push back on?)
- Priya responds to Sarah's financial analysis (what is the financial model missing?)

**Round 3 — The Key Disagreement:**
What is the single biggest point where the agents fundamentally disagree? Stage a direct debate — 3 exchanges, each agent making their strongest argument.

---

**THE SYNTHESIS:**

After the full deliberation:
1. What do all 3 agents agree on? (The non-negotiables)
2. Where is there genuine uncertainty that even the panel can't resolve?
3. The composite recommendation: what would a wise decision-maker take from this panel analysis?
4. The conditions: Under what circumstances should Apex definitely proceed? Under what circumstances should they definitely not?

---

**REFLECTION:**
What did having 3 different perspectives reveal that asking a single AI "should we do this?" would have missed?''',
    },
]
