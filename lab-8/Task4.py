import unittest

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            self.items[name].append(price)
        else:
            self.items[name] = [price]

    def remove_item(self, name):
        if name in self.items:
            self.items[name].pop()
            if not self.items[name]:
                del self.items[name]
            return True
        return False

    def total_cost(self):
        return sum(price for prices in self.items.values() for price in prices)

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertEqual(self.cart.total_cost(), 1.5)

    def test_add_multiple_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.assertEqual(self.cart.total_cost(), 3.5)

    def test_add_same_item_multiple_times(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("apple", 2.0)
        self.assertEqual(self.cart.total_cost(), 3.5)

    def test_remove_item(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.assertTrue(self.cart.remove_item("apple"))
        self.assertEqual(self.cart.total_cost(), 2.0)

    def test_remove_item_multiple_times(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("apple", 2.0)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.total_cost(), 1.5)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.total_cost(), 0.0)

    def test_remove_nonexistent_item(self):
        self.assertFalse(self.cart.remove_item("orange"))

    def test_total_cost_empty_cart(self):
        self.assertEqual(self.cart.total_cost(), 0.0)

if __name__ == "__main__":
    unittest.main()