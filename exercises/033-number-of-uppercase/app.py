# EJERCICIO 33 - number of uppercase - no test
# Your code here
def number_of_uppercase(letters):
    counts = {
    "UPPERCASE": 0,
    "LOWERCASE": 0
}
    for character in letters:
        if character.isupper():
            counts["UPPERCASE"] += 1
        elif character.islower():
            counts["LOWERCASE"] += 1
    return "UPPERCASE" + " " + str(counts["UPPERCASE"]) + " " + "LOWERCASE" + " " + str(counts["LOWERCASE"])
print(number_of_uppercase("Hello world!"))
