# EJERCICIO 12 - tens digit
# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  return (num % 100) // 10
# Invoke the function with any integer
print(tens_digit(1234))
print(tens_digit(179))
