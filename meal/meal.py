def main():

time= input("What time is it(HH:MM) :?)"


def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)
    return hours + (minutes / 60)

if 7:00 <= time <= 8:00:
    print("brekfast)"
elif 13:00 time <= 14:00:
    print("lunch")
elif 19:00 time <= 20:00:
    print("Dinner")
main()
