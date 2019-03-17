import random

#define cointoss
def cointoss(number_of_flips):
    
    #initialize
    heads = 0
    tails = 0
    
    #simulate coin flipping by generating a random number between 1 and 2
    for i in range(0, number_of_flips):
        coin = int(random.random() * 2) + 1

        if coin == 1:
            heads += 1
        else:
            tails += 1
            
    #print reseults: number_of_flips, heads & tails
    print("Total number of coin flips: " + "{:,}".format(number_of_flips))
    print("Total number of heads: " + "{:,}".format(heads))
    print("Total number of tails: " + "{:,}".format(tails))

#infinite loop asking user for a number_of_flips and printing results of the cointoss function
while True:
    
    number_of_flips = int(input("Enter a number of time\'s to flip the coin: "))

    cointoss(number_of_flips)
    
