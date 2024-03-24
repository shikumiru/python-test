import unittest
from calc import Calc

class ClacTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calc().add(1, 2), 3)
        
    def test_minus(self):
        self.assertEqual(Calc().minus(3,2),1)
        
    def test_multiply(self):
        self.assertEqual(Calc().multiply(1, 2), 2)
        
    def test_divide(self):
        self.assertEqual(Calc().divide(8, 2), 4)
        
if __name__ == "__main__":
    unittest.main()