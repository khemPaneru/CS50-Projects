
# m= mass in kg

def calculate(m):
    # c = speed of light in m/s

    c = 300000000
    # E = Energy
    E = m * (c ** 2)
    return E


def main():
    m =int(input("Enter mass in kg: " ))
    # "calculate" fun is called
    result = calculate(m)
    print( f"The converted energy {result} in joules")

main()


