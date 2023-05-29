from datetime import date

if __name__ == "__main__":
    DELTA = (date.today() - date(2022, 2, 1))
    years = DELTA.days / 365
    months = DELTA.days / 30.417
    days = DELTA.days

    if round(months) % 12 == 0: months = 0
    else: months /= 12

    print("\033[0;30;42mStarted drumming on Feb. 1st, 2022!\033[0;0;0m",
        "\n\033[2m➤ That's %d days (%d month(s), and %d year(s))!\033[0;0;0m"
        %(days, months, years))
