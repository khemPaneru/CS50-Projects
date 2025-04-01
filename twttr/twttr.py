
user_input = input("Input")

vowel = "aeiouAEIOU"


for char in user_input:
    if char not in  vowel:
        print(char, end=" ")
