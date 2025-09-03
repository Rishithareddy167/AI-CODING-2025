import unittest
import re

def is_valid_email(email):
    # Check for exactly one '@'
    if email.count('@') != 1:
        return False
    
    local, domain = email.split('@')

    # Must not be empty
    if not local or not domain:
        return False
    
    # Must not start or end with special characters
    if not local[0].isalnum() or not local[-1].isalnum():
        return False
    if not domain[0].isalnum() or not domain[-1].isalnum():
        return False

    # Domain must contain at least one dot, and TLD >= 2 chars
    if '.' not in domain:
        return False
    if len(domain.split('.')[-1]) < 2:
        return False

    # Allowed characters (alphanumeric, ., _, -)
    local_pattern = r'^[A-Za-z0-9][A-Za-z0-9._-]*[A-Za-z0-9]$'
    domain_pattern = r'^[A-Za-z0-9][A-Za-z0-9.-]*[A-Za-z0-9]$'

    if not re.match(local_pattern, local):
        return False
    if not re.match(domain_pattern, domain):
        return False
    
    return True


class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe@mail.co"))
        self.assertTrue(is_valid_email("a_b-c.d@domain.com"))
        self.assertTrue(is_valid_email("user123@sub.domain.org"))

    def test_missing_at_or_dot(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user@examplecom"))
        self.assertFalse(is_valid_email("userexamplecom"))

    def test_multiple_at(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@ex@ample.com"))

    def test_starts_or_ends_with_special(self):
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("user.@example.com"))
        self.assertFalse(is_valid_email("-user@example.com"))
        self.assertFalse(is_valid_email("user-@example.com"))
        self.assertFalse(is_valid_email("_user@example.com"))
        self.assertFalse(is_valid_email("user_@example.com"))
        self.assertFalse(is_valid_email("user@example.com."))
        self.assertFalse(is_valid_email("user@example.com-"))
        self.assertFalse(is_valid_email("user@example.com_"))

    def test_empty_and_invalid(self):
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email("@."))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("user@com."))
        self.assertFalse(is_valid_email("user@domain"))     # no dot in domain
        self.assertFalse(is_valid_email("user@site.c"))     # TLD too short


if __name__ == "__main__":
    unittest.main()
