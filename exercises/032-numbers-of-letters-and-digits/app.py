# EJERCICIO 32 - numbers of letters and digits
# Your code here
def letters_and_digits(sentence):
    counts = {
    "LETTERS": 0,
    "DIGITS": 0
}
    for character in sentence:
        if character.isalpha():
            counts["LETTERS"] += 1
        elif character.isdigit():
            counts["DIGITS"] += 1
    return "LETTERS" + " " + str(counts["LETTERS"]) + " " + "DIGITS" + " " + str(counts["DIGITS"])
print(letters_and_digits("hello world! 123"))
