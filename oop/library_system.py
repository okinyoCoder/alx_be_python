class Book:
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class  EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, {self.file_size}kB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count= page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, {self.page_count}: 234"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
       self.books.append(book)

    def list_books(self):
       for book in self.books:
           print(book)