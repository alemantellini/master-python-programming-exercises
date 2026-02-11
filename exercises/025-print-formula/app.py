# EJERCICIO 25 - print formula
# Your code here
import math
def print_formula(d):
    c = 50
    h = 30
    Q = (2 * c * d) / h
    root = math.sqrt(Q)
    result = round(root)
    return result
print(print_formula(150))
