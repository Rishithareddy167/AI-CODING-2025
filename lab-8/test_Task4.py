import unittest
from Task4 import ShoppingCart

class ShoppingCartUnitTests(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertEqual(self.cart.items, {"apple": [1.5]})
        self.assertEqual(self.cart.total_cost(), 1.5)

    def test_add_multiple_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.assertEqual(self.cart.items, {"apple": [1.5], "banana": [2.0]})
        self.assertEqual(self.cart.total_cost(), 3.5)

    def test_add_same_item_multiple_times(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("apple", 2.0)
        self.assertEqual(self.cart.items, {"apple": [1.5, 2.0]})
        self.assertEqual(self.cart.total_cost(), 3.5)

    def test_remove_item(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        result = self.cart.remove_item("apple")
        self.assertTrue(result)
        self.assertNotIn("apple", self.cart.items)
        self.assertEqual(self.cart.total_cost(), 2.0)

    def test_remove_item_multiple_times(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("apple", 2.0)
        self.assertTrue(self.cart.remove_item("apple"))
        self.assertEqual(self.cart.items, {"apple": [1.5]})
        self.assertEqual(self.cart.total_cost(), 1.5)
        self.assertTrue(self.cart.remove_item("apple"))
        self.assertEqual(self.cart.items, {})
        self.assertEqual(self.cart.total_cost(), 0.0)

    def test_remove_nonexistent_item(self):
        self.assertFalse(self.cart.remove_item("orange"))

    def test_total_cost_empty_cart(self):
        self.assertEqual(self.cart.total_cost(), 0.0)

    def test_remove_item_from_empty_cart(self):
        self.assertFalse(self.cart.remove_item("apple"))

    def test_add_and_remove_multiple_items(self):
        self.cart.add_item("apple", 1.0)
        self.cart.add_item("banana", 2.0)
        self.cart.add_item("apple", 1.5)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.items, {"apple": [1.0], "banana": [2.0]})
        self.cart.remove_item("banana")
        self.assertEqual(self.cart.items, {"apple": [1.0]})
        self.assertEqual(self.cart.total_cost(), 1.0)

if __name__ == "__main__":
    unittest.main()