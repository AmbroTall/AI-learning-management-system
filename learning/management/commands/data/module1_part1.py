"""
Module 1 Part 1: Prompt Engineering Fundamentals
Challenges 1-8: Basics and Core Concepts (3-4 hours)
"""

MODULE1_PART1_CHALLENGES = [
    {
        'title': 'Your First AI Conversation',
        'description': 'Learn the basics of communicating with AI',
        'difficulty': 'beginner',
        'order': 1,
        'points': 10,
        'instructions': '''Welcome to AI! Let's start with the basics.

**Your Goal:** Have a simple conversation with AI about your career goals.

**What to do:**
1. Introduce yourself
2. Ask AI to help you explore tech careers
3. Be specific about your interests and background

**Tips:**
- Be clear and direct
- Provide context about yourself
- Ask open-ended questions

**Example Context:**
"I'm a construction worker interested in switching to tech. I'm good with my hands and problem-solving. What tech careers might suit me?"''',
        'example_prompt': 'Hi! I\'m John, currently working in construction for 10 years. I\'m really interested in switching to tech because I love problem-solving and learning new tools. I\'m good at understanding how systems work together. Based on this, what tech careers would you recommend for someone like me? Please explain why each might be a good fit.',
    },
    {
        'title': 'Be Specific, Get Better Results',
        'description': 'Learn why specificity matters in prompts',
        'difficulty': 'beginner',
        'order': 2,
        'points': 15,
        'instructions': '''Vague prompts = vague answers. Specific prompts = useful answers!

**Your Goal:** Get AI to create a specific study plan for learning Python.

**Be specific about:**
1. Your current skill level (complete beginner? some coding?)
2. Time available (hours per week)
3. Your learning goal (what do you want to build?)
4. Deadline or timeframe

**Bad Example:** "Help me learn Python"
**Good Example:** Include all 4 details above!

**Challenge:** 
Create a prompt that gets AI to make a personalized 8-week Python learning plan for a complete beginner with 10 hours/week available.''',
        'example_prompt': 'I need a detailed 8-week Python learning plan. Context: I\'m a complete beginner with zero coding experience. I can dedicate 10 hours per week. My goal is to build a simple web scraper for job listings by the end. Please structure it week-by-week with specific topics, resources, and a small project each week to practice.',
    },
    {
        'title': 'Providing Context is Key',
        'description': 'Learn how context improves AI responses',
        'difficulty': 'beginner',
        'order': 3,
        'points': 15,
        'instructions': '''AI doesn't know your background unless you tell it!

**Your Goal:** Get AI to explain a technical concept at YOUR level.

**The Scenario:**
You need to understand what "API" means, but most explanations are too technical.

**What to include:**
1. What you need explained
2. Your background/experience level
3. Why you need to know (context helps!)
4. How you learn best (examples? analogies?)

**Challenge:**
Get AI to explain "API" in a way that someone with NO tech background can understand. Use an analogy they'd relate to!''',
        'example_prompt': 'Can you explain what an API is? Context: I have zero tech background - I work in retail management. I keep hearing about APIs in job descriptions for tech roles. Can you explain it using an analogy related to restaurants or retail that I would understand? Make it simple and practical.',
    },
    {
        'title': 'Breaking Down Complex Tasks',
        'description': 'Learn to structure multi-step requests',
        'difficulty': 'beginner',
        'order': 4,
        'points': 20,
        'instructions': '''Big tasks need clear structure!

**Your Goal:** Get AI to help you write a professional email with multiple requirements.

**The Task:**
You need to email a hiring manager about a job application. The email should:
1. Thank them for the interview
2. Mention 2 specific things discussed
3. Address a concern they raised (your lack of degree)
4. Express enthusiasm
5. Include a call-to-action
6. Be under 200 words

**Challenge:**
Structure your prompt to cover ALL requirements clearly. Number them or use bullet points!''',
        'example_prompt': '''Help me write a follow-up email after a job interview. Requirements:

**Context:**
- Interviewed for Junior Developer role with Sarah Chen yesterday
- She was concerned about my lack of CS degree
- We discussed the company's Python migration project and their remote work culture

**Email must include:**
1. Thank her for her time
2. Reference the Python migration project we discussed
3. Address her degree concern (I have online certificates + portfolio)
4. Show enthusiasm for the remote culture they described
5. Ask about next steps
6. Keep it under 200 words, professional but warm tone

Please draft this email.''',
    },
    {
        'title': 'Using Examples to Guide AI',
        'description': 'Learn how examples shape AI output',
        'difficulty': 'beginner',
        'order': 5,
        'points': 20,
        'instructions': '''Show AI what you want with examples!

**Your Goal:** Get AI to write social media posts in a specific style.

**The Scenario:**
You're helping a local business with their social media. They want posts that are:
- Friendly and casual (not corporate)
- Include a question to engage followers
- 2-3 sentences max
- Use emojis (but not too many!)

**Challenge:**
Provide 2 example posts you like, then ask AI to create 3 more in the same style about different topics.

**Topics for new posts:**
1. New product launch
2. Customer appreciation
3. Behind-the-scenes content''',
        'example_prompt': '''I need social media posts for a small coffee shop. Here's the style we want:

**Example 1:**
"Just brewed our new seasonal blend! ☕ Rich, smooth, with hints of caramel. What's your go-to coffee order on a rainy day? 🌧️"

**Example 2:**
"Morning sunshine! ☀️ Our pastry chef just pulled fresh croissants from the oven. Can you smell them from there? 😊 Stop by before they're gone!"

**Task:**
Write 3 more posts in this exact style for:
1. Announcing a new WiFi upgrade
2. Thanking customers for 5 years in business  
3. Introducing a new barista named Mike

Keep the same tone, length, and emoji usage!''',
    },
    {
        'title': 'Specifying Format and Structure',
        'description': 'Control how AI formats its responses',
        'difficulty': 'intermediate',
        'order': 6,
        'points': 20,
        'instructions': '''You can tell AI exactly HOW to format answers!

**Your Goal:** Get a formatted comparison table from AI.

**The Scenario:**
You're comparing 3 online learning platforms to decide where to study. You want:
- A table format
- Specific comparison criteria
- Clear pros/cons
- A recommendation at the end

**Platforms to compare:**
1. Coursera
2. Udemy  
3. Codecademy

**Compare on:**
- Price
- Certificate value
- Course variety
- Learning style
- Best for beginners?

**Challenge:**
Request the information in a specific format (table + summary).''',
        'example_prompt': '''Compare these 3 learning platforms for me: Coursera, Udemy, and Codecademy.

**Format Required:**
Create a comparison table with these columns:
- Platform name
- Monthly cost
- Certificate value (industry-recognized?)
- Course variety (1-10 scale)
- Learning style (video, interactive, etc.)
- Beginner-friendly? (Yes/No + brief note)

After the table, provide:
1. A 2-sentence summary of each platform
2. Your recommendation for someone who is: complete beginner, wants hands-on practice, budget-conscious, aiming for a career change to web development

Keep it concise and scannable!''',
    },
    {
        'title': 'Setting the Right Tone',
        'description': 'Learn to specify tone and style',
        'difficulty': 'intermediate',
        'order': 7,
        'points': 20,
        'instructions': '''Tone matters! Professional? Casual? Technical? Simple?

**Your Goal:** Get AI to explain the same concept in 3 different tones.

**The Concept:** How GitHub works

**Three audiences:**
1. Your 12-year-old cousin (super simple, fun)
2. Your boss (professional, business-focused)
3. A fellow learner (casual, encouraging)

**Challenge:**
Ask AI to write one explanation for each audience. Specify the tone clearly!''',
        'example_prompt': '''Explain "what is GitHub and why developers use it" in 3 different ways:

**Version 1 - For my 12-year-old cousin:**
- Use simple everyday language
- Include a fun analogy (maybe video games or school projects?)
- 3-4 sentences max
- Enthusiastic tone

**Version 2 - For my boss (non-technical manager):**
- Professional tone
- Focus on business value
- No jargon
- 4-5 sentences
- Emphasize collaboration and project management

**Version 3 - For a fellow coding beginner:**
- Casual, friendly tone
- Mention what we'll actually use it for
- 4-5 sentences
- Encouraging and practical

Please write all three versions.''',
    },
    {
        'title': 'Iterating and Refining',
        'description': 'Learn to improve responses through follow-up',
        'difficulty': 'intermediate',
        'order': 8,
        'points': 25,
        'instructions': '''First answer not perfect? Refine it!

**Your Goal:** Get AI to create and then refine a resume bullet point.

**The Scenario:**
You're updating your resume. You have a bullet point but it's weak:
"Worked on team projects and helped with various tasks"

**Challenge:**
1. First, ask AI to improve it (give context about your actual role)
2. Then, refine it further with specific requirements:
   - Start with action verb
   - Include a metric/number
   - Show impact/result
   - Keep under 20 words

**Your actual role:**
- Led a 5-person team
- Reduced project completion time
- Improved process efficiency

Show the iterative improvement process!''',
        'example_prompt': '''Help me improve this weak resume bullet point:
"Worked on team projects and helped with various tasks"

**Context:**
- Role: Team Lead at construction company
- Actually led a 5-person crew
- Reduced project completion time by 30%
- Implemented new safety protocols

**First request:** Rewrite it to be more impressive and specific.

**Then, refine it to meet these criteria:**
- Start with strong action verb (Led, Spearheaded, Directed, etc.)
- Include the 30% improvement metric
- Show business impact
- Maximum 20 words
- Focus on leadership and results

Give me both versions (improved, then refined).''',
    },
]
