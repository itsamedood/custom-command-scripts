from datetime import date
from calendar import month


if __name__ == "__main__":
    today = date.today()
    yy = today.year
    mm = today.month

    print(month(yy, mm))
