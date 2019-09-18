import random

print(dir(random))
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

for i in range(0, 101, 50):
    print("{:>3}".format(i))

print(0 / 0)
