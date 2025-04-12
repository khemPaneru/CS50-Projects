
def main():
    months_name = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
          ]
    while True:
        try:
            date= input("Date").strip()
            if "/" in date:
                date.split("/") = parts

            if len(parts) == 3:
                month, day, year = parts

                if month.isdigit() and day.isdigits() and year.isdigits():
                    month, day, year = int(month), int(day), int(year)

                    if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                elif "," in data:
                    date.split(" ") = parts
                    if len(parts) == 3 and "," in parts[1]:
                        month, day, year = parts

                        if months in months_name and days.isdigits() and years.isdigit():
                            month = months_name.index(month) + 1
                            day , year = int(day), int(year)

                            if 1 <= day <= 31:
                                print(f{"year:04}-{month:02}-{day:02}")
                                      break
            except EOFError:
                break
if __name__ = "__main__":
    main()

