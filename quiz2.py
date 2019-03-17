##while True:
##    
##    amount = float(input("Enter item(s) amount: $"))
##    
##    if amount > 100:
##        amount = amount - amount * .10
##        print("\nBecause you spent over $100.00 you received a 10% discount.\n"
##              "Your new total for your item(s) is: " + "${:,.2f}".format(amount))
##        input()
##    elif amount < 100 and amount > 50:
##        amount = amount - amount * .05
##        print("\nBecause you spent over $50.00 you received a 5% discount.\n"
##              "Your new total for your item(s) is: " + "${:,.2f}".format(amount))
##        input()
##    elif amount < 50:
##        amount = amount
##        print("\nBecause you spent under $50.00 no discount applies.\n"
##              "Your total for your item(s) is still: " + "${:,.2f}".format(amount))
##        input()
    
def total_sod_cost(a, b, c):
    sod_cost = a * b * c
    return sod_cost

print("${:,.2f}".format(total_sod_cost(10, 20, 3)))

    
