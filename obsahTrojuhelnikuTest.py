import unittest
import obsahTrojuhelniku

class Testing(unittest.TestCase):
    def test(self):
        self.assertEqual(obsahTrojuhelniku.areaTriangle(5,4,3), 6)

    def test2(self):
        self.assertEqual(obsahTrojuhelniku.areaTriangle(10,8,6), 24)

if __name__ == '__main__':
    unittest.main()                 
