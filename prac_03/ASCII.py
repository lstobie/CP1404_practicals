def main():
    LOWER_LIMIT = 33
    UPPER_LIMIT = 127
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    cord = int(input("Enter a number between {} and {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
    if LOWER_LIMIT <= cord <= UPPER_LIMIT:
        print("The character for {} is {}".format(cord, chr(cord)))
    else:
        print("invalid")
    for i in range(LOWER_LIMIT, UPPER_LIMIT + 1):
        print("{0:>3}{1:>10}".format(i, chr(i)))
    # I only know data frames can edit column numbers unless we want an if/elif/elif... code with limits


main()
