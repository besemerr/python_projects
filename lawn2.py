while True:
    while True:
        try:
            #step 1: compute area of lawn1_area
            lawn1_area = int(input("Enter (Length) of Lawn(1): ")) * int(input("Enter (Width) of Lawn(1): "))
            break
        except ValueError:
            print("Invalid Input...")
    while True:
        try:      
            #step 2: compute are of lawn2_area
            lawn2_area = int(input("Enter (Length) of Lawn(2): ")) * int(input("Enter (Width) of Lawn(2): "))
            break
        except ValueError:
            print("Invalid Input...")
    while True:
        try:
            #step 3: compute the cost per sqft
            cost_per_sqft = float(input("Enter the cost of sod per Sqft: $"))
            break
        except ValueError:
            print("Invalid Input...")
    while True:
        try:
            #step 4: compute total cost per sqft
            total_sod_cost = (lawn1_area + lawn2_area) * cost_per_sqft
            break
        except ValueError:
            print("Invalid Input...")

    #step 5: print total cost to sod lawn1 & lawn2
    print("The area of lawn #1: " + "{:,}".format(lawn1_area) + " Sqft"
          "\nThe area of lawn #2: " + "{:,}".format(lawn2_area) + " Sqft"
          "\nThe cost per Sqft: " + "${:,.2f}".format(cost_per_sqft) + "\nThe total"
          " cost to sod both lawn\'s: " + "${:,.2f}".format(total_sod_cost))

    input()
