# EJERCICIO 17 - total cost
# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    total_d = d * n
    total_c = c * n
    extra_d = total_c // 100
    total_c = total_c % 100
    total_d = total_d + extra_d
    return (total_d, total_c)
# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
print(total_cost(3, 75, 4))
print(total_cost(2, 35, 3))
