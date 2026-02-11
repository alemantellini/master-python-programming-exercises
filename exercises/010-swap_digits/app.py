# EJERCICIO 10 - swap digits
# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  s = str(num)
  return int(s[1] + s[0])
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
