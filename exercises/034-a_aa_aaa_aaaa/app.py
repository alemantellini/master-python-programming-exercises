# EJERCICIO 34 - a_aa_aaa_aaaa
# Your code here
def computed_value(a):
    result = 0
    for i in range(1, 5):
        new_number = int(str(a)*i)
        result += new_number
    return result
print(computed_value(9))
