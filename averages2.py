##intialization
import sys
import time

numbers_list = []

print("\n")


##timer for loading the program (visual effect)
for i in range(3,0,-1):
    sys.stdout.write(str(i) + " ")
    time.sleep(.4)
    if i < 2:
        sys.stdout.write(".")
        time.sleep(.4)
        sys.stdout.write(".")
        time.sleep(.4)    
        print(".\n")
        time.sleep(1)
        break
    

##infinite loop(entire program)
while True:


    ##infinite loop for exception handling for first input question
    ## reads input for how many numbers to average
    while True:

        try:

            print("How many numbers would you like to average?")
            time.sleep(1.5)
            y = int(input("Must be a minimum of 7: "))
            y = int(y)
            break
        
        except ValueError:
           
            print("Invalid Input...")
            time.sleep(1.5)


    ##defines average as a function
    def avg(numbers_list):
        return sum(numbers_list) / len(numbers_list)


    ##infinite loop for exception handling for second input question
    ## loop structure: reading input from first question and multiple
    ## inputs from second question, calculating, and printing average
    ## of total numbers entered
    while True:

        try:
            
            while y < 7:
                print("Must be a minumum of 7...")
                time.sleep(1.5)
                y = int(input("Please try again: "))
            while y != len(numbers_list):
                numbers_list.append(int(input("Enter a number: ")))
            else:
                print(numbers_list)
                time.sleep(1.5)
                print("The average of the " + str(y) + " number\'s you"
                      " entered is: " + str(avg(numbers_list)))
                time.sleep(2)
                y = int(y)
                break

        except ValueError:
            print("Invalid Input...")
            time.sleep(1.5)

                
            


                

