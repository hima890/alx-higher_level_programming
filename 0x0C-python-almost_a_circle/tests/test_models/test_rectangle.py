import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init(self):
        """Test the initialization of the Rectangle class."""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

if __name__ == '__main__':
    unittest.main()
