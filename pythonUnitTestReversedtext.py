import unittest
import reverseText

class Testing(unittest.TestCase):
    def test(self):
        self.assertEqual(reverseText.reverseText("text"), 'txet')

    def test2(self):
        self.assertEqual(reverseText.reverseText("slovo"), 'ovols')

if __name__ == '__main__':
    unittest.main()

