#step 1: compute area of lawn1_area
lawn1_area = 12 * 30

#step 2: compute are of lawn2_area
lawn2_area = 20 * 40

#step 3: compute the cost per sqft
cost_per_sqft = 3

#step 4: compute total cost per sqft
total_sod_cost = (lawn1_area + lawn2_area) * cost_per_sqft

#step 5: print total cost to sod lawn1 & lawn2
print("The area of lawn #1: " + str(lawn1_area) + " Sqft"
      "\nThe area of lawn #2: " + str(lawn2_area) + " Sqft"
      "\nThe cost per Sqft: " + "${:,.2f}".format(cost_per_sqft) + "\nThe total"
      " cost to sod both lawn\'s: " + "${:,.2f}".format(total_sod_cost))
