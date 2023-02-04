from interfaces.iborrowed_state import IBorrowedState
from interfaces.iborrower import IBorrower
from interfaces.ibook import IBook
from datetime import datetime, timedelta

class BorrowedState(IBorrowedState):

    def __init__(self, borrower: IBorrower, book: IBook):
        self.borrower = borrower
        self.book = book
        self.checked_at = datetime.today()
    
    def __eq__(self, other_state):
        return self.borrower == other_state.borrower and self.book == other_state.book 