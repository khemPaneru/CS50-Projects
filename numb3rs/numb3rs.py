import re

def main():
    user_input = input("IPV4 Address: ")
    print(validate)

def validate(ip):
    if not re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
        return False
    try:
        octets = ip.split(".")
        if len(octets) !=4:
            return False
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False

         return True
    except ValueError:
        return False
if __name__ == "__main__"
    main()
