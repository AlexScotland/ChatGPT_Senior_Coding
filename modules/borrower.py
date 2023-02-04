from interfaces.iborrower import IBorrower

class Borrower(IBorrower):

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
    
    def __eq__(self, other_borrower):
        return self.name == other_borrower.name and self.address == other_borrower.address