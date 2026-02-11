# EJERCICIO 29 - remove duplicate words
# Your code here
def remove_duplicate_words(text):
    my_list = text.split()
    my_set = set(my_list)
    result = sorted(my_set)
    x = " ".join(result)
    return x
print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))
