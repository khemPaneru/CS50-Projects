
# end="" :It's an argument or parameter passed to the print() function used to
        #  peint in same line without introducing
        #  new line for printing as python does by defaultuser_input = input("Input: ")

vowel = "aeiouAEIOU"

print("Output:", end=" ")

for char in user_input:
    if char not in  vowel:

        print( char, end="")
print()
