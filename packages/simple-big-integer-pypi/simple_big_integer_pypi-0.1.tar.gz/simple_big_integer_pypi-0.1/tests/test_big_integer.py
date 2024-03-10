import unittest
from big_integer.big_integer import BigInteger

class TestBigInteger(unittest.TestCase):
    def test_addition(self):
        num1 = BigInteger("12345678901234567890")
        num2 = BigInteger("98765432109876543210")
        result = num1 + num2
        self.assertEqual(str(result), "111111111011111111100")

if __name__ == "__main__":
    unittest.main()
