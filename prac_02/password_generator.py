import random


CAPITALS = "QWERTYUIOPASDFGHJKLZXCVBNM"
LOWERCASE = "qwertyuiopasdfghjklzxcvbnm"
NUMERIC = "1234567890"
SPECIAL = """
    `~!@#$%^&*()-_=+[]{}\\|;:'"<>,./?
    """


def main():
    password_length = int(input("how long is this password?"))
    password = ""
    choice_list = [CAPITALS, LOWERCASE, NUMERIC, SPECIAL]
    for i in range(0, password_length):
        char = random.choice(random.choice(choice_list))
        password += char
    print(password)
    while not is_valid_password(password, SPECIAL):
        password = ""
        print("Invalid password!")
        choice_list = [CAPITALS, LOWERCASE, NUMERIC, SPECIAL]
        for i in range(0, password_length):
            char = random.choice(random.choice(choice_list))
            password += char
        print(password)
    print("valid password")


def is_valid_password(password, SPECIAL):
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
        elif char in SPECIAL:
            count_special += 1
        else:
            return False
    if count_lower == 0:
        return False
    if count_upper == 0:
        return False
    if count_digit == 0:
        return False
    if count_special == 0:
        return False
    return True


main()
