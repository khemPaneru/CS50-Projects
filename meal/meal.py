
def main():
    time= input("What time is it(HH:MM):? ")

    time_in_hour = convert(time)

    if 7.00 <= time_in_hour <= 8.00:
        print("brekfast")
    elif 12.00 <= time_in_hour <= 13.00:
        print("lunch")
    elif 18.00 <= time_in_hour <= 19.0:
        print("Dinner")

def convert(clock):
    hours, minutes = clock.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + (minutes / 60)

#use dunder method
if __name__ == "__main__":

    main()
