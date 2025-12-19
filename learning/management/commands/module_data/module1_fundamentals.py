# Module 1: AI Chat Mastery - Fundamentals Section
# 15 challenges covering basic to intermediate prompt engineering

FUNDAMENTALS_CHALLENGES = [
    {
        'title': 'Lesson 1: Your First Prompt',
        'description': 'Learn the basics of crafting an effective AI prompt',
        'difficulty': 'beginner',
        'order': 1,
        'points': 10,
        'instructions': '''Welcome to AI Prompt Engineering! 🎉

**What You'll Learn:**
- How to communicate clearly with AI
- The importance of being specific
- How to get the results you want

**Your Challenge:**
Get the AI to write a professional email introducing yourself to a new team.

**Tips:**
- Be specific about what you want
- Provide context (who you are, what team)
- Mention the tone you want (professional, friendly, etc.)

**Why This Matters:**
In the real world, you'll use AI for emails, reports, and communications daily. Clear prompts = better results!

Try to make your prompt clear and complete in one message.''',
        'example_prompt': 'Write a professional email introducing myself as Sarah Johnson, a new cybersecurity analyst joining the SOC team at TechCorp. Keep it friendly but professional, around 3 paragraphs. Mention my background in network security and excitement to work with the team.',
    },
    {
        'title': 'Lesson 2: The Power of Context',
        'description': 'Learn how providing context dramatically improves AI responses',
        'difficulty': 'beginner',
        'order': 2,
        'points': 15,
        'instructions': '''Context is EVERYTHING! 🎯

**What You'll Learn:**
- Why context matters
- How to provide the right background information
- Adjusting complexity for your audience

**Your Challenge:**
Get the AI to explain a complex cybersecurity concept (like zero-day exploits) to someone with NO technical background.

**The Key:**
- Specify your audience clearly (age, background, knowledge level)
- Mention the complexity level you want
- Give constraints (length, use of analogies, examples)

**Real-World Application:**
You'll often need to explain technical concepts to non-technical people (managers, clients, family). This skill is GOLD.

The more context you provide, the better the response!''',
        'example_prompt': 'Explain what a "zero-day exploit" is to my non-technical manager who has never worked in cybersecurity. Use a simple analogy they can relate to (maybe about houses or locks?). Keep it under 150 words and avoid technical jargon.',
    },
    {
        'title': 'Lesson 3: Structured Requests',
        'description': 'Use structure to get organized, actionable responses',
        'difficulty': 'beginner',
        'order': 3,
        'points': 15,
        'instructions': '''Structure = Clarity! 📋

**What You'll Learn:**
- How to request specific formats
- Getting organized outputs
- Making AI responses actionable

**Your Challenge:**
Get the AI to create a morning routine plan for a cybersecurity professional, with specific time blocks and categories.

**Try To:**
- Ask for a specific format (bullet points, numbered list, time blocks)
- Request specific sections or categories
- Set time constraints or priorities

**Real-World Use:**
When you need reports, schedules, or organized information, structured prompts get you exactly what you need - no back-and-forth!

Show that you can request structured output!''',
        'example_prompt': 'Create a morning routine for a busy SOC analyst working 12-hour shifts. Structure it with: 1) Wake-up and prep (45 min), 2) Exercise/mental clarity (30 min), 3) Breakfast and news review (30 min), 4) Pre-shift briefing prep (15 min). Use time blocks and bullet points for each section. Include tips for staying alert during long shifts.',
    },
    {
        'title': 'Lesson 4: Being Specific Gets Results',
        'description': 'Learn the difference between vague and specific prompts',
        'difficulty': 'beginner',
        'order': 4,
        'points': 15,
        'instructions': '''Specific > Vague, Always! 🎯

**What You'll Learn:**
- Why vague prompts fail
- How to add specificity
- The power of details

**Challenge:**
Compare these two prompts:
- ❌ "Write about cybersecurity"
- ✅ "Write a 200-word introduction to ransomware attacks for small business owners, explaining what they are, how they happen, and 3 prevention tips"

**Your Task:**
Write a highly specific prompt to get AI to help you analyze a suspicious email. Include:
- What you need analyzed
- What you're looking for (phishing indicators)
- Format you want the answer in
- Level of detail needed

**Real-World:**
In cybersecurity, specificity saves time. "Check this" vs "Analyze this email for phishing indicators: suspicious sender, URL analysis, attachment risks" - which gets better results?''',
        'example_prompt': 'I received a suspicious email claiming to be from our IT department asking me to "verify my credentials" by clicking a link. Analyze this scenario and tell me: 1) What are the red flags? 2) What specific phishing techniques might be used? 3) What should I check before clicking anything? 4) How should I report this? Format as a numbered checklist I can follow.',
    },
    {
        'title': 'Lesson 5: Tone and Style Control',
        'description': 'Master how to control the tone of AI responses',
        'difficulty': 'intermediate',
        'order': 5,
        'points': 20,
        'instructions': '''AI can adapt to any tone you need! 🎭

**What You'll Learn:**
- How to specify tone (formal, casual, technical, simple)
- Adjusting for different audiences
- Style consistency

**Your Challenge:**
Get AI to explain the same security concept (like firewalls) in THREE different tones:
1. Casual (for a friend)
2. Professional (for a colleague)
3. Executive summary (for leadership)

**Ask AI to:**
- Write one explanation in each tone
- Keep each under 100 words
- Show how the same info changes with audience

**Real-World Application:**
You'll write differently for your team vs your boss vs a client. This skill is crucial!

Master tone control = Master communication.''',
        'example_prompt': 'Explain what a firewall does in three different ways: 1) Casual tone for a non-tech friend, 2) Professional tone for a fellow security analyst, 3) Executive summary for C-level leadership. Keep each explanation under 100 words. Show me how the same concept adapts to different audiences.',
    },
    {
        'title': 'Lesson 6: The Iterative Approach',
        'description': 'Learn to refine and improve responses through follow-ups',
        'difficulty': 'intermediate',
        'order': 6,
        'points': 20,
        'instructions': '''First try rarely perfect - and that's OK! 🔄

**What You'll Learn:**
- How to refine prompts
- Following up for better results
- The power of iteration

**Your Challenge:**
Write a prompt to create a tweet about a recent security breach, but make it:
- Under 280 characters
- Informative but not alarming
- Include a key lesson learned
- Professional tone
- No technical jargon

**The Learning:**
Your first prompt might not nail all requirements. That's NORMAL! Real work involves refinement.

**Try This:**
1. Write your first prompt
2. See what AI returns
3. Think: what's missing?
4. Refine and try again

This is how professionals work with AI!''',
        'example_prompt': 'Write a professional tweet about the recent Equifax data breach. Make it: under 280 characters, informative but not fear-mongering, include one key lesson for consumers, avoid technical jargon. Tone should be educational and empowering, not scary.',
    },
    {
        'title': 'Lesson 7: Using Examples (Few-Shot Learning)',
        'description': 'Teach AI through examples to get consistent results',
        'difficulty': 'intermediate',
        'order': 7,
        'points': 25,
        'instructions': '''Show, don't just tell! 💡

**What You'll Learn:**
- Few-shot learning technique
- How to provide examples
- Getting consistent formatting

**The Technique:**
Instead of just describing what you want, SHOW examples!

**Your Challenge:**
You need to categorize security incidents. Give AI 2-3 examples of how you want it done, then ask it to categorize new incidents.

**Example Structure:**
"Here's how I categorize incidents:
- Incident: Failed login attempts from unusual location → Category: Suspicious Activity, Severity: Low
- Incident: Ransomware detected on workstation → Category: Active Threat, Severity: Critical

Now categorize these new incidents using the same format..."

**Real-World:**
This is how you train AI to work YOUR way, with YOUR standards.

Examples = Better consistency!''',
        'example_prompt': '''I need to categorize security incidents. Here are examples of my format:

EXAMPLE 1:
Incident: Multiple failed SSH login attempts from IP 192.168.1.100
Category: Brute Force Attack
Severity: Medium
Action: Block IP, monitor for 24 hours

EXAMPLE 2:
Incident: Suspicious outbound traffic to known C2 server
Category: Potential Compromise
Severity: Critical
Action: Isolate system immediately, begin forensics

Now categorize these incidents using the same format:
1. User clicked on phishing link in email
2. Outdated software detected on 15 workstations
3. Unusual data exfiltration pattern detected''',
    },
    {
        'title': 'Lesson 8: Role-Playing for Expert Responses',
        'description': 'Assign roles to AI for specialized, expert-level responses',
        'difficulty': 'intermediate',
        'order': 8,
        'points': 25,
        'instructions': '''Give AI a role, get expert advice! 👔

**What You'll Learn:**
- The "Act as..." technique
- Getting specialized perspectives
- Role-based expertise

**The Power:**
"Act as a [role] with [experience]" makes AI respond from that perspective!

**Your Challenge:**
Get security advice as if from a seasoned CISO who has handled major breaches.

**Technique:**
- Start with "Act as..." or "You are..."
- Give credentials/background
- Ask your question with specific context

**Examples:**
- "Act as a penetration tester with 15 years experience..."
- "You are a forensics expert who has investigated ransomware attacks..."
- "Act as a security architect who designs zero-trust networks..."

**Real-World:**
Get expert-level advice on demand!''',
        'example_prompt': 'Act as a Chief Information Security Officer (CISO) who has successfully managed security for Fortune 500 companies and handled 3 major data breaches. My company just experienced a phishing attack that compromised 5 employee credentials. What are your immediate priorities in the first 24 hours? What are the next 7-day and 30-day action items? Give me a strategic response focusing on both technical and communication aspects.',
    },
    {
        'title': 'Lesson 9: Constraint-Based Prompting',
        'description': 'Use constraints to guide AI toward specific solutions',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 25,
        'instructions': '''Constraints = Creativity within boundaries! 📏

**What You'll Learn:**
- Setting boundaries for AI
- Using constraints productively
- Getting focused responses

**Your Challenge:**
Create a security awareness training plan with SPECIFIC constraints:
- Budget: $5,000
- Time: Must complete in 30 days
- Team: 50 employees (mixed technical levels)
- Must cover: Phishing, password security, data handling
- Format: Mix of self-paced and interactive

**Why Constraints Matter:**
In real work, you ALWAYS have limitations. Teaching AI your constraints gets realistic, actionable advice.

**The Formula:**
"Given [constraints], help me [goal] by providing [specific output]"

Constraints make AI responses practical, not just theoretical!''',
        'example_prompt': 'Help me design a security awareness training program with these constraints: Budget of $5,000, must train 50 employees in 30 days, team has mixed technical skills (from HR to IT), must cover phishing, password security, and data handling. I need: 1) A week-by-week schedule, 2) Mix of training methods (online/in-person/interactive), 3) How to measure effectiveness, 4) Budget breakdown. Make it practical and achievable.',
    },
    {
        'title': 'Lesson 10: Multi-Step Instructions',
        'description': 'Break complex tasks into clear, sequential steps',
        'difficulty': 'intermediate',
        'order': 10,
        'points': 25,
        'instructions': '''Complex tasks need step-by-step guidance! 📝

**What You'll Learn:**
- Breaking down complex requests
- Sequential instruction design
- Getting comprehensive responses

**Your Challenge:**
Ask AI to help you create a comprehensive incident response plan. But don't just say "make a plan" - break it into clear steps!

**The Approach:**
"Help me create an incident response plan. For each phase, provide:
1. [What you want for phase 1]
2. [What you want for phase 2]
3. [What you want for phase 3]..."

**Your Task:**
Create a prompt that asks for an incident response plan with:
- Detection phase (what to look for)
- Containment phase (immediate actions)
- Eradication phase (removing threat)
- Recovery phase (getting back to normal)
- Lessons learned phase (documentation)

Each phase should have specific, actionable steps.

**Real-World:**
Complex security projects need structured planning. This is how you do it!''',
        'example_prompt': '''Help me create a comprehensive incident response plan for a ransomware attack. Structure it in these phases:

1. DETECTION PHASE: What are the early warning signs? What tools/logs should we monitor?

2. CONTAINMENT PHASE: Immediate actions to prevent spread (within first hour)

3. ISOLATION PHASE: How to isolate affected systems without disrupting business

4. ERADICATION PHASE: Steps to remove the ransomware and verify systems are clean

5. RECOVERY PHASE: How to restore systems and data safely

6. POST-INCIDENT PHASE: Documentation, lessons learned, and prevention improvements

For each phase, provide 3-5 specific, actionable steps that a SOC team can follow. Include timeline estimates.''',
    },
    {
        'title': 'Lesson 11: Comparison and Analysis Prompts',
        'description': 'Ask AI to compare, contrast, and analyze options',
        'difficulty': 'advanced',
        'order': 11,
        'points': 30,
        'instructions': '''AI excels at analysis and comparison! 📊

**What You'll Learn:**
- Comparative analysis prompts
- Decision-making with AI
- Pros/cons evaluation

**Your Challenge:**
You need to choose between different security tools or approaches. Ask AI to provide a structured comparison.

**The Framework:**
"Compare [Option A] vs [Option B] based on:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
Present as a table/structured format."

**Your Task:**
Compare two security approaches (e.g., traditional antivirus vs EDR, perimeter security vs zero-trust) with criteria like:
- Cost
- Effectiveness
- Implementation difficulty
- Maintenance requirements
- Best use cases

**Real-World:**
You'll constantly evaluate tools, vendors, and approaches. AI can help you think through decisions!''',
        'example_prompt': '''Compare traditional antivirus solutions vs modern EDR (Endpoint Detection and Response) for a mid-sized company (200 employees). Analyze based on:

1. Threat detection capabilities
2. Response time to incidents
3. Cost (implementation + ongoing)
4. IT staff training required
5. Impact on system performance
6. Compliance requirements

Present as a comparison table, then provide a recommendation based on: limited IT staff (team of 3), moderate budget ($50K/year for security), need to meet HIPAA compliance, and experiencing increase in sophisticated attacks.''',
    },
    {
        'title': 'Lesson 12: Problem-Solving Frameworks',
        'description': 'Use AI to work through problems systematically',
        'difficulty': 'advanced',
        'order': 12,
        'points': 30,
        'instructions': '''Structured problem-solving with AI! 🧩

**What You'll Learn:**
- Problem decomposition
- Root cause analysis
- Systematic troubleshooting

**Your Challenge:**
Present a security problem and ask AI to help you solve it using a structured framework.

**The Framework:**
1. Define the problem clearly
2. Identify root causes
3. Brainstorm solutions
4. Evaluate solutions
5. Create action plan

**Your Task:**
Present a problem like:
"Our company is experiencing frequent phishing attacks despite training. Employees are still clicking malicious links."

Ask AI to:
- Analyze why training isn't working
- Identify root causes
- Propose multi-layered solutions
- Prioritize actions
- Create an implementation plan

**Real-World:**
Security problems are complex. Systematic approaches help!''',
        'example_prompt': '''Our company has a problem: Despite mandatory security training, employees are still falling for phishing attacks. Last month, 15 employees clicked malicious links, with 3 resulting in compromised credentials.

Help me solve this using a structured approach:

1. ROOT CAUSE ANALYSIS: Why is our training failing? What might we be missing?

2. CONTRIBUTING FACTORS: What makes employees vulnerable to phishing?

3. MULTI-LAYERED SOLUTIONS: Propose solutions across these layers:
   - Technical controls
   - Process improvements  
   - Training enhancements
   - Cultural changes

4. PRIORITIZATION: Rank solutions by:
   - Impact (high/medium/low)
   - Cost (high/medium/low)
   - Implementation time (quick wins vs long-term)

5. 90-DAY ACTION PLAN: Give me a realistic implementation timeline.

Be specific and practical.''',
    },
    {
        'title': 'Lesson 13: Asking the Right Questions',
        'description': 'Learn to extract information through strategic questioning',
        'difficulty': 'advanced',
        'order': 13,
        'points': 30,
        'instructions': '''Sometimes AI needs to ask YOU questions! ❓

**What You'll Learn:**
- Clarifying requirements
- Information gathering
- Two-way conversation

**The Technique:**
Instead of trying to think of everything, ask AI to help you think through what's needed!

**Your Challenge:**
You're planning a security audit but don't know what to include. Ask AI to interview YOU by asking clarifying questions.

**The Prompt Structure:**
"I need to plan a security audit for my company. Before you help me create the plan, ask me 10 important questions you need to know about my environment, priorities, and constraints. Then use my answers to create a customized audit plan."

**Your Task:**
Create a prompt that:
1. States your goal
2. Asks AI to gather requirements through questions
3. Specifies what information AI should gather
4. Explains you'll answer before they provide solution

**Real-World:**
Good consultants ask questions before giving advice. Train AI to do the same!''',
        'example_prompt': '''I need to conduct a comprehensive security assessment of our organization, but I'm not sure what to prioritize or how to structure it.

Before you provide a plan, please ask me 8-10 critical questions about:
- Our organization (size, industry, compliance needs)
- Current security posture
- Known vulnerabilities or concerns
- Budget and timeline constraints
- Technical environment (cloud, on-prem, hybrid)
- Previous assessment findings
- Specific goals for this assessment

After I answer your questions, create a customized security assessment plan tailored to our specific situation.

What questions do you need answered?''',
    },
    {
        'title': 'Lesson 14: Template Creation',
        'description': 'Build reusable templates for recurring tasks',
        'difficulty': 'advanced',
        'order': 14,
        'points': 30,
        'instructions': '''Create templates for tasks you do repeatedly! 📋

**What You'll Learn:**
- Template design
- Reusable formats
- Standardization

**Your Challenge:**
Create a template for security incident reports that you can reuse.

**The Approach:**
Ask AI to create a template that you can fill in each time an incident occurs.

**Your Task:**
Request a security incident report template with:
- Standard sections (Incident Overview, Timeline, Impact Assessment, Response Actions, Root Cause, Prevention Measures)
- Placeholders for variable information
- Severity classification guide
- Stakeholder communication sections
- Follow-up action items

**The Power:**
Once you have a good template, you save hours on every incident! This is efficiency!

**Your Prompt Should:**
- Specify all sections needed
- Request clear placeholders
- Ask for formatting guidance
- Include severity classification
- Cover all stakeholders

**Real-World:**
Security pros use templates for incidents, assessments, reports, and more. Build your library!''',
        'example_prompt': '''Create a comprehensive security incident report template that our SOC team can use for all incidents. Include:

1. INCIDENT OVERVIEW section with:
   - Incident ID and date/time
   - Severity classification (Critical/High/Medium/Low) with criteria
   - Type of incident (malware, phishing, DDoS, data breach, etc.)
   - Affected systems/users
   - Current status

2. TIMELINE section:
   - Detection time
   - Response initiation
   - Key actions taken (with timestamps)
   - Resolution time

3. TECHNICAL DETAILS:
   - Initial indicators
   - Attack vector
   - Systems compromised
   - Data affected

4. IMPACT ASSESSMENT:
   - Business impact
   - Data impact
   - Financial impact
   - Reputation impact

5. RESPONSE ACTIONS:
   - Containment measures
   - Eradication steps
   - Recovery actions

6. ROOT CAUSE ANALYSIS:
   - How did this happen?
   - What was the vulnerability?

7. LESSONS LEARNED:
   - What went well
   - What needs improvement

8. PREVENTION MEASURES:
   - Short-term fixes
   - Long-term improvements

9. STAKEHOLDER COMMUNICATION:
   - Who was notified
   - When and how

Make it professional and ready to use. Include placeholder text like [INSERT DETAILS HERE] where needed.''',
    },
    {
        'title': 'Lesson 15: Meta-Prompting (Prompts About Prompts!)',
        'description': 'Ask AI to help you create better prompts',
        'difficulty': 'advanced',
        'order': 15,
        'points': 35,
        'instructions': '''Use AI to improve your prompting skills! 🎓

**What You'll Learn:**
- Meta-cognitive prompting
- Self-improvement techniques
- Advanced prompt engineering

**The Concept:**
Ask AI to critique and improve your own prompts!

**Your Challenge:**
Give AI a prompt you've written, then ask it to:
1. Identify what's good about it
2. Point out what's missing
3. Suggest improvements
4. Provide an enhanced version

**Example Flow:**
"Here's a prompt I wrote: [your prompt]

Analyze this prompt and tell me:
- What works well?
- What's unclear or missing?
- How could I improve specificity?
- What context should I add?
Then provide an improved version."

**Your Task:**
Write a basic prompt (can be about anything security-related), then ask AI to help you make it MUCH better through analysis and suggestions.

**Real-World:**
The best way to get better at prompting is to practice AND get feedback. AI can be your prompting coach!

**This is advanced:** You're learning to learn!''',
        'example_prompt': '''I wrote this prompt for a security-related task:

"Help me create a password policy for my company."

Now I need you to be my prompt engineering coach. Analyze this prompt and tell me:

1. WHAT'S MISSING: What information would help you give a better answer? (Company size? Industry? Compliance needs? Current issues?)

2. WHAT'S VAGUE: What could be more specific?

3. WHAT FORMAT: How should I specify what format I want the answer in?

4. IMPROVED VERSION: Rewrite this prompt to be much more effective. Show me what a really good prompt looks like for this task.

5. WHY IT'S BETTER: Explain what makes the improved version more effective.

Teach me to write better prompts!''',
    },
]
