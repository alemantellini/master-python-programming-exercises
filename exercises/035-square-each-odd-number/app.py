# EJERCICIO 35 - square each odd number - no test
# Your code here
def square_odd_numbers(num):
    my_string = num.split(",")
    my_new_list = []
    for i in my_string:
        n = int(i)
        odd = n % 2 != 0
        if odd:
            square = n**2
            my_new_list.append(square)
    return my_new_list
print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))
