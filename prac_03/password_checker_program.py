MIN_LENGTH = 10


def main():
    password = get_password()
    print_word(password)


def print_word(password):
    shown_word = ''
    for char in range(0, len(password) + 1):
        shown_word += '*'
    print(shown_word)


def get_password():
    password = input("password?")
    while len(password) < MIN_LENGTH:
        password = input("password length invalid. password?")
    return password


main()
