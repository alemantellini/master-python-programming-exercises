# EJERCICIO 14 - digit after decimal point
# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
  return int((num % 1) * 10)
# Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))
print(first_digit(3.14))
