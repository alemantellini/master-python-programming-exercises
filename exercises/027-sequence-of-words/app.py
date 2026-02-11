# EJERCICIO 27 - sequence of words
# Your code here
def sequence_of_words(text): 
    my_list = text.split(",")
    my_list.sort()
    result = ", ".join(my_list) 
    return result 
print(sequence_of_words("without,hello,bag,world"))
