"""
Module 1 Extra Lessons: Critical Thinking & Ethics
Three additional lessons covering AI task identification, critical evaluation, and ethical use.
"""

MODULE1_EXTRA_CHALLENGES = {
    'when_to_use_ai': {
        'title': 'When to Use AI (and When Not To)',
        'description': 'Learn to assess when AI is the right tool and when human judgement is essential',
        'difficulty': 'beginner',
        'order': 2,
        'points': 15,
        'instructions': '''Not every task needs AI. Knowing **when** to use it — and when to rely on your own skills — is one of the most important things you'll learn.

**What You'll Learn:**
- How to assess whether a task is suitable for AI
- The types of tasks AI excels at vs. struggles with
- How to evaluate risk and decide when human judgement matters more
- A simple framework for making the call

**The Framework — Ask Yourself:**
1. **Complexity:** Is this a routine task (good for AI) or does it need deep domain expertise?
2. **Risk:** What happens if the output is wrong? Low stakes (email draft) vs. high stakes (legal advice, medical info)?
3. **Creativity vs. Accuracy:** Do I need creative ideas (AI is great) or verified facts (AI can hallucinate)?
4. **Personal Touch:** Does this need MY authentic voice, or is a polished draft fine?
5. **Sensitivity:** Does this involve confidential data, personal information, or ethical concerns?

**AI is Great For:**
- Brainstorming and generating ideas
- Drafting and rewriting text
- Summarising long documents
- Explaining concepts in simple terms
- Structuring your thoughts
- Repetitive formatting tasks

**Think Twice Before Using AI For:**
- Final decisions on important matters
- Anything requiring verified, up-to-date facts (always check!)
- Tasks involving confidential or sensitive personal data
- Situations where authenticity and personal voice matter most
- Legal, medical, or financial advice

**Your Challenge:**
You'll be given 6 workplace scenarios below. For each one, decide:
- Should you use AI? (Yes / No / Partially)
- Why or why not?
- If yes, what specifically would you ask AI to do?
- If partially, what part should AI handle and what should you do yourself?

**The Scenarios:**
1. Writing a thank-you email to a colleague who helped you on a project
2. Summarising a 20-page research report for your team meeting
3. Deciding whether to accept a job offer from a new company
4. Creating a presentation outline for a topic you know well
5. Checking if a contract clause is legally binding
6. Drafting social media posts for your company's new product launch

**Your prompt must show clear reasoning for each scenario** — don't just say "yes" or "no." Explain your thinking using the framework above.

**Why This Matters:**
In the workplace, using AI at the wrong moment can be just as costly as not using it at all. Sending an AI-drafted message that sounds generic when a personal touch was needed? That's a problem. But spending 2 hours writing something AI could draft in 30 seconds? That's wasted time. The skill is knowing the difference.''',
        'example_prompt': '''I need to practise deciding when to use AI and when not to. Here are 6 workplace scenarios — for each one, I'll assess whether AI is the right tool.

**Scenario 1: Writing a thank-you email to a colleague who helped on a project**
- Use AI? **Partially**
- Reasoning: AI can help me structure the email and make sure I don't miss anything, but the core message should be genuine and personal. I'd use AI to suggest a format, then write the actual content myself so it feels authentic.
- AI's role: Suggest a structure (opening, specific thanks, future collaboration mention, warm closing)
- My role: Fill in the personal details, genuine feelings, and specific examples only I would know

**Scenario 2: Summarising a 20-page research report for a team meeting**
- Use AI? **Yes**
- Reasoning: This is exactly what AI excels at — processing large amounts of text and pulling out key points. The risk is low (it's a summary, not a decision), and it saves significant time.
- AI's role: Read the report and create a structured summary with key findings, recommendations, and action items
- My role: Review the summary for accuracy, add my own insights, and highlight what's most relevant for my specific team

**Scenario 3: Deciding whether to accept a job offer**
- Use AI? **No (mostly)**
- Reasoning: This is a deeply personal decision involving my values, career goals, family situation, and gut feeling. AI doesn't know my full context and can't weigh emotional factors. However, I might use AI for one small part — comparing the financial package (salary, benefits, pension) against market rates.
- What I should do myself: Reflect on career goals, talk to trusted people, consider work-life balance and company culture

**Scenario 4: Creating a presentation outline for a topic I know well**
- Use AI? **Partially**
- Reasoning: I already have the expertise, so AI won't add knowledge. But it CAN help me structure my thoughts, suggest a logical flow, and make sure I haven't missed obvious sections. Low risk, high time-saving.
- AI's role: Suggest an outline structure and flow
- My role: Reorder based on what I know works, add my examples and insights

**Scenario 5: Checking if a contract clause is legally binding**
- Use AI? **No**
- Reasoning: This is high-stakes and requires verified legal expertise. AI can hallucinate legal information and doesn't know the specific laws in my jurisdiction. Getting this wrong could have serious consequences. I should consult a qualified solicitor.
- Exception: I might ask AI to explain legal jargon in plain English so I understand the clause better before speaking to a lawyer.

**Scenario 6: Drafting social media posts for a new product launch**
- Use AI? **Yes**
- Reasoning: AI is excellent at generating creative copy variations, suggesting hashtags, and adapting tone for different platforms. The risk is manageable (I'll review before posting), and it can produce multiple options quickly.
- AI's role: Draft 3-4 variations for each platform (LinkedIn, Instagram, X) with different tones and hooks
- My role: Select the best options, ensure brand voice consistency, fact-check product claims, add any insider knowledge''',
    },
    'dont_trust_verify': {
        'title': "Don't Trust, Verify",
        'description': 'Learn to critically evaluate AI outputs for accuracy, bias, and reliability',
        'difficulty': 'intermediate',
        'order': 11,
        'points': 20,
        'instructions': '''AI can sound incredibly confident while being completely wrong. This lesson teaches you to be a smart, critical consumer of AI-generated content.

**What You'll Learn:**
- How to spot AI hallucinations (made-up facts, fake sources, invented statistics)
- How to check AI outputs for accuracy and bias
- Red flags that signal unreliable AI content
- A practical verification checklist you can use every time

**The Problem:**
AI doesn't "know" things — it predicts what sounds right. This means it can:
- Invent statistics that sound plausible but are completely made up
- Create fake citations to non-existent research papers
- Present one-sided arguments as balanced analysis
- Confidently give outdated information
- Reflect biases from its training data

**Red Flags to Watch For:**
1. **Suspiciously round numbers** — "Studies show 73.2% of..." (often fabricated)
2. **Vague attributions** — "Research shows..." or "Experts say..." (which research? which experts?)
3. **Too-perfect examples** — Real life is messy; if every example works perfectly, be suspicious
4. **Confident tone on controversial topics** — AI may present one perspective as the only truth
5. **Outdated information** — AI has a knowledge cutoff and may not reflect recent changes

**Your Verification Checklist:**
- Can I find this fact from a reliable, independent source?
- Does this statistic appear in any credible publication?
- Are the cited sources real? (Google them!)
- Does this advice account for my specific context and location?
- Is this presenting a balanced view, or just one perspective?
- When was this information last accurate?

**Your Challenge:**
Ask AI to write a **briefing document** on a topic of your choice (e.g., remote work trends, the gig economy, renewable energy in the UK, or AI in education).

Then, **critically evaluate the response** by:

1. **Fact-checking:** Identify at least 3 specific claims in the response. For each one, state whether you believe it's accurate, potentially made up, or needs verification — and explain why.

2. **Source analysis:** Does the response cite sources? Are they real? If no sources are given, note that as a red flag.

3. **Bias detection:** Is the response balanced, or does it lean in one direction? What perspectives might be missing?

4. **Currency check:** Could any of this information be outdated? What would you need to verify is still current?

5. **Overall reliability rating:** Give the response a reliability score out of 10 and justify it.

**Your prompt should include BOTH:**
- The original request to AI (the briefing document)
- Your critical evaluation of the response (the 5 points above)

**Pro Tip:**
Get into the habit of asking AI: "Which of these facts are you most and least confident about?" — AI can sometimes flag its own uncertainty if you ask directly.

**Why This Matters:**
In the workplace, sharing AI-generated content without checking it can damage your credibility. A made-up statistic in a client presentation, a fake citation in a report, or biased advice that ignores key factors — these mistakes reflect on YOU, not the AI. Verification isn't optional; it's professional.''',
        'example_prompt': '''**Part 1 — My Request to AI:**

Write me a briefing document on the current state of remote work in the UK in 2025. Include:
- Key statistics on remote/hybrid work adoption
- How it's changed since the pandemic
- Impact on productivity (what does the evidence say?)
- The main arguments for and against remote work from employers
- Any recent policy changes or trends
- What experts predict for the next 2-3 years

Keep it factual and cite your sources where possible. Aim for about 500 words.

---

**Part 2 — My Critical Evaluation of the AI Response:**

**1. Fact-Checking (3 specific claims):**

- Claim: "58% of UK workers now have the option to work from home at least one day a week"
  - Verdict: **Needs verification.** This sounds plausible based on ONS data, but the exact percentage needs checking against the latest ONS Labour Force Survey. AI may have made up the specific number.

- Claim: "A Stanford study by Nicholas Bloom found that hybrid workers were 35% less likely to quit"
  - Verdict: **Partially accurate.** Nicholas Bloom at Stanford IS a real researcher who studies remote work. He has published findings about reduced attrition. But I need to verify the exact "35%" figure — AI often gets the researcher right but invents the specific statistic.

- Claim: "The UK government introduced the Flexible Working Bill in 2023, giving workers the right to request flexible working from day one"
  - Verdict: **Likely accurate.** The Employment Relations (Flexible Working) Act did pass, and it did change the right to request from 26 weeks to day one. But I should check if the implementation date is correctly stated.

**2. Source Analysis:**
The response mentioned "ONS data," "a Stanford study," and "CIPD research" but didn't give specific URLs, publication dates, or report titles. This makes verification harder. Two of the three sources are real organisations, which is good, but without specific report names, I can't confirm the exact figures cited.

**3. Bias Detection:**
The response leaned slightly **pro-remote work.** The benefits section was longer and more detailed than the drawbacks. Missing perspectives: impact on junior employees and career progression, commercial property implications, the digital divide (not everyone has a good home setup), and the view of sectors where remote work isn't possible (manufacturing, healthcare, retail).

**4. Currency Check:**
- Remote work statistics change rapidly — any figures from 2023 might not reflect 2025 reality
- Government policy may have evolved since AI's training data cutoff
- The "expert predictions" section is the least reliable — AI is essentially guessing what experts might say

**5. Overall Reliability Rating: 6/10**
The general narrative is sound and aligns with what I know about UK remote work trends. However, the specific statistics need independent verification, the perspective is somewhat one-sided, and the sources aren't specific enough to check. I'd use this as a starting point for research, but I wouldn't present any of these figures in a meeting without confirming them first.''',
    },
    'ai_ethics': {
        'title': 'AI Ethics and Responsible Use',
        'description': 'Understand privacy, transparency, and copyright when using AI in the workplace',
        'difficulty': 'intermediate',
        'order': 20,
        'points': 20,
        'instructions': '''Using AI effectively is important. Using it **responsibly** is essential. This lesson covers the ethical and practical boundaries every AI user should understand.

**What You'll Learn:**
- What you should NEVER share with AI chatbots
- When and how to disclose AI use
- Copyright and intellectual property concerns
- Workplace policies and professional standards
- How to use AI ethically in academic and professional settings

**1. Privacy — What NOT to Share with AI**

AI chatbots process your inputs on external servers. Treat every prompt as if it could be seen by others.

**Never input into AI:**
- Personal data (full names, addresses, phone numbers, NHS numbers)
- Financial information (bank details, salary data, credit card numbers)
- Confidential business information (trade secrets, unreleased plans, internal strategy)
- Passwords, API keys, or security credentials
- Private conversations or sensitive HR matters
- Client or customer data without explicit consent

**Instead:**
- Use anonymised or fictional data when practising
- Replace real names with placeholders ("Person A," "Company X")
- Check your organisation's AI usage policy before inputting any work data

**2. Transparency — When to Disclose AI Use**

**Always disclose when:**
- Submitting academic work (most institutions have AI-use policies)
- Creating content published under your name
- Providing advice or recommendations to clients
- The output will be used in official documents or decisions
- Your workplace policy requires it

**You generally don't need to disclose when:**
- Using AI for personal brainstorming or idea generation
- Checking grammar or rephrasing your own writing
- Using AI as a research starting point (but verify the facts!)
- Internal note-taking or personal productivity

**3. Copyright and Intellectual Property**

Key questions to consider:
- **AI-generated content:** In most jurisdictions, AI-generated text cannot be copyrighted. If you need copyright protection, you must add substantial original contribution.
- **Input content:** Don't paste copyrighted material into AI and ask it to "rewrite" it — this is ethically questionable and potentially illegal.
- **Training data concerns:** AI models were trained on vast amounts of internet data, raising questions about fair use and creator compensation.

**4. Workplace AI Policies**

Many organisations now have AI usage policies. Common rules include:
- Approved AI tools list (not all platforms may be allowed)
- Data classification rules (what can/cannot be input)
- Disclosure requirements for AI-assisted work
- Quality assurance processes for AI-generated content

**Your Challenge:**
You work in a busy office and encounter the following 5 situations in a single week. For each one, write a prompt that demonstrates **ethical AI use** — or explain why you should NOT use AI in that situation.

**Situation 1:** Your manager asks you to summarise a confidential board meeting for the team newsletter. You have the full meeting minutes with names, financial projections, and strategic plans.

**Situation 2:** You need to write a blog post for your company website about industry trends. You want to use AI to help draft it.

**Situation 3:** A colleague shares a client's personal details (name, email, project brief) and asks you to "run it through AI" to generate a proposal.

**Situation 4:** You're applying for an internal promotion and need to write a personal statement. You're considering using AI to write the whole thing.

**Situation 5:** You want to use AI to help you learn a new skill (data analysis) for your own professional development.

**For each situation, your response must cover:**
- Can/should you use AI here? (Yes / No / With modifications)
- What are the ethical concerns?
- If using AI, show the SAFE prompt you would write
- What would you do differently to protect privacy, maintain transparency, and act professionally?

**Why This Matters:**
AI misuse can lead to data breaches, legal issues, damaged trust, and professional consequences. The people who thrive with AI aren't just the ones who write clever prompts — they're the ones who use it responsibly. Ethical AI use protects you, your colleagues, and your organisation.''',
        'example_prompt': '''I'm practising ethical AI use in workplace scenarios. Here are 5 situations and how I'd handle each one responsibly:

---

**Situation 1: Summarising confidential board meeting minutes**

- Use AI? **With significant modifications**
- Ethical concerns: The minutes contain sensitive financial data, strategic plans, and people's names. Putting this directly into an AI chatbot risks data exposure.
- My safe approach:

Prompt I WOULD use:
"I need to write a summary of an internal meeting for a team newsletter. The meeting covered three topics: Q3 financial performance, a new product launch timeline, and team restructuring. Can you give me a professional newsletter template with placeholder sections for: key highlights, decisions made, action items, and next steps? Keep the tone positive and informative."

What I did differently: I gave AI the STRUCTURE of what I need without sharing ANY actual confidential content. I'll fill in the real details myself after getting the template. No names, no numbers, no strategy details shared with AI.

---

**Situation 2: Writing a company blog post about industry trends**

- Use AI? **Yes, with disclosure**
- Ethical concerns: The blog will be published publicly under the company's name. Readers deserve to know if AI was involved. Also, I need to verify any facts or trends AI generates.
- My safe approach:

Prompt I WOULD use:
"Help me draft a 600-word blog post about the top 5 trends in digital marketing for small businesses in 2025. Write in a conversational, accessible tone suitable for small business owners who aren't tech-savvy. For each trend, include: what it is, why it matters, and one practical tip to get started. Please flag which claims you're most and least confident about so I know what to fact-check."

What I'd do after: Fact-check every statistic and claim. Add my own insights and examples. Include a note in the blog like "This post was drafted with AI assistance and reviewed by [my name]." Run it past my manager before publishing.

---

**Situation 3: Using a client's personal details to generate a proposal**

- Use AI? **No — not with their personal data**
- Ethical concerns: This is a clear data protection issue. Sharing a client's name, email, and project details with an AI platform could violate GDPR, your company's data policy, and the client's trust. The colleague's request is well-intentioned but risky.
- What I would do: Politely explain to my colleague that we shouldn't input client data into AI tools. Instead, I'd create an anonymised version:

Prompt I WOULD use:
"I'm writing a project proposal for a client in the retail sector. They need a website redesign with these requirements: [list requirements WITHOUT identifying details]. Can you help me structure a professional proposal with sections for: project overview, our approach, timeline, deliverables, and pricing structure? Use placeholder text where client-specific details should go."

What I did differently: Removed all identifying information. Used the client's industry and requirements without names, emails, or specific details. I'll add the real client details manually in the final document.

---

**Situation 4: Writing a personal statement for an internal promotion**

- Use AI? **Partially — for structure only**
- Ethical concerns: A personal statement should reflect YOUR authentic voice, genuine achievements, and real motivations. If you use AI to write the whole thing, you're misrepresenting yourself. The hiring panel wants to hear from YOU, not from AI. If discovered, it could seriously damage your credibility.
- My safe approach:

Prompt I WOULD use:
"I'm writing a personal statement for an internal promotion to Senior Marketing Executive. Can you suggest a strong structure for a 500-word personal statement? I want to cover: my journey in the company, key achievements, leadership examples, and my vision for the role. Just give me the structure with guiding questions for each section — I'll write the actual content myself."

What I did differently: I asked for structure and guidance, NOT for AI to write my statement. The actual words, stories, and achievements will be mine. This is similar to asking a mentor for advice on how to structure your statement — which is perfectly acceptable.

---

**Situation 5: Learning data analysis for professional development**

- Use AI? **Yes — this is an ideal use case!**
- Ethical concerns: Minimal. This is personal learning, no sensitive data is involved, and no one else is affected. This is exactly what AI is great for.
- My safe approach:

Prompt I WOULD use:
"I'm a marketing professional with no data analysis experience. I want to learn data analysis to improve my career prospects. Can you create a 4-week learning plan for me? I can dedicate about 5 hours per week. I learn best by doing practical exercises rather than watching videos. Cover: spreadsheet skills (Excel/Google Sheets), basic data visualisation, understanding common metrics, and an introduction to tools like Power BI or Tableau. For each week, suggest specific skills to learn and a mini-project to practise them."

Why this is fine: No confidential data, no ethical concerns, purely for self-improvement. I'm using AI as a learning coach, which is one of its best applications.''',
    },
}
