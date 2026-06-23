# DecodeLabs AI Project 1
## LogicBot — Rule-Based AI Chatbot

**Internship Track:** Artificial Intelligence  
**Training Kit:** DecodeLabs Industrial Training Kit, Batch 2026  
**Project:** Project 1 — Rule-Based AI Chatbot  
**Language:** Python 3  
**Developer:** Muneeb Haider

---

## Project Overview

LogicBot is a rule-based AI chatbot built in Python. It answers predefined user questions through clean control flow, dictionary lookup, keyword matching, and fallback handling.

The chatbot follows this flow:

```text
User Input → Sanitization → Rule Matching → Response Selection → Output
```

The project is intentionally deterministic. Every answer comes from a visible rule, which makes the bot easy to understand, debug, test, and explain during internship verification.

---

## What Makes This Version Stronger

This is not only a basic `if-else` chatbot. It has a more professional structure while still staying inside the Project 1 rule-based requirement.

- 69 exact question patterns
- 27 keyword intent groups
- DecodeLabs-related questions and answers
- AI, chatbot, rule-based AI, IPO model, white-box AI, guardrails, and submission guidance
- Greeting and exit command handling
- Input sanitization for case, punctuation, and extra spaces
- Human-like response variations
- Fallback response for unknown questions
- Session memory for user name
- Trace command to explain why the bot answered
- Stats command to show chatbot knowledge size
- Chat history logging
- Unit tests
- Project report and submission checklist

---

## Folder Structure

```text
decodelabs_ai_project1_rule_based_chatbot/
│
├── main.py
├── requirements.txt
├── run_chatbot.bat
├── run_chatbot.sh
├── README.md
│
├── src/
│   ├── chatbot.py
│   ├── intents.py
│   └── utils.py
│
├── tests/
│   └── test_chatbot.py
│
├── docs/
│   ├── project_report.md
│   ├── question_bank.md
│   └── submission_checklist.md
│
└── assets/
    └── sample_output.txt
```

---

## How to Run

### Windows

Open the project folder in Command Prompt and run:

```bash
python main.py
```

Or double-click:

```text
run_chatbot.bat
```

### Linux / macOS

```bash
python3 main.py
```

Or:

```bash
chmod +x run_chatbot.sh
./run_chatbot.sh
```

No external packages are required.

---

## Best Demo Questions

Use these questions for screenshots or project verification:

```text
hello
what is project 1
requirements
what is DecodeLabs
what is sanitization
why use dictionary
what is white box AI
certificate fee
submission tips
how to get recommendation
my name is Muneeb
what is my name
trace
stats
exit
```

---

## Example Output

```text
You: what is project 1
LogicBot: Project 1 is a Rule-Based AI Chatbot. It is a foundation task where the bot responds to predefined inputs using control flow and logic.

You: requirements
LogicBot: The core requirements are: handle greetings, handle exit commands, use if-else logic, and run in a continuous loop.

You: certificate fee
LogicBot: I should not guess about certificate payment. This project kit does not clearly say whether the certificate has a separate fee, so the safest step is to confirm through DecodeLabs’ official contact.

You: trace
LogicBot: Last response came from: keyword rule match: certificate_fee. That is why this bot is easy to inspect.
```

---

## How the Bot Works

### 1. Sanitization

The bot first cleans input:

```text
"  HELLO!!! " → "hello"
```

This makes matching more reliable.

### 2. If-Else Decision Flow

The chatbot checks important cases first:

```text
empty input → exit command → name memory → trace/stats → time/date → intent matching → fallback
```

### 3. Dictionary Matching

Exact inputs are matched through `DIRECT_INTENTS`.

### 4. Keyword Matching

If an exact input is not found, the bot searches keyword groups in `KEYWORD_INTENTS`.

### 5. Fallback

If no rule matches, the bot gives a helpful default response instead of crashing.

---

## Testing

Run:

```bash
python -m unittest discover tests
```

The tests check:

- input sanitization
- name extraction
- greeting handling
- Project 1 answer
- DecodeLabs answer
- safe certificate fee answer
- exit command
- name memory
- trace response
- fallback response

---

## Final Submission Suggestion

For a strong internship submission, attach:

1. Project ZIP file
2. Screenshot of chatbot welcome screen
3. Screenshot showing Project 1 and DecodeLabs questions
4. Screenshot showing fallback and exit command
5. Screenshot of test result
6. README.md
7. Project report

This makes the work look complete, understandable, and professionally prepared.
