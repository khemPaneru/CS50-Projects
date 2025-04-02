


user_input = input("Input: ")

vowel = "aeiouAEIOU"

print("Output:", end=" ")

for char in user_input:
    if char not in  vowel:
        #end="" :parameter is used in the print() function to specify what should be printed at the end
        # of the output instead of the default newline (\n).

        print( char, end="")
print()
