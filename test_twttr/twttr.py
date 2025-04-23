

def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

def main():
    user_input = input("Input: ")
    print("Output:", shorten(user_input))

if __name__ == "__main__":
    main()
