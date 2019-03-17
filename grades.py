import sys

while True:
    
    def grade(x):
        if x > 100:
            print("Error")
        elif x >= 90 and x <= 100:
            print("A")
        elif x >= 80 and x <= 89:
            print("B")
        elif x >= 70 and x <= 79:
            print("C")
        elif x >= 60 and x <= 69:
            print("D")
        elif x <= 59:
            print("F")


    x = int(input("Enter your grade percentage: " + "%"))

    grade(x)
