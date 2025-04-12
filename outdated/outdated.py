
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
     # Format: MM/DD/YYYY
            if "/" in date:
                parts = date.split("/")
            if len(parts) == 3:
                month, day, year = parts
                if month.isdigit() and day.isdigit() and year.isdigit():
                    month, day, year = int(month), int(day), int(year)

                    if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                        break
 # Format: Month Day, Year
                elif "," in date:
                    parts = date.replace(",", "").split(" ")
                    if len(parts) == 3 and "," in parts[1]:
                        month = parts[0]
                        day = parts[1]
                        year = parts[2]

                        if month in months_name and day.isdigit() and year.isdigit():
                            month = months_name.index(month)
                            month +=1
                            day , year = int(day), int(year)

                            if 1 <= day <= 31:
                                print(f"{year:04}-{month:02}-{day:02}")
                                break
        except EOFError:
                break
if __name__ == "__main__":
    main()

