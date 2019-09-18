MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            calc_fahrenheit(celsius)
            print("Result for {} F: {:.2f} C".format(fahrenheit, celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calc_celsius(fahrenheit)
            print("Result for {} C: {:.2f} F".format(celsius, fahrenheit))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calc_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def calc_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


main()
