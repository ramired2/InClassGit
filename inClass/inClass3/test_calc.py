import unittest
import calc1

class testCaseCalc(unittest.TestCase):
    #adding
    def test_Add(self):
        result = calc1.add(7,3)
        self.assertEqual(result, 10)

        result = calc1.add(7,b)
        self.assertEqual(result, 7)

    # subtracting
    def test_sub(self):
        result = calc1.sub(16,9)
        self.assertEqual(result, 7)

    # multiplying
    def test_mult(self):
        result = calc1.mul(9,50)
        self.assertEqual(result, 450)

    # dividing
    def test_div(self):
        result = calc1.div(81, 3)
        self.assertEqual(result, 27)

        result = calc1.div(6, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()