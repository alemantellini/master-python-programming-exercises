# EJERCICIO 23 - list and tuple
# Your code here
def list_and_tuple(*args):
    my_list = []
    for i in args:
        my_list.append(str(i))
    my_tuple = tuple(my_list)
    print(my_list)
    print(my_tuple)
    return my_list, my_tuple
list_and_tuple(34, 67, 55, 33, 12, 98)
