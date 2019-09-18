

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print("Result for {} C: {:.2f} F".format(celsius, fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("Result for {} F: {:.2f} C".format(fahrenheit, celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")