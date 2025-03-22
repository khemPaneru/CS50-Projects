
def convert(string_input):
   khem = string_input.replace(":)" ,"🙂").replace(":(" ,"🙁")
    return khem

def main():
    user_input= input("Give your input in emoticons")
    result = convert(user_input)
    print(result)

main()
