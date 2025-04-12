def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Handle MM/DD/YYYY
            if "/" in date:
                parts = date.split("/")
                if len(parts) == 3:
                    month, day, year = parts
                    if month.isdigit() and day.isdigit() and year.isdigit():
                        month = int(month)
                        day = int(day)
                        year = int(year)
                        if 1 <= month <= 12 and 1 <= day <= 31:
                            print(f"{year:04}-{month:02}-{day:02}")
                            break

            # Handle Month Day, Year (e.g., September 8, 1636)
            elif "," in date:
                date = date.replace(",", "")  # remove comma
                parts = date.split()
                if len(parts) == 3:
                    month_name, day, year = parts
                    if month_name in months and day.isdigit() and year.isdigit():
                        month = months.index(month_name) + 1
                        day = int(day)
                        year = int(year)
                        if 1 <= day <= 31:
                            print(f"{year:04}-{month:02}-{day:02}")
                            break

        except EOFError:
            break
