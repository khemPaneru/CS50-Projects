user_input = input("Input: ")

vowel = "aeiouAEIOU"

# Print the output label once
print("Output:", end=" ")

# Loop through each character in the input string
for char in user_input:
    if char not in vowel:  # If the character is not a vowel
        print(char, end="")  # Print the character without a newline after it
