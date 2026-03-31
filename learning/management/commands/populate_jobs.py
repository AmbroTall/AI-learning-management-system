"""
Management command to seed AI job postings across all LearnPulse modules.

Usage:
    python manage.py populate_jobs
"""

from django.core.management.base import BaseCommand
from learning.models import JobPosting, Module


# module_key → lookup hint (matches title substring, case-insensitive)
MODULE_KEYS = {
    'prompt':   'Prompt Engineering',
    'tools':    'AI Tools',
    'agents':   'AI Agents',
    'coding':   'Coding',
    'cyber':    'Cybersecurity',
    'chat':     'Chat',
    'builder':  'Build AI',
    'data':     'Data',
}

JOBS = [
    # ── Module: Prompt Engineering ──────────────────────────────────────────
    {
        'title': 'Data Annotation Specialist',
        'icon_emoji': '🏷️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Label, classify, and annotate text, image, and audio datasets used to train large '
            'language models and computer vision systems. Your work directly shapes how AI models '
            'understand the world — accuracy and consistency are paramount.\n\n'
            '⚡ Demand for annotators is surging as model releases accelerate. Positions fill within '
            'days of opening. Certified candidates are placed 3× faster than uncertified applicants.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 15,
        'pay_max': 22,
        'pay_period': 'hour',
        'pay_note': 'Flexible hours',
        'tags': ['Text Labeling', 'Image Classification', 'Quality Control', 'Attention to Detail'],
        'spots_available': 20,
        'order': 1,
        'module_key': 'prompt',
    },
    {
        'title': 'RLHF Feedback Specialist',
        'icon_emoji': '🧠',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Provide structured human feedback to train AI models via Reinforcement Learning from '
            'Human Feedback (RLHF). You\'ll rank AI-generated responses, identify failure modes, '
            'and write preference annotations that guide model alignment and helpfulness.\n\n'
            '🔥 RLHF roles are among the highest-demand positions in AI right now. Multiple top labs '
            'compete for certified talent — don\'t leave this opportunity for someone else.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 18,
        'pay_max': 28,
        'pay_period': 'hour',
        'pay_note': 'Part-time friendly',
        'tags': ['RLHF', 'Preference Ranking', 'Response Evaluation', 'Critical Thinking'],
        'spots_available': 15,
        'order': 2,
        'module_key': 'prompt',
    },
    {
        'title': 'Prompt Engineer',
        'icon_emoji': '✍️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Design, test, and iterate on prompts that elicit high-quality, reliable outputs from '
            'large language models. You\'ll build prompt libraries, document best practices, and '
            'work closely with the model evaluation team to close capability gaps.\n\n'
            '📈 Prompt engineering is now listed as a top-10 in-demand skill by LinkedIn. Certified '
            'engineers are earning $25–$40/hr fully remote. This batch of positions closes once filled.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 25,
        'pay_max': 40,
        'pay_period': 'hour',
        'pay_note': 'Full-time',
        'tags': ['Prompt Design', 'LLM Evaluation', 'Chain-of-Thought', 'Technical Writing'],
        'spots_available': 8,
        'order': 3,
        'module_key': 'prompt',
    },
    {
        'title': 'AI Content Evaluator',
        'icon_emoji': '📋',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Assess AI-generated content for accuracy, safety, helpfulness, and alignment with '
            'guidelines. You\'ll apply structured rubrics to evaluate model outputs across diverse '
            'domains including factual QA, creative writing, coding, and reasoning tasks.\n\n'
            '⏳ This role posts weekly — but spots fill within 48 hours of each posting. Evaluation '
            'roles are the gateway to senior AI quality positions. Apply before Monday\'s reset.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 16,
        'pay_max': 26,
        'pay_period': 'hour',
        'pay_note': 'Flexible schedule',
        'tags': ['Content Review', 'Safety Evaluation', 'Rubric Scoring', 'Multi-domain'],
        'spots_available': 12,
        'order': 4,
        'module_key': 'prompt',
    },
    {
        'title': 'LLM Tester & Red-teamer',
        'icon_emoji': '🛡️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Proactively probe AI systems to identify vulnerabilities, harmful outputs, jailbreaks, '
            'and edge-case failures. You\'ll document adversarial prompts, reproduce issues '
            'reliably, and collaborate with alignment teams to patch discovered weaknesses.\n\n'
            '🚨 Only 5 spots available. Red-teaming is a senior-track role and slots are almost never '
            'reopened once filled. Certified candidates who apply this week will be reviewed first.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 28,
        'pay_max': 40,
        'pay_period': 'hour',
        'pay_note': 'Senior track',
        'tags': ['Red-teaming', 'Adversarial Prompting', 'AI Safety', 'Bug Reporting'],
        'spots_available': 5,
        'order': 5,
        'module_key': 'prompt',
    },
    {
        'title': 'AI Conversation Quality Analyst',
        'icon_emoji': '💬',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Review and score AI chatbot conversations for quality, tone, factual accuracy, and '
            'user satisfaction. You\'ll flag edge cases, write improvement annotations, and help '
            'shape how the next generation of conversational AI behaves.\n\n'
            '🔔 New batch of positions opens every Monday. Last week\'s openings filled in under '
            '72 hours — get your certificate ready and be first in queue.'
        ),
        'job_type': 'remote',
        'contract_type': 'part_time',
        'pay_min': 14,
        'pay_max': 20,
        'pay_period': 'hour',
        'pay_note': '10–20 hrs/week',
        'tags': ['Conversation Review', 'Quality Assurance', 'NLP', 'User Experience'],
        'spots_available': 18,
        'order': 6,
        'module_key': 'prompt',
    },

    # ── Module: AI Tools & Platform Features ────────────────────────────────
    {
        'title': 'AI Tools Integration Consultant',
        'icon_emoji': '🔧',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Help businesses identify, evaluate, and integrate AI productivity tools into their '
            'workflows. You\'ll audit existing processes, recommend AI solutions, and onboard '
            'teams onto platforms like Claude, ChatGPT, Notion AI, and Copilot.\n\n'
            '📊 72% of companies plan to adopt AI tools in the next 12 months — but less than '
            '15% have certified staff to lead the rollout. This is your career accelerant.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 22,
        'pay_max': 38,
        'pay_period': 'hour',
        'pay_note': 'Project-based',
        'tags': ['AI Tools', 'Business Integration', 'Workflow Automation', 'Consulting'],
        'spots_available': 10,
        'order': 10,
        'module_key': 'tools',
    },
    {
        'title': 'AI Platform Trainer',
        'icon_emoji': '📚',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Deliver training sessions and create learning materials that help non-technical '
            'teams adopt AI platforms confidently. You\'ll design workshops, write guides, '
            'and track adoption metrics to demonstrate ROI.\n\n'
            '🎯 Corporate AI training budgets have tripled in 2025. Certified trainers are booked '
            'solid — the pipeline is full but the talent supply is critically short.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 20,
        'pay_max': 32,
        'pay_period': 'hour',
        'pay_note': 'Full-time',
        'tags': ['Training Delivery', 'Curriculum Design', 'AI Adoption', 'Communication'],
        'spots_available': 7,
        'order': 11,
        'module_key': 'tools',
    },
    {
        'title': 'AI Productivity Specialist',
        'icon_emoji': '⚡',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Embed AI tools into day-to-day operations for client organisations — from automated '
            'drafting and summarisation to meeting intelligence and task management. Measure, '
            'report, and optimise AI productivity gains.\n\n'
            '⏰ This role type didn\'t exist 18 months ago. Companies are now racing to hire. '
            'The first certified cohort of specialists is getting offers within 2 weeks of applying.'
        ),
        'job_type': 'hybrid',
        'contract_type': 'full_time',
        'pay_min': 2800,
        'pay_max': 4200,
        'pay_period': 'month',
        'pay_note': 'Full-time',
        'tags': ['AI Tools', 'Productivity', 'Process Improvement', 'Automation'],
        'spots_available': 6,
        'order': 12,
        'module_key': 'tools',
    },

    # ── Module: AI Agents & Automation ─────────────────────────────────────
    {
        'title': 'AI Automation Workflow Designer',
        'icon_emoji': '🤖',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Design and deploy end-to-end AI automation workflows using agents, APIs, and '
            'no-code/low-code platforms. You\'ll map manual processes, identify automation '
            'opportunities, and build self-running pipelines that save hours per week.\n\n'
            '🌊 The automation wave is here — and every business needs someone who can ride it. '
            'Certified automation designers have a 91% placement rate. Spots are allocated weekly.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 26,
        'pay_max': 42,
        'pay_period': 'hour',
        'pay_note': 'Project-based',
        'tags': ['AI Agents', 'Workflow Automation', 'API Integration', 'Process Design'],
        'spots_available': 9,
        'order': 20,
        'module_key': 'agents',
    },
    {
        'title': 'AI Agent QA Tester',
        'icon_emoji': '🔍',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Validate and quality-test AI agent systems — autonomous pipelines that browse the web, '
            'write code, and make decisions. You\'ll design test scenarios, document failure modes, '
            'and ensure agent behaviour meets safety and accuracy standards.\n\n'
            '🚀 Agentic AI is the fastest-growing area in tech. QA testers for agents earn premium '
            'rates because the skill is rare. Be among the first certified cohort — spots are limited.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 24,
        'pay_max': 38,
        'pay_period': 'hour',
        'pay_note': 'Flexible',
        'tags': ['Agent Testing', 'QA', 'Autonomous Systems', 'Safety Evaluation'],
        'spots_available': 8,
        'order': 21,
        'module_key': 'agents',
    },
    {
        'title': 'Intelligent Process Automation Specialist',
        'icon_emoji': '⚙️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Combine traditional RPA with AI agents to build smarter automation solutions. '
            'You\'ll analyse repetitive business tasks, implement AI-enhanced pipelines, '
            'and maintain reliability at scale.\n\n'
            '💼 IPA specialists are replacing $80K/year consulting engagements with leaner, '
            'certified in-house talent. Companies are paying premium for certified staff now '
            'rather than waiting — this window won\'t stay open.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 3200,
        'pay_max': 5000,
        'pay_period': 'month',
        'pay_note': 'Full-time',
        'tags': ['RPA', 'AI Agents', 'Process Automation', 'Integration'],
        'spots_available': 5,
        'order': 22,
        'module_key': 'agents',
    },

    # ── Module: Coding with AI ───────────────────────────────────────────────
    {
        'title': 'AI-Assisted Software Developer',
        'icon_emoji': '💻',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Build production-ready software features using AI pair-programming tools. '
            'You\'ll leverage tools like GitHub Copilot, Claude Code, and Cursor to ship '
            'faster, write cleaner code, and review AI-generated pull requests.\n\n'
            '📉 Traditional dev hiring is slowing. AI-assisted dev hiring is accelerating. '
            'Developers certified in AI-enhanced workflows earn 30% more than peers. '
            'This cohort starts immediately upon placement.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 30,
        'pay_max': 55,
        'pay_period': 'hour',
        'pay_note': 'Full-time',
        'tags': ['Python', 'AI Pair Programming', 'GitHub Copilot', 'Code Review'],
        'spots_available': 12,
        'order': 30,
        'module_key': 'coding',
    },
    {
        'title': 'Junior AI Developer',
        'icon_emoji': '🌱',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Entry-level developer role for certified graduates — work on real AI-powered '
            'applications alongside senior engineers. You\'ll build features, fix bugs, '
            'write tests, and learn production AI development on the job.\n\n'
            '🎓 This role was created specifically for LearnPulse graduates. No experience '
            'required beyond your certification — it\'s your guaranteed pathway in. '
            '14 people applied last week alone. Apply before spots are gone.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 18,
        'pay_max': 28,
        'pay_period': 'hour',
        'pay_note': 'Entry-level',
        'tags': ['Python', 'Django', 'AI Integration', 'Beginner-Friendly'],
        'spots_available': 10,
        'order': 31,
        'module_key': 'coding',
    },
    {
        'title': 'AI Code Review Specialist',
        'icon_emoji': '🔎',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Review AI-generated code for correctness, security, and maintainability. '
            'You\'ll audit Copilot/Claude outputs, flag hallucinations, document patterns '
            'of failure, and help teams build safer AI-assisted development practices.\n\n'
            '🔒 As companies ship more AI-written code, review specialists are becoming '
            'compliance requirements — not optional. Certified reviewers are already '
            'being hired before job ads even go public. This listing closes Friday.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 25,
        'pay_max': 40,
        'pay_period': 'hour',
        'pay_note': 'Flexible',
        'tags': ['Code Review', 'AI Safety', 'Security Audit', 'Python', 'Quality'],
        'spots_available': 7,
        'order': 32,
        'module_key': 'coding',
    },

    # ── Module: Cybersecurity with AI ────────────────────────────────────────
    {
        'title': 'AI Threat Intelligence Analyst',
        'icon_emoji': '🔐',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Use AI tools to monitor, analyse, and respond to cybersecurity threats. '
            'You\'ll build threat intelligence pipelines, investigate anomalies flagged '
            'by AI systems, and produce actionable security reports for clients.\n\n'
            '🚨 AI-augmented cyber attacks are rising sharply — and defenders who understand '
            'both AI and security are the most valuable people in the industry. '
            'Certified analysts are receiving offers within days. 4 spots left this week.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 35,
        'pay_max': 55,
        'pay_period': 'hour',
        'pay_note': 'Senior',
        'tags': ['Threat Intelligence', 'AI Security', 'SIEM', 'Incident Response'],
        'spots_available': 4,
        'order': 40,
        'module_key': 'cyber',
    },
    {
        'title': 'AI Security Audit Specialist',
        'icon_emoji': '🛡️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Audit AI systems and LLM deployments for security vulnerabilities, data leakage '
            'risks, and compliance gaps. You\'ll write audit reports, recommend mitigations, '
            'and help organisations deploy AI safely.\n\n'
            '📜 New AI security regulations mean every enterprise deploying AI needs certified '
            'auditors. The supply of certified specialists is less than 10% of demand. '
            'Apply now — compliance deadlines are driving urgent hiring.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 30,
        'pay_max': 50,
        'pay_period': 'hour',
        'pay_note': 'Project-based',
        'tags': ['Security Audit', 'LLM Security', 'Compliance', 'Risk Assessment'],
        'spots_available': 6,
        'order': 41,
        'module_key': 'cyber',
    },
    {
        'title': 'Cybersecurity Automation Engineer',
        'icon_emoji': '⚔️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Build and maintain AI-driven cybersecurity automation — from automated phishing '
            'detection to intelligent SOAR playbooks. You\'ll integrate AI models into security '
            'operations centres and reduce mean-time-to-respond.\n\n'
            '💡 SOC automation is the #1 budget priority for CISOs in 2026. Engineers who '
            'hold both cybersecurity and AI certifications command a double premium. '
            'This is one of only 8 openings this quarter.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 4000,
        'pay_max': 6500,
        'pay_period': 'month',
        'pay_note': 'Full-time',
        'tags': ['Security Automation', 'SOAR', 'AI Integration', 'Python', 'Incident Response'],
        'spots_available': 8,
        'order': 42,
        'module_key': 'cyber',
    },

    # ── Module: AI Chat Mastery (legacy modules) ─────────────────────────────
    {
        'title': 'AI Chatbot Dialogue Writer',
        'icon_emoji': '🗨️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Write, edit, and improve dialogue scripts for AI chatbots and virtual assistants. '
            'You\'ll craft natural, on-brand conversations, handle edge cases, and use AI tools '
            'to rapidly iterate on dialogue trees.\n\n'
            '✨ Every brand now needs a chatbot. Dialogue writers who also understand AI are '
            'the missing link — and they\'re being hired at premium rates to fill the gap. '
            'Applications reviewed within 24 hours.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 16,
        'pay_max': 28,
        'pay_period': 'hour',
        'pay_note': 'Flexible',
        'tags': ['Dialogue Writing', 'Chatbot Design', 'UX Writing', 'NLP'],
        'spots_available': 14,
        'order': 50,
        'module_key': 'chat',
    },

    # ── Module: Build AI-Powered Tools ──────────────────────────────────────
    {
        'title': 'AI Product Builder',
        'icon_emoji': '🏗️',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Use AI APIs (Claude, OpenAI, Gemini) to build lightweight SaaS tools and internal '
            'productivity apps. You\'ll go from idea to deployed product, owning the full stack '
            'with AI at the core of every feature.\n\n'
            '🚀 The barrier to shipping AI products has never been lower — but the people who '
            'can actually do it are rare. Certified builders are co-founders, employees, and '
            'consultants. 9 teams are waiting for someone with your skills.'
        ),
        'job_type': 'remote',
        'contract_type': 'contract',
        'pay_min': 28,
        'pay_max': 50,
        'pay_period': 'hour',
        'pay_note': 'Project-based',
        'tags': ['Claude API', 'Product Development', 'Full-Stack', 'AI Integration'],
        'spots_available': 9,
        'order': 60,
        'module_key': 'builder',
    },

    # ── Module: AI + Data Magic ──────────────────────────────────────────────
    {
        'title': 'AI Data Insights Analyst',
        'icon_emoji': '📊',
        'organisation_name': 'LearnPulse · AI Training Division',
        'description': (
            'Use AI tools to extract, clean, analyse, and visualise data for business decisions. '
            'You\'ll build automated reporting pipelines, produce executive summaries using AI, '
            'and turn raw data into clear narratives stakeholders can act on.\n\n'
            '📈 Data roles augmented by AI are replacing purely manual analyst positions. '
            'Companies want analysts who can work 5× faster with AI tools. '
            'This cohort\'s intake closes at end of month — 11 spots remaining.'
        ),
        'job_type': 'remote',
        'contract_type': 'full_time',
        'pay_min': 2500,
        'pay_max': 4000,
        'pay_period': 'month',
        'pay_note': 'Full-time',
        'tags': ['Data Analysis', 'AI Tools', 'Python', 'Visualisation', 'Reporting'],
        'spots_available': 11,
        'order': 70,
        'module_key': 'data',
    },
]


