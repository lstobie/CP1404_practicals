try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# non-integer input other than 0 for denominator
# When will a ZeroDivisionError occur?
# denominator input is 0
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# while/if/else conditions
