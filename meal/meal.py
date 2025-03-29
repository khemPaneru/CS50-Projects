def main():

    time= input("What time is it(HH:MM) :?")

    time_in_hour = convert(time)

    if 7:00 <= time_in_hour <= 8:00:
        print("brekfast)"
    elif 13:00 <= time_in_hour <= 14:00:
        print("lunch")
    elif 19:00 time_in_hour <= 20:00:
        print("Dinner")
    else:
        print("No meal time")

def convert(clock):
    hours, minutes = clock.split(":")

    hours = int(hours)
    minutes = int(minutes)
    return hours + (minutes / 60)


main()
