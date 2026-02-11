# EJERCICIO 30 - divisable binary
# Your code here
def divisible_binary(num):
    my_list = num.split(",")
    my_new_list = []
    for i in my_list:
        decimal = int(i, 2)
        divisible = decimal % 5 == 0
        if divisible:
            my_new_list.append(i)
    result = ",".join(my_new_list)
    return result 
print(divisible_binary("0100,0011,1010,1001"))
