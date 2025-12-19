# Module 1: AI Chat Mastery - Memory & Chat Management Section
# 10 challenges teaching students how to use memory features and maintain context

MEMORY_CHAT_CHALLENGES = [
    {
        'title': 'Lesson 16: Understanding AI Memory',
        'description': 'Learn how Claude\'s memory feature works and why it matters',
        'difficulty': 'beginner',
        'order': 16,
        'points': 20,
        'instructions': '''Welcome to Memory & Context Management! 🧠

**What You'll Learn:**
- What AI memory is
- Why it's powerful
- How to use it effectively

**The Concept:**
Claude can remember information across conversations! This means you don't have to repeat yourself every time.

**Your Challenge:**
Create a prompt that teaches Claude about YOUR work context, so future conversations are personalized.

**What to Include:**
- Your role and responsibilities
- Your company/industry
- Common tasks you do
- Preferences for how you like information presented

**Example Structure:**
"Remember these details about me:
- I'm a [role] at [company]
- I primarily work on [tasks]
- I prefer [communication style]
- My main challenges are [problems]"

**Real-World Power:**
Once Claude knows your context, every future conversation is already personalized! No more repeating "I work in cybersecurity" every time.

**Your Task:**
Write a comprehensive "memory primer" for Claude about your professional context. Make future conversations easier!''',
        'example_prompt': '''Please remember these details about me for our future conversations:

PROFESSIONAL CONTEXT:
- I'm a SOC Analyst at a mid-sized healthcare company (500 employees)
- My team monitors security events 24/7 in rotating shifts
- We use Splunk for SIEM, CrowdStrike for EDR
- I'm responsible for triaging security alerts and escalating incidents

WORK PATTERNS:
- I work 12-hour shifts (7am-7pm)
- I handle 50-100 security alerts per shift
- Most common incidents: phishing attempts, failed login attempts, policy violations

COMMUNICATION PREFERENCES:
- I prefer concise, actionable responses
- Use bullet points when possible
- Prioritize practical steps over theory
- When explaining technical concepts, assume I have basic security knowledge

CURRENT PRIORITIES:
- Reducing false positives in our alert system
- Improving incident documentation
- Learning threat hunting techniques

CONSTRAINTS:
- Limited budget for new tools
- Small team (only 3 analysts)
- Need solutions that work with existing tools

Remember all of this for our future conversations so you can give me personalized, relevant advice!''',
    },
    {
        'title': 'Lesson 17: Building Conversation Context',
        'description': 'Learn to maintain context across a long conversation',
        'difficulty': 'beginner',
        'order': 17,
        'points': 20,
        'instructions': '''Context is the thread that connects a conversation! 🧵

**What You'll Learn:**
- How to reference previous messages
- Building on earlier context
- Maintaining coherent conversations

**The Challenge:**
Start a multi-turn conversation about a security project, where each message builds on the previous one.

**Your Task - Part 1:**
Begin a conversation about implementing a new security control. Your first prompt should:
- Introduce the project
- Ask for initial advice
- Set up context for follow-up questions

**Then (in the same conversation):**
- Ask follow-up questions that reference previous answers
- Add new information that builds on earlier discussion
- Show how context compounds over multiple turns

**Example Flow:**
Turn 1: "I need to implement MFA for our company..."
Turn 2: "Based on your suggestion of Duo Security, how would that integrate with..."
Turn 3: "Given the 30-day timeline you mentioned and the $10K budget, what about..."

**Real-World:**
Complex problems aren't solved in one message. Learn to have productive multi-turn conversations!

**Try it:** Start a conversation and keep it going for 3-4 turns, each building on the last.''',
        'example_prompt': '''PROJECT: I need to implement Multi-Factor Authentication (MFA) for our company.

CONTEXT:
- Company: 75 employees, mostly remote
- Current situation: Just passwords, no MFA
- Recent incident: One account was compromised due to weak password
- Timeline: Need to implement within 60 days
- Budget: Roughly $8,000-$10,000
- Technical environment: Microsoft 365, some cloud apps (Salesforce, Slack)

WHAT I NEED:
Give me initial recommendations for:
1. Which MFA solution might work best for our setup
2. Rough timeline for implementation
3. Main challenges I should prepare for

After you answer, I'll have follow-up questions about implementation details.''',
    },
    {
        'title': 'Lesson 18: Referencing Previous Conversations',
        'description': 'Learn to reference past chats and build on them',
        'difficulty': 'beginner',
        'order': 18,
        'points': 20,
        'instructions': '''Your conversation history is a knowledge base! 📚

**What You'll Learn:**
- How to reference past conversations
- Building on previous work
- Creating continuity

**The Power:**
With memory, Claude can remember past conversations! You can say "Remember when we discussed..." and continue where you left off.

**Your Challenge:**
Create a prompt that references a hypothetical previous conversation and builds on it.

**Format:**
"In our previous conversation about [topic], you recommended [solution]. Now I want to take the next step..."

**Your Task:**
Write a prompt that:
1. References a past conversation (can be hypothetical)
2. Summarizes key points from it
3. Asks to build on that foundation
4. Shows continuity of thought

**Example:**
"Last week we discussed implementing a SIEM solution, and you recommended starting with Splunk Cloud. I've now gotten budget approval for $15K. Based on our previous discussion about our log volume (5GB/day) and team size (3 analysts), can you help me create a detailed implementation plan?"

**Real-World:**
Projects evolve over weeks/months. Being able to continue conversations without starting from scratch is HUGE!''',
        'example_prompt': '''In our previous conversation about reducing phishing incidents, you suggested a multi-layered approach including:
1. Enhanced email filtering
2. User training with simulated phishing
3. Implementation of DMARC/SPF/DKIM
4. Adding a phishing report button

We've now successfully implemented items 1 and 3. Email filtering blocked 87% more phishing attempts, and we have full DMARC enforcement.

NOW I want to focus on item 2 - the user training. Given that our previous discussion established:
- We have 200 employees across 5 departments
- Budget is $5,000 for training
- We need to complete training in 45 days
- Previous training had poor engagement (only 60% completion)

Help me design an engaging phishing simulation and training program that addresses the low engagement issue we discussed. Build on what we established before.''',
    },
    {
        'title': 'Lesson 19: Progressive Learning Pattern',
        'description': 'Use AI to learn complex topics progressively',
        'difficulty': 'intermediate',
        'order': 19,
        'points': 25,
        'instructions': '''Master complex topics step-by-step! 📈

**What You'll Learn:**
- Progressive learning technique
- Building knowledge incrementally
- When to add complexity

**The Pattern:**
Start simple → Verify understanding → Add complexity → Practice → Level up

**Your Challenge:**
Learn a complex security topic (like network segmentation, zero-trust, or threat hunting) through a progressive conversation.

**The Approach:**
1. "Explain [topic] in simple terms first"
2. "OK, now add more technical detail about [aspect]"
3. "Give me a practical example of [application]"
4. "What are common mistakes when implementing this?"
5. "How would I apply this in [your specific context]?"

**Your Task:**
Create a learning plan for a complex security topic. Structure your prompts to:
- Start with fundamentals
- Gradually increase complexity
- Include check-points for understanding
- Connect to your real work
- End with practical application

**Real-World:**
You can't learn everything at once. Progressive learning with AI is like having a patient tutor who adapts to YOUR pace!''',
        'example_prompt': '''I want to understand Zero Trust Architecture, but I'm new to this concept. Let's learn this progressively:

STEP 1 (Foundation): Explain Zero Trust Architecture in simple terms. What's the core concept? Use an analogy that's easy to grasp. Keep it under 200 words.

After I confirm I understand Step 1, we'll move to:

STEP 2 (Technical Details): Explain the key components and how they work together

STEP 3 (Practical Application): Show me a real-world example of implementing Zero Trust in a mid-sized company

STEP 4 (Common Pitfalls): What do organizations get wrong when implementing Zero Trust?

STEP 5 (My Context): How would Zero Trust apply to my healthcare organization with legacy systems?

Let's start with Step 1. Explain the fundamentals in simple terms.''',
    },
    {
        'title': 'Lesson 20: Remembering Preferences and Styles',
        'description': 'Teach Claude your communication preferences',
        'difficulty': 'intermediate',
        'order': 20,
        'points': 25,
        'instructions': '''Make AI adapt to YOUR style! 🎨

**What You'll Learn:**
- Setting communication preferences
- Consistent response formatting
- Personalized interactions

**The Power:**
Tell Claude once how you like information presented, and future responses will match your preferences!

**Your Challenge:**
Create a comprehensive "style guide" for how you want Claude to communicate with you.

**What to Include:**
- Response length preferences (concise vs detailed)
- Format preferences (bullets, paragraphs, tables)
- Technical level (assume expertise or explain basics)
- Tone (formal, casual, direct)
- When to use examples vs theory
- How to handle complex topics

**Your Task:**
Write a prompt that teaches Claude YOUR communication style, covering:
1. How technical you want responses
2. Preferred formats and structures
3. When you want details vs summaries
4. Your learning style
5. Any pet peeves or preferences

**Real-World:**
Everyone consumes information differently. Teaching AI your style = better communication every time!''',
        'example_prompt': '''Please remember my communication preferences for all future conversations:

RESPONSE STYLE:
- Be direct and concise - I value efficiency
- Lead with the answer/key point, then provide supporting details
- Use bullet points for lists and action items
- Keep responses under 300 words unless I specifically ask for more detail

TECHNICAL LEVEL:
- I'm a cybersecurity professional with 3 years experience
- Assume I understand basic security concepts (don't explain what phishing is)
- DO explain advanced concepts or new technologies
- When suggesting tools, assume I'm familiar with common ones

FORMAT PREFERENCES:
- For step-by-step processes: Use numbered lists
- For comparisons: Use tables or clear pros/cons format
- For complex topics: Start with a 1-sentence summary
- Always separate "what to do" from "why to do it"

LEARNING STYLE:
- I learn best with real-world examples and use cases
- Show me practical applications before theory
- When teaching concepts, use security-specific analogies
- Include "common mistakes" sections when relevant

WHEN I'M PROBLEM-SOLVING:
- Give me options ranked by priority
- Include quick wins vs long-term solutions
- Always consider budget and resource constraints
- Focus on actionable next steps

PET PEEVES:
- Don't be overly cautious or add too many disclaimers
- Don't suggest "consulting with a professional" - I am the professional
- Skip generic advice like "it depends" - give specific guidance even if you need to make assumptions

Remember all of this and adapt your communication style accordingly!''',
    },
    {
        'title': 'Lesson 21: Project-Based Memory',
        'description': 'Use memory to track ongoing projects and tasks',
        'difficulty': 'intermediate',
        'order': 21,
        'points': 25,
        'instructions': '''Track projects across multiple conversations! 📊

**What You'll Learn:**
- Project state tracking
- Status updates
- Continuity across sessions

**The Concept:**
Tell Claude about an ongoing project once, then update it as you progress. Claude remembers the current state!

**Your Challenge:**
Set up a project tracking system with Claude.

**Your Task:**
Create a prompt that:
1. Introduces a security project you're working on
2. Defines current status
3. Lists pending tasks
4. Sets success criteria
5. Asks Claude to remember all this

**Then in Future Conversations:**
- "Update: I've completed task X from our security project"
- "What's the next priority for the project we discussed?"
- "Given the blocker we discovered, how should we adjust the project plan?"

**Example Structure:**
"I'm starting a project to migrate our security monitoring to the cloud. Remember these details:
- Goal: [specific goal]
- Timeline: [dates]
- Current phase: [where we are]
- Completed: [what's done]
- Next steps: [what's pending]
- Blockers: [current challenges]
- Budget status: [remaining funds]"

**Real-World:**
Security projects span weeks/months. Having AI remember the context means every conversation picks up where you left off!''',
        'example_prompt': '''I'm starting a major security project and need you to track it across our conversations.

PROJECT: Security Awareness Training Program Overhaul

BACKGROUND:
- Current training is outdated PowerPoint, poor engagement (45% completion)
- Recent audit flagged inadequate security awareness
- Leadership approved $25K budget and 90-day timeline
- 250 employees across 4 locations need training

PROJECT GOALS:
1. Achieve 95% completion rate
2. Reduce successful phishing simulation clicks from 35% to under 10%
3. Meet compliance requirements (HIPAA, SOC 2)
4. Create sustainable ongoing training (not just one-time)

CURRENT STATUS:
- Week 1 of 12
- Researching training platforms and vendors
- Gathering requirements from department heads
- Budget: $25K allocated, $0 spent so far

TASKS PENDING:
1. Select training platform (due: Week 2)
2. Develop content modules (Week 3-5)
3. Launch phishing simulation baseline (Week 3)
4. Pilot with IT department (Week 6)
5. Company-wide rollout (Week 7-10)
6. Measure and report results (Week 11-12)

KEY STAKEHOLDERS:
- CISO (my boss) - wants quarterly metrics
- HR Director - worried about employee pushback
- Compliance Officer - focused on audit requirements

KNOWN CHALLENGES:
- Resistance to "more training"
- 4 different office locations/time zones
- Remote workforce (60% work from home)
- Need mobile-friendly solution

Remember all of this. I'll update you on progress and ask for advice as challenges come up. Track our project state across conversations.''',
    },
    {
        'title': 'Lesson 22: Decision Tracking',
        'description': 'Track decisions and their rationale over time',
        'difficulty': 'intermediate',
        'order': 22,
        'points': 25,
        'instructions': '''Remember WHY you made decisions! 🤔

**What You'll Learn:**
- Tracking decision rationale
- Revisiting past choices
- Learning from outcomes

**The Challenge:**
Security decisions have consequences. Tracking the reasoning helps you learn and explain to others.

**Your Task:**
Create a system where Claude helps you track important decisions.

**Format:**
"Remember this decision:
- What we decided: [choice made]
- When: [date]
- Why: [reasoning]
- Alternatives considered: [other options]
- Expected outcome: [what we hoped would happen]
- Concerns: [what worried us]"

Then later:
"Remember that decision about [X]? Here's what actually happened... Given this outcome, what lessons can we learn?"

**Your Prompt Should:**
1. Document a security decision you made (real or hypothetical)
2. Capture all the context and reasoning
3. Ask Claude to remember it
4. Set up for future retrospective

**Real-World:**
When your boss asks "Why did we choose vendor X over Y?" 6 months later, you'll have the complete reasoning documented!

Decision tracking = Better learning and accountability.''',
        'example_prompt': '''Please remember this important security decision for future reference:

DECISION: Selected Okta over Duo for our MFA implementation

DATE: [Current date]

CONTEXT:
- Needed to implement MFA for 150 users
- Budget: $12,000/year
- Timeline: 60 days to implement
- Environment: Microsoft 365, Salesforce, several custom apps

OPTIONS CONSIDERED:
1. Okta - $13/user/month = $23,400/year
2. Duo - $6/user/month = $10,800/year
3. Microsoft MFA (built-in) - Minimal cost but limited features

WHY WE CHOSE OKTA:
- Better integration with our custom applications
- More robust reporting for compliance
- Single Sign-On benefits beyond just MFA
- IT Director had positive experience with it at previous company
- Longer-term scalability as we grow

CONCERNS/TRADEOFFS:
- Over budget by $11,400/year
- More complex to implement (4 weeks vs 2 weeks for Duo)
- Requires more training for help desk
- Vendor lock-in concerns

EXPECTED OUTCOMES:
- 90%+ adoption within 60 days
- Reduced password reset tickets (50% reduction)
- Better security posture (zero compromised accounts)
- Positive user experience with SSO

METRICS TO TRACK:
- Adoption rate (weekly)
- Help desk tickets (before/after)
- Security incidents related to authentication
- User satisfaction (survey after 90 days)

FOLLOW-UP CHECK-IN: 90 days from now

Remember all of this so we can review the decision later and learn from the outcomes. I'll update you on how it's going.''',
    },
    {
        'title': 'Lesson 23: Learning from Past Conversations',
        'description': 'Review and learn from your conversation history',
        'difficulty': 'advanced',
        'order': 23,
        'points': 30,
        'instructions': '''Your conversations are a learning resource! 📖

**What You'll Learn:**
- Extracting lessons from past work
- Pattern recognition
- Continuous improvement

**The Power:**
Review what you've discussed with Claude to identify patterns, lessons, and areas for growth.

**Your Challenge:**
Create a "retrospective review" prompt that asks Claude to analyze themes across your conversations.

**Your Task:**
Ask Claude to review what you've discussed together and identify:
- Common challenges you face
- Topics you frequently ask about
- Skills you're developing
- Patterns in your questions
- Suggested areas for growth

**The Prompt:**
"Based on our past conversations about [topic area], what patterns do you notice in the challenges I face? What skills have I been developing? What areas should I focus on learning next?"

**Example:**
"We've had multiple conversations about incident response over the past month. Looking back at those discussions, what themes emerge? What am I getting better at? What gaps do you still see in my approach? What should I learn next?"

**Real-World:**
Self-awareness drives growth. Use AI to help you see patterns you might miss!

Meta-learning = Learning how you learn!''',
        'example_prompt': '''Based on all our previous conversations about cybersecurity and my work as a SOC analyst, I want you to help me reflect and identify areas for growth.

Please analyze our conversation history and tell me:

1. RECURRING THEMES:
   What topics do I ask about most often?
   What challenges keep coming up?
   
2. SKILL DEVELOPMENT:
   What areas have I been actively learning about?
   What progress have you observed in my thinking?
   What concepts did I struggle with initially but now grasp better?

3. KNOWLEDGE GAPS:
   What important topics haven't we covered yet?
   What areas of security do I seem less confident about?
   Where do my questions reveal blind spots?

4. STRENGTH PATTERNS:
   What am I consistently good at?
   What types of problems do I solve effectively?
   What's my natural approach to challenges?

5. GROWTH RECOMMENDATIONS:
   Based on my role, current skills, and the patterns you see, what should I focus on learning next?
   What would give me the biggest impact?
   Are there specific resources, certifications, or projects you'd recommend?

6. CONVERSATION PATTERNS:
   How has my use of AI evolved?
   Am I asking better questions over time?
   What could I do differently to get more value from our conversations?

Be honest and specific. Help me see patterns I might not notice myself. The goal is continuous improvement.''',
    },
    {
        'title': 'Lesson 24: Collaborative Problem-Solving Memory',
        'description': 'Work on complex problems across multiple sessions',
        'difficulty': 'advanced',
        'order': 24,
        'points': 30,
        'instructions': '''Complex problems take time to solve! 🧩

**What You'll Learn:**
- Multi-session problem-solving
- Tracking progress on complex issues
- Building solutions incrementally

**The Scenario:**
Some security problems can't be solved in one conversation. Break them into pieces and work on them over time.

**Your Challenge:**
Set up a complex, multi-faceted security problem and work on it piece by piece.

**The Approach:**
Session 1: Define the problem and break it into components
Session 2: Deep dive into component 1
Session 3: Deep dive into component 2
Session 4: Integrate solutions
Session 5: Create implementation plan

**Your Task:**
Create a comprehensive prompt that:
1. Introduces a complex security challenge
2. Asks Claude to break it into manageable pieces
3. Sets up for multi-session work
4. Defines what to tackle first
5. Asks Claude to remember the overall context

**Real-World:**
Real security projects are complex. You'll research, test, get feedback, adjust, and iterate. AI that remembers context makes this manageable!

**Example Problem:**
"Our company is planning to move from on-premises infrastructure to hybrid cloud, and we need to redesign our entire security architecture. This is a 6-month project with many components. Let's break this down and work on it piece by piece..."''',
        'example_prompt': '''I'm facing a complex security challenge that we'll need to work on across multiple conversations. Please remember the entire context and help me break this into manageable pieces.

THE CHALLENGE: Security Architecture Redesign for Cloud Migration

BACKGROUND:
- Company: Financial services firm, 300 employees, heavily regulated (FINRA, SOC 2)
- Current: 100% on-premises infrastructure, traditional perimeter security
- Goal: Migrate 60% of services to AWS over 12 months
- Must maintain security and compliance throughout migration
- Budget: $150K for new security tools/services
- Timeline: 12 months, must show progress quarterly

COMPLEXITY FACTORS:
- Legacy applications that can't move to cloud
- Hybrid environment for at least 2 years
- Compliance requirements don't change (must adapt to cloud)
- Team has limited cloud security experience
- Business can't tolerate downtime
- Need to maintain current security controls while adding new ones

COMPONENTS I SEE:
1. Identity and Access Management (IAM) strategy for hybrid environment
2. Network security redesign (micro-segmentation, zero-trust)
3. Data protection across cloud and on-prem
4. Monitoring and logging (SIEM in hybrid environment)
5. Compliance mapping (ensuring cloud controls meet requirements)
6. Incident response updates for cloud
7. Team training and skills development

MY QUESTIONS:
- Is this the right breakdown or am I missing components?
- What should we tackle first given dependencies?
- What are the biggest risks in a hybrid security model?

Let's work on this systematically. Today, help me refine this breakdown and identify the critical path. In future conversations, we'll deep dive into each component.

Remember all of this context - this is a 12-month journey we're starting.''',
    },
    {
        'title': 'Lesson 25: Memory-Enhanced Workflows',
        'description': 'Create repeatable workflows that leverage memory',
        'difficulty': 'advanced',
        'order': 25,
        'points': 35,
        'instructions': '''Build workflows that get smarter over time! ⚙️

**What You'll Learn:**
- Creating repeatable processes
- Workflows that improve with use
- Leveraging accumulated context

**The Concept:**
Set up workflows with Claude that remember your environment, preferences, and past results. Each time you run the workflow, it's smarter than before!

**Your Challenge:**
Create a repeatable workflow for a regular task (like weekly security reviews, incident triage, or vulnerability management).

**Your Task:**
Design a workflow prompt that:
1. Defines the recurring task
2. Documents your environment/context once
3. Specifies the process steps
4. Asks Claude to remember and refine over time
5. Includes feedback loops

**Example Workflow:**
"Weekly Security Review Protocol

Remember this workflow - I run it every Monday morning:

1. I'll provide this week's data:
   - Alert count by category
   - Incident count and severity
   - New vulnerabilities discovered
   - Patch status
   
2. You analyze and provide:
   - Week-over-week trends
   - Anomalies to investigate
   - Priorities for this week
   - Recommendations

3. Over time, learn:
   - What types of anomalies matter for our environment
   - Seasonal patterns in our alerts
   - What recommendations we actually implement
   - Our capacity constraints"

**Real-World:**
Many security tasks repeat weekly/monthly. Workflows that remember context save HOURS!

Build it once, improve it forever!''',
        'example_prompt': '''I want to establish a repeatable workflow for our Monday morning security review. Remember this entire process and help me execute it each week, getting better over time.

WORKFLOW: Weekly Security Review & Planning

CONTEXT TO REMEMBER:
- Team: 3 SOC analysts covering 24/7
- Environment: 200 endpoints, 50 servers, 15 cloud instances
- Tools: Splunk SIEM, CrowdStrike EDR, Nessus vulnerability scanner
- Coverage: Mon-Fri 7am-7pm in-house, overnight via monitoring service
- Priorities: Reduce MTTD, improve documentation, cross-train team

WEEKLY DATA I'LL PROVIDE:
1. Alert Statistics:
   - Total alerts generated
   - Breakdown by severity (Critical/High/Medium/Low)
   - Breakdown by category (malware, unauthorized access, policy violation, etc.)
   - False positive rate
   
2. Incident Summary:
   - Total incidents investigated
   - Incidents escalated
   - Average response time
   - Open incidents
   
3. Vulnerability Status:
   - New vulnerabilities discovered
   - Critical vulns patched
   - Critical vulns remaining
   - Patch compliance %
   
4. Operational Notes:
   - Tool issues or downtime
   - Team absences or training
   - Any major changes to environment

WHAT I NEED FROM YOU EACH WEEK:
1. TREND ANALYSIS:
   - Week-over-week changes
   - Notable increases/decreases
   - Patterns emerging
   
2. ANOMALY DETECTION:
   - What looks unusual for our baseline?
   - What needs investigation?
   
3. PRIORITY RECOMMENDATIONS:
   - Top 3 priorities for this week
   - Quick wins we can tackle
   - Long-term items to plan for
   
4. LEARNING INSIGHTS:
   - What's improving over time?
   - What's getting worse?
   - Suggested process changes

CONTINUOUS IMPROVEMENT:
- Remember what issues recur (so we can address root causes)
- Track which recommendations we implement vs ignore (understand constraints)
- Learn our normal patterns (so anomalies stand out)
- Note seasonal patterns (end of quarter, holidays, etc.)

THIS WEEK'S DATA (Example for first run):
Alerts: 847 total (up from 623 last week)
- Critical: 12, High: 89, Medium: 445, Low: 301
- Top categories: Failed logins (234), Malware detected (45), Policy violations (178)
- False positive rate: 32%

Incidents: 23 investigated, 4 escalated
- Avg response time: 45 minutes (target: 30 min)
- Open incidents: 2 (both low severity)

Vulnerabilities: 15 new, 8 critical patched, 3 critical remaining
- Patch compliance: 87%

Notes: New firewall rules deployed Tuesday, caused alert spike. One analyst on vacation.

Please analyze and provide your weekly review using the format above. Remember this entire workflow for future Mondays.''',
    },
]
