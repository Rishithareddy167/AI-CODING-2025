import unittest
from Task1 import is_valid_email

class CustomTestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("alice@example.com"))
        self.assertTrue(is_valid_email("bob.smith@domain.co"))
        self.assertTrue(is_valid_email("a_b-c.d@domain.com"))
        self.assertTrue(is_valid_email("user123@sub.domain.org"))

    def test_invalid_no_at(self):
        self.assertFalse(is_valid_email("alice.example.com"))
        self.assertFalse(is_valid_email("aliceexamplecom"))

    def test_invalid_no_dot(self):
        self.assertFalse(is_valid_email("alice@examplecom"))
        self.assertFalse(is_valid_email("alice@com"))

    def test_multiple_at(self):
        self.assertFalse(is_valid_email("alice@@example.com"))
        self.assertFalse(is_valid_email("alice@ex@ample.com"))

    def test_starts_or_ends_with_special(self):
        self.assertFalse(is_valid_email(".alice@example.com"))
        self.assertFalse(is_valid_email("alice.@example.com"))
        self.assertFalse(is_valid_email("-alice@example.com"))
        self.assertFalse(is_valid_email("alice-@example.com"))
        self.assertFalse(is_valid_email("_alice@example.com"))
        self.assertFalse(is_valid_email("alice_@example.com"))
        self.assertFalse(is_valid_email("alice@example.com."))
        self.assertFalse(is_valid_email("alice@example.com-"))
        self.assertFalse(is_valid_email("alice@example.com_"))

    def test_empty_and_invalid(self):
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email("@."))
        self.assertFalse(is_valid_email("alice@.com"))
        self.assertFalse(is_valid_email("alice@com."))

    def test_invalid_characters(self):
        self.assertFalse(is_valid_email("alice!@example.com"))
        self.assertFalse(is_valid_email("alice$@example.com"))
        self.assertFalse(is_valid_email("alice@exa#mple.com"))
        self.assertFalse(is_valid_email("ali ce@example.com"))

        def test_tld_too_short(self):
            self.assertFalse(is_valid_email("alice@example.c"))
            self.assertFalse(is_valid_email("bob@domain.x"))

        def test_subdomains(self):
            self.assertTrue(is_valid_email("user@sub.domain.com"))
            self.assertTrue(is_valid_email("user@a.b.c.domain.org"))

        def test_numeric_local_and_domain(self):
            self.assertTrue(is_valid_email("12345@67890.com"))
            self.assertTrue(is_valid_email("a1b2c3@1a2b3c.com"))

        def test_dot_and_dash_in_domain(self):
            self.assertTrue(is_valid_email("user@my-domain.com"))
            self.assertTrue(is_valid_email("user@my.domain.com"))
            self.assertFalse(is_valid_email("user@-domain.com"))
            self.assertFalse(is_valid_email("user@domain-.com"))
            self.assertFalse(is_valid_email("user@.domain.com"))
            self.assertFalse(is_valid_email("user@domain.com-"))

        def test_dot_and_dash_in_local(self):
            self.assertTrue(is_valid_email("a.b-c_d@domain.com"))
            self.assertFalse(is_valid_email(".abc@domain.com"))
            self.assertFalse(is_valid_email("abc.@domain.com"))
            self.assertFalse(is_valid_email("-abc@domain.com"))
            self.assertFalse(is_valid_email("abc-@domain.com"))
            self.assertFalse(is_valid_email("_abc@domain.com"))
            self.assertFalse(is_valid_email("abc_@domain.com"))

        def test_uppercase_emails(self):
            self.assertTrue(is_valid_email("USER@EXAMPLE.COM"))
            self.assertTrue(is_valid_email("User.Name@Domain.Co"))

if __name__ == "__main__":
    unittest.main()