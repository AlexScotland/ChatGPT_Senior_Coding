import pytest
from unittest.mock import Mock


from modules.library import Library
from modules.book import Book
from modules.borrower import Borrower
from modules.borrowed_state import BorrowedState
from modules import helpers
from datetime import datetime, timedelta

def test_add_book_too_library():
    my_library = Library()
    new_book = Book(123, "Test: The Book", "Test Author")
    assert not my_library.books.get(new_book.isbn)
    my_library.add_book_to_library(new_book)
    assert my_library.books.get(new_book.isbn)

def test_checkout_book_from_library():
    my_library = Library()
    new_borrower = Borrower("Alex", "123 Sesame Street")
    new_book = Book(123, "Test: The Book", "Test Author")
    my_library.add_book_to_library(new_book)
    assert len(my_library.books.get(new_book.isbn)) == 1
    out_come = my_library.checkout_book_from_library(new_book, new_borrower)
    assert len(my_library.books.get(new_book.isbn)) == 0
    assert isinstance(out_come, BorrowedState)

def test_checkout_book_from_library_where_book_doesnt_exist():
    my_library = Library()
    new_borrower = Borrower("Alex", "123 Sesame Street")
    new_book = Book(123, "Test: The Book", "Test Author")
    out_come = my_library.checkout_book_from_library(new_book, new_borrower)
    assert not out_come

def test_checkin_book_to_library(monkeypatch):
    my_library = Library()
    new_borrower = Borrower("Alex", "123 Sesame Street")
    new_book = Book(123, "Test: The Book", "Test Author")
    my_library.add_book_to_library(new_book)
    def new_check_if_book_late(checked_at):
        return False
    
    assert len(my_library.books.get(new_book.isbn)) == 1
    out_come = my_library.checkout_book_from_library(new_book, new_borrower)
    assert len(my_library.books.get(new_book.isbn)) == 0
    monkeypatch.setattr("modules.helpers.check_if_book_late", new_check_if_book_late)
    out_come = my_library.checkin_book_from_library(new_book, new_borrower)
    assert out_come
    assert len(my_library.books.get(new_book.isbn)) == 1

def test_generate_report():
    my_library = Library()
    new_borrower = Borrower("Alex", "123 Sesame Street")
    new_book = Book(123, "Test: The Book", "Test Author")
    my_library.add_book_to_library(new_book)
    my_library.add_book_to_library(new_book)
    my_library.add_book_to_library(new_book)
    new_book = Book(456, "Test: The Book 2", "Test Author")
    my_library.add_book_to_library(new_book)
    my_library.add_book_to_library(new_book)
    my_library.checkout_book_from_library(new_book, new_borrower)
    my_report = my_library.generate_report()
    assert my_report['checked_out_books'] == 1
    assert my_report['overdue_books'] == 0
    