from django.core.management.base import BaseCommand
from learning.models import Module, Challenge, Achievement


class Command(BaseCommand):
    help = 'Populate the database with sample modules and challenges'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')
        
        # Create Modules
        modules_data = [
            {
                'title': 'AI Chat Mastery',
                'description': 'Master the art of prompt engineering. Learn to communicate effectively with AI through structured challenges that teach you to craft precise, effective prompts.',
                'module_type': 'chat',
                'order': 1,
                'duration_hours': 15,
                'icon': '💬',
            },
            {
                'title': 'Build AI-Powered Tools',
                'description': 'Build real AI tools from scratch! Create a task manager with calendar integration, build a smart assistant agent, and automate workflows. Hands-on projects using Claude API.',
                'module_type': 'builder',
                'order': 2,
                'duration_hours': 20,
                'icon': '🚀',
            },
            {
                'title': 'Code with AI Assistant',
                'description': 'Learn Python coding with AI as your personal tutor! Build simple games, calculators, and apps. AI guides you step-by-step - perfect for absolute beginners.',
                'module_type': 'coding',
                'order': 3,
                'duration_hours': 20,
                'icon': '💻',
            },
            {
                'title': 'AI + Data Magic',
                'description': 'Unlock the power of AI for data analysis. Learn to ask the right questions, visualize insights, and make data-driven decisions.',
                'module_type': 'data',
                'order': 4,
                'duration_hours': 15,
                'icon': '📊',
            },
        ]
        
        for module_data in modules_data:
            module, created = Module.objects.get_or_create(
                title=module_data['title'],
                defaults=module_data
            )
            if created:
                self.stdout.write(f'Created module: {module.title}')
        
        # Set up module prerequisites (each module requires previous one)
        modules = Module.objects.all().order_by('order')
        for i, module in enumerate(modules):
            if i > 0:
                module.prerequisite = modules[i-1]
                module.save()
                self.stdout.write(f'Set prerequisite for {module.title}: {module.prerequisite.title}')
        
        # Create Challenges for AI Chat Mastery
        chat_module = Module.objects.get(title='AI Chat Mastery')
        
        chat_challenges = [
            {
                'title': 'Your First Prompt',
                'description': 'Learn the basics of crafting an effective AI prompt',
                'difficulty': 'beginner',
                'order': 1,
                'points': 10,
                'instructions': '''Welcome to your first challenge!

Your goal: Get the AI to write a professional email introducing yourself to a new team.

Tips:
- Be specific about what you want
- Provide context (who you are, what team)
- Mention the tone you want (professional, friendly, etc.)

Try to make your prompt clear and complete in one message.''',
                'example_prompt': 'Write a professional email introducing myself as John Doe, a new software engineer joining the Platform team. Keep it friendly but professional, around 3 paragraphs.',
            },
            {
                'title': 'The Power of Context',
                'description': 'Learn how providing context improves AI responses',
                'difficulty': 'beginner',
                'order': 2,
                'points': 15,
                'instructions': '''Context is everything!

Your goal: Get the AI to explain quantum computing to a 10-year-old.

The key here is to:
- Specify your audience clearly (age, background)
- Mention the complexity level you want
- Give constraints (length, use of analogies)

The more context you provide, the better the response!''',
                'example_prompt': 'Explain quantum computing to a 10-year-old child who loves LEGO. Use simple analogies they can understand. Keep it under 100 words.',
            },
            {
                'title': 'Structured Requests',
                'description': 'Use structure to get organized responses',
                'difficulty': 'intermediate',
                'order': 3,
                'points': 20,
                'instructions': '''Structure helps AI give you exactly what you need.

Your goal: Get the AI to create a morning routine plan with specific categories.

Try to:
- Ask for a specific format (bullet points, numbered list, etc.)
- Request specific sections or categories
- Set time constraints or priorities

Show that you can request structured output!''',
                'example_prompt': 'Create a morning routine for a busy professional. Structure it with: 1) Wake-up time and activities (30 min), 2) Exercise routine (20 min), 3) Breakfast ideas (15 min), 4) Work prep (15 min). Use bullet points for each section.',
            },
            {
                'title': 'The Iterative Approach',
                'description': 'Learn to refine and improve responses through follow-ups',
                'difficulty': 'intermediate',
                'order': 4,
                'points': 20,
                'instructions': '''Sometimes the first response isn\'t perfect - and that\'s okay!

Your goal: Get the AI to write a tweet about climate change, but make it:
- Under 280 characters
- Inspiring but not preachy
- Include a call to action
- Use ONE relevant emoji

Your first prompt might not nail all these requirements. That's the learning!''',
                'example_prompt': 'Write an inspiring tweet about taking action on climate change. Keep it under 280 characters, include a call to action, and use one relevant emoji. Make the tone hopeful, not preachy.',
            },
            {
                'title': 'Role-Playing for Better Results',
                'description': 'Assign roles to AI for specialized responses',
                'difficulty': 'advanced',
                'order': 5,
                'points': 25,
                'instructions': '''Give the AI a role to get expert-level responses!

Your goal: Get business advice as if from a startup mentor who has built 3 successful companies.

Technique:
- Start with "Act as..." or "You are..."
- Give the AI credentials/background
- Ask your question with specific context

The AI will respond from that perspective!''',
                'example_prompt': 'Act as a successful startup founder who has built and sold 3 tech companies. I\'m launching a SaaS product and struggling with pricing. My target market is small businesses (10-50 employees). What pricing strategy would you recommend and why?',
            },
            {
                'title': 'Build Your AI Personal Assistant',
                'description': 'Create a multi-step AI agent that manages tasks',
                'difficulty': 'advanced',
                'order': 6,
                'points': 50,
                'instructions': '''🚀 CAPSTONE PROJECT: Build a real AI agent!

You'll create a prompt that makes Claude act as your personal assistant that can:
1. Understand complex multi-step requests
2. Break down tasks into actionable steps
3. Provide structured responses with priorities
4. Remember context across the conversation

Your Challenge:
Create a prompt that gets Claude to help you plan a productive week by:
- Taking your goals and available time
- Breaking them into daily tasks
- Prioritizing based on importance/urgency
- Creating a realistic schedule
- Providing morning briefings

Requirements for your prompt:
✓ Define the AI's role clearly (Personal Productivity Assistant)
✓ Specify the output format (daily breakdown, time blocks, priorities)
✓ Include instructions for handling conflicts
✓ Request actionable, specific tasks (not vague goals)
✓ Ask for a summary/overview at the start

Example scenario to use:
"I have 3 work projects due this week, need to exercise 4 times, have 2 doctor appointments on Tuesday and Thursday afternoon, and want to learn Python basics. I work 9-5 Mon-Fri and have evenings/weekends free."

Pro Tips:
- Use XML tags or markdown for structure
- Be explicit about priorities
- Request specific time blocks
- Ask for contingency planning

This is a real-world skill - many professionals use prompts like this daily!''',
                'example_prompt': '''Act as my Personal Productivity Assistant with expertise in time management and goal achievement.

CONTEXT:
- I have 3 work projects due this week (Project A - high priority, Project B - medium, Project C - low)
- Need to exercise 4 times (30 min sessions)
- Doctor appointments: Tuesday 2-3pm, Thursday 3-4pm
- Want to study Python basics (4 hours total this week)
- Available: Mon-Fri 9am-5pm for work, evenings 6-10pm, weekends 8am-8pm

YOUR TASK:
Create a detailed weekly schedule that:

1. OVERVIEW: Start with a week-at-a-glance summary showing main focus each day

2. DAILY BREAKDOWN: For each day provide:
   - Morning priorities (top 3 things)
   - Time-blocked schedule (be specific with hours)
   - Evening tasks/activities
   
3. PROJECT ALLOCATION:
   - Dedicate focused blocks for each work project
   - Ensure Project A gets priority time slots
   
4. BALANCE:
   - Schedule exercise sessions at optimal times
   - Include Python learning in manageable chunks
   - Build in buffer time for unexpected issues

5. FORMAT:
Use this structure:
📅 [DAY]
🌅 Morning Focus: [3 priorities]
⏰ Schedule:
  9:00-11:00: [Activity]
  11:00-12:00: [Activity]
  ... etc
🌙 Evening: [Tasks]

Provide realistic, actionable guidance that I can follow immediately.''',
            },
        ]
        
        for challenge_data in chat_challenges:
            challenge, created = Challenge.objects.get_or_create(
                module=chat_module,
                title=challenge_data['title'],
                defaults=challenge_data
            )
            if created:
                self.stdout.write(f'Created challenge: {challenge.title}')
        
        # Set up challenge prerequisites (each requires previous one in order)
        chat_challenges_ordered = Challenge.objects.filter(module=chat_module).order_by('order')
        for i, challenge in enumerate(chat_challenges_ordered):
            if i > 0:
                challenge.prerequisite_challenge = chat_challenges_ordered[i-1]
                challenge.save()
                self.stdout.write(f'Set prerequisite for {challenge.title}')
        
        # Create Challenges for Build AI-Powered Tools module
        builder_module = Module.objects.get(title='Build AI-Powered Tools')
        
        builder_challenges = [
            {
                'title': 'Project 1: Smart Task Manager',
                'description': 'Build a task management system that uses AI to prioritize and organize tasks',
                'difficulty': 'beginner',
                'order': 1,
                'points': 30,
                'instructions': '''Welcome to your first AI-powered project!

You'll build a SMART TASK MANAGER that:
- Takes a list of tasks from the user
- Uses AI to analyze and prioritize them
- Suggests optimal scheduling
- Categorizes tasks automatically

YOUR TASK:
Write a prompt that instructs Claude to:
1. Accept a list of tasks (can be simple text)
2. Analyze each task for urgency and importance
3. Prioritize them using the Eisenhower Matrix (Urgent/Important)
4. Suggest when to do each task
5. Return results in a clear, organized format

BONUS: Ask AI to explain WHY it prioritized tasks that way.

Think about: What information does AI need? How should the output be structured?''',
                'example_prompt': '''I have these tasks to complete:
- Finish project report
- Reply to client emails
- Gym workout
- Update LinkedIn profile
- Fix bug in code
- Call mom
- Prepare presentation for Monday
- Buy groceries

Analyze these tasks and:
1. Categorize each as: Urgent & Important, Important but Not Urgent, Urgent but Not Important, or Neither
2. Suggest a priority order (1 being highest)
3. Recommend when to do each task (today, this week, when you have time)
4. Explain your reasoning for the top 3 priorities

Format the response in a clear table or list.''',
            },
            {
                'title': 'Project 2: Calendar Event Creator',
                'description': 'Create an AI agent that understands natural language and generates calendar events',
                'difficulty': 'intermediate',
                'order': 2,
                'points': 40,
                'instructions': '''Build an AI-powered calendar assistant!

THE CHALLENGE:
People say things like "Let's meet next Tuesday at 2pm for coffee" or "Schedule my dentist appointment for the 15th"

Your AI should:
1. Parse natural language time expressions
2. Extract event details (what, when, where, duration)
3. Create a structured calendar event
4. Handle edge cases (conflicts, unclear times)
5. Return data in a format ready to add to a calendar

YOUR TASK:
Write a prompt that makes Claude act as a calendar agent. It should:
- Understand various time formats
- Extract all event details
- Ask for clarification if needed
- Return structured data (JSON format preferred)
- Handle multiple events in one request

REAL-WORLD USE:
This is how calendar apps like Google Calendar understand your natural language input!''',
                'example_prompt': '''Act as a calendar event parser. Your job is to convert natural language into structured calendar events.

When I give you text, extract and return in this JSON format:
{
  "event_title": "string",
  "date": "YYYY-MM-DD",
  "start_time": "HH:MM",
  "end_time": "HH:MM",
  "duration_minutes": number,
  "location": "string or null",
  "notes": "string",
  "needs_clarification": boolean,
  "questions": ["list of questions if unclear"]
}

Handle edge cases:
- If time is unclear, ask for clarification
- If duration isn't specified, suggest reasonable defaults
- Today's date is 2024-12-09 (Monday)

Parse this request:
"Schedule lunch with Sarah next Wednesday at noon, probably at that Italian place downtown. Should take about an hour."''',
            },
            {
                'title': 'Project 3: Email Response Agent',
                'description': 'Build an AI agent that reads emails and drafts appropriate responses',
                'difficulty': 'intermediate',
                'order': 3,
                'points': 40,
                'instructions': '''Create an intelligent email response system!

THE SCENARIO:
You receive dozens of emails daily. An AI agent should:
1. Read and understand the email content
2. Determine the appropriate tone (formal/casual)
3. Identify what response is needed
4. Draft a suitable reply
5. Flag emails that need human review

YOUR TASK:
Design a prompt that makes Claude act as an email assistant. It should:
- Analyze incoming email content
- Determine urgency and intent
- Draft an appropriate response
- Match the sender's tone
- Include all necessary information
- Flag sensitive topics for human review

CHALLENGE YOURSELF:
Handle different email types: customer inquiries, meeting requests, complaints, thank you notes.''',
                'example_prompt': '''Act as an intelligent email response assistant.

For each email I provide:
1. Analyze the tone, intent, and urgency
2. Draft an appropriate response matching the sender's formality level
3. Include all necessary information
4. Flag if human review is needed (sensitive topics, complaints, negotiations)
5. Suggest subject line if replying to a thread

Format response as:
---
ANALYSIS:
- Intent: [what they want]
- Tone: [formal/casual]
- Urgency: [high/medium/low]
- Needs human review: [yes/no, why]

DRAFT RESPONSE:
[your drafted email]

SUBJECT LINE: [suggestion]
---

Here's the email to respond to:
"Hi there, I ordered item #12345 last week but it still hasn't arrived. The tracking hasn't updated in 3 days. This was supposed to be a birthday gift for tomorrow. Can you help? Thanks, frustrated customer."''',
            },
            {
                'title': 'Project 4: Meeting Notes Agent',
                'description': 'Build an AI that takes raw meeting transcripts and creates actionable summaries',
                'difficulty': 'advanced',
                'order': 4,
                'points': 50,
                'instructions': '''Create a meeting intelligence system!

THE PROBLEM:
Meetings generate lots of discussion but unclear action items. Your AI agent should:
1. Process meeting transcripts or notes
2. Identify key decisions made
3. Extract action items with owners
4. Detect follow-up questions
5. Create a professional summary
6. Identify topics for next meeting

YOUR TASK:
Build a prompt that makes Claude an expert meeting analyzer. It should:
- Parse messy, conversational text
- Identify WHO is responsible for WHAT by WHEN
- Categorize discussion topics
- Highlight unresolved issues
- Create a shareable summary document
- Suggest agenda items for next meeting

ADVANCED:
Handle interruptions, tangents, and unclear assignments.''',
                'example_prompt': '''Act as a meeting intelligence agent. Transform meeting transcripts into actionable summaries.

TRANSCRIPT:
[Multiple people talking]
John: "So about the website redesign, are we going with the blue theme?"
Sarah: "I think so, but we need to check with marketing first. Can someone do that?"
Mike: "I'll ask them by Friday. Oh and we still need to finalize the budget."
Sarah: "Right, I forgot about that. John, can you pull those numbers?"
John: "Sure, when do you need it?"
Sarah: "Before next week's meeting. Also, did anyone follow up on the vendor proposal?"
Mike: "Not yet, I've been swamped. Maybe Sarah can?"
Sarah: "OK I'll do it. We should probably schedule a follow-up for next Wednesday."

CREATE OUTPUT WITH:
1. MEETING SUMMARY (2-3 sentences)
2. DECISIONS MADE (list with context)
3. ACTION ITEMS (format: [OWNER] - [TASK] - [DEADLINE])
4. OPEN QUESTIONS (unresolved items)
5. FOLLOW-UP NEEDED (what to discuss next time)
6. PARTICIPANTS (identified from transcript)

Make it ready to share with the team immediately.''',
            },
            {
                'title': 'Project 5: Multi-Agent Workflow',
                'description': 'Design a system where multiple AI agents work together',
                'difficulty': 'advanced',
                'order': 5,
                'points': 60,
                'instructions': '''Build a multi-agent AI system! 🤯

THE CONCEPT:
Instead of one AI doing everything, create specialized agents that work together:
- Agent 1: Understands user request
- Agent 2: Plans the approach
- Agent 3: Executes the task
- Agent 4: Reviews and improves the output

YOUR TASK:
Design a prompt system where you simulate multiple AI agents collaborating. 

EXAMPLE USE CASE:
User wants to plan a birthday party. The agents should:
1. ANALYST AGENT: Understand requirements (budget, guests, preferences)
2. PLANNER AGENT: Create a detailed plan (venue, food, activities, timeline)
3. RESEARCHER AGENT: Find specific options (restaurants, venues, entertainment)
4. COORDINATOR AGENT: Organize everything into a final actionable plan

CHALLENGE:
Write ONE comprehensive prompt that simulates this multi-agent workflow. Show how each "agent" builds on the previous one's work.

This teaches you how modern AI systems are architected!''',
                'example_prompt': '''Simulate a multi-agent AI system for event planning. You'll play 4 specialized agents:

👤 AGENT 1 - ANALYST: Understand and structure the request
📋 AGENT 2 - PLANNER: Create strategic plan
🔍 AGENT 3 - RESEARCHER: Find specific options
✅ AGENT 4 - COORDINATOR: Finalize actionable plan

USER REQUEST:
"I want to plan a surprise 30th birthday party for my friend Sarah. She loves Italian food and board games. Budget is $500. About 15 people. Sometime in the next 3 weeks on a weekend evening."

PROCESS:
For each agent, show:
- What information they extract/create
- Their reasoning
- Their output to the next agent

AGENT 1 - ANALYST:
[Analyze the request, identify key requirements, note any missing info]

AGENT 2 - PLANNER:
[Create party structure: venue type, food approach, activities, timeline, budget breakdown]

AGENT 3 - RESEARCHER:
[Suggest specific options for venue, catering, games, decorations within budget]

AGENT 4 - COORDINATOR:
[Final checklist, timeline, assignments, contingency plans]

Show how agents collaborate and build on each other's work!''',
            },
        ]
        
        for challenge_data in builder_challenges:
            challenge, created = Challenge.objects.get_or_create(
                module=builder_module,
                title=challenge_data['title'],
                defaults=challenge_data
            )
            if created:
                self.stdout.write(f'Created challenge: {challenge.title}')
        
        # Create Challenges for Code with AI Assistant module
        coding_module = Module.objects.get(title='Code with AI Assistant')
        
        coding_challenges = [
            {
                'title': 'Lesson 1: Your First Python Program',
                'description': 'Learn Python basics with AI as your coding buddy',
                'difficulty': 'beginner',
                'order': 1,
                'points': 20,
                'instructions': '''Welcome to coding with AI! 🎉

YOU DON'T NEED TO KNOW ANYTHING ABOUT CODING!

THE CHALLENGE:
Ask AI to help you write your very first Python program: a simple calculator that adds two numbers.

WHAT TO DO:
1. Ask AI to explain what a Python program is (in simple words)
2. Ask AI to write a calculator program that:
   - Asks the user for two numbers
   - Adds them together
   - Shows the result
3. Ask AI to explain each line of code like you're 10 years old

LEARNING GOALS:
- Understand that AI can write code for you
- Learn how to ask AI to explain code
- See how programs take input and give output

Your prompt should ask for both THE CODE and THE EXPLANATION.

Remember: There's no shame in asking "dumb" questions to AI!''',
                'example_prompt': '''I'm a complete beginner who has never coded before. Help me create my first Python program!

I want to make a simple calculator that adds two numbers.

Please:
1. Write the complete Python code for this calculator
2. Add comments explaining each line
3. Explain in simple terms (like I'm 10 years old) what each part does
4. Tell me how to run this program
5. Show me what it will look like when I run it

Make it super simple and beginner-friendly!''',
            },
            {
                'title': 'Lesson 2: Build a Number Guessing Game',
                'description': 'Create an interactive game with AI guidance',
                'difficulty': 'beginner',
                'order': 2,
                'points': 25,
                'instructions': '''Let's make your first real game! 🎮

THE PROJECT:
Build a number guessing game where:
- Computer thinks of a random number (1-100)
- Player tries to guess it
- Computer says "too high" or "too low"
- Player wins when they guess correctly

YOUR TASK:
Ask AI to help you build this game step by step. Your prompt should request:

1. The complete working code
2. Explanation of new concepts (random numbers, loops, if statements)
3. How to make the game more fun (add guesses counter, difficulty levels)
4. Help you understand ANY part you find confusing

PRO TIP:
If you don't understand something AI wrote, just ask "Can you explain [specific part] more simply?"

LEARNING GOALS:
- Learn about loops (doing things multiple times)
- Learn about conditionals (if/else)
- Understand random numbers
- Build something fun!''',
                'example_prompt': '''Help me build a number guessing game in Python! I'm a beginner.

THE GAME:
- Computer picks a random number between 1-100
- I guess numbers
- Computer tells me if I'm too high or too low
- I keep guessing until I get it right
- Game tells me how many guesses I took

WHAT I NEED:
1. Write the complete Python code with helpful comments
2. Explain these concepts in simple terms:
   - What is a "loop" and why do we need it?
   - What does "random" mean in programming?
   - How does the computer compare my guess?
3. Show me exactly what the game will look like when playing
4. Add a feature to count how many guesses I make
5. Explain how I can make the game harder or easier

Write it so even my grandma could understand!''',
            },
            {
                'title': 'Lesson 3: Create a To-Do List App',
                'description': 'Build a useful app that manages tasks',
                'difficulty': 'intermediate',
                'order': 3,
                'points': 30,
                'instructions': '''Build something USEFUL! 📝

THE PROJECT:
Create a to-do list program that can:
- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Save tasks so they don't disappear when you close the program

YOUR TASK:
This is more complex! You'll need to ask AI for help with:
- Storing multiple items (lists)
- Saving data to a file
- Creating a menu system
- Handling user choices

APPROACH:
1. Start by asking AI for a simple version (just add and view)
2. Then ask how to add more features one at a time
3. If you get stuck, show AI the code and ask what's wrong

LEARNING GOALS:
- Work with lists (storing multiple things)
- Save data to files (persistence)
- Create interactive menus
- Debug problems with AI's help

This teaches you how professional developers work: building features incrementally!''',
                'example_prompt': '''I want to build a to-do list app in Python. I'm still learning, so I need help!

FEATURES I WANT:
1. Add tasks to my list
2. View all my tasks
3. Mark tasks as done (maybe with a ✓)
4. Delete tasks I don't need
5. Save my tasks so they're there next time I run the program

HELP ME WITH:
1. Write the code with clear comments explaining everything
2. Explain how to store multiple tasks (I heard about "lists"?)
3. Show me how to save data to a file (so tasks don't disappear)
4. Create a simple menu so users can choose what to do
5. Explain any new concepts in simple terms

Start with a basic version (add and view), then we can add more features.

Also, if something goes wrong, how do I use you to help fix it?''',
            },
            {
                'title': 'Lesson 4: Build a Simple Chatbot',
                'description': 'Create a chatbot that responds to different messages',
                'difficulty': 'intermediate',
                'order': 4,
                'points': 35,
                'instructions': '''Build your own chatbot! 🤖

THE PROJECT:
Create a simple chatbot that:
- Greets users by name
- Responds to common questions
- Tells jokes
- Gives random advice
- Has personality!

YOUR TASK:
Ask AI to help you build an interactive chatbot. Learn about:
- Pattern matching (recognizing what users say)
- Dictionaries (storing question/answer pairs)
- Random responses (so it's not boring)
- Making it feel conversational

MAKE IT FUN:
Give your chatbot a personality! Is it funny? Sarcastic? Wise? Friendly?

LEARNING GOALS:
- Work with dictionaries (key-value pairs)
- String operations (analyzing text)
- Creating engaging user experiences
- Adding personality to your programs

BONUS CHALLENGE:
Make it remember things the user tells it!''',
                'example_prompt': '''Help me create a simple chatbot in Python! I want to learn how chatbots work.

MY CHATBOT SHOULD:
1. Ask the user's name and remember it
2. Respond to greetings ("hi", "hello", "hey")
3. Answer simple questions:
   - "how are you?" → funny/friendly response
   - "tell me a joke" → random joke from a list
   - "give me advice" → random advice
4. Recognize when it doesn't understand something
5. Have a fun personality (maybe sarcastic or wise?)

TEACH ME:
1. Write the complete code with explanations
2. Show me how to store different responses (I think these are "dictionaries"?)
3. How to make responses random so it's not boring
4. How to find keywords in what users type
5. How to make it remember the user's name throughout the chat

Make it beginner-friendly but also teach me cool tricks!

BONUS: How could I make it remember things users tell it during the conversation?''',
            },
            {
                'title': 'Lesson 5: Create a Quiz Game',
                'description': 'Build an interactive quiz with scoring',
                'difficulty': 'intermediate',
                'order': 5,
                'points': 35,
                'instructions': '''Build an interactive quiz game! 🧠

THE PROJECT:
Create a quiz game that:
- Asks multiple-choice questions
- Keeps track of the score
- Shows correct answers if player is wrong
- Gives a final grade at the end
- Can add difficulty levels

YOUR TASK:
Work with AI to build this game. You'll learn:
- Storing structured data (questions + answers)
- Keeping score
- Giving feedback
- Making it replayable

CHALLENGE YOURSELF:
- Add different difficulty levels
- Include a timer
- Save high scores
- Add question categories

LEARNING GOALS:
- Data structures (organizing complex information)
- Score tracking
- User feedback
- Making programs replayable

This is how educational apps are built!''',
                'example_prompt': '''Help me build a quiz game in Python! I want to understand how quiz apps work.

THE QUIZ SHOULD:
1. Ask 5 multiple choice questions
2. Tell the user if they're right or wrong after each question
3. If wrong, show the correct answer
4. Keep track of the score
5. Show final results with a message (like "Great job!" or "Keep practicing!")

QUESTIONS (you can write them or let me add my own):
- General knowledge
- Simple math
- Fun trivia

TEACH ME:
1. Write the complete code with clear explanations
2. How to store questions and answers together (data structures)
3. How to check if the answer is correct
4. How to keep track of points
5. How to make it easy to add more questions later

BONUS FEATURES:
- Add difficulty levels (easy/medium/hard)
- Add a timer for each question
- Save the high score
- Let player play again

Explain everything so I truly understand how it works!''',
            },
            {
                'title': 'Lesson 6: Build a Password Generator',
                'description': 'Create a tool that generates secure passwords',
                'difficulty': 'advanced',
                'order': 6,
                'points': 40,
                'instructions': '''Build a practical security tool! 🔒

THE PROJECT:
Create a password generator that:
- Makes random strong passwords
- Lets users choose length
- Includes letters, numbers, symbols
- Checks password strength
- Can generate multiple passwords

YOUR TASK:
Ask AI to help you understand:
- Random selection from different character types
- Password security principles
- User input validation
- Making tools user-friendly

REAL-WORLD APPLICATION:
This is a tool you'll actually use! Professional developers build similar utilities.

LEARNING GOALS:
- Working with random selections
- String manipulation
- Input validation
- Creating reusable tools
- Understanding security basics

CHALLENGE:
Add a password strength checker that rates passwords as weak/medium/strong!''',
                'example_prompt': '''Help me build a password generator in Python! I want to create strong passwords.

FEATURES:
1. Generate random passwords with:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Special characters (!@#$%^&*)
2. Let user choose password length
3. Generate multiple passwords at once
4. Check if a password is strong/weak
5. Copy password to clipboard (if possible)

WHAT I WANT TO LEARN:
1. Write clean, commented code
2. How to randomly select characters
3. How to make passwords secure (what makes a password strong?)
4. How to let users customize the password
5. How to check password strength

ADVANCED FEATURES:
- Avoid confusing characters (like O and 0, l and 1)
- Remember password requirements (some sites need symbols, etc.)
- Generate pronounceable passwords vs totally random

Explain security concepts too - why are strong passwords important?''',
            },
            {
                'title': 'Final Project: Build Your Own App!',
                'description': 'Design and build any program you can imagine with AI as your co-developer',
                'difficulty': 'advanced',
                'order': 7,
                'points': 50,
                'instructions': '''NOW YOU'RE A DEVELOPER! 🎓

THE ULTIMATE CHALLENGE:
Come up with YOUR OWN idea for a Python program and build it with AI's help!

IDEAS TO INSPIRE YOU:
- Budget tracker
- Habit tracker
- Simple game (rock-paper-scissors, tic-tac-toe)
- Recipe organizer
- Workout logger
- Study timer with breaks
- Random quote generator
- Simple drawing program
- Music playlist manager
- Weather reminder

YOUR TASK:
1. Describe your app idea to AI
2. Ask AI to help you break it down into steps
3. Build it feature by feature with AI's guidance
4. Test it and ask AI to help fix bugs
5. Add cool extra features

LEARNING GOALS:
- Project planning (breaking big ideas into small steps)
- Problem solving (when things don't work)
- Feature development (adding new capabilities)
- Testing and debugging (fixing problems)
- Creative thinking (making it your own)

THIS IS HOW REAL DEVELOPERS WORK WITH AI!

Show that you've learned how to use AI as a powerful coding partner.''',
                'example_prompt': '''I want to build my own Python app! Help me bring my idea to life.

MY IDEA:
[Describe your app idea here - what does it do? Who is it for? What problem does it solve?]

HELP ME:
1. Is this idea good for a beginner project? (If too complex, help me simplify)
2. Break down my idea into smaller features I can build one at a time
3. What will I need to learn to build this?
4. Create a step-by-step plan (like a roadmap)
5. Help me build it piece by piece

THEN:
- Write the code for each feature with explanations
- Help me test it and fix any bugs
- Suggest improvements or cool features I could add
- Teach me best practices (how professional developers do it)

I want to understand EVERYTHING I'm building!

[Start with the simplest version first, then we'll add features]''',
            },
        ]
        
        for challenge_data in coding_challenges:
            challenge, created = Challenge.objects.get_or_create(
                module=coding_module,
                title=challenge_data['title'],
                defaults=challenge_data
            )
            if created:
                self.stdout.write(f'Created challenge: {challenge.title}')
        
        # Create Achievements
        achievements_data = [
            {
                'name': 'First Steps',
                'description': 'Complete your first challenge',
                'achievement_type': 'first_challenge',
                'icon': '🎯',
                'points_required': 0,
            },
            {
                'name': 'Getting Started',
                'description': 'Complete 5 challenges',
                'achievement_type': 'explorer',
                'icon': '🚀',
                'points_required': 50,
            },
            {
                'name': 'Rising Star',
                'description': 'Complete 25 challenges',
                'achievement_type': 'explorer',
                'icon': '⭐',
                'points_required': 250,
            },
            {
                'name': 'Speed Demon',
                'description': 'Complete a challenge in under 2 minutes',
                'achievement_type': 'speed_demon',
                'icon': '⚡',
                'points_required': 0,
            },
            {
                'name': 'Perfectionist',
                'description': 'Score 95+ on any challenge',
                'achievement_type': 'perfectionist',
                'icon': '💎',
                'points_required': 0,
            },
        ]
        
        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                name=achievement_data['name'],
                defaults=achievement_data
            )
            if created:
                self.stdout.write(f'Created achievement: {achievement.name}')
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))
