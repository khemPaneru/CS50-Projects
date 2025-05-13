from datetime import date
import inflect
import sys

def main():
    # Initialize inflect engine to convert numbers to words
    p = inflect.engine()

    # Prompt user for their birthdate
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

    try:
        # Parse the input into a date object
        birth_year, birth_month, birth_day = map(int, birthdate.split('-'))
        birth_date = date(birth_year, birth_month, birth_day)
    except ValueError:
        # If the input format is incorrect, exit the program
        print("Invalid date format.")
        sys.exit(1)

    # Get today's date
    today = date.today()

    # Calculate the difference between today and the birthdate
    delta = today - birth_date

    # Calculate minutes lived
    minutes = delta.days * 24 * 60  # Convert days to minutes

    # Convert the minutes to words and print
    print(p.number_to_words(minutes, andword=", "))

if __name__ == "__main__":
    main()
