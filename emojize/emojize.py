
import emoji

def main():
    text = input("Input ")
    emojize = emoji.emojize(text, language="alias")
    print(f"Output: ", emojize)
if __name__ =="__main__":
    main()
