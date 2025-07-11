import sys
import config
import unittest
from app import point as p

# sys.path.append(config.APP_PATH)

# Εναλλακτικά !
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
print("Absolote path to our project:", end=": ")
print(str(Path(__file__).resolve().parent.parent))
print()

class TestApp(unittest.TestCase):
    def test_addition(self):
        """Test the addition of two Point objects."""
        p1 = p.Point(1, 2)
        p2 = p.Point(3, 4)
        expected = p.Point(4, 6)
        self.assertEqual(p1 + p2, expected)
        # Expected outcome: (1+3, 2+4) = (4, 6)
    
    def test_addition_with_number(self):
        """Test the addition of a Point object and a number."""
        p1 = p.Point(1, 2)
        number = 3
        expected = p.Point(4, 5)
        self.assertEqual(p1 + number, expected)
        self.assertEqual(number + p1, expected)
        # Expected outcome for p1 + number: (1+3, 2+3) = (4, 5)
        # Expected outcome for number + p1: (3+1, 3+2) = (4, 5)
    
    def test_subtraction(self):
        """Test the subtraction of two Point objects."""
        p1 = p.Point(5, 6)
        p2 = p.Point(3, 4)
        expected = p.Point(2, 2)
        self.assertEqual(p1 - p2, expected)
        # Expected outcome: (5-3, 6-4) = (2, 2)
    
    def test_subtraction_with_number(self):
        """Test the subtraction of a number from a Point object."""
        p1 = p.Point(5, 6)
        number = 2
        expected = p.Point(3, 4)
        self.assertEqual(p1 - number, expected)
        # Expected outcome for p1 - number: (5-2, 6-2) = (3, 4)
        self.assertEqual(number - p1, p.Point(-3, -4))
        # Expected outcome for number - p1: (2-5, 2-6) = (-3, -4)
    
    def test_multiplication(self):
        """Test the multiplication of a Point object by a number."""
        p1 = p.Point(1, 2)
        number = 3
        expected = p.Point(3, 6)
        self.assertEqual(p1 * number, expected)
        self.assertEqual(number * p1, expected)
        # Expected outcome for p1 * number: (1*3, 2*3) = (3, 6)
        # Expected outcome for number * p1: (3*1, 3*2) = (3, 6)
    
    def test_equality(self):
        """Test the equality of two Point objects."""
        p1 = p.Point(1, 2)
        p2 = p.Point(1, 2)
        self.assertTrue(p1 == p2)
        # Expected outcome: True, since (1, 2) == (1, 2)
    
    def test_inequality(self):
        """Test the inequality of two Point objects."""
        p1 = p.Point(1, 2)
        p2 = p.Point(3, 4)
        self.assertTrue(p1 != p2)
        # Expected outcome: True, since (1, 2) != (3, 4)
    
    def test_equality_with_non_point(self):
        """Test the equality check with a non-Point object."""
        p1 = p.Point(1, 2)
        self.assertFalse(p1 == (1, 2))
        # Expected outcome: False, since Point(1, 2) is not equal to tuple (1, 2)

if __name__ == '__main__':
    unittest.main()
