from interfaces.ireport import IReport

class Report(IReport):

    @staticmethod
    def generate(library):
        return {
            "checked_out_books": len(library.borrowed_books),
            "overdue_books": len(library.get_all_overdue_books())
        }