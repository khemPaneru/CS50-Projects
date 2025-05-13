from datetime import date
import inflect
import sys

def calculate_minutes(birthdate):
    # Calculate the difference between today's date and the birthdate
    today = date.today()  # Get today's date directly inside the function
    birthdate = date(*map(int, birthdate.split('-')))  # Convert input string to date
    delta = today - birthdate
    minutes = delta.days * 24 * 60  # Convert days to minutes
    return minutes

def convert_to_words(minutes):
    # Convert minutes to words using inflect
    p = inflect.engine()
    return p.number_to_words(minutes).lower()  # Ensure the result is lowercase

def main():
    try:
        # Prompt the user for their birthdate in YYYY-MM-DD format
        birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

        # Validate and process the birthdate
        minutes = calculate_minutes(birthdate)

        # Convert the minutes to words and print the result
        minutes_in_words = convert_to_words(minutes)
        print(f"{minutes_in_words} minutes")

    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        sys.exit(1)

if __name__ == "__main__":
    main()
