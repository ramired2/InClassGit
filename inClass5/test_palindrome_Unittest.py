import unittest
import palindrome

class testCasePalindrome(unittest.TestCase):
    def test_palindrome(self):
    
        result = palindrome.palin()
        self.assertIsNot(result, -1)
    
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()