import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regular expression to match valid time formats
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    # If the input doesn't match the expected format, raise a ValueError
    if not match:
        raise ValueError("Invalid input format")

    # Extract the matched groups
    h1, m1, am_pm1, h2, m2, am_pm2 = match.groups()

    # Set minutes to "00" if not provided
    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    # Convert hours and minutes to integers for easy manipulation
    h1, m1 = int(h1), int(m1)
    h2, m2 = int(h2), int(m2)

    # Validate that the hours and minutes are within valid ranges
    if not (0 <= m1 < 60) or not (0 <= m2 < 60) or not (1 <= h1 <= 12) or not (1 <= h2 <= 12):
        raise ValueError("Invalid time")

    # Convert both times to 24-hour format
    start_24 = to_24_hour(h1, m1, am_pm1)
    end_24 = to_24_hour(h2, m2, am_pm2)

    # Return the formatted result in 24-hour format
    return f"{start_24} to {end_24}"


def to_24_hour(hour, minute, period):
    #Converts a 12-hour time to a 24-hour time.
    if period == "AM":
        if hour == 12:  # Midnight case
            hour = 0
    elif period == "PM":
        if hour != 12:  # PM times except 12 PM need 12 added
            hour += 12
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
