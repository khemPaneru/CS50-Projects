
user_input = input("Input")

vowel = "aeiouAEIOU"
result = ""

for char in user_input:
    if char not in  vowel:
        result += char
print(f"{result}")
