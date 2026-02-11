# EJERCICIO 42.1 - init and str methods
# Your code here
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

# Create an instance of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Print the information using the __str__ method
print(book1)
