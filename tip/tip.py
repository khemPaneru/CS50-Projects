def main():
    dollars = dollars_to_float(input("How much was your meal: ?"))
    percent = percent_to_float(input("How much percent would you like to  tips: ?"))
    tips = dollars * percent
    print(f"Leave ${tips:.2f}")


# use string method
def dollars_to_float(d):
    return float(d.strip('$'))

def percent_to_float(p):
    return float(p.strip('%')) /100



main()
