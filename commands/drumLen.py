from datetime import date

if __name__ == "__main__": print(f"\033[0;30;42mStarted drumming on Feb. 1st, 2022; that's {(date.today() - date(2022, 2, 1)).days} days so far!\033[0;0;0m\n")
