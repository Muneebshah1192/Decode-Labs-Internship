from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from chatbot import RuleBasedChatbot
from utils import extract_name, sanitize_input


class TestRuleBasedChatbot(unittest.TestCase):
    def test_sanitize_input(self) -> None:
        self.assertEqual(sanitize_input("  Hello!!!  "), "hello")
        self.assertEqual(sanitize_input("What   is   AI?"), "what is ai")

    def test_name_extraction(self) -> None:
        self.assertEqual(extract_name("my name is muneeb"), "Muneeb")
        self.assertEqual(extract_name("call me ali raza"), "Ali Raza")
        self.assertIsNone(extract_name("this is not a name sentence"))

    def test_greeting(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        response, should_exit = bot.generate_response("Hello")
        self.assertFalse(should_exit)
        self.assertGreater(len(response), 10)

    def test_project_answer(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        response, should_exit = bot.generate_response("What is Project 1?")
        self.assertFalse(should_exit)
        self.assertTrue("Rule-Based" in response or "chatbot" in response.lower())

    def test_decodelabs_answer(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        response, should_exit = bot.generate_response("What is DecodeLabs?")
        self.assertFalse(should_exit)
        self.assertIn("DecodeLabs", response)

    def test_certificate_fee_safe_answer(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        response, should_exit = bot.generate_response("Do I have to pay for certificate?")
        self.assertFalse(should_exit)
        self.assertTrue("confirm" in response.lower() or "verify" in response.lower())

    def test_exit_command(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        response, should_exit = bot.generate_response("bye")
        self.assertTrue(should_exit)
        self.assertGreater(len(response), 5)

    def test_name_memory(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        bot.generate_response("my name is muneeb")
        response, should_exit = bot.generate_response("what is my name")
        self.assertFalse(should_exit)
        self.assertIn("Muneeb", response)

    def test_trace(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        bot.generate_response("requirements")
        response, should_exit = bot.generate_response("trace")
        self.assertFalse(should_exit)
        self.assertIn("Last response came from", response)

    def test_fallback(self) -> None:
        bot = RuleBasedChatbot(enable_logging=False)
        response, should_exit = bot.generate_response("random unknown question xyz")
        self.assertFalse(should_exit)
        self.assertGreater(len(response), 10)


if __name__ == "__main__":
    unittest.main()
