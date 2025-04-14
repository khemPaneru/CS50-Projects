
import emoji

def main():
    text = input("Input ")
    converted_text = emoji.emojize(text, language="alias")
    print(f"Output: ",  converted_text)
main()
