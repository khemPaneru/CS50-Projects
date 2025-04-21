
import sys
import random
from pyfiglet import Figlet

fig = Figlet()
fonts_available = fig.getFonts()
if len(sys.argv) == 1:
    f = random.choice(fonts_available)
elif len(sys.argv) ==3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):

    if sys.argv[2] in fonts_available:
        f = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

fig.setFont(font=f)
text = input("Input: ")
print(fig.renderText(text))




