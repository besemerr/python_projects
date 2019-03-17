##read wall area, window area, & Sqft per gallon
WallArea = (12 * 8 * 2) + (10 * 8 * 2)
WindowArea = (5 * 3) + (6 * 2)
SqftPerGal = 100

##calculate paint needed to paint entire room minus windows
PaintNeeded = (WallArea - WindowArea) / SqftPerGal

##print result of how much paint is needed for the job
print("Wall Area: " + str(WallArea) + " Sqft")
print("Window Area: " + str(WindowArea) + " Sqft")
print("Sqft Per Gallon: " + str(SqftPerGal) + " Sqft")
print("The amount of paint required: " + str(PaintNeeded) + " Gallons")

