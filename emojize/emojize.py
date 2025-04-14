
import emoji

def main():
    text = input("Input: ")
    converted_text = emoji.emojize(text, language="alias")
    print(f"Output: ",  converted_text)

if __name__ =="__main__":
    main()
