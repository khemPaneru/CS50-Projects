import csv
import sys


if len(sys.argv) != 3:
    sys.exit("Usage: python program.py input_file output_file")


input_file = sys.argv[1]
output_file = sys.argv[2]

# Try to open the input file and read its contents
try:
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)  # Use DictReader to read CSV data into dictionaries

        students = []  # List to store student data


        for row in reader:
            name = row["name"]
            house = row["house"]


            last, first = name.split(", ")

            students.append({
                "first": first,
                "last": last,
                "house": house
            })

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

# Try to open the output file and write the modified student data
try:
    with open(output_file, "w", newline='') as output:
        fieldnames = ["first", "last", "house"]  # Define the CSV field names
        writer = csv.DictWriter(output, fieldnames=fieldnames)  # Create a writer object

        writer.writeheader()  # Write the header row to the output file
        for student in students:
            writer.writerow(student)  # Write each student's data to the output file


except Exception as e:
    sys.exit(f"Could not write to {output_file}: {e}")
