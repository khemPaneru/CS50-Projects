
def convert():
   khem =input_in_string.replace(":) " ,"🙂").replace(":( " ,"🙁")
    return khem
def main():
   user_input= input("Give your input in emoticons")
    result = convert(user_input)
    print(result)

main()
