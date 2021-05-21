# import unittest
# import hw1

# class testCaseLeapYear(unittest.TestCase):
#     def test_leapYear(self):
    
#         result = hw1.leap()
#         self.assertGreater(result, 0)
#         self.assertEqual((result%4), 0)

# if __name__ == "__main__":
#     unittest.main()

import pytest
import hw1

def test_leapYear():
    result = hw1.leap()
    assert result > 0

    assert result % 4 == 0
    assert (result % 100 == 0 and result % 400 == 0)