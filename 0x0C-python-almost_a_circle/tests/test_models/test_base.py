import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_init(self):
        """Test the initialization of the Base class."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()
