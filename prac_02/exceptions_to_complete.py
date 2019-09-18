finished = False
result = 0
while not finished:
    try:
        result = int(input("give a result"))
        print(result)
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
