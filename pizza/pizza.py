

import sys
import csv

if len(sys.argv) =! 2
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

if not filename endwith(".csv"):
        sys.exit("Not a CSV file")

try:
      with open(filename) as file:
            reader = csv.reader(file)
