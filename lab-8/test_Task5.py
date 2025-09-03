import unittest
from Task5 import convert_date_format

class TestConvertDateFormatExternal(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")
        self.assertEqual(convert_date_format("2025-09-03"), "03-09-2025")

    def test_invalid_format(self):
        self.assertEqual(convert_date_format("2023/10/15"), "Invalid format")
        self.assertEqual(convert_date_format("15-10-2023"), "Invalid format")
        self.assertEqual(convert_date_format("2023-10"), "Invalid format")
        self.assertEqual(convert_date_format("20231015"), "Invalid format")
        self.assertEqual(convert_date_format(""), "Invalid format")
        self.assertEqual(convert_date_format("2023-1-5"), "Invalid format")
        self.assertEqual(convert_date_format("abcd-ef-gh"), "Invalid format")

    def test_edge_cases(self):
        self.assertEqual(convert_date_format("0000-00-00"), "00-00-0000")
        self.assertEqual(convert_date_format("9999-99-99"), "99-99-9999")

if __name__ == "__main__":
    unittest.main()