

import sys
import csv

if len(sys.argv) =! 2
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

if not filename endwith(".csv"):
        sys.exit("Not a CSV file")

try:
      with open(filename) as pizza_file:
            reader = csv.reader(pizza_file)
            table = list(reader)
            print(tabulate(table[1:], headers=table[0],tablefmt="grid"))

except FileNotFoundError:
      sys.exit("File not exist)
