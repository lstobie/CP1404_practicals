MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    if len(password) not in range(MIN_LENGTH, MAX_LENGTH + 1):
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isnumeric():
            count_digit += 1
        elif char.isalpha():
            if char.isupper():
                count_upper += 1
            else:
                count_lower += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
        else:
            return False
    if count_lower == 0:
        return False
    if count_upper == 0:
        return False
    if count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED is True:
        if count_special == 0:
            return False
        else:
            pass
    return True


main()
