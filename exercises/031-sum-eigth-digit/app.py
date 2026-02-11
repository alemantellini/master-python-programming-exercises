# EJERCICIO 31 - sum eighth digit (all digits even) - no test
# Your code here
def all_digits_even():
    result = []
    my_list = range(1000, 3001)
    for num in my_list:
        all_even = True
        for digit in str(num):
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
             result.append(str(num))
    print(",".join(result))
all_digits_even()
