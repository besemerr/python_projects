import sys

#define discount function
def discount_per_week(original_price):

    #initialize days of the week, discount rate & current price
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    discount_rate = 0.1
    current_price = original_price

    #calculates for every day of the week an additional 10% and then prints results for each day of the week
    for day in days:
        current_price = current_price * (1 - discount_rate)
        sys.stdout.write("The discount price on " + str(day) + " is: ${:,.2f} ".format(current_price) + " \n")

#infinite loop asking user for the original cost of an item and then calling the discount function defined above
while True:
    original_price = float(input("Enter the cost of an item: $"))
    discount_per_week(original_price)
