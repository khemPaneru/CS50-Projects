
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$
    match = re.match(pattern, s)
if not match:
    raise ValueError("Invalid input format")
h1, m1, am_pm1, h2, m2, am_pm2 = match.group()

if __name__ == "__main__":
    main()
