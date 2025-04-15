import sys
import random
from pyfiglet import Figlet

fig = figlet()
fonts_available = figlet.getfonts()
if len(sys.argv) = 1:
font = random.choice(fonts_available)
elif len(sys.argv) ==3 and (sys.argv[1] == "-f" or sys.arv[1] == "__font"):

    if sys.argv[2] in fonts_available:
        font = sys.argv[2]
    else:
        sys.exit("invalid")
else:
sys.exit("exit")
fif.setFont(font=font)
text = input("Input: ")
print(fig.RenderText(text))


