def main():


    plate = input("input")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(khem):
        if not (2< len(khem) >= 6):
            return False

        if not khem[:2]:  #or khem[0:2]
            return False

        for i in range(len(khem)):
            if khem[i].isdigit():
                if khem[i] == 0:
                    return False
                if not khem[i].isdigit():
                    return False
                break

        return True

    # Check if all characters are alphanumericEnsures
    #  no spaces, punctuation, or special characters

        if not khem.isalnum():
            return false




main()
