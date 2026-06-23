from __future__ import annotations

import random
import re
import string
from datetime import datetime


def sanitize_input(raw_text: str) -> str:
    text = raw_text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text)
    return text


def choose_response(options: list[str], **values: str) -> str:
    return random.choice(options).format(**values)


def extract_name(clean_text: str) -> str | None:
    patterns = (
        r"^my name is ([a-zA-Z ]{2,30})$",
        r"^i am ([a-zA-Z ]{2,30})$",
        r"^im ([a-zA-Z ]{2,30})$",
        r"^call me ([a-zA-Z ]{2,30})$",
    )

    blocked_words = {
        "ai", "chatbot", "student", "intern", "developer", "fine", "good", "okay", "here"
    }

    for pattern in patterns:
        match = re.match(pattern, clean_text)
        if not match:
            continue

        name = match.group(1).strip()
        words = name.split()
        if 1 <= len(words) <= 3 and not any(word in blocked_words for word in words):
            return name.title()

    return None


def get_time_message() -> str:
    now = datetime.now()
    return f"Current system time is {now.strftime('%I:%M %p')} on {now.strftime('%d %B %Y')}."


def log_message(file_path: str, speaker: str, message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {speaker}: {message}\n")
