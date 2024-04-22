import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_init(self):
        """Test the initialization of the Square class."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

if __name__ == '__main__':
    unittest.main()
