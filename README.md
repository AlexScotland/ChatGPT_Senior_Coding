# Library for ChatGPT Senior Interview


## Requirements:
 - Add a new book to the library
 - Search for a book by its title, author, or ISBN
 - Check out a book to a borrower
 - Check in a book from a borrower
 - Generate reports about the books in the library (e.g. books checked out, books overdue, etc.)

 ## Design Class Diagram
```mermaid
---
title: Library System
---
classDiagram
    class Library {
        +dict books isbn:[books]
        +array borrowed_books [BorrowedState]
        +add_book_to_library(Book) -> bool
        +checkout_book_from_library(Book, Borrower) -> BorrowedState
        +checkin_book_to_library(Book, Borrower) -> bool
        +generate_report(self) -> Report
        }
    
    class IBorrower {
        +String name
        +String address
    }

    class Borrower~IBorrower~ {
        +String name
        +String address
    }

    class IBook {
        +String isbn
        +String title
        +String author
    }

    class Book ~IBook~ {
        +String isbn
        +String title
        +String author
    }

    class BorrowedState ~IBorrowedState~ {
        +class borrower Borrower
        +class book Book
        +time borrowed_at
    }

    class IBorrowedState {
        +class borrower Borrower
        +class book Book
        +time borrowed_at
    }

    class IReport {
        +list checked_out_books
        +list overdue_books
    }

    class Report ~IReport~ {
        +list checked_out_books
        +list overdue_books
    }
    %%% Operations
    Library --> Book : Has Many

    Report --> Library

    IBorrower <|-- Borrower
    IBook <|-- Book
    IBorrowedState <|-- BorrowedState
    IReport <|-- Report

    BorrowedState --> Borrower : Has One
    Library --> BorrowedState : Has Many
    BorrowedState --> Book : Has One
    
```