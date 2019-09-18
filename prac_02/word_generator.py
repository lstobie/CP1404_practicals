"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HARD_CONSONANTS = "bdfgjklmrsvyz"
ALL_SOFT = "aeiouchn"
SPECIAL = "!@#$%^&*()_+\\"


def main():
    word_length = 8
    word = ""
    word_format = []
    for char in range(0, word_length + 1):
        word_format.append(random.randint(1, 5))
    print(word_format)
    true_format = ''.join((str(e) for e in word_format))
    print(true_format)
    for kind in true_format:
        if kind == "1":
            word += random.choice(CONSONANTS)
        elif kind == "2":
            word += random.choice(VOWELS)
        elif kind == "3":
            word += random.choice(HARD_CONSONANTS)
        elif kind == "4":
            word += random.choice(ALL_SOFT)
        else:
            word += random.choice(SPECIAL)
    print(word)


main()
