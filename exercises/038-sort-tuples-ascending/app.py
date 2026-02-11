# EJERCICIO 38 - sort tuples ascending
from operator import itemgetter
# Your code here
def sort_tuples_ascending(list_of_strings):
    list_of_tuples = []
    for s in list_of_strings:
        tuple_item = tuple(s.split(','))
        list_of_tuples.append(tuple_item)
    sorted_list = sorted(list_of_tuples, key=itemgetter(0,1,2))
    return sorted_list
print(sort_tuples_ascending(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85']))
