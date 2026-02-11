# EJERCICIO 39 - class that iterates - no test
# Your code here
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n
    def generator(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i
n = 50
div7 = DivisibleBySeven(n)
for num in div7.generator():
    print(num)
