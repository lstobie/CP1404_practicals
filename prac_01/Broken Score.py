"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def result():
    score = float(input("Enter score: "))
    if score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score >= 0:
        print("Bad")
    else:
        print("Invalid score")


result()

# ctrl alt L
# removes warnings
