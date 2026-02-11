# EJERCICIO 15 - car route
# Complete the function to return the amount of days it will take to cover a route
def car_route(n,m):
  import math 
  distance = m / n
  result = math.ceil(distance)
  return result
# Invoke the function with two integers
print(car_route(20, 40))