def _find_module(key):
    """Try to find a Module whose title contains a hint substring (case-insensitive)."""
    hint = MODULE_KEYS.get(key, '')
    if hint:
        return Module.objects.filter(title__icontains=hint, is_active=True).first()
    return None


class Command(BaseCommand):
    help = 'Seed comprehensive AI job postings across all LearnPulse modules (safe to re-run)'

    def handle(self, *args, **options):
        created = 0
        skipped = 0

        for job_data in JOBS:
            module_key = job_data.pop('module_key', None)

            if JobPosting.objects.filter(title=job_data['title']).exists():
                self.stdout.write(f'  Skip (exists): {job_data["title"]}')
                if module_key:
                    job_data['module_key'] = module_key
                skipped += 1
                continue

            tags = job_data.pop('tags')
            job = JobPosting.objects.create(**job_data, tags=tags)

            mod = _find_module(module_key) if module_key else None
            if mod:
                job.required_modules.add(mod)
                self.stdout.write(self.style.SUCCESS(f'  Created: {job.title} (requires: {mod.title})'))
            else:
                self.stdout.write(self.style.WARNING(f'  Created: {job.title} (no module matched for key={module_key})'))

            created += 1

            # restore for any hypothetical re-use
            job_data['tags'] = tags
            if module_key:
                job_data['module_key'] = module_key

        self.stdout.write(
            self.style.SUCCESS(f'\nDone — {created} created, {skipped} skipped.')
        )
