# EJERCICIO 44 - static methods
# Your code here
class MathOperations:
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2
operation1 = MathOperations()
result1 = MathOperations.add_numbers(10, 15)
print(result1)
