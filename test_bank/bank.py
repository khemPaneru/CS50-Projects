

def main():

   message= input("Greeting: ")
    print(f"${value(message)}")


def value(greeting ):
    greeting_lower = greeting.lower()

    if  greeting_lower.startswith("hello") :
        return 0

    elif greeting.startswith("h") :
        return 20
    else:
       return 100

if __name__ == "__main__":
    

    main()
