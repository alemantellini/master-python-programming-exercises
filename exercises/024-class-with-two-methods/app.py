# EJERCICIO 24 - class with two methods
# Your code here
class InputOutString:
    def __init__(self):
        self.name = ""
    def get_string(self):
        self.name = input("Ingrese su nombre")
    def print_string(self):
        print(self.name.upper())
my_object = InputOutString()
my_object.get_string()
my_object.print_string()
