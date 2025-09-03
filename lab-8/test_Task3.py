import unittest
from Task3 import is_sentence_palindrome

class TestIsSentencePalindromeExternal(unittest.TestCase):
    def test_true_palindromes(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("Madam, in Eden, I'm Adam"))
        self.assertTrue(is_sentence_palindrome("Able was I, I saw Elba"))
        self.assertTrue(is_sentence_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_sentence_palindrome("Red roses run no risk, sir, on Nurse's order."))

    def test_false_palindromes(self):
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))
        self.assertFalse(is_sentence_palindrome("Hello, world!"))
        self.assertFalse(is_sentence_palindrome("Palindrome test sentence"))

    def test_edge_cases(self):
        self.assertTrue(is_sentence_palindrome(""))
        self.assertTrue(is_sentence_palindrome("!@#$%^&*()"))  # Only punctuation
        self.assertTrue(is_sentence_palindrome("A"))           # Single character
        self.assertTrue(is_sentence_palindrome("  "))          # Only spaces

    def test_mixed_cases(self):
        self.assertTrue(is_sentence_palindrome("RaceCar"))
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertFalse(is_sentence_palindrome("12345"))
        self.assertTrue(is_sentence_palindrome("1a2b2a1"))
        self.assertFalse(is_sentence_palindrome("1a2b3a1"))

if __name__ == "__main__":
    unittest.main()