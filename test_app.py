import unittest
from app import add, subtract, convert_to_cny


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)

    def test_convert_to_cny(self):
        self.assertEqual(convert_to_cny(100, "USD"), 690.0)
        self.assertEqual(convert_to_cny(10, "EUR"), 75.0)
        self.assertEqual(convert_to_cny(50, "CNY"), 50.0)
        self.assertEqual(convert_to_cny(1000, "JPY"), 50.0)

    def test_convert_invalid_currency(self):
        with self.assertRaises(ValueError):
            convert_to_cny(10, "GBP")


if __name__ == "__main__":
    unittest.main()
