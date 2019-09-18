"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def bonus_calc():
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        sale_bonus = sales * 0.1
    else:
        sale_bonus = sales * 0.15
    print(sale_bonus, "is your bonus")


bonus_calc()
