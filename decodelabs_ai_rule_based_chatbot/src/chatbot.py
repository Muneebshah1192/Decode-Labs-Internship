from __future__ import annotations

import argparse
from pathlib import Path

from intents import BOT_NAME, DIRECT_INTENTS, EXIT_COMMANDS, KEYWORD_INTENTS, RESPONSES
from utils import choose_response, extract_name, get_time_message, log_message, sanitize_input

HISTORY_FILE = Path(__file__).resolve().parent.parent / "chat_history.txt"


class RuleBasedChatbot:
    def __init__(self, enable_logging: bool = True) -> None:
        self.enable_logging = enable_logging
        self.user_name: str | None = None
        self.message_count = 0
        self.last_trace: dict[str, str] | None = None

    def detect_intent(self, clean_input: str) -> tuple[str, str]:
        exact_intent = DIRECT_INTENTS.get(clean_input)

        if exact_intent:
            return exact_intent, "exact dictionary match"
        else:
            for intent, keywords in KEYWORD_INTENTS.items():
                if any(keyword in clean_input for keyword in keywords):
                    return intent, "keyword rule match"

        return "fallback", "fallback rule"

    def generate_response(self, raw_input: str) -> tuple[str, bool]:
        clean_input = sanitize_input(raw_input)
        self.message_count += 1
        self._log("User", raw_input)

        if clean_input == "":
            return self._reply("Please type something so I can respond.", "empty input", False)

        if clean_input in EXIT_COMMANDS:
            return self._reply(choose_response(RESPONSES["goodbye"]), "exit command", True)

        detected_name = extract_name(clean_input)
        if detected_name:
            self.user_name = detected_name
            text = choose_response(RESPONSES["name_saved"], name=detected_name)
            return self._reply(text, "name memory rule", False)

        if clean_input in {"what is my name", "do you know my name", "tell my name"}:
            if self.user_name:
                text = choose_response(RESPONSES["user_name"], name=self.user_name)
            else:
                text = choose_response(RESPONSES["no_name"])
            return self._reply(text, "session memory check", False)

        if clean_input in {"clear my name", "forget my name"}:
            self.user_name = None
            return self._reply(choose_response(RESPONSES["name_cleared"]), "clear memory rule", False)

        if clean_input in {"trace", "why this answer"}:
            return self._reply(self._trace_message(), "trace request", False, save_trace=False)

        if clean_input == "stats":
            text = self._stats_message()
            return self._reply(text, "stats rule", False)

        if "time" in clean_input or "date" in clean_input or clean_input == "today":
            return self._reply(get_time_message(), "time/date utility rule", False)

        intent, method = self.detect_intent(clean_input)
        text = choose_response(RESPONSES.get(intent, RESPONSES["fallback"]))
        return self._reply(text, f"{method}: {intent}", False)

    def _reply(self, text: str, trace: str, should_exit: bool, save_trace: bool = True) -> tuple[str, bool]:
        if save_trace:
            self.last_trace = {"method": trace, "bot": text}
        self._log(BOT_NAME, text)
        return text, should_exit

    def _trace_message(self) -> str:
        if not self.last_trace:
            return choose_response(RESPONSES["trace_empty"])
        return f"Last response came from: {self.last_trace['method']}. That is why this bot is easy to inspect."

    def _stats_message(self) -> str:
        known_inputs = len(DIRECT_INTENTS)
        keyword_groups = len(KEYWORD_INTENTS)
        saved_name = self.user_name if self.user_name else "not set"
        return (
            f"Session stats: {self.message_count} user messages, {known_inputs} exact inputs, "
            f"{keyword_groups} keyword groups, saved name: {saved_name}."
        )

    def _log(self, speaker: str, message: str) -> None:
        if self.enable_logging:
            log_message(str(HISTORY_FILE), speaker, message)


def print_welcome() -> None:
    print("=" * 72)
    print("🤖 LogicBot | DecodeLabs AI Project 1 | Rule-Based AI Chatbot")
    print("=" * 72)
    print("Ask about AI, Project 1, DecodeLabs, requirements, certificate fee, or submission tips.")
    print("Type 'help' for examples. Type 'exit' or 'bye' to close.")
    print("-" * 72)


def run_chatbot(enable_logging: bool = True) -> None:
    bot = RuleBasedChatbot(enable_logging=enable_logging)
    print_welcome()

    while True:
        try:
            user_input = input("You: ")
            response, should_exit = bot.generate_response(user_input)
            print(f"{BOT_NAME}: {response}")
            if should_exit:
                break
        except KeyboardInterrupt:
            print(f"\n{BOT_NAME}: Session stopped safely. Goodbye!")
            break


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DecodeLabs Project 1 Rule-Based Chatbot")
    parser.add_argument("--no-log", action="store_true", help="Run without saving chat history")
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    run_chatbot(enable_logging=not args.no_log)
