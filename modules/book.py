from interfaces.ibook import IBook

class Book(IBook):

    def __init__(self, isbn: int, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
    
    def __eq__(self, other_book):
        return self.isbn == other_book.isbn and self.title == other_book.title and self.author == other_book.author