# EJERCICIO 41 - frequency of words
# Your code here
def compute_word_frequency(text):
    words = text.split()
    frequency = {}
    result = ""
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    for word in sorted(frequency):
        result += f"{word}: {frequency[word]}\n"
    return result[:-1]
print(compute_word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))
