from datetime import datetime


def is_later_than_today(due_date: datetime.date(), today: datetime.date()):
    # checks if the date is later than today and within the same month
    diff = due_date - today
    diff_in_s = diff.total_seconds()
    days  = divmod(diff, 86400)[0]
    return True if days < 30 else False
