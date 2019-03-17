#intialize instructions, sqft per gallon, numpy, time, & the lists of deadspace
# dimensions
print("Use this program to calculate the amount of paint needed \n"
      "for a given area of a room. \n\nPaint coverage = 100sqft/gal \n"
      "\nDeadspace = Windows or doors not being painted.\n"
      "\nEach wall\'s area is multiplied by 2, assuming each wall"
      "\nhas another adjacent wall with the same dimension\'s.\n\n")

import numpy as np
import time

SqftPerGal = 350
c = []
d = []

#infinite loop (entire program)
while True:

    #def wallarea & deadspacearea as a function
    def WallArea(a1,b1,a2,b2):
        return a1 * b1 * 2 + a2 * b2 * 2

    def DeadspaceArea(c,d):
        array = np.multiply(c, d)
        return int(sum(array))

    #infinite exception handling gathering input for wall area
    while True:
        try:
            a1 = int(input("Enter First Wall (Length): "))
            break
        except ValueError:
            print("Invalid Input...")
            time.sleep(1)

    while True:
        try:
            b1 = int(input("Enter First Wall (Height): "))
            break
        except ValueError:
            print("Invalid Input...")
            time.sleep(1)

    while True:
        try:
            a2 = int(input("Enter Second Wall (Length): "))
            break
        except ValueError:
            print("Invalid Input...")
            time.sleep(1)
            
    while True:
        try:
            b2 = int(input("Enter Second Wall (Height): "))
            break
        except ValueError:
            print("Invalid Input...")
            time.sleep(1)

    #infinite exception handling gathering input to determine how many deadspace's to calculate for total deadspace area       
    while True:
        try:
            w = int(input("\nHow many Deadspace\'s? (window\'s or door\'s): "))
            break
        except ValueError:
            print("Invalid Input...")
            time.sleep(1)

    #repeat deadspace input in range of 'w' with infinite exception handling
    for i in range(w):
        while True:
            try:
                c.append(int(input("Enter a Deadspace (Length): ")))
                break
            except ValueError:
                print("Invalid Input...")
                time.sleep(1)
                
        while True:    
            try:
                d.append(int(input("Enter a Deadspace (Height): ")))
                break
            except ValueError:
                print("Invalid Input...")
                time.sleep(1)
    
                #if there is no deadspace; calculate & print results (how many gallons of paint needed)
                if w == 0:
                    PaintNeeded = WallArea(a1,b1,a2,b2) / SqftPerGal
                    SurfaceArea = WallArea(a1,b1,a2,b2)
                    print("\nThe surface area of the room is " + "{:,}".format(SurfaceArea) + " Sqft."
                          " \nand will require " + "{:,.2f}".format(PaintNeeded) + " gallon\'s of paint.")
                
    #calculate & print results (how many gallons of paint needed) when deadspace is subtracted from wall area
    PaintNeeded = (WallArea(a1,b1,a2,b2) - DeadspaceArea(c,d)) / SqftPerGal
    SurfaceArea = (WallArea(a1,b1,a2,b2) - DeadspaceArea(c,d))

    print("\nThe surface area of the room is " + "{:,}".format(SurfaceArea) + " Sqft."
          " \nand will require " + "{:,.2f}".format(PaintNeeded) + " gallon\'s of paint.")

    input()

    
