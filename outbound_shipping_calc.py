##initialize
import numpy as np
import time
import sys
import os

os.system("mode con cols=50 lines=28")

##defining basic weight per item variables
pallet_weight = 33 #lbs

eleven_ounce_weight = .840 #lbs

fifteen_ounce_weight = 1.138 #lbs

thirty_two_ounce_weight = 2.354 #lbs

fifty_nine_ounce_weight = 4.138 #lbs


##infinite loop
while True:

    print("\n\n           Outbound Shipping Calculator           \n\n")


    ##loop exception handling gathering input for eleven ounce bottles
    while True:
        try:
            eleven_ounce_qty = int(input("Enter Quantity   (11oz 6-Pack): "))

            eleven_ounce_total_weight = (eleven_ounce_weight * 6 * eleven_ounce_qty)

            print("Total Weight (" + "{:,}".format(eleven_ounce_qty) + ") (11oz 6-Pack):("  + "{:,.2f}".format(eleven_ounce_total_weight) + " lbs)")
            break
        
        except ValueError:
            print("Invalid Input...")
            time.sleep(1)

            
    ##loop exception handling gathering input for fifteen ounce bottle weight
    while True:
        try:
            fifteen_ounce_qty = int(input("\nEnter Quantity   (15oz 6-Pack): "))

            fifteen_ounce_total_weight = (fifteen_ounce_weight * 6 * fifteen_ounce_qty)

            print("Total Weight (" + "{:,}".format(fifteen_ounce_qty) + ") (15oz 6-Pack):(" + "{:,.2f}".format(fifteen_ounce_total_weight) + " lbs)")
            break

        except ValueError:
            print("Invalid Input...")
            time.sleep(1)


    ##loop exception handling gathering input for thirty-two ounce bottle weight       
    while True:
        try:
            thirty_two_ounce_qty = int(input("\nEnter Quantity   (32oz 6-Pack): "))

            thirty_two_ounce_total_weight = (thirty_two_ounce_weight * 6 * thirty_two_ounce_qty)

            print("Total Weight (" + "{:,}".format(thirty_two_ounce_qty) + ") (32oz 6-Pack):(" + "{:,.2f}".format(thirty_two_ounce_total_weight) + " lbs)")
            break

        except ValueError:
            print("Invalid Input...")
            time.sleep(1)


    ##loop exception handling gathering input for fifty-nine ounce bottle weight  
    while True:
        try:
            fifty_nine_ounce_qty = int(input("\nEnter Quantity   (59oz 4-Pack): "))

            fifty_nine_ounce_total_weight = (fifty_nine_ounce_weight * 4 * fifty_nine_ounce_qty)

            print("Total Weight (" + "{:,}".format(fifty_nine_ounce_qty) + ") (59oz 4-Pack):(" + "{:,.2f}".format(fifty_nine_ounce_total_weight) + " lbs)")
            break

        except ValueError:
            print("Invalid Input...")
            time.sleep(1)


    ##loop exception handling gathering input for pallet weight        
    while True:
        try:
            pallet_qty = int(input("\nEnter Quantity (Pallets): "))

            pallet_total_weight = (pallet_weight * pallet_qty)

            print("Total Weight (" + str(pallet_qty) + ") pallets:(" + str(pallet_total_weight) + " lbs)")

            ##printing required output
            total_gross_weight = (eleven_ounce_total_weight + fifteen_ounce_total_weight + thirty_two_ounce_total_weight + fifty_nine_ounce_total_weight + pallet_total_weight)


            print("\nTotal Gross Weight: (" + "{:,.2f}".format(total_gross_weight) + " lbs)\n")
            break

        except ValueError:
            print("Invalid Input...")
            time.sleep(1)

    
    ##exit loop
    while True:
        end = input("\nExit {y/n]: ")

        if end.lower().startswith("n"):
            break
        elif end.lower().startswith("y"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                   \n\n                 Evolution Fresh")
            time.sleep(2.8)
            sys.exit()
        else:
            print("Invalid Input...")
            
