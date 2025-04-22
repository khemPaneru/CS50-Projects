import requests
import sys

if len(sys.argv) !=2:
    sys.exit(""Missing command-line argument"")

try:
    bitcoin = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")
    
url = 0944621b45ce907b4bd9521557a03170ba66a48b1f8a1a39c080d4f545f73728
