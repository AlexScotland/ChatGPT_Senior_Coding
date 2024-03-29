# Library for ChatGPT Senior Interview

## Question
![image](https://i.imgur.com/C4v4hNb.png)

## Showcased technologies
* OOP ✔️
* Factory Pattern using Interfaces ✔️
* Pytest ✔️
* Broken down Mermaid Design ✔️
* Works! ✔️

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