import unittest
from Calc import Calculator  # 確保你的檔案名稱是 Calc.py，並且有 Calculator 類別

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)  # 5 - 2 = 3

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)  # 4 * 3 = 12

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)  # 10 / 2 = 5
    
    def test_divide_float(self):
        calc = Calculator()
        result = calc.divide(7, 3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(5, 0)  # 除以 0 應該拋出錯誤

if __name__ == "__main__":
    unittest.main()
