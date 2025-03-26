

def main():
    user_input = input("Greeting: ").strip().lower()

#startswith() :is a string method used to check if a string
#  starts with a specified prefix like hello or h in this case .
# if not it will return false

    if user_input.startswith("hello") :
        print("$0")

    elif user_input.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
