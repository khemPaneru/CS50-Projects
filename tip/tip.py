def main():
    dollars = float(input("How much was your meal: ?)")
    percent = float(input("How much percent of meal do you want to give tips: ?)")
    tips = dollars * percent
    print(f"Leave {tips},.2f)
main()
