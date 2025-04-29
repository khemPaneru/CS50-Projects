

import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

try:
      with open(filename) as pizza_file:
            reader = csv.reader(pizza_file)
            table = list(reader)
            print(tabulate(table[1:], headers=table[0],tablefmt="grid"))

except FileNotFoundError:
      sys.exit("File not exist")
