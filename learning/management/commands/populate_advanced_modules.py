from django.core.management.base import BaseCommand
from learning.models import Module, Challenge

class Command(BaseCommand):
    help = 'Populate advanced Module 1 & 2 challenges'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating advanced challenges for Modules 1 & 2...')
        
        # ============================================================
        # MODULE 1: AI Chat Mastery - EXPANDED (15-20 hours)
        # ============================================================
        chat_module = Module.objects.get(title='AI Chat Mastery')
        
        # Delete old challenges to replace with comprehensive ones
        Challenge.objects.filter(module=chat_module).delete()
        
        module1_challenges = [
            # ===== SECTION 1: BASICS (3 hours) =====
            {
                'title': 'Lesson 1: Your First AI Conversation',
                'description': 'Learn how to start a conversation with AI and get useful responses',
                'difficulty': 'beginner',
                'order': 1,
                'points': 10,
                'instructions': '''Welcome to AI Chat Mastery! 🎯

THE CHALLENGE:
Have a conversation with AI to plan a birthday party. Ask AI to help you:
1. Choose a theme
2. Create a guest list structure
3. Plan activities
4. Budget breakdown

WHAT YOU'LL LEARN:
- How to start conversations with AI
- How to ask clear questions
- How to get structured responses

YOUR TASK:
Write ONE prompt that asks AI to help you plan a birthday party for a 10-year-old. Include:
- Number of guests (around 15 kids)
- Budget ($300)
- Theme preferences (they love dinosaurs)
- Duration (3 hours)

Make it conversational and natural!''',
                'example_prompt': '''Help me plan a birthday party! Here's what I need:
- It's for my 10-year-old who LOVES dinosaurs
- About 15 kids will come
- I have $300 to spend
- Party is 3 hours long (2pm-5pm)

Can you suggest:
1. A fun dinosaur theme idea
2. Activities that kids would enjoy
3. Food ideas
4. How to split my $300 budget

Keep it simple and fun!''',
            },
            {
                'title': 'Lesson 2: The Power of Context',
                'description': 'Learn why context makes AI responses way better',
                'difficulty': 'beginner',
                'order': 2,
                'points': 10,
                'instructions': '''Context = Better Responses! 📚

THE CHALLENGE:
Get AI to write a message declining a job offer, but with specific context.

WITHOUT CONTEXT: "Write a job rejection email"
WITH CONTEXT: Include your situation, tone, and specific details

SCENARIO:
You're declining a job offer because:
- You accepted another position
- You liked the company
- You want to stay in touch
- Keep it professional but warm

YOUR TASK:
Write a prompt with FULL context so AI writes a perfect rejection email.

TIP: More context = Better results!''',
                'example_prompt': '''I need help writing a professional email to decline a job offer.

Context:
- Company: TechCorp
- Position: Junior Developer
- Interviewer: Sarah Chen (hiring manager)
- Reason: I accepted another offer
- My feelings: I really liked the company and team
- Tone: Professional but warm, leave door open for future

Please write an email that:
1. Thanks them for the opportunity
2. Declines professionally
3. Gives brief reason (accepted another offer)
4. Expresses hope to stay in touch
5. Keeps it concise (under 150 words)''',
            },
            {
                'title': 'Lesson 3: Breaking Down Complex Tasks',
                'description': 'Learn to break big requests into clear steps',
                'difficulty': 'beginner',
                'order': 3,
                'points': 15,
                'instructions': '''Big tasks need structure! 🏗️

THE CHALLENGE:
Ask AI to help you prepare for a job interview, but structure your request clearly.

WHAT TO INCLUDE:
1. Your situation (job, industry, experience level)
2. Specific help needed (research, questions, answers)
3. Desired format (bullet points, sections, etc.)
4. Timeline/constraints

YOUR TASK:
Write a structured prompt asking AI to help you prepare for a job interview.

JOB: Customer service representative at a bank
YOUR EXPERIENCE: 2 years in retail
INTERVIEW: In 3 days''',
                'example_prompt': '''Help me prepare for a job interview!

MY SITUATION:
- Job: Customer Service Representative at Regional Bank
- My background: 2 years in retail (cashier, handled money)
- Interview date: In 3 days
- My concern: Never worked in banking

WHAT I NEED:
1. RESEARCH SECTION:
   - What should I know about banking customer service?
   - Common challenges in this role

2. QUESTIONS THEY MIGHT ASK:
   - List 5 likely interview questions
   - For each question, give me a good answer structure

3. QUESTIONS I SHOULD ASK:
   - 3-4 smart questions to ask them

4. PREPARATION TIPS:
   - What to do in next 3 days

Format everything clearly with headers and bullet points!''',
            },
            {
                'title': 'Lesson 4: Using Examples to Guide AI',
                'description': 'Show AI exactly what you want with examples',
                'difficulty': 'intermediate',
                'order': 4,
                'points': 15,
                'instructions': '''Examples = Clarity! 💡

THE CHALLENGE:
Get AI to write social media posts for your business, but use examples to show the style you want.

WHY EXAMPLES WORK:
- AI sees your tone
- AI matches your style
- Results are more accurate

YOUR TASK:
You run a small coffee shop. Ask AI to write 3 Instagram captions, but:
1. Give an example of a caption you like
2. Explain what makes it good
3. Ask for similar ones

BUSINESS: Local coffee shop, friendly vibe, eco-conscious''',
                'example_prompt': '''I need Instagram captions for my coffee shop "Bean There."

OUR VIBE: Friendly, community-focused, eco-conscious, warm

EXAMPLE I LOVE:
"☕ Starting your Monday right with our new Maple Cinnamon Latte! Made with locally-sourced maple syrup from Johnson's Farm. Come cozy up with us! 🍁"

WHY I LIKE THIS:
- Specific product name
- Mentions local sourcing (we care about that!)
- Warm, inviting tone
- Emoji use is light but adds feeling
- Includes a call to action

CREATE 3 MORE CAPTIONS like this for:
1. Announcing we're now open Sundays
2. Featuring our new breakfast sandwich
3. Promoting our reusable cup discount

Match the tone, style, and emoji use!''',
            },
            {
                'title': 'Lesson 5: Asking AI to Improve Its Own Work',
                'description': 'Learn iterative prompting - making responses better',
                'difficulty': 'intermediate',
                'order': 5,
                'points': 20,
                'instructions': '''Iteration = Perfection! 🔄

THE CHALLENGE:
Write a prompt that asks AI for something, THEN asks AI to improve it.

THIS TEACHES:
- First draft → refinement process
- How to give feedback to AI
- Getting exactly what you want

YOUR TASK:
Ask AI to write a product description for an eco-friendly water bottle, then in THE SAME prompt, ask it to make it better.

STRUCTURE:
1. First request (write description)
2. Then ask to improve it (make it more persuasive, add benefits, etc.)

PRODUCT: Stainless steel water bottle, keeps drinks cold 24hrs, plastic-free''',
                'example_prompt': '''I need help writing a product description.

PRODUCT: EcoFlow Stainless Steel Water Bottle
FEATURES:
- Keeps drinks cold for 24 hours
- 100% plastic-free
- BPA-free
- Leak-proof lid
- Fits cup holders
- 32oz capacity
- 5 color options

TASK PART 1:
Write a product description (about 100 words) that highlights these features.

TASK PART 2:
After you write it, improve it by:
1. Making the opening line more attention-grabbing
2. Adding emotional appeal (why people WANT this)
3. Including a call-to-action at the end
4. Make it more persuasive overall

Show me both versions (original and improved) so I can see the difference!''',
            },

            # ===== SECTION 2: MAINTAINING CONVERSATIONS (4 hours) =====
            {
                'title': 'Lesson 6: Building on Previous Responses',
                'description': 'Learn how to continue conversations naturally with AI',
                'difficulty': 'intermediate',
                'order': 6,
                'points': 20,
                'instructions': '''Conversations build on context! 💬

THE CHALLENGE:
Write a multi-turn conversation prompt where each question builds on the previous answer.

REAL-WORLD USE:
- Refining ideas
- Deep research
- Problem solving
- Creative work

YOUR TASK:
You're planning to start a side business. Write a prompt that:
1. Asks AI for business ideas based on your skills
2. Then picks one and asks for a detailed plan
3. Then asks about specific challenges
4. Finally asks for first steps

SIMULATE A CONVERSATION in ONE prompt!

YOUR SKILLS: Graphic design, 5 years experience, love teaching''',
                'example_prompt': '''I want to brainstorm a side business. Let's have a conversation:

MY BACKGROUND:
- Skills: Graphic design (5 years professional)
- Love: Teaching and helping others learn
- Time: 10-15 hours/week available
- Budget: $500 to start

CONVERSATION FLOW:

QUESTION 1: Based on my skills and constraints, suggest 3 side business ideas. For each, briefly explain the concept and why it fits me.

[Wait for AI response]

QUESTION 2: I like idea #2 the most. Give me a detailed plan:
- How to start
- What I'd need
- Time commitment
- Potential earnings in first 3 months

[Wait for AI response]

QUESTION 3: What are the 3 biggest challenges I'd face with this business? Be realistic.

[Wait for AI response]

QUESTION 4: Give me a concrete action plan for the first 2 weeks. What should I do each day?

Please go through this conversation step by step, answering each question fully before moving to the next!''',
            },
            {
                'title': 'Lesson 7: Using Memory - Projects Across Sessions',
                'description': 'Learn to make AI remember context for ongoing projects',
                'difficulty': 'intermediate',
                'order': 7,
                'points': 25,
                'instructions': '''Memory = Continuity! 🧠

THE CHALLENGE:
Write a prompt that ESTABLISHES context for an ongoing project that you'll work on across multiple sessions.

WHY THIS MATTERS:
- Real projects take multiple sessions
- You need AI to remember your project details
- Saves you from repeating yourself

YOUR TASK:
You're writing a novel. Create a prompt that:
1. Establishes the project (your novel)
2. Gives key details AI should remember
3. Sets expectations for future conversations
4. Asks for specific help today

NOVEL DETAILS:
- Genre: Mystery
- Setting: Small coastal town
- Main character: Detective Sarah Mills, 35, returning to hometown
- Plot: Series of strange burglaries

**Note:** In real use, you'd start new chats by saying "Continuing our novel project..." and AI would remember!''',
                'example_prompt': '''I'm starting a long-term project and need your help across multiple sessions.

PROJECT: Writing a Mystery Novel

KEY DETAILS (please remember these):
📚 TITLE: "Tides of Secrets"
📍 SETTING: Oceanview, small coastal Maine town (population 3,000)
👤 PROTAGONIST: Detective Sarah Mills
   - Age: 35
   - Background: Left Oceanview 15 years ago, now returning
   - Personality: Methodical, haunted by past, struggles with small-town politics

🔍 PLOT: Series of strange burglaries in town
   - Items stolen: Old photographs, personal journals, family heirlooms
   - Pattern: Only targeting founding families
   - Twist: Connected to town's dark secret from 30 years ago

✍️ WRITING STYLE: Atmospheric, character-driven, slow-burn suspense

STATUS: Currently outlining, no chapters written yet

TODAY'S HELP:
I need to develop 3 major supporting characters:
1. The police chief (Sarah's former mentor)
2. A local historian (potential ally or suspect?)
3. A wealthy family matriarch (connected to founding families)

For each character, provide:
- Name and age
- Occupation and role in town
- Personality traits (3-4)
- Secret they're hiding
- How they help or hinder Sarah's investigation

Make them feel real and complex!

[In future chats, I'll say "Continuing our Tides of Secrets project" and you'll remember all this context]''',
            },
            {
                'title': 'Lesson 8: Chain of Thought - Teaching AI to Think',
                'description': 'Get better answers by asking AI to show its reasoning',
                'difficulty': 'advanced',
                'order': 8,
                'points': 25,
                'instructions': '''Make AI think step-by-step! 🤔

THE CHALLENGE:
Ask AI to solve a problem, but request it shows its thinking process.

CHAIN OF THOUGHT = Asking AI to:
- Break down its reasoning
- Show each step
- Explain its logic

RESULT: More accurate, thoughtful answers

YOUR TASK:
You're deciding between two job offers. Ask AI to help you decide, but make it show its reasoning process step by step.

JOB A: Higher pay, longer commute, big company
JOB B: Lower pay, walking distance, startup''',
                'example_prompt': '''Help me decide between two job offers. I want you to think through this step-by-step and show your reasoning.

JOB A: Enterprise Solutions Corp
- Salary: $85,000/year
- Commute: 1.5 hours each way (by car)
- Company: Fortune 500, 10,000+ employees
- Role: Junior Data Analyst on established team
- Benefits: Excellent (full health, 401k match, 4 weeks vacation)
- Growth: Structured career path, annual reviews
- Culture: Professional, formal, stable

JOB B: DataFlow Startup
- Salary: $70,000/year
- Commute: 15-minute walk
- Company: Startup, 25 employees
- Role: Data Analyst (more responsibilities)
- Benefits: Good (health, basic 401k, 3 weeks vacation)
- Growth: Learn many things, more responsibility fast
- Culture: Casual, fast-paced, uncertain future

MY PRIORITIES (in order):
1. Work-life balance
2. Learning opportunities
3. Financial stability
4. Career growth

PLEASE ANALYZE STEP-BY-STEP:

STEP 1: Evaluate each job against each priority
STEP 2: Consider trade-offs (what I give up with each choice)
STEP 3: Think about 1-year, 3-year, 5-year implications
STEP 4: Consider my life stage (I'm 26, single, no debt)
STEP 5: Make recommendation with clear reasoning

Show me your complete thought process, not just the answer!''',
            },

            # ===== SECTION 3: ADVANCED TECHNIQUES (4 hours) =====
            {
                'title': 'Lesson 9: Role-Playing for Expert Advice',
                'description': 'Get specialized knowledge by assigning AI specific roles',
                'difficulty': 'advanced',
                'order': 9,
                'points': 30,
                'instructions': '''Roles = Expertise! 👔

THE CHALLENGE:
Ask AI to take on a specific expert role and give advice from that perspective.

WHY IT WORKS:
- AI responds with expert-level knowledge
- Uses professional terminology
- Gives more detailed, credible advice

YOUR TASK:
You want to negotiate a salary raise. Ask AI to act as an experienced career coach and help you prepare.

INCLUDE:
- The role AI should take
- Their credentials/background
- Your specific situation
- What advice you need''',
                'example_prompt': '''I need expert help with salary negotiation.

YOUR ROLE:
Act as an experienced Career Coach and Salary Negotiation Expert with:
- 15 years experience coaching professionals
- Specialized in tech industry negotiations
- Helped 500+ people successfully negotiate raises
- Former HR director at Fortune 500 company

MY SITUATION:
- Current role: Software Developer (2 years at company)
- Current salary: $75,000
- Want to ask for: $90,000 (20% raise)
- Performance: Consistently exceeded goals, took on extra projects
- Market rate: $85-95k for my role in my city
- Annual review: Coming up in 2 weeks

AS A SALARY NEGOTIATION EXPERT, HELP ME:

1. REALISTIC ASSESSMENT:
   - Is my ask reasonable given my situation?
   - What should I actually ask for?

2. BUILDING MY CASE:
   - What evidence/achievements should I highlight?
   - How to quantify my contributions?

3. THE CONVERSATION:
   - Script: How to start the conversation with my manager
   - Responses: How to handle common pushbacks
   - Alternatives: What if they say no to salary but offer other benefits?

4. TIMING & STRATEGY:
   - Best time to have this conversation
   - What to do before, during, after

5. RED FLAGS:
   - What mistakes should I avoid?

Give me professional, actionable advice as an expert would!''',
            },
            {
                'title': 'Lesson 10: Constraints Drive Creativity',
                'description': 'Learn how adding constraints gets better, focused results',
                'difficulty': 'advanced',
                'order': 10,
                'points': 30,
                'instructions': '''Constraints = Better Results! 🎯

THE CHALLENGE:
Write a creative prompt with SPECIFIC constraints that guide AI to produce exactly what you want.

CONSTRAINTS TO USE:
- Length (exact word count)
- Style (tone, voice)
- Structure (format)
- Content rules (must include/exclude)
- Audience (who it's for)

YOUR TASK:
Ask AI to write a "About Me" section for your professional website, but add 5+ specific constraints.

ABOUT YOU:
- Freelance photographer
- Specialize in wedding photography
- 8 years experience
- Based in Austin, Texas
- Want to attract high-end clients''',
                'example_prompt': '''Write an "About Me" section for my photography website.

WHO I AM:
- Professional wedding photographer
- 8 years experience
- Austin, Texas based
- Shot 100+ weddings
- Style: Candid, emotional, natural light

CONSTRAINTS:

1. LENGTH: Exactly 150-175 words
2. TONE: Professional but warm and approachable
3. STRUCTURE:
   - First paragraph: Who I am and my philosophy (3-4 sentences)
   - Second paragraph: My experience and approach (3-4 sentences)
   - Final sentence: Call to action
4. MUST INCLUDE:
   - The phrase "authentic moments"
   - Reference to Austin/Texas
   - My years of experience
   - What makes my style unique
5. MUST AVOID:
   - Clichés like "passion for photography" or "love what I do"
   - Technical jargon
   - Overly promotional language
   - First person past tense
6. VOICE: First person, confident but not arrogant
7. AUDIENCE: Engaged couples, budget $5,000+, value artistry

Make it feel genuine and make high-end clients want to hire me!''',
            },

            # ===== SECTION 4: REAL-WORLD APPLICATIONS (4 hours) =====
            {
                'title': 'Lesson 11: Research & Analysis',
                'description': 'Use AI to research topics and analyze information',
                'difficulty': 'advanced',
                'order': 11,
                'points': 35,
                'instructions': '''AI = Research Assistant! 🔍

THE CHALLENGE:
Ask AI to research a topic and provide structured analysis.

YOUR TASK:
You're considering learning data science. Ask AI to:
1. Research the field
2. Analyze job prospects
3. Compare learning paths
4. Give actionable recommendations

MAKE YOUR PROMPT:
- Specific about your situation
- Request structured output
- Ask for sources/evidence
- Include decision criteria''',
                'example_prompt': '''I need comprehensive research to make an important career decision.

MY SITUATION:
- Current: Marketing manager (5 years experience)
- Age: 30
- Location: Remote work preferred
- Time: Can dedicate 15-20 hours/week to learning
- Budget: $3,000 for courses/bootcamps
- Timeline: Want to transition in 12-18 months

RESEARCH TOPIC: Transitioning to Data Science Career

COMPREHENSIVE ANALYSIS NEEDED:

1. FIELD OVERVIEW:
   - What does a data scientist actually do day-to-day?
   - Is it right for someone from marketing?
   - How has the field changed 2020-2024?

2. SKILLS ASSESSMENT:
   - What skills from marketing transfer?
   - What technical skills are essential?
   - What math background is required?

3. LEARNING PATHS (compare 3 options):
   - Self-taught (online courses)
   - Bootcamp (immersive program)
   - Part-time master's degree
   
   For each, analyze:
   - Time required
   - Cost
   - Success rate for career changers
   - Employer perception
   - Pros and cons

4. JOB MARKET REALITY:
   - Entry-level salaries for career changers
   - Hiring trends 2024
   - Remote work opportunities
   - Competition level
   - What employers want to see

5. RECOMMENDATION:
   - Given MY specific situation, what path makes most sense?
   - Realistic timeline for me?
   - What should I do in first 3 months?
   - Red flags or challenges I should expect?

6. ACTION PLAN:
   - Specific steps for next 30, 60, 90 days
   - Resources to start with
   - How to know if this is right for me

Be realistic and honest. I want the truth, not just encouragement!''',
            },
            {
                'title': 'Lesson 12: Problem-Solving Framework',
                'description': 'Use AI to systematically solve complex problems',
                'difficulty': 'advanced',
                'order': 12,
                'points': 35,
                'instructions': '''Structure = Solutions! 🎯

THE CHALLENGE:
Present a real problem to AI and ask it to use a structured problem-solving approach.

YOUR TASK:
You run a small online store and sales dropped 40%. Ask AI to help diagnose and solve the problem using a systematic framework.

INCLUDE:
- Clear problem statement
- Relevant data/context
- Request specific framework
- Ask for actionable solutions''',
                'example_prompt': '''I have a serious business problem and need systematic help solving it.

PROBLEM: My online store sales dropped 40% in the last 2 months

BUSINESS CONTEXT:
- Online store: Handmade jewelry
- Been running: 3 years
- Previous sales: $8,000-10,000/month
- Current sales: $4,000-5,000/month
- No major changes to products
- Same social media activity
- Website still running fine

WHAT I'VE NOTICED:
- Website traffic is actually UP 20%
- Social media engagement is normal
- Email open rates are the same
- Shopping cart abandonment increased (was 60%, now 85%)
- Customer complaints: None
- Competition: Two new stores opened selling similar items

PLEASE USE THIS PROBLEM-SOLVING FRAMEWORK:

STEP 1 - DEFINE THE PROBLEM:
   - What is the core issue here?
   - What are symptoms vs root cause?

STEP 2 - GATHER & ANALYZE DATA:
   - What data points are most important?
   - What additional data should I collect?
   - What does the data tell us?

STEP 3 - GENERATE HYPOTHESES:
   - List 5 possible reasons for the sales drop
   - Rank them by likelihood

STEP 4 - TEST & VALIDATE:
   - For top 3 hypotheses, how can I test if they're the cause?
   - What would I see if each hypothesis is true?

STEP 5 - DEVELOP SOLUTIONS:
   - For each likely cause, what are 2-3 solutions?
   - Quick wins (do immediately)
   - Long-term fixes

STEP 6 - ACTION PLAN:
   - What should I do THIS WEEK?
   - What should I do THIS MONTH?
   - How will I measure if solutions work?

Be thorough and analytical. Help me save my business!''',
            },
        ]
        
        # Create all Module 1 challenges
        for i, challenge_data in enumerate(module1_challenges):
            challenge, created = Challenge.objects.get_or_create(
                module=chat_module,
                title=challenge_data['title'],
                order=i + 1,
                defaults=challenge_data
            )
            if created:
                self.stdout.write(f'✅ Created: {challenge.title}')
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Created {len(module1_challenges)} challenges for Module 1!'))
        
        # TO BE CONTINUED: Module 2 challenges will be added next...
        self.stdout.write(self.style.WARNING('\nModule 2 challenges coming next...'))
