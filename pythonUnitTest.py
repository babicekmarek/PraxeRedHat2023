import unittest
import faktorial

class Testing(unittest.TestCase):

    def test(self):
        self.assertEqual(faktorial.faktorial(5), 120)

    def test2(self):
        self.assertEqual(faktorial.faktorial(3), 7)

if __name__ == '__main__':
    unittest.main()
    
