from interfaces.ibook import IBook
from interfaces.iborrower import IBorrower

from modules.borrowed_state import BorrowedState
from modules.report import Report
from modules.helpers import check_if_book_late

class Library():

    def __init__(self):
        self.books = {}
        self.borrowed_books = []
    
    def add_book_to_library(self, book: IBook):
        if not self.books.get(book.isbn):
            self.books[book.isbn] = []
        current_book_in_library = self.books.get(book.isbn)
        current_book_in_library.append(book)
    
    def checkout_book_from_library(self, book: IBook, borrower: IBorrower) -> BorrowedState:
        if not self.books.get(book.isbn) or len(self.books.get(book.isbn)) < 1:
            return False
        book_too_borrow = self.books.get(book.isbn).pop(0)
        new_borrowed_state = BorrowedState(borrower, book_too_borrow)
        self.borrowed_books.append(new_borrowed_state)
        return new_borrowed_state

    def checkin_book_from_library(self, book: IBook, borrower: IBorrower) -> bool:
        target_borrowed_state = self.__get_borrowed_state_from_book_and_borrower(book, borrower)
        if not target_borrowed_state:
            return False
        if check_if_book_late(target_borrowed_state.checked_at):
            return "Late"
        self.add_book_to_library(target_borrowed_state.book)
        return self.__remove_borrowed_book_state(target_borrowed_state)

    def __remove_borrowed_book_state(self, book_state):
        for index, iterated_book_state in enumerate(self.borrowed_books):
            if book_state == iterated_book_state:
                self.borrowed_books.pop(index)
                return True
        return False

    def __get_borrowed_state_from_book_and_borrower(self, book: IBook, borrower: IBorrower):
        for borrowed_state in self.borrowed_books:
            if borrowed_state.borrower == borrower and borrowed_state.book == book:
                return borrowed_state
        return False

    def generate_report(self):
        return Report.generate(self)
    
    def get_all_overdue_books(self):
        all_overdue = []
        for book in self.borrowed_books:
            if check_if_book_late(book.checked_at):
                 all_overdue.append(book)
        return all_overdue