from datetime import date


def det_age(born):
    now = date.today()
    try:
        birthday = born.replace(year=now.year)
    except ValueError:
        birthday = born.replace(year=now.year, month=born.month + 1, day=1)
    if birthday > now:
        return now.year - born.year - 1, "years old"
    else:
        return now.year - born.year, "years old"


print(det_age(date(2001, 6, 24)))
