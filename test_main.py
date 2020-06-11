import unittest
from main import adder

class TestAdder(unittest.TestCase):
    def test_simple_adder(self):
        res = adder(1, 2)
        self.assertEqual(res, 3)

if __name__ == "__main__":
    unittest.main()
