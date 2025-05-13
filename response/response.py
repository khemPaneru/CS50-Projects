
import validators

def main():

    input_email = input("What's is your email? ").strip()

    if validators.email(input_email):
      print("Valid")

    else:
      print("Invalid")


if __name__ == "__main__":
    main()
