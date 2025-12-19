"""
Module 1 Part 2: Memory & Context Management
Challenges 9-16: Managing conversations and context (4-5 hours)
"""

MODULE1_PART2_CHALLENGES = [
    {
        'title': 'Understanding AI Memory Basics',
        'description': 'Learn how AI remembers within conversations',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 25,
        'instructions': '''AI remembers your conversation... but only the current one!

**Your Goal:** Learn to build context within a conversation.

**Key Concept:**
- AI remembers what you said earlier in THIS chat
- It forgets when you start a new chat
- You need to reference previous context

**Challenge:**
Create a prompt that:
1. Establishes your project (building a portfolio website)
2. Asks for advice on color schemes
3. Then in your NEXT message, reference that conversation and ask about fonts
4. Show you understand how to maintain context

Write BOTH prompts (first and follow-up).''',
        'example_prompt': '''**First Prompt:**
I'm building my first portfolio website to showcase my coding projects. I want it to look professional but approachable. The site will feature:
- 5 Python projects
- My background story (career transition from construction)
- Contact form

What color scheme would you recommend? I'm thinking something modern and tech-focused but not too cold or corporate.

**Follow-up Prompt (after AI responds):**
Thanks! Based on the color scheme you just recommended, what font pairings would work well? I need:
- A heading font that's bold and professional
- A body text font that's very readable
- Should work with the colors you suggested

Please explain why each font choice works with the overall design.''',
    },
    {
        'title': 'Building Multi-Turn Conversations',
        'description': 'Master the art of conversation flow',
        'difficulty': 'intermediate',
        'order': 10,
        'points': 25,
        'instructions': '''Complex tasks need multiple back-and-forth exchanges!

**Your Goal:** Plan a 3-message conversation to build a project plan.

**The Project:**
Creating a personal budget tracker (you'll build this later!)

**Message 1:** Introduce the project idea, get initial feedback
**Message 2:** Based on feedback, ask about specific features
**Message 3:** Request a technical roadmap

**Challenge:**
Write all 3 prompts showing how each builds on the previous response. Use phrases like:
- "Based on what you just said..."
- "Building on that idea..."
- "Considering your feedback about..."''',
        'example_prompt': '''**Message 1:**
I want to build a simple personal budget tracker as my first coding project. Goals:
- Track income and expenses
- Categorize spending
- Show monthly summaries
- Nothing too complex - I'm a beginner

Is this a good first project? What should I focus on first?

**Message 2 (after AI responds):**
Based on your feedback about starting simple, let me narrow down the features. For my MVP (first working version), which 3 features are absolutely essential? And which ones can I add later as "nice-to-haves"?

Original features I was thinking:
- Manual entry of transactions
- Spending categories
- Monthly reports
- Budget limits/alerts
- Data visualization (charts)
- Export to Excel

**Message 3 (after AI prioritizes):**
Perfect! Based on the 3 core features you recommended, can you create a beginner-friendly roadmap? Break it into:
- Week 1: [what to learn/build]
- Week 2: [what to learn/build]
- Week 3: [what to learn/build]
- Week 4: [what to learn/build]

Assume I know basic Python but nothing about web development yet.''',
    },
    {
        'title': 'Providing Context Upfront',
        'description': 'Learn to front-load important context',
        'difficulty': 'intermediate',
        'order': 11,
        'points': 30,
        'instructions': '''Give AI all context at the start for best results!

**Your Goal:** Create a comprehensive context block for a complex task.

**The Task:**
You need help preparing for a technical interview.

**Context to provide:**
- Your background (current role, experience level)
- The role you're interviewing for
- Your strengths and weak areas
- Timeline (interview date)
- What kind of help you need

**Challenge:**
Write a single, well-structured prompt that includes ALL context upfront, then makes a clear request.

Use formatting (bullet points, sections) to organize the context!''',
        'example_prompt': '''I need help preparing for a technical interview. Here's my complete context:

**My Background:**
- Currently: Warehouse logistics coordinator (5 years)
- Learning: Python and SQL (6 months of online courses)
- Completed: 3 portfolio projects (inventory tracker, data dashboard, web scraper)
- No CS degree, but have Google IT Support Certificate

**The Interview:**
- Role: Junior Data Analyst at healthcare company
- Interview Date: 2 weeks from today
- Format: 1-hour technical interview + 30-min behavioral

**My Strengths:**
- Strong problem-solving skills
- Good with Excel and data analysis concepts
- Can explain technical concepts simply
- Real work experience with data/logistics

**My Weak Areas:**
- Statistics (only basic knowledge)
- Never done technical interview before
- Nervous about coding on the spot
- Limited SQL practice (only learned theory)

**What I Need:**
1. List of topics to study (prioritized by importance)
2. Practice problems I should work on
3. Tips for explaining my non-traditional background
4. How to stay calm during live coding
5. A 2-week study schedule

Please create a comprehensive interview prep plan based on this!''',
    },
    {
        'title': 'Maintaining Context Across Topics',
        'description': 'Learn to reference earlier context when changing topics',
        'difficulty': 'intermediate',
        'order': 12,
        'points': 30,
        'instructions': '''Keep AI aware of your situation even when topics shift!

**Your Goal:** Have a conversation that covers multiple related topics while maintaining context.

**The Scenario:**
You're planning a career transition. You'll discuss:
1. Resume updates
2. Skill gaps  
3. Networking strategy

Each topic builds on your overall goal!

**Challenge:**
Write 3 prompts (one per topic) where each references your core context: career transition from retail → tech support.''',
        'example_prompt': '''**Prompt 1 - Resume:**
I'm transitioning from retail management (8 years) to tech support. I need to update my resume to highlight transferable skills. 

Current resume focuses on:
- Staff management (15-person team)
- Inventory systems (used POS software daily)
- Customer problem-solving
- Training new employees

How should I reframe these for tech support roles? What's transferable?

**Prompt 2 - Skill Gaps:**
Following up on my retail → tech support transition we just discussed: I've analyzed tech support job postings. They want:
- Ticketing systems (I have none)
- Basic networking (I'm weak here)
- Windows/Mac troubleshooting (some knowledge)
- Customer service (this is my strength!)

Given my retail background and customer service experience, which gaps should I prioritize? What's the fastest way to fill them?

**Prompt 3 - Networking:**
For my retail → tech support transition (we discussed resume and skills): I need a networking strategy. Problems:
- Don't know anyone in tech
- Never been to networking events
- Uncomfortable with "selling myself"
- But I AM good at building customer relationships!

How can I leverage my retail networking skills (customer relationships, team building) for tech networking? Give me a practical action plan.''',
    },
    {
        'title': 'Using Memory for Personalization',
        'description': 'Teach AI your preferences for consistent help',
        'difficulty': 'intermediate',
        'order': 13,
        'points': 30,
        'instructions': '''Train AI to remember your style and preferences!

**Your Goal:** Establish your preferences, then use them.

**The Concept:**
Tell AI upfront:
- How you learn best
- Your communication style
- Your constraints (time, budget)
- Your goals

Then reference these in future requests!

**Challenge:**
First message: Establish your learning profile
Second message: Request help with a topic, referencing your profile''',
        'example_prompt': '''**Message 1 - Setting Preferences:**
Before we start working together, here's how I learn best:

**My Learning Style:**
- I'm a hands-on learner (need to DO things, not just read)
- Short explanations work better than long lectures
- I love real-world examples and analogies
- Need to see the "why" before the "how"

**My Constraints:**
- 1 hour per day for learning (early mornings, 6-7am)
- Limited budget ($20/month max for resources)
- Need free or cheap tools
- Working full-time, so no bootcamps

**My Communication Preference:**
- Give me actionable steps, not just theory
- If I'm wrong, tell me directly (I can take it!)
- Use simple language, avoid unnecessary jargon
- Break big concepts into small pieces

**My Goals:**
- Land a junior developer job in 6 months
- Focus on practical skills over credentials
- Build a portfolio of real projects

Got it? Let's work together with this in mind!

**Message 2 - Using Preferences:**
Based on my learning style (hands-on, practical, 1 hour/day) and budget constraints ($20/month) that I just shared:

I need to learn Git and GitHub this week. But most tutorials are:
- Too long and theoretical
- Assume I have time for 3-hour videos
- Don't explain WHY I need it

Can you create a learning plan that fits MY style? I want to:
- Understand the core concept quickly (the "why")
- Practice with a real mini-project
- Have something working in 5 days
- Use free tools only

Remember: hands-on, actionable steps, broken into 1-hour daily chunks!''',
    },
    {
        'title': 'Context Windows and Token Limits',
        'description': 'Understand AI memory limitations',
        'difficulty': 'intermediate',
        'order': 14,
        'points': 30,
        'instructions': '''AI memory has limits! Learn to work within them.

**Your Goal:** Learn to summarize and carry forward key context.

**The Reality:**
- Very long conversations can lose early context
- AI has a "memory limit" (token window)
- Solution: Periodically summarize what matters

**The Scenario:**
You've had a long conversation about building a website. Now you need to reference it in a new chat.

**Challenge:**
Write a prompt for a NEW conversation that summarizes the key points from your "previous" conversation and makes a new request.

Include:
- Brief summary of previous discussion
- Key decisions made
- Current status
- New question''',
        'example_prompt': '''Hi! I need to continue our website project discussion from yesterday. Let me catch you up:

**Previous Conversation Summary:**
- Project: Portfolio website for career transition (construction → web dev)
- Design: Decided on blue/gray color scheme, minimalist style
- Sections: Home, Projects (5 Python projects), About Me, Contact
- Tech Stack: Started with HTML/CSS/JavaScript (no framework yet)
- Progress: Finished basic HTML structure, started CSS

**Key Decisions Made:**
1. Mobile-first approach
2. No complicated animations (keep it clean)
3. Prioritize fast loading over fancy features
4. Include GitHub links for each project

**Current Status:**
- HTML structure: ✅ Done
- CSS styling: 30% complete
- JavaScript: Not started
- Content (project descriptions): Need to write these

**Today's Question:**
For the "Projects" section, I need to write compelling descriptions of my 5 Python projects. They're:
1. Budget tracker
2. Web scraper (job listings)
3. Weather dashboard  
4. Automation script (file organizer)
5. Simple API

Given my goal (career transition, showing skills to employers), how should I structure each project description? What should I emphasize? Should they all follow the same format?

Please give me a template I can use for all 5.''',
    },
    {
        'title': 'Memory for Code Reviews',
        'description': 'Use context to get better code feedback',
        'difficulty': 'advanced',
        'order': 15,
        'points': 35,
        'instructions': '''When asking for code review, context is EVERYTHING!

**Your Goal:** Get useful code feedback by providing rich context.

**What AI needs to know:**
- Your skill level
- What the code does
- What you're unsure about
- What specific feedback you want
- The code itself

**Challenge:**
Write a prompt asking for code review. Include:
1. Your experience level
2. What you're trying to accomplish
3. Specific concerns you have
4. The code (you can use a simple example)
5. Type of feedback wanted (performance? readability? best practices?)''',
        'example_prompt': '''I need a code review. Context first:

**My Level:**
- Learning Python for 3 months
- This is my 4th project
- Understand basics but unsure about best practices
- First time using functions extensively

**What This Code Does:**
A simple password validator that checks if a password is strong enough. Rules:
- At least 8 characters
- Has uppercase and lowercase
- Has a number
- Has a special character

**My Concerns:**
1. Is this the "Pythonic" way to do it?
2. Am I handling errors correctly?
3. Could it be simpler/more readable?
4. Any security issues I'm missing?

**The Code:**
```python
def validate_password(password):
    if len(password) < 8:
        return False, "Too short"
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*"
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True
    
    if not has_upper:
        return False, "Needs uppercase"
    if not has_lower:
        return False, "Needs lowercase"  
    if not has_digit:
        return False, "Needs number"
    if not has_special:
        return False, "Needs special character"
    
    return True, "Strong password!"

# Test it
result, message = validate_password("MyPass123!")
print(f"Valid: {result}, Message: {message}")
```

**What I Want:**
- Is this readable for other beginners?
- Better way to check for character types?
- Any Python features I should use instead?
- Rate it: beginner/intermediate/advanced code?

Please be honest but constructive!''',
    },
    {
        'title': 'Session Management Strategy',
        'description': 'Learn when to continue vs. start fresh',
        'difficulty': 'advanced',
        'order': 16,
        'points': 35,
        'instructions': '''Know when to continue a conversation vs. start a new one!

**Your Goal:** Understand conversation strategy.

**When to CONTINUE a conversation:**
- Building on previous work
- Need context from earlier
- Iterating on a solution
- Same topic/project

**When to START FRESH:**
- Completely new topic
- Old context might confuse AI
- Previous conversation was messy
- Need a clean slate

**Challenge:**
You have 2 scenarios. For each, explain whether you'd continue or start fresh, and write the appropriate prompt.

**Scenario 1:**
You spent an hour discussing a Python project structure. Now you need help with a JavaScript problem.

**Scenario 2:**
You got feedback on your resume yesterday. Today you want to implement the changes and get a second review.''',
        'example_prompt': '''**Scenario 1: START FRESH**
*Why:* Different language, different context. Python discussion might confuse a JavaScript question.

*New Conversation Prompt:*
I'm learning JavaScript and stuck on array methods. Quick context:
- I know Python well (used lists frequently)
- New to JavaScript (1 week in)
- Understand variables, functions, conditionals

Problem: I need to filter an array of numbers, keeping only values > 10. In Python I'd use list comprehension, but what's the JavaScript way?

```javascript
let numbers = [5, 12, 8, 130, 44, 3];
// Need to get: [12, 130, 44]
```

What's the best approach? Show me the solution and explain how it works.

---

**Scenario 2: CONTINUE CONVERSATION**
*Why:* Same topic (resume), need previous context (the feedback), iterating on it.

*Follow-up Prompt in Same Conversation:*
I've implemented your feedback from yesterday on my resume. Changes made:
- Reworded all bullet points with action verbs ✅
- Added metrics to 3 accomplishments ✅  
- Removed the "objective" section ✅
- Tightened it from 2 pages to 1.5 pages ✅

Still working on:
- The "Skills" section (you said it was too generic)

Can you review my updated "Skills" section now? Here's what I have:

**Skills:**
- Python (pandas, requests, flask)
- SQL (PostgreSQL, MySQL)
- Data Analysis (Excel, Tableau)
- Problem Solving
- Team Collaboration

Based on your earlier feedback, how can I make this more specific and impressive? Should I include proficiency levels? Projects where I used each skill?''',
    },
]
