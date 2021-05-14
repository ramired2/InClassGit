import unittest
import wordcount

class testCaseWordCount(unittest.TestCase):
    def test_count(self):
    
        result = wordcount.count()
        self.assertGreater(result,0)


if __name__ == "__main__":
    unittest.main()