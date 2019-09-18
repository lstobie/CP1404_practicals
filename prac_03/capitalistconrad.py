import random

MAX_INCREASE = random.uniform(0, 0.175)  # 10%
MAX_DECREASE = random.uniform(0, 0.05)  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = random.uniform(8, 12)
INITIAL_DAY = 0
out_file = open("OUTPUT_FILE.txt", 'w')

day = INITIAL_DAY
price = INITIAL_PRICE
print("${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
    day += 1
    price *= (1 + price_change)
    print("On day {} price is ${:,.2f}".format(day, price), file=out_file)
out_file.close()
