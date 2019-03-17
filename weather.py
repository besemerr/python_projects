import random

def wind_speed_calc():

    #windspeed generation module
    windspeed = []
    for i in range (0, 14):
        random_number = int(random.random() * 31)
        windspeed.append(random_number)
        print("Generated Wind Speed Value for Day", i, "is" ,windspeed[i])

    #average windspeed module
    avg = 0
    for i in range(0, 14):
        avg = avg + windspeed[i]
    avg = avg / 14
    print("\n\nThe Average Wind Speed: ", avg)

    #highest windspeed module
    highest_speed = -1
    highest_speed_day = -1
    for i in range(0, 14):
        if windspeed[i] > highest_speed:
            highest_speed = windspeed[i]
            highest_speed_day = i
    print("\n\nThe Highest Wind Speed: ", highest_speed)
    print("The Highest Wind Speed Day: ", highest_speed_day)

    #lowest windspeed module
    lowest_speed = 100
    lowest_speed_day = -1
    for i in range(0, 14):
        if windspeed[i] < lowest_speed:
            lowest_speed = windspeed[i]
            lowest_speed_day = i
    print("\n\nThe Lowest Wind Speed: ", lowest_speed)
    print("The Lowest Wind Speed Day: ", lowest_speed_day, "\n\n")

    #difference between daily windspeed and highest windspeed module
    for i in range(0, 14):
        difference = highest_speed - windspeed[i]
        print("Day", i, "Wind Speed is", difference, "miles less than the Highest Wind Speed.")
        

wind_speed_calc()
