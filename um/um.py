import re
 def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r'\bum\b'

    output = re.findall(pattern, s, re.INGORECASE)
    return len(output)

if __name__ == "__main__":
   main()
