# Calc.py

class Calculator:
    def add(self, a, b):
        """回傳 a + b"""
        return a + b

    def subtract(self, a, b):
        """回傳 a - b"""
        return a - b

    def multiply(self, a, b):
        """回傳 a * b"""
        return a * b

    def divide(self, a, b):
        return a / b
        """回傳 a / b，如果 b 為 0 則拋出錯誤"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return int (a / b)
