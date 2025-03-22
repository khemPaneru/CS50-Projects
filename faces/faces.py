

#made a function
def convert(string_input):
    #use_replaec_method
    khem = string_input.replace(":)" ,"🙂").replace(":(" ,"🙁")
    return khem

def main():
    user_input= input("Give your input in emoticons")
    #call the function with arug
    
    result = convert(user_input)
    print(result)

main()
