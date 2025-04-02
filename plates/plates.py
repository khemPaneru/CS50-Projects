def main():


    plate = input("input")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(khem):
         # Check length constraint (between 2 and 6 characters)
        if not (2< len(khem) >= 6):
            return False

# # Check if first two characters are letters
        if not khem[:2].isalpha()  #or khem[0:2]
            return False

        for i in range(len(khem)):
            if khem[i].isdigit():
                if khem[i] == 0:
                    return False
                if not khem[i].isdigit():
                    return False
                break

        return True

    # Check if all characters are alphanumeric
    # (comb of a-z,A-z,0-9 ,doesnt includes ! @ # $ % & * or spaces.)


        if not khem.isalnum():
            return false




main()
