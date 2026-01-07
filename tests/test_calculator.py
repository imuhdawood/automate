import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        """Create a Calculator instance for each test."""
        self.calc = Calculator()

    def test_add(self):
        """Verify addition of two numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        """Verify subtraction of two numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        """Verify multiplication of two numbers."""
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        """Verify division with a non-zero divisor."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Ensure division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
