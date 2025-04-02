def main():

    user_input = input("Plate: ")

    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")


def is_valid(khem):
# Check length constraint (between 2 and 6 characters)
        if not (2< len(khem) >= 6):
            return False

## Check if first two characters are letters
        if not khem[:2].isalpha():  #or khem[0:2]
            return False

# Check if all characters are alphanumeric or not
        if not khem.isalnum():
            return False

        for i in range(len(khem)):
            if khem[i].isdigit():
                if khem[i] == 0:
                    return False
                if not khem[i].isdigit():
                    return False
                break

        return True



main()
