#initialize input list of numbers
number_list = []

while True:

    #define and calculate average
    def avg(number_list):
        return sum(number_list) / len(number_list)

    #take up to 7 user input and add to number_list
    # and then print average of all 7 inputs.
    while len(number_list) < 7:
        number_list.append(int(input("Please enter a number: ")))
    else:
        print("The average of the seven numbers you entered is: "
              + str(avg(number_list)))
        print(number_list)
        number_list = []

