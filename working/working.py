
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid input format")

    h1, m1, am_pm1, h2, m2, am_pm2 = match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6)

    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    h1, m1 = int(h1), int(m1)
    h2, m2 = int(h2), int(m2)

    if not (0<= m1  < 60) or not (0 <= m2 < 60) or not (1 <= h1 <= 12) or not (1 <= h2 <= 12):
        raise ValueError("Invalid time")

    start_24 = to_24_hour(h1, m1, am_pm1)
    end_24 = to_24_hour(h2,m2, am_pm2)

    return f"{start_24} to {end_24}"

def to_24_hour(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour +=12
    return f"{hour:02}:{minute:02}"




if __name__ == "__main__":
    main()
