# EJERCICIO 16 - century
# Complete the function to return the respective number of the century
def century(year):
  import math 
  number = year / 100
  result = math.ceil(number)
  return result
# Invoke the function with any given year
print(century(2001))
