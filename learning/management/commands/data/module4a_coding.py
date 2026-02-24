"""
Module 4A: Capstone — Coding with AI (Track A)
Challenges 1-15: Learning to code using AI as your personal tutor and pair programmer
"""

MODULE4A_CODING_CHALLENGES = [
    {
        'title': 'Question 1: Why Learn to Code with AI?',
        'description': 'Explore how AI makes programming accessible and why coding + AI is a career superpower',
        'difficulty': 'beginner',
        'order': 1,
        'points': 20,
        'instructions': '''Welcome to Track A — Coding with AI. You're about to learn one of the most valuable skills in the modern world, with the most powerful learning tool ever created.

**What You'll Learn:**
- Why coding combined with AI knowledge is a unique career advantage
- What AI can do for someone learning to code (and what it can't)
- What "learn to code with AI" actually looks like in practice

**Why This Combination is Powerful:**
A few years ago, learning to code meant memorising syntax, reading dense documentation, and being stuck for hours on errors. Today, with AI:
- You can write code by describing what you want in English
- AI explains every line and concept as you learn
- When you're stuck, AI diagnoses the problem instantly
- You can build real things from day one — not just toy exercises

**What You'll Build in This Track:**
By the end of these 15 lessons, you'll have built:
- A personalised profile programme
- A quiz game
- A daily schedule generator
- A contact book application
- A budget tracker
- A mini data dashboard
- Your own AI-powered application

**The AI Coding Mindset:**
You don't need to memorise everything — you need to understand concepts, communicate clearly, and review code intelligently. These are skills you already have from Modules 1-3.

**Your Challenge:**
Explore what's possible. Write, run (mentally), and understand your first piece of code — guided by AI every step of the way.''',
        'example_prompt': '''I'm starting to learn programming using AI as my guide. I want to explore what's possible and write my first piece of code.

---

**PART 1 — SHOW ME WHAT'S POSSIBLE**

Without me writing anything yet, show me 5 real things I could build in Python within the next 3 months — starting from zero experience. For each:
- What the programme does (in plain English)
- What it would look like running (describe the user experience)
- What skills it would teach me
- Why it would be genuinely useful in real life

Make these genuinely exciting, not textbook exercises.

---

**PART 2 — MY FIRST PROGRAMME**

Let's write something real right now. Write a Python programme that:
- Asks me my name
- Asks me my age
- Asks me what I do for work
- Asks me one thing I want to learn this year
- Then displays a personalised welcome message using all my answers

For example, if I enter: Name=Alex, Age=28, Work=Marketing Manager, Want to learn=Python
The programme should output something like:
"Welcome, Alex! You're 28 years old and work as a Marketing Manager. This year, you're going to learn Python — and you've already started! 🎉"

**Do two things:**
1. Write the complete programme
2. Explain every single line — what it does, why it's written that way, and what would happen if I changed it

I should understand this code well enough to modify it myself.

---

**PART 3 — MODIFY IT WITH ME**

Now I want to change the programme. I'll describe what I want in English, and you'll help me code it:

**Change 1:** "After the welcome message, ask me to rate my current coding confidence from 1-10, then show a different encouraging message based on whether I rate myself 1-4, 5-7, or 8-10."

**Change 2:** "Save all my answers to a text file called 'my_profile.txt' so they're remembered."

For each change: write the new code, highlight exactly what changed, and explain why those changes work.

---

**PART 4 — THE CODING MINDSET**

Based on what we've done together in this lesson:
1. What's the most important concept to understand about Python before going further?
2. What should I NOT try to memorise at this stage?
3. How should I use AI as I learn to code — what's the most effective way to use it?
4. What's my goal by the end of these 15 lessons?

Give me honest, practical guidance — not cheerleading.''',
    },
    {
        'title': 'Question 2: Your Coding Environment',
        'description': 'Set up Python and write your first working programmes with AI guidance',
        'difficulty': 'beginner',
        'order': 2,
        'points': 20,
        'instructions': '''Before we go further, let's make sure you have the right setup and understand the environment where your code runs.

**What You'll Learn:**
- How to set up Python on your computer with AI guidance
- The difference between different ways to run Python code
- How to read error messages (they're helpful, not scary!)

**Your Options for Running Python:**

**Option 1 — Online (No Setup Required):**
- Google Colab: Free, runs in your browser, great for beginners
- Replit: Online editor with AI built in
- Python.org online: Quick testing

**Option 2 — Local Installation (More Control):**
- Python + VS Code: The professional setup
- Python + IDLE: Simpler, built-in when you install Python
- Cursor: AI-first editor

**Recommended for Beginners:** Start with Google Colab or Replit — no setup, focus on learning.

**Understanding Error Messages:**
Every programmer sees error messages. The secret: read them carefully, they tell you exactly what went wrong.

Common Python errors:
- `SyntaxError` — you made a typo or missed something
- `NameError` — you used a variable that doesn't exist yet
- `TypeError` — you tried to do something invalid (like add a number to a word)
- `IndentationError` — Python is very strict about spacing (4 spaces = 1 indent)

**Your Challenge:**
Set up your environment and write 3 progressively more complex programmes. For each one, also intentionally introduce an error and practice reading the error message.

The goal: by the end of this lesson, errors should feel informative, not frustrating.''',
        'example_prompt': '''Help me set up my coding environment and write 3 progressively complex programmes. I want to feel comfortable with the basics before going further.

---

**PART 1 — ENVIRONMENT SETUP**

I'm a complete beginner. Walk me through setting up my coding environment:

Option A: I want to start online with no setup
→ Step-by-step instructions for setting up Google Colab (with screenshots described in words)

Option B: I want to install Python locally on Windows
→ Step-by-step instructions from python.org download to running first programme

For the option you recommend for absolute beginners, give me the complete setup guide. Then: the first command/code I should run to test that everything is working.

---

**PART 2 — THREE PROGRAMMES (INCREASING COMPLEXITY)**

**Programme 1: Hello, World (and more)**
Write and explain:
```python
print("Hello, World!")
name = input("What's your name? ")
print("Hello, " + name + "!")
```

Explain: What is print()? What is input()? What are the quotation marks for? What does the + do here?

**Programme 2: Simple Calculator**
Write a programme that:
- Asks the user for two numbers
- Asks them whether they want to add, subtract, multiply, or divide
- Shows the result

Write this programme, explain every line, then tell me: what would happen if the user types "hello" instead of a number? (Introduce the concept of type errors)

**Programme 3: Temperature Converter**
Write a programme that:
- Asks if the user wants to convert Celsius to Fahrenheit, or Fahrenheit to Celsius
- Takes their temperature input
- Shows the converted result with a clear explanation

Formula: F = (C × 9/5) + 32 | C = (F - 32) × 5/9

Explain the if/else logic in this programme clearly.

---

**PART 3 — LEARNING FROM ERRORS**

For each of these broken programmes, diagnose the error and fix it:

**Broken Programme 1:**
```
print("My name is " + name)
name = "Alex"
```
What error will this cause? Why? How do you fix it?

**Broken Programme 2:**
```
age = input("How old are you? ")
next_year = age + 1
print("Next year you'll be " + next_year)
```
What error will this cause? Why? (Hint: input() always gives you text, not numbers) How do you fix it?

**Broken Programme 3:**
```
score = 75
if score >= 60:
print("You passed!")
```
What error? Why? How do you fix it?

---

**PART 4 — THE DEBUGGING MINDSET**

Teach me how to approach errors systematically:
1. When I see a Python error, what's the first thing to look at?
2. What does "line X" in an error message mean?
3. The 3-step debugging approach I should use every time
4. When it's appropriate to paste an error into AI vs try to figure it out first''',
    },
    {
        'title': 'Question 3: Variables & Data Types',
        'description': 'Master the building blocks of programming — storing and working with information',
        'difficulty': 'beginner',
        'order': 3,
        'points': 20,
        'instructions': '''Everything in programming is about information. Variables are how you store it. Data types are what kind of information it is.

**What You'll Learn:**
- What variables are and how to use them
- The main Python data types (strings, integers, floats, booleans)
- How to work with and manipulate different types of data

**Python's Main Data Types:**

| Type | What It Is | Example |
|------|-----------|---------|
| `str` (String) | Text | `"Hello"`, `"Alex"` |
| `int` (Integer) | Whole numbers | `42`, `-7`, `0` |
| `float` | Decimal numbers | `3.14`, `99.99` |
| `bool` (Boolean) | True or False | `True`, `False` |
| `list` | Multiple values | `["Apple", "Banana", "Cherry"]` |
| `dict` (Dictionary) | Key-value pairs | `{"name": "Alex", "age": 28}` |

**Variables:**
Think of a variable as a named box. You put something in the box and give it a label so you can use it later.

```python
name = "Alex"        # String variable
age = 28             # Integer variable
score = 9.5          # Float variable
is_student = True    # Boolean variable
```

**Your Challenge:**
Build a "Personal Profile Programme" — a programme that stores information about you using all the main data types, then displays it in different formatted ways.

This teaches you how variables hold information and how different data types behave differently.''',
        'example_prompt': '''Build a Personal Profile Programme that demonstrates all the main Python data types. Walk me through every concept as we build it.

---

**PART 1 — STORING MY PROFILE**

Write a programme that stores all this information using the correct data type for each:

- My name: "Jordan Clarke"
- My age: 29
- My height: 1.72 (metres)
- Whether I'm employed: True
- My job title: "Marketing Manager"
- My salary: 38500.00
- My hobbies: ["Running", "Photography", "Cooking"]
- My profile details (as a dictionary): name, age, city, and job

**For EVERY variable:**
- Write the code to create it
- Explain which data type you chose and WHY that type (not int for height, for example)
- Show how to check the data type using Python's type() function

---

**PART 2 — DISPLAYING THE PROFILE**

Now write code to display my profile in 3 different formats:

**Format 1: Simple print statements**
Print each piece of information on its own line with a clear label.

**Format 2: An f-string sentence**
Use Python f-strings to create a paragraph like:
"My name is Jordan Clarke. I'm 29 years old and I work as a Marketing Manager. I'm 1.72m tall."

Explain what an f-string is and how it works. Why is this better than using + to join strings?

**Format 3: Dictionary display**
Show how to access individual items from my profile dictionary.
Then show how to loop through and print every key and value.

---

**PART 3 — MANIPULATING DATA TYPES**

Show me how to work with each type:

**Strings:**
- Make my name uppercase
- Count how many letters are in my name
- Check if my job title contains the word "Manager"
- Replace "Marketing" with "Senior Marketing" in my job title

**Numbers:**
- Calculate how many months old I am (age × 12)
- Calculate my monthly salary from annual (salary / 12)
- Round the monthly salary to 2 decimal places

**Lists:**
- Add a new hobby: "Reading"
- Remove "Running" from my hobbies list
- Check if "Photography" is in my list
- Count how many hobbies I have
- Print only the first 2 hobbies

**Booleans:**
- Write an if statement that prints "You're employed!" if is_employed is True
- Write an if statement that prints "Student discount applies!" if age is under 26

---

**PART 4 — BUILD THE INTERACTIVE VERSION**

Now make this interactive — ask the user to input their own profile details, store them in variables with the right types, then display their completed profile.

Challenge: input() always returns a string. How do you convert it to the right type? Show me the code for this and explain why it matters.''',
    },
    {
        'title': 'Question 4: Making Decisions in Code',
        'description': 'Learn how code makes choices using if/else logic and build a quiz game',
        'difficulty': 'beginner',
        'order': 4,
        'points': 25,
        'instructions': '''Real programmes make decisions. "If the score is over 80, say well done. If it's under 50, suggest studying more." This is if/else logic — the foundation of all interactive software.

**What You'll Learn:**
- How if, elif, and else work
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)
- How to build interactive programmes that respond differently to different inputs

**If/Else in Plain English:**
```python
if condition:
    do this
elif other_condition:
    do this instead
else:
    do this if nothing else matched
```

**Comparison Operators:**
- `==` means "is equal to" (note: = assigns, == compares!)
- `!=` means "is not equal to"
- `>` means "greater than"
- `<` means "less than"
- `>=` means "greater than or equal to"
- `<=` means "less than or equal to"

**Logical Operators:**
- `and` — both conditions must be true
- `or` — at least one condition must be true
- `not` — reverses a boolean

**Your Challenge:**
Build a **Quiz Game** that:
- Asks 5 questions
- Accepts user answers
- Tells them if each answer is right or wrong immediately
- Keeps a running score
- At the end, gives different feedback based on their score

Use if/elif/else throughout. Make it a real, playable game.''',
        'example_prompt': '''Build a complete Quiz Game that demonstrates if/else logic throughout. Walk me through every decision point in the code.

---

**THE QUIZ GAME SPEC:**

Build a 5-question quiz on a topic of your choice (make it interesting — not just maths).

Requirements:
- Print a welcome message and rules at the start
- Ask each question and wait for input
- Use if/else to check if the answer is right or wrong
- Print immediate feedback after each answer ("Correct! ✓" or "Wrong! The answer was...")
- Keep a score variable that increases for correct answers
- At the end, show the final score out of 5
- Give different messages based on score:
  - 5/5: "Perfect score! You're a genius!"
  - 3-4: "Great job! Well above average."
  - 2: "Not bad, but room for improvement."
  - 0-1: "Better luck next time — try again!"
- After the results, ask if they want to play again (Y/N)

---

**PART 1 — THE BASIC QUIZ**

Write the complete quiz programme for this UK history quiz:

Q1: In what year did World War II end? (Answer: 1945)
Q2: Who was the UK's first female Prime Minister? (Answer: Margaret Thatcher)
Q3: What is the capital of Scotland? (Answer: Edinburgh)
Q4: In what year did England win the FIFA World Cup? (Answer: 1966)
Q5: What is the UK's longest river? (Answer: River Severn)

Write the full code, then explain every if/else block — what decision is being made and why the code is structured that way.

---

**PART 2 — MAKING IT SMARTER**

The basic quiz is too strict — "margaret thatcher" and "Margaret Thatcher" should both be correct.

Modify the programme to:
1. Accept answers regardless of capitalisation (hint: .lower() method)
2. Accept common abbreviations or partial answers (Q3: accept "Edinburgh" or "edinburgh")
3. Handle completely empty answers without crashing

Show me the updated code and explain what changed.

---

**PART 3 — DIFFICULTY LEVELS**

Add a difficulty system at the start:
- Ask if they want Easy, Medium, or Hard mode
- Easy: Show a hint after a wrong answer
- Medium: No hints, but show the answer after wrong answer
- Hard: No hints, don't reveal the correct answer — just "Wrong!"

Show how nested if/else handles this. Explain what "nested" means.

---

**PART 4 — LOGICAL OPERATORS IN ACTION**

Show me examples of and, or, and not in the context of this quiz:

1. Write an if statement that gives a bonus message if they score 5/5 AND complete in under 60 seconds
2. Write a check that prints "Close!" if their answer contains either "severn" OR "river severn"
3. Use "not" to write a check: if the user has NOT played before, show the full instructions; if they have, show a shorter version

---

**PART 5 — THE COMPLETE POLISHED GAME**

Write the final, complete version of the quiz with all improvements included. This should be something I'd be genuinely happy to show someone as my first real programme.''',
    },
    {
        'title': 'Question 5: Loops & Repetition',
        'description': 'Automate repetitive tasks with for loops and while loops',
        'difficulty': 'beginner',
        'order': 5,
        'points': 25,
        'instructions': '''Computers excel at doing things over and over — perfectly, without complaining. Loops are how you make that happen.

**What You'll Learn:**
- `for` loops — repeat an action a set number of times
- `while` loops — repeat until a condition changes
- How to use `range()` to control repetition
- `break` and `continue` to control loop flow

**For Loop:**
```python
for i in range(5):
    print(f"This is repetition number {i+1}")
```
Does the indented code 5 times (for i = 0, 1, 2, 3, 4)

**For Loop over a list:**
```python
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"I love {fruit}!")
```

**While Loop:**
```python
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # IMPORTANT: must update the condition or loop runs forever!
```

**Your Challenge:**
Build a **Personalised Daily Schedule Generator** — a programme that:
- Asks the user how many tasks they need to schedule today
- Collects each task using a loop
- Asks for time and priority for each
- Displays the complete schedule sorted by time
- Loops to let them add more tasks or quit

This is a real tool someone could actually use.''',
        'example_prompt': '''Build a Personalised Daily Schedule Generator using loops. Explain every loop clearly — why I'm using for vs while, and what would break if I did it differently.

---

**THE PROGRAMME SPEC:**

Build a schedule generator that:

**Step 1 — Greeting and Setup:**
- Welcome the user
- Ask for their name
- Ask what day's schedule they're building

**Step 2 — Task Collection (using a while loop):**
- Keep asking "Would you like to add a task? (yes/no)"
- While they say yes: collect the task name, time (e.g., "09:30"), and priority (High/Medium/Low)
- Store each task in a list of dictionaries
- When they say no, move to displaying the schedule

**Step 3 — Schedule Display (using a for loop):**
- Loop through all the tasks
- Display them in a formatted, readable schedule
- Show task number, time, name, and priority
- Show the total number of tasks

**Step 4 — Summary Statistics:**
- Count how many High priority tasks there are
- Count how many Medium and Low
- Show the busiest time block (if 3+ tasks between 9am-12pm, flag it)

---

**PART 1 — BUILD THE CORE PROGRAMME**

Write the complete programme. For EVERY loop:
- State clearly: why a for loop or a while loop (not the other)?
- What would go wrong if you used the wrong type?
- Where could this loop run forever if we're not careful?

---

**PART 2 — LOOP CONTROL: BREAK AND CONTINUE**

Add these features to demonstrate break and continue:

**Using break:**
Add a maximum task limit of 10. If the user tries to add an 11th task, show a warning message and stop the input loop with break.

**Using continue:**
If the user accidentally enters an empty task name (just presses Enter), use continue to skip that iteration and ask again rather than saving a blank task.

Show the code for both and explain what break and continue actually do in a loop.

---

**PART 3 — NESTED LOOPS**

Now build a "Weekly Schedule" version — ask for tasks for each day of the week (Monday to Friday).

This requires a loop inside a loop (nested loops):
- Outer loop: for each day (Monday, Tuesday, ...)
- Inner loop: for each task on that day

Show me nested loops in action and explain:
- How Python knows which loop each line belongs to (indentation!)
- A common mistake beginners make with nested loops

---

**PART 4 — THE RANGE FUNCTION**

Show me 5 different ways to use range() and what each produces:
1. range(10)
2. range(1, 11)
3. range(0, 100, 10)
4. range(10, 0, -1)
5. range(len(my_tasks_list))

For each: what numbers does it produce? When would you use this variant?

---

**PART 5 — COMPLETE SCHEDULE WITH SORTING**

In the final version, sort the tasks by time before displaying them. Python's sort() function can do this.

Show me how to sort a list of dictionaries by a specific key — and explain what a "lambda function" is in simple terms (you need one for sorting dictionaries).''',
    },
    {
        'title': 'Question 6: Functions',
        'description': 'Write reusable code blocks and build a toolkit of practical functions',
        'difficulty': 'intermediate',
        'order': 6,
        'points': 30,
        'instructions': '''Functions are the backbone of good code. Instead of writing the same logic over and over, you write it once, name it, and call it whenever you need it.

**What You'll Learn:**
- How to define and call functions
- Parameters and return values
- Why well-named functions make code readable
- Building a reusable "toolkit" of functions

**Function Anatomy:**
```python
def function_name(parameter1, parameter2):
    """Docstring: what this function does"""
    # code goes here
    return result
```

**Key Concepts:**
- `def` — tells Python you're defining a function
- Parameters — inputs the function receives
- `return` — the output the function gives back
- Calling a function: `result = function_name(arg1, arg2)`

**Default Parameters:**
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alex")           # "Hello, Alex!"
greet("Alex", "Hi")     # "Hi, Alex!"
```

**Your Challenge:**
Build a "Utility Toolkit" — a collection of 6 genuinely useful functions you could actually use in real life. This teaches functions while creating something practical.

By the end, you should be able to call any function in your toolkit and get a useful result.''',
        'example_prompt': '''Build a Utility Toolkit of 6 genuinely useful Python functions. For each one, explain the design choices and demonstrate it working.

---

**FUNCTION 1: Tip Calculator**

Write a function that calculates the tip for a restaurant bill.

Requirements:
- Parameters: bill_amount, tip_percentage (default: 15), number_of_people (default: 1)
- Returns: a dictionary with total_bill, tip_amount, amount_per_person
- Handles edge cases: what if number_of_people is 0? (would cause division by zero)

Then write 3 different ways to call this function showing how default parameters work.

---

**FUNCTION 2: Word Counter**

Write a function that analyses a piece of text.

Requirements:
- Parameter: text (a string)
- Returns: a dictionary with word_count, character_count (no spaces), sentence_count, most_common_word
- Should work with any text input

Test it with: "The quick brown fox jumps over the lazy dog. The dog barked at the fox."

---

**FUNCTION 3: Password Generator**

Write a function that generates a random secure password.

Requirements:
- Parameters: length (default: 12), include_symbols (default: True)
- Returns: a randomly generated password string
- Must use Python's random and string modules (explain what these are)
- If include_symbols is False, only use letters and numbers

---

**FUNCTION 4: Temperature Converter Toolkit**

Write 3 small functions that convert between Celsius, Fahrenheit, and Kelvin:
- celsius_to_fahrenheit(celsius)
- fahrenheit_to_celsius(fahrenheit)
- celsius_to_kelvin(celsius)

Then write a 4th function: convert_temperature(value, from_unit, to_unit)
This master function calls the right sub-function based on the units given.

This demonstrates functions calling other functions.

---

**FUNCTION 5: Text Formatter**

Write a function that formats text for professional use.

Requirements:
- Parameters: text, format_type ("title", "sentence", "upper", "lower")
- Returns: the correctly formatted text
- title format: First Letter Of Each Word Capitalised
- sentence format: Only the first letter capitalised, rest lowercase
- Use if/elif/else to choose the right formatting

---

**FUNCTION 6: Simple Budget Checker**

Write a function that helps someone track a simple budget.

Requirements:
- Parameters: income, expenses (a list of amounts), savings_goal_percentage (default: 20)
- Returns: a dictionary with total_expenses, remaining_after_expenses, savings_target, is_meeting_savings_goal (True/False), surplus_or_deficit

---

**BRING IT TOGETHER:**

Write a main programme that calls all 6 functions in a demo:
- Create some test data
- Call each function with realistic inputs
- Print the results in a readable format

This shows me what a real Python file with multiple functions looks like.

---

**EXPLAIN:**
1. What's the difference between a parameter and an argument?
2. What happens if a function doesn't have a return statement?
3. Why should functions do ONE thing? Why is a 200-line function a problem?
4. What is a "docstring" and why write one for every function?''',
    },
    {
        'title': 'Question 7: Working with Data',
        'description': 'Master lists and dictionaries to organise, search, and manage information',
        'difficulty': 'intermediate',
        'order': 7,
        'points': 30,
        'instructions': '''Real programmes manage collections of data — lists of customers, dictionaries of settings, records of transactions. This lesson is about working with data structures.

**What You'll Learn:**
- Advanced list operations
- Dictionaries for structured data
- List comprehensions (a Pythonic power feature)
- Sorting and filtering data

**Lists in Depth:**
```python
students = ["Alice", "Bob", "Charlie", "Diana"]
students.append("Eve")     # Add to end
students.insert(0, "Adam") # Add at position
students.remove("Bob")     # Remove by value
students.sort()            # Sort alphabetically
students.reverse()         # Reverse the list
print(len(students))       # How many items
print(students[0])         # First item (index 0)
print(students[-1])        # Last item
print(students[1:3])       # Slice: items 1 and 2
```

**Dictionaries:**
```python
contact = {
    "name": "Alice",
    "email": "alice@example.com",
    "phone": "07700 900123",
    "age": 28
}
print(contact["name"])         # Access by key
contact["job"] = "Developer"   # Add new key
del contact["age"]             # Delete a key
print(contact.keys())          # All keys
print(contact.values())        # All values
```

**Your Challenge:**
Build a **Contact Book Application** — a programme that stores, searches, and manages a list of contacts using lists of dictionaries.

This is a real, useful programme that demonstrates everything about working with data.''',
        'example_prompt': '''Build a complete Contact Book Application that demonstrates working with lists and dictionaries. This should be a genuinely useful programme.

---

**THE CONTACT BOOK SPEC:**

The programme should:
1. Store contacts (each as a dictionary with: name, email, phone, notes)
2. Let the user: Add a contact, View all contacts, Search by name or email, Edit a contact, Delete a contact, Quit
3. Show a menu after each action
4. Handle errors gracefully (what if they search for someone who doesn't exist?)

---

**PART 1 — DATA STRUCTURE DESIGN**

Before we write the programme, design the data structure.

Show me:
1. What does one contact look like as a Python dictionary? (All fields, realistic example)
2. What does the contacts list look like with 3 contacts in it?
3. How would I access just Alice's email from a list of contacts?
4. How would I loop through all contacts and print just their names?

---

**PART 2 — CORE FUNCTIONS**

Write each core function separately with full explanation:

**add_contact(contacts, name, email, phone, notes=""):**
- Adds a new contact dictionary to the list
- Validates that name and email are not empty
- Checks if a contact with that email already exists (no duplicates)

**view_all_contacts(contacts):**
- Displays all contacts in a readable format
- Shows contact number, name, email, phone
- If no contacts: "No contacts found. Add one first!"

**search_contacts(contacts, query):**
- Searches by name OR email (case-insensitive)
- Returns a list of matching contacts
- Shows how many matches were found

**edit_contact(contacts, name):**
- Finds the contact by name
- Lets the user update any field
- Saves the changes

**delete_contact(contacts, name):**
- Finds and removes a contact
- Asks "Are you sure? (yes/no)" before deleting

---

**PART 3 — LIST COMPREHENSIONS**

Show me list comprehensions — Python's powerful shortcut for working with lists.

For the contacts list, use list comprehensions to:
1. Get a list of just all contact names
2. Get all contacts whose name starts with "A"
3. Get all contacts who have notes (notes field is not empty)
4. Get all email addresses in uppercase

For each: first show the "traditional" for loop version, then the list comprehension. Explain why list comprehensions are Pythonic and when to use (and not use) them.

---

**PART 4 — SORTING AND FILTERING**

Show me 3 different ways to sort the contact list:
1. Alphabetically by name (A-Z)
2. Alphabetically by name (Z-A)
3. By name length (shortest to longest)

Also show: how to filter contacts to only show those who have a phone number stored.

Use Python's sorted() function and lambda — explain both clearly.

---

**PART 5 — THE COMPLETE PROGRAMME**

Write the complete, working contact book with a menu interface.

The menu loop should look like:
```
--- Contact Book ---
1. Add contact
2. View all contacts
3. Search
4. Edit contact
5. Delete contact
6. Quit
Enter choice (1-6):
```

Make this a complete, usable programme I could actually run and use.''',
    },
    {
        'title': 'Question 8: Reading & Writing Files',
        'description': 'Make your programmes remember information by saving and loading data from files',
        'difficulty': 'intermediate',
        'order': 8,
        'points': 30,
        'instructions': '''Right now, all your programmes forget everything when they close. Files fix that.

**What You'll Learn:**
- How to read and write text files
- How to work with CSV files (spreadsheet data)
- How to save and load programme data so it persists
- Exception handling — what to do when files don't exist

**File Operations:**
```python
# Writing to a file
with open("my_file.txt", "w") as file:
    file.write("Hello, file!")

# Reading from a file
with open("my_file.txt", "r") as file:
    content = file.read()

# Appending to a file
with open("my_file.txt", "a") as file:
    file.write("\nNew line added!")
```

**File Modes:**
- `"r"` — read (file must exist)
- `"w"` — write (creates file, overwrites if exists)
- `"a"` — append (adds to end of existing file)

**CSV Files with Python:**
```python
import csv

# Write CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "email"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "email": "alice@example.com"})

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])
```

**Your Challenge:**
Upgrade your Contact Book from the previous lesson to save contacts to a CSV file — so they persist between sessions.''',
        'example_prompt': '''Upgrade the Contact Book to save and load data from a CSV file. Also build a separate Expense Tracker that reads from a CSV and produces a spending summary.

---

**PART 1 — UPGRADE THE CONTACT BOOK**

Take the contact book from the previous lesson and add file persistence:

**save_contacts(contacts, filename="contacts.csv"):**
- Saves all contacts to a CSV file
- Creates the file if it doesn't exist
- Overwrites the file with updated data each time

**load_contacts(filename="contacts.csv"):**
- Reads contacts from the CSV file at programme start
- Returns an empty list if the file doesn't exist (first run)
- Handles the FileNotFoundError gracefully

Show:
1. The complete save function with explanation
2. The complete load function with explanation
3. How the main programme calls these (when to save, when to load)
4. What the contacts.csv file looks like after saving 3 contacts

---

**PART 2 — EXCEPTION HANDLING**

File operations can fail. Teach me to handle errors properly using try/except.

Show exception handling for these scenarios:
1. The file doesn't exist when trying to read it
2. The file is corrupted or empty
3. The user doesn't have permission to write to the location
4. The CSV is missing expected column headers

For each: what error type Python raises, and how to handle it gracefully (with a helpful message, not a crash).

**Also explain:**
- What's the difference between try, except, else, and finally?
- When should you use except Exception as e vs specific error types?

---

**PART 3 — EXPENSE TRACKER**

Build a separate programme that reads expense data from CSV and produces a summary.

**The Input CSV (expenses.csv):**
Build a realistic CSV file with these columns: date, category, description, amount

Add 10 fictional expenses across 5 categories (Food, Transport, Entertainment, Bills, Shopping)

**The Analysis Programme:**
Read this CSV and produce:
1. Total spending overall
2. Total spending by category (as a table)
3. The most expensive single purchase
4. Average daily spend
5. Which category has the highest spending
6. A simple text-based bar chart showing spending by category

---

**PART 4 — JSON FILES**

CSV is for spreadsheet-like data. JSON is for structured data. Show me the difference.

**Convert the contact book to save/load from JSON instead of CSV:**

Show:
- How to import and use Python's json module
- The json.dump() and json.load() functions
- What the contacts.json file looks like
- When to use JSON vs CSV (what are each best for?)

---

**PART 5 — LOG FILE WRITER**

Create a simple logging function that any programme can use:

**write_log(message, filename="app_log.txt"):**
- Appends a log entry to the log file
- Each entry includes: timestamp, the message
- Use append mode so old logs are preserved

Show how to add logging to the contact book (log every: add, edit, delete action with timestamp).''',
    },
    {
        'title': 'Question 9: Connecting to the Web — APIs',
        'description': 'Fetch real data from the internet and build your first web-connected programme',
        'difficulty': 'intermediate',
        'order': 9,
        'points': 35,
        'instructions': '''Your programmes don't have to be isolated. APIs let you connect to real data from the internet — weather, news, financial data, maps, and more.

**What You'll Learn:**
- What an API is and how web requests work
- How to use Python's `requests` library to fetch data
- How to parse JSON responses
- How to build useful tools from free public APIs

**What is an API?**
An API (Application Programming Interface) is a way for programmes to talk to each other. When you request weather data, your programme sends a request to a weather API, which sends back data your programme can use.

**The Requests Library:**
```python
import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)  # 200 = success
data = response.json()       # Convert response to Python dictionary
```

**Free APIs to Explore:**
- **Open-Meteo** — Free weather data, no key needed
- **REST Countries** — Country data (population, capitals, currencies)
- **Open Notify** — ISS location and astronauts in space
- **JSONPlaceholder** — Fake data for testing
- **ExchangeRate API** — Currency exchange rates

**HTTP Status Codes:**
- `200` — OK (success)
- `404` — Not found
- `401` — Unauthorised (need API key)
- `500` — Server error

**Your Challenge:**
Build a programme that fetches real data from a public API and presents it usefully. No API key required — use free, open APIs.''',
        'example_prompt': '''Build two programmes that connect to free public APIs and display real data. Walk me through how APIs work in Python.

---

**PROGRAMME 1: WEATHER CHECKER**

Use the Open-Meteo API (free, no key needed) to build a weather checker.

**API:** https://api.open-meteo.com/v1/forecast

**What to build:**
1. Ask the user for a city name
2. Use a coordinates API or hardcode coordinates for a few UK cities
3. Fetch the current weather from Open-Meteo
4. Display:
   - Current temperature (Celsius)
   - Wind speed
   - Weather condition (sunny, cloudy, rainy etc.)
   - Temperature for the next 24 hours
5. Handle errors: what if the API is down? What if the city isn't found?

For the full tutorial, use these coordinates if needed:
- London: lat=51.5074, lon=-0.1278
- Manchester: lat=53.4808, lon=-2.2426
- Edinburgh: lat=55.9533, lon=-3.1883

Write the complete programme and explain:
- What `requests.get()` actually does
- What a "response" object contains
- How to access nested data in a JSON response (e.g., response["current"]["temperature_2m"])

---

**PROGRAMME 2: COUNTRY INFORMATION EXPLORER**

Use the REST Countries API (free, no key) to build a country explorer.

**API:** https://restcountries.com/v3.1/name/{country_name}

**What to build:**
1. Ask the user for a country name
2. Fetch the country data
3. Display:
   - Official name
   - Capital city
   - Population (formatted with commas: 67,886,011 not 67886011)
   - Region and subregion
   - Currencies (name and symbol)
   - Languages spoken
   - Flag emoji (most countries have one in the API!)
4. Ask if they want to look up another country (loop)
5. Handle "country not found" gracefully

---

**PART 3 — UNDERSTANDING THE RESPONSE**

Before writing the programme, explain:

1. What does the JSON response from the REST Countries API look like for "France"? (Show me the structure)
2. How do you access nested data? (e.g., how to get the capital from a response that has data["capital"][0])
3. What happens if you try to access a key that doesn't exist in the JSON? How do you handle this safely using .get() vs direct access?

---

**PART 4 — ERROR HANDLING FOR APIs**

Show me comprehensive error handling for API requests:

1. What if the internet connection fails?
2. What if the API returns a 404 (not found)?
3. What if the API returns a 500 (server error)?
4. What if the response isn't valid JSON?
5. How to add a timeout so your programme doesn't hang if the API is slow

Write a reusable function: safe_api_request(url) that handles all these cases gracefully.

---

**PART 5 — BUILDING SOMETHING USEFUL**

Using either API (or both!), build a small "UK Travel Information Tool" that:
- Takes a destination country as input
- Shows weather information (if available)
- Shows country information
- Gives a one-line "travel tip" based on the data (e.g., "Currency: Euro — remember to exchange before you go!")
- Works for any country, not just UK cities

This should be a useful, polished tool.''',
    },
    {
        'title': 'Question 10: Error Handling & Debugging with AI',
        'description': 'Master the art of finding, understanding, and fixing bugs using AI as your debugging partner',
        'difficulty': 'intermediate',
        'order': 10,
        'points': 30,
        'instructions': '''Every programmer writes buggy code. The difference between beginners and experts isn't writing perfect code — it's debugging efficiently.

**What You'll Learn:**
- How to read and understand Python error messages
- Systematic debugging strategies
- How to use AI as a debugging partner
- Writing defensive code that prevents common errors

**The Debugging Process:**
1. **Read the error message carefully** — it tells you the type, the file, and the line
2. **Find the traceback** — follow the error up through the call stack
3. **Reproduce the error** — make it happen consistently
4. **Form a hypothesis** — what do you think is wrong?
5. **Test your hypothesis** — add print statements or check variables
6. **Fix and verify** — fix the issue and confirm the error is gone

**Types of Bugs:**
- **Syntax errors** — Python can't parse your code (typo, missing bracket)
- **Logic errors** — Code runs but gives wrong answers (the hardest to find!)
- **Runtime errors** — Code crashes during execution (division by zero, missing key)
- **Type errors** — Wrong data type for the operation

**Using AI for Debugging:**
Best practice: Show AI the error message AND the relevant code. The better your description, the faster the fix.

**Your Challenge:**
Debug 5 broken programmes — each with different bug types. Then write a comprehensive guide to AI-assisted debugging.''',
        'example_prompt': '''Debug 5 broken programmes with AI assistance. For each one, teach me to diagnose and fix it systematically.

---

**BROKEN PROGRAMME 1: The Score Calculator**
```python
def calculate_grade(scores):
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)

    if average >= 90:
        grade = "A"
    if average >= 70:
        grade = "B"
    if average >= 60:
        grade = "C"
    else:
        grade = "F"

    return grade

student_scores = [85, 92, 78, 95, 88]
print(f"Grade: {calculate_grade(student_scores)}")
```

**Problem:** This always returns "F" even for high scores. Find the logic error and fix it. Explain what went wrong.

---

**BROKEN PROGRAMME 2: The Contact Saver**
```python
contacts = [
    {"name": "Alice", "phone": "07700 900123"},
    {"name": "Bob", "phone": "07700 900456"},
]

def find_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            return contact["phone"]

result = find_contact(contacts, "Charlie")
print(f"Charlie's number: {result.upper()}")
```

**Problem:** This crashes when Charlie isn't found. Diagnose the error, explain what None is and why it causes this problem, and fix the function.

---

**BROKEN PROGRAMME 3: The Expense Tracker**
```python
expenses = []

def add_expense(description, amount):
    expense = {
        "description": description,
        "amount": amount
    }
    expenses.append(expense)

def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

add_expense("Coffee", "3.50")
add_expense("Lunch", 12.00)
add_expense("Transport", "2.80")

print(f"Total: £{calculate_total():.2f}")
```

**Problem:** This crashes when calculating the total. What's wrong with the data types? Fix it and explain the mistake.

---

**BROKEN PROGRAMME 4: The Infinite Loop**
```python
def countdown(start):
    count = start
    while count != 0:
        print(f"T-minus {count}...")
        count -= 2
    print("Liftoff!")

countdown(10)
countdown(7)  # This one will run forever!
```

**Problem:** Works for even numbers but runs forever for odd numbers. Explain why and fix it without breaking the even-number behaviour.

---

**BROKEN PROGRAMME 5: The File Reader**
```python
def read_config(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    config = {}
    for line in lines:
        key, value = line.split("=")
        config[key] = value

    return config

settings = read_config("settings.txt")
print(settings)
```

**Problem:** This breaks in 3 different ways. Find all 3 issues:
1. What if the file doesn't exist?
2. What if a line doesn't contain "="?
3. What extra characters might be on each line that cause problems?

Fix all 3 issues and make this function robust.

---

**PART 6 — THE AI DEBUGGING GUIDE**

Based on these 5 examples, write a "Debugging with AI" guide for beginners:
1. What information to ALWAYS give AI when asking for debugging help
2. What to try before asking AI (things you should check yourself first)
3. The 3 most common Python bugs and how to spot them quickly
4. How to use print() statements to diagnose problems
5. When AI debugging advice might be wrong (and how to verify it)''',
    },
    {
        'title': 'Question 11: Building a Simple Web Page',
        'description': 'Create your first web page with HTML and CSS, guided by AI',
        'difficulty': 'intermediate',
        'order': 11,
        'points': 30,
        'instructions': '''Python builds the logic. HTML and CSS build what people actually see. Together, they let you create real web tools.

**What You'll Learn:**
- HTML basics: how web pages are structured
- CSS basics: how web pages are styled
- How to create a portfolio page that shows your coding work
- How AI helps you build visual things without being a designer

**HTML Basics:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>Main Heading</h1>
    <h2>Subheading</h2>
    <p>A paragraph of text.</p>
    <a href="https://example.com">A link</a>
    <img src="image.jpg" alt="Description">
    <ul>
        <li>List item 1</li>
        <li>List item 2</li>
    </ul>
</body>
</html>
```

**CSS Basics:**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    color: #333333;
    font-size: 2rem;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 8px;
}
```

**Your Challenge:**
Build a **Personal Portfolio Web Page** that showcases the programmes you've built in this track.

This is a real web page you could put online to show potential employers what you've made. Let AI guide the HTML and CSS — you direct what it should look like.''',
        'example_prompt': '''Build a complete Personal Portfolio Web Page for me — a real page that showcases my coding projects from this course. Guide me through every HTML and CSS decision.

---

**THE PORTFOLIO CONTENT:**

My name: Alex Morrison
Tagline: "Junior Developer | Learning Python with AI"
About me: I'm a marketing professional who has just completed an AI skills programme. I've built Python projects including a quiz game, contact book, expense tracker, and weather app.

Projects to showcase:
1. Quiz Game — Tests general knowledge with 5 questions, score tracking, and difficulty levels
2. Contact Book — Stores and manages contacts with search, edit, and delete features
3. Daily Schedule Generator — Helps plan the day with priority-based task management
4. Weather & Country Info Tool — Fetches real data from public APIs

Skills to list: Python, APIs, File handling, Data structures, AI-assisted development

Contact: alex.morrison@example.com | GitHub: alexmorrison (fictional)

---

**PART 1 — THE HTML STRUCTURE**

Build the complete HTML for this portfolio page. For every HTML element you use:
- Explain what it does
- Explain why you chose it (not a different element)
- Point out the correct semantic HTML (e.g., why use <section> not just <div>?)

The page should have:
- Navigation bar
- Hero section (name, tagline, brief intro)
- About section
- Projects section (4 project cards)
- Skills section
- Contact section
- Footer

---

**PART 2 — THE CSS STYLING**

Write the CSS to make this page look genuinely professional. For every style decision:
- Explain what it does visually
- Explain the why (why this colour? why this padding?)

**Style requirements:**
- Clean, modern design (not bland but not flashy)
- Good typography (Google Font — recommend one that works for a tech portfolio)
- Professional colour scheme (provide the hex codes you chose and why)
- Responsive basics — should look decent on mobile too
- Project cards with hover effects
- Smooth appearance — consistent spacing, aligned elements

---

**PART 3 — MAKING IT INTERACTIVE (JavaScript basics)**

Add a tiny bit of JavaScript — just enough to see how it works:

1. A "scroll to top" button that appears when the user scrolls down
2. A simple toggle for "Light Mode / Dark Mode"
3. A contact form that shows a thank-you message when submitted (without actually sending)

For each: explain what JavaScript is doing and how it connects to the HTML.

---

**PART 4 — PUTTING IT ONLINE**

Explain how to publish this portfolio for free:
- What is GitHub Pages and how do you use it?
- Step-by-step: from HTML file on my computer to live URL
- What the URL would look like
- What to do if something looks wrong after publishing

---

**PART 5 — AI-ASSISTED WEB DESIGN**

Reflect on using AI for web development:
1. What did AI help most with in building this page?
2. Where do you still need a human designer's judgment?
3. What's the next thing I'd learn to make this page more impressive?
4. How could I add Python backend functionality to this page? (Introduce the concept without requiring me to learn it now)''',
    },
    {
        'title': 'Question 12: Working with Databases',
        'description': 'Store data permanently using SQLite and build a task manager with a real database',
        'difficulty': 'intermediate',
        'order': 12,
        'points': 35,
        'instructions': '''CSV files work for simple data. Databases are for everything else — fast searching, complex queries, multiple users, and large datasets.

**What You'll Learn:**
- What databases are and when to use them instead of files
- SQLite basics — the perfect beginner database (no setup required)
- Basic SQL: CREATE, INSERT, SELECT, UPDATE, DELETE
- Building a Python programme that uses a real database

**SQLite with Python:**
```python
import sqlite3

# Connect to database (creates if not exists)
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
""")

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
```

**Why Databases Over Files:**
- Much faster searching (imagine searching 1 million contacts!)
- Can handle multiple users accessing at once
- Data relationships (a task belongs to a project)
- Built-in data integrity checks

**Your Challenge:**
Build a **Task Manager** application with a SQLite database backend — allowing tasks to be added, listed, completed, and deleted — with the data persisting permanently.''',
        'example_prompt': '''Build a complete Task Manager application with a SQLite database backend. Walk me through every database concept as we build it.

---

**THE TASK MANAGER SPEC:**

The application should:
1. Store tasks in a SQLite database (tasks.db)
2. Each task has: id (auto-assigned), title, description, priority (High/Medium/Low), due_date, status (pending/completed), created_at
3. Allow: Add task, View all tasks, View pending only, Mark as complete, Edit task, Delete task, Quit

---

**PART 1 — DATABASE DESIGN**

Before writing code, design the database:

1. Write the SQL CREATE TABLE statement for the tasks table
2. Explain every column:
   - What data type? (TEXT, INTEGER, REAL, BLOB)
   - Why NOT NULL on some fields?
   - What is PRIMARY KEY AUTOINCREMENT?
   - What is DEFAULT in SQL?
3. Show an example of what 3 rows in this table would look like
4. What would a second table look like if I wanted to add "Projects" that tasks belong to? (Introduce the concept of relationships/foreign keys)

---

**PART 2 — DATABASE CONNECTION CLASS**

Create a TaskDatabase class that handles all database operations:

```python
class TaskDatabase:
    def __init__(self, db_name="tasks.db"):
        # Connect to database, create table if not exists

    def add_task(self, title, description, priority, due_date):
        # INSERT new task

    def get_all_tasks(self):
        # SELECT all tasks

    def get_pending_tasks(self):
        # SELECT where status = 'pending'

    def complete_task(self, task_id):
        # UPDATE status to 'completed'

    def delete_task(self, task_id):
        # DELETE task by id

    def close(self):
        # Close the connection
```

Write the complete implementation of each method with full explanation.

---

**PART 3 — SQL QUERY MASTERY**

Show me these SQL queries with Python examples:

1. Get all tasks sorted by priority (High first, then Medium, then Low)
2. Get all overdue tasks (due_date is before today)
3. Count how many tasks are in each status
4. Search tasks where the title contains a search term (LIKE operator)
5. Get tasks created in the last 7 days

For each query: write the SQL, wrap it in a Python function, and explain the SQL syntax in plain English.

---

**PART 4 — THE COMPLETE APPLICATION**

Build the full task manager with a command-line menu interface.

Show what it looks like running:
```
--- Task Manager ---
1. Add new task
2. View all tasks
3. View pending tasks
4. Mark task as complete
5. Delete task
6. Search tasks
7. Statistics
8. Quit
```

Make the display nicely formatted — use column alignment and status indicators.

---

**PART 5 — STATISTICS AND REPORTING**

Add a Statistics page that shows:
- Total tasks, pending tasks, completed tasks
- Completion rate (% of tasks completed)
- Overdue tasks count
- Tasks due today and in the next 7 days
- Most productive day (day with most completions)

Show the SQL queries that power each statistic.''',
    },
    {
        'title': 'Question 13: Mini Project — Build a Budget Tracker',
        'description': 'Build a complete, real-world budget tracking application from start to finish',
        'difficulty': 'advanced',
        'order': 13,
        'points': 40,
        'instructions': '''You now have all the skills to build something genuinely useful. This mini project brings them all together.

**What You'll Build:**
A complete budget tracker that:
- Stores transactions in a database
- Categorises income and expenses
- Provides a monthly spending summary
- Shows spending trends and insights
- Exports reports to CSV

**Skills This Combines:**
- Variables and data types (transaction data)
- Functions (all operations encapsulated)
- Loops (processing transaction lists)
- File I/O (CSV export)
- Databases (SQLite for persistent storage)
- Error handling (graceful failures)

**This is a real project.** By the end, you'll have a working application you actually built — and could show to an employer.

**Project Requirements:**
1. SQLite database with transactions table
2. Add income and expense transactions
3. View all transactions with filters (date range, category)
4. Monthly summary: income, expenses, net balance
5. Category breakdown with percentages
6. Visual bar chart (text-based) of spending by category
7. Export transactions to CSV
8. Simple budget goal setting and tracking

Complete this project end-to-end, writing every function and explaining every design decision.''',
        'example_prompt': '''Build a complete Budget Tracker application. This is my first real project — I want it to be something I'm genuinely proud of.

---

**PART 1 — PROJECT PLANNING**

Before writing any code, design the project:

1. **Database Schema:** Design the complete SQLite database. What tables? What columns? Show the CREATE TABLE statements.

2. **Feature List:** What can the user do? Write a complete list of all features, prioritised (core vs nice-to-have).

3. **Function Map:** List every function the project needs, with a one-line description of what each does. Organise them by what they do (database, display, calculations, etc.)

4. **Data Flow:** Walk through one complete user action — adding an expense — from the user typing to the data being saved. Every step.

---

**PART 2 — THE DATABASE LAYER**

Build the complete database module (budget_db.py):

Functions needed:
- `initialise_database()` — creates tables if they don't exist
- `add_transaction(date, type, category, description, amount)` — adds income or expense
- `get_transactions(start_date=None, end_date=None, category=None)` — with filters
- `get_monthly_summary(year, month)` — total income, expenses, balance
- `get_category_totals(month, year)` — breakdown by category
- `set_budget_goal(category, monthly_limit)` — sets spending limits
- `check_budget_goals(month, year)` — checks if any limits exceeded
- `export_to_csv(filename, start_date=None, end_date=None)` — CSV export

Write every function with full explanation.

---

**PART 3 — CALCULATIONS AND INSIGHTS**

Build the calculations module (budget_calc.py):

- `calculate_net_balance(income_total, expense_total)` — simple but build it as a function
- `calculate_category_percentages(category_totals, total_expenses)` — what % is each category
- `calculate_savings_rate(income, expenses)` — what % is being saved
- `generate_spending_trend(transactions)` — week-over-week or day-over-day totals
- `identify_top_spending_categories(category_totals, n=3)` — top n categories

---

**PART 4 — THE DISPLAY LAYER**

Build the display module (budget_display.py):

- `display_transaction_table(transactions)` — formatted table with alignment
- `display_monthly_summary(summary_data)` — clear income/expense/balance display
- `display_category_chart(category_totals)` — text-based bar chart
- `display_budget_goals_status(goals, actuals)` — green for under, red for over
- `display_insights(transactions, summaries)` — 3 interesting insights from the data

For the bar chart, make it look like:
```
Food        ████████████████░░░░  £340 (42%)
Transport   ████████░░░░░░░░░░░░  £180 (22%)
Shopping    ██████░░░░░░░░░░░░░░  £140 (17%)
```

---

**PART 5 — THE MAIN APPLICATION**

Build the main.py that brings everything together with a menu interface.

Show the complete application flow from start (loading the database) to quit (close connection).

Include sample data: add 15 fictional transactions across 3 months and show what the application looks like with real data.

---

**PART 6 — REFLECTION**

After building this, answer:
1. What was the hardest part of this project?
2. What would you add if you had another week to work on it?
3. What have you learned about how real programmes are structured?
4. How is this different from the tutorial exercises you did in earlier lessons?''',
    },
    {
        'title': 'Question 14: Mini Project — Build a Data Dashboard',
        'description': 'Create an interactive data dashboard that displays and analyses a real dataset',
        'difficulty': 'advanced',
        'order': 14,
        'points': 40,
        'instructions': '''Data is everywhere. Being able to pull it together, analyse it, and display it clearly is one of the most in-demand technical skills.

**What You'll Build:**
A data dashboard that:
- Reads data from multiple sources (CSV + API)
- Processes and analyses the data
- Displays key metrics and visualisations
- Updates data with a refresh command

**New Concepts in This Project:**

**Pandas (optional introduction):**
Python's data analysis library — makes working with tabular data much easier than lists of dictionaries.

**Matplotlib (text-based alternative):**
For this project, we'll create text-based charts that work in any terminal.

**Data Pipeline:**
- Source → Collect → Clean → Process → Display → Refresh

**Your Challenge:**
Build a personal finance dashboard that combines your budget tracker data with live currency exchange rates (from a free API) to show:
- Monthly financial health metrics
- Spending trends
- Currency comparison (if any international transactions)
- Forecast for the month-end based on current spending pace

This is your most ambitious project so far — design, build, and present it.''',
        'example_prompt': '''Build a complete Data Dashboard project. This should be polished enough to show as a portfolio piece.

---

**THE DASHBOARD CONCEPT:**
"FinView" — a personal finance dashboard that shows my financial health at a glance. It reads from my budget tracker database AND fetches live exchange rates from an API.

---

**PART 1 — DASHBOARD ARCHITECTURE**

Design the complete architecture:

1. **Data sources:** Where does each metric come from?
2. **Processing layer:** What calculations happen between data and display?
3. **Display layer:** What does the user see and how?
4. **Refresh cycle:** How does the user get updated data?

Draw a text-based architecture diagram showing the flow.

---

**PART 2 — THE METRICS TO DISPLAY**

Design 6 dashboard panels:

**Panel 1: Financial Health Score**
Calculate a 0-100 score based on: savings rate, budget adherence, spending trend. Show as a large number with a label (Good/Warning/Poor).

**Panel 2: This Month at a Glance**
- Income so far this month
- Expenses so far
- Net balance
- Days left in month
- Projected month-end balance (based on daily average spend)

**Panel 3: Spending by Category (Bar Chart)**
Visual bar chart of this month's spending, compared to monthly budget goals.

**Panel 4: Trend Chart**
Last 6 months of net balance as a line chart (text-based).

**Panel 5: Top 3 Insights**
AI-generated observations about the spending data — the 3 most interesting patterns or recommendations.

**Panel 6: Exchange Rate Ticker**
Live GBP exchange rates against USD, EUR, AUD (from free API).

---

**PART 3 — THE COMPLETE DASHBOARD DISPLAY**

Write the code that renders the full dashboard in the terminal.

It should look something like:
```
╔════════════════════════════════════════╗
║         FINVIEW DASHBOARD              ║
║         Last updated: 14:32            ║
╠═══════════════╦════════════════════════╣
║ HEALTH: 74    ║ FEBRUARY SUMMARY       ║
║ ████████░░    ║ Income:    £3,200      ║
║ Good          ║ Expenses:  £2,140      ║
║               ║ Balance:   £1,060      ║
╚═══════════════╩════════════════════════╝
```

Show the complete display code with sample data output.

---

**PART 4 — THE AI INSIGHTS ENGINE**

Build the insights generator:

Write a function that takes the financial data and produces 3 specific, actionable insights.

NOT generic insights like "You spent money this month." Real insights like:
- "Your food spending is 23% higher than last month — you had 3 restaurant visits over £50"
- "At current pace, you'll exceed your Transport budget by £45 this month"
- "You're on track to save £380 this month — your best month this year"

Write the function that generates these from real data.

---

**PART 5 — PORTFOLIO PRESENTATION**

Write a README.md for this project — the documentation file that goes on GitHub:

Include:
- Project title and description
- Features list
- Screenshot (describe what a screenshot would show)
- How to install and run
- How to use the main features
- Technologies used
- What you learned building it
- Future improvements

This is what an employer sees when they look at your GitHub.''',
    },
    {
        'title': 'Question 15: Capstone — Build Your Own AI-Powered Application',
        'description': 'Design, build, and present your own original AI-powered application',
        'difficulty': 'advanced',
        'order': 15,
        'points': 50,
        'instructions': '''This is your Track A Capstone. You've learned Python, databases, APIs, web basics, and file handling. Now you bring it all together in one original, AI-powered application that you design yourself.

**What This Capstone Demonstrates:**
- Application design thinking (not just coding)
- Combining multiple skills in one coherent project
- Integrating an AI API (like Claude or OpenAI) into a Python programme
- Solving a real problem for a real user
- Producing work you're genuinely proud of

**What "AI-Powered" Means:**
Your application should call an AI API (like the Anthropic Claude API or OpenAI API) as a core feature — not just as a novelty. The AI should do something genuinely useful that couldn't easily be done another way.

**Project Ideas (or bring your own):**
- AI Study Buddy: Enter a topic, get an AI-generated lesson, quiz, and flashcards
- Smart Cover Letter Generator: Input your CV + job description, get a personalised cover letter
- AI Journal with Mood Tracking: Write daily, AI analyses mood and patterns over time
- Recipe AI: Input ingredients you have, get recipe ideas and nutritional information
- AI Meeting Summariser: Input meeting notes, get structured output with action items

**Requirements:**
- Solves a real problem for a real person
- Uses at least 2 Python modules/libraries
- Stores data persistently (file or database)
- Has a clean, usable interface (command-line is fine)
- Integrates an AI API call as a core feature
- Includes proper error handling
- Comes with documentation (README)

**Make it genuinely yours.** Choose something you'd actually want to use.''',
        'example_prompt': '''This is my Track A Capstone. I'm building an original AI-powered application — and I want to design it properly from concept to completion.

---

**MY APPLICATION CONCEPT:**
"SkillSprint" — an AI-powered learning companion that creates personalised mini-lessons on any topic, quizzes you, tracks your progress, and adapts difficulty based on performance.

**The Problem it Solves:**
I want to learn new skills in spare moments (commute, lunch break) but I don't want to commit to a full course. SkillSprint generates bite-sized, personalised lessons on demand — and remembers what I've learned so each session builds on the last.

---

**PART 1 — FULL APPLICATION DESIGN**

Before writing any code, complete the design:

**A) User Story:**
Write 5 user stories in the format: "As a [user], I want to [action] so that [benefit]."
These describe what the application must do from the user's perspective.

**B) Feature Specification:**
List every feature of the final application:
- Core features (must have for v1.0)
- Nice-to-have features (v1.1 or later)
- Out of scope (explicitly excluded)

**C) Data Model:**
Design the database schema. What tables? What data do we store?
(Topics, lessons, quiz results, user progress, settings)

**D) Application Architecture:**
Map out the files and modules:
- main.py (what's in it?)
- database.py (what functions?)
- ai_engine.py (what functions?)
- display.py (what functions?)

**E) User Interface Design:**
Describe the main menu and every screen in the application. What does the user see and do at each step?

---

**PART 2 — THE AI ENGINE**

Build the AI integration module (ai_engine.py):

**Function 1: generate_lesson(topic, difficulty, prior_knowledge_summary)**
- Calls Claude/OpenAI API
- Prompt designed to generate a structured mini-lesson
- Lesson format: Introduction (2 paragraphs), Key concepts (3-5 bullet points), Real-world example, Practice exercise
- Returns structured lesson data

Write the complete function including the system prompt and user prompt. Explain every prompt design decision.

**Function 2: generate_quiz(lesson_content, num_questions=5)**
- Takes a lesson and generates a quiz
- Returns 5 multiple choice questions with correct answers and explanations
- Difficulty matches the lesson difficulty

Write the complete function.

**Function 3: generate_feedback(quiz_results, topic)**
- Takes quiz performance data
- Returns personalised feedback and what to review
- Suggests what to learn next

Write the complete function.

---

**PART 3 — THE COMPLETE APPLICATION**

Write the complete, working application — all files, all functions.

Show it running for a complete session:
1. User opens the app
2. Chooses to learn a new topic: "Python list comprehensions"
3. Gets an AI-generated lesson
4. Takes a 5-question quiz
5. Gets feedback and score
6. Progress is saved
7. Returns to menu

Show realistic AI-generated content for each step.

---

**PART 4 — TESTING YOUR APPLICATION**

Design a testing plan:
- What are the 5 most important things to test?
- What inputs could break the application?
- How do you test the AI integration without using up API credits?
- What edge cases exist?

Write and run 3 test scenarios.

---

**PART 5 — THE PORTFOLIO PRESENTATION**

Create the complete portfolio documentation:

**README.md:**
Write a professional README that would impress someone reviewing your GitHub.

**Demo Script:**
Write a 3-minute walkthrough of your application — what you'd say if presenting it to a panel. Cover: the problem, how it works, the technical highlights, and what you'd improve.

**What You Learned:**
Write a genuine reflection (500 words): what was hardest, what you're most proud of, how your thinking changed across the 15 lessons, and where you go from here.

This capstone is your proof of what's possible when you combine coding skills with AI fluency. Make it count.''',
    },
]
