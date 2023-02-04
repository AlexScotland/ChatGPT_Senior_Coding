from datetime import datetime, timedelta

def check_if_book_late(date_time, day_to_check = 14):
    difference = date_time - datetime.today()
    if difference.days > day_to_check:
        return True
    return False