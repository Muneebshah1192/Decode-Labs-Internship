# Project Report
## LogicBot — Rule-Based AI Chatbot

## 1. Introduction

LogicBot is a Python-based rule-based chatbot created for DecodeLabs Artificial Intelligence Project 1. The project focuses on explicit control flow instead of machine learning. The purpose is to prove that a chatbot can respond intelligently when a developer defines clean rules, conditions, and response patterns.

## 2. Objective

The objective is to create a chatbot that:

- accepts user input continuously
- sanitizes the input
- handles greetings
- handles exit commands
- uses if-else decision-making
- responds to predefined questions
- gives fallback replies for unknown questions

## 3. Requirement Mapping

| Requirement | Status | Implementation |
|---|---:|---|
| Handle greetings | Completed | `DIRECT_INTENTS`, `KEYWORD_INTENTS`, `RESPONSES` |
| Handle exit commands | Completed | `EXIT_COMMANDS` and clean `break` in loop |
| Use if-else logic | Completed | `generate_response()` and `detect_intent()` |
| Run in continuous loop | Completed | `while True` inside `run_chatbot()` |
| Predefined responses | Completed | `RESPONSES` dictionary |
| 5+ intents | Exceeded | 69 exact inputs and 27 keyword groups |
| Fallback response | Completed | `fallback` response list |
| Input sanitization | Completed | `sanitize_input()` |
| Clean project structure | Completed | Separate `src`, `tests`, `docs`, and `assets` folders |

## 4. System Flow

```text
Raw Input
   ↓
Input Sanitization
   ↓
Empty / Exit / Memory / Utility Checks
   ↓
Exact Dictionary Match
   ↓
Keyword Intent Match
   ↓
Fallback Response
   ↓
Output
```

## 5. Main Features

### Greeting Handling

The chatbot responds to common greetings such as:

```text
hello, hi, hey, salam, good morning
```

### Exit Commands

The chatbot exits safely when the user enters:

```text
exit, quit, bye, goodbye, stop, close, end
```

### DecodeLabs Questions

The chatbot can answer questions about:

- DecodeLabs training kit
- AI internship foundation phase
- Project 1 overview
- project requirements
- skills learned
- contact details from the project kit
- certificate and fee safety guidance

### AI Concept Questions

The chatbot includes rule-based answers about:

- Artificial Intelligence
- chatbot basics
- rule-based AI
- input sanitization
- dictionary lookup
- IPO model
- white-box AI
- AI guardrails
- fallback design

### Human-Like Session Memory

The bot can store the user's name during the session.

Example:

```text
User: my name is Muneeb
LogicBot: Nice to meet you, Muneeb. I’ll remember your name during this session.
```

### Trace Command

The `trace` command explains how the previous answer was selected. This supports the white-box concept because the response path is visible.

Example:

```text
User: trace
LogicBot: Last response came from: exact dictionary match: project_overview.
```

### Stats Command

The `stats` command shows the chatbot's current session and knowledge-base size.

## 6. Why Dictionary Lookup Was Used

A long `if-elif` ladder becomes difficult to maintain when more rules are added. A dictionary keeps the chatbot cleaner because exact user questions can be mapped directly to intent names.

This version uses both:

- exact dictionary matching
- keyword-based rule matching

That makes the bot more flexible while staying fully rule-based.

## 7. Safety and Honesty

The bot does not guess about fee or certificate payment details. If the information is not confirmed inside the project kit, it tells the user to verify through official DecodeLabs contact channels. This is better than giving unsupported claims.

## 8. Testing

The project includes unit tests for:

- sanitization
- name extraction
- greeting
- Project 1 response
- DecodeLabs response
- certificate fee safety answer
- exit command
- memory
- trace
- fallback

Run tests with:

```bash
python -m unittest discover tests
```

## 9. Limitations

This chatbot is not a machine-learning chatbot. It cannot understand every possible sentence. Its answers depend on predefined rules and keyword groups. This limitation is expected because Project 1 focuses on rule-based AI foundations.

## 10. Future Improvements

Possible improvements:

- GUI interface
- web version using Flask
- Urdu/Hindi language support
- voice input/output
- JSON-based knowledge base
- admin panel to add new intents
- optional LLM fallback after rule matching

## 11. Conclusion

LogicBot completes the core requirements of DecodeLabs AI Project 1 and adds professional improvements such as a larger question bank, session memory, traceability, tests, sample output, and documentation. The result is a clean, explainable, and submission-ready rule-based AI chatbot.
