# EJERCICIO 13 - sum of digits
# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  hundreds = num // 100
  tens = (num % 100) // 10
  units = num % 10
  return hundreds + tens + units
# Invoke the function with any three-digit number
print(digits_sum(123))
