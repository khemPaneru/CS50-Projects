import sys
import os


if len(sys.argv) !=2:
      sys.exit(1)

   #chekc if file name exist or not

filename = sys.argv[1]

# Check if the file ends with .py
if not filename.endswith(".py"):
      sys.exit(1)

#check if the file exists
if not os.path.isfile(filename):
       sys.exit(1)
# Initialize a counter for lines of code
count = 0

#open and read a file
with open (filename) as file:
     for line in file:
          stripped_line = line.strip()

  # Skip blank lines and comment lines
          if stripped_line == "" or stripped_line.startswith('#'):
               continue
          count +=1

print(count)



