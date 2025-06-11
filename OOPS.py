# A class Book with title, author, and price. Add a method to display all info.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}")

# Create an instance of Book and display its information
book1 = Book("1984", "George Orwell", 9.9998)
book1.display_info()