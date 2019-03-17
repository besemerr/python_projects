import sys
import random

def string_times_x(input_string, printing_number):
    i = 0
    while i < printing_number:
        input_string = random.range(input_string)
        sys.stdout.write(input_string)
        i = i + 1


string_times_x('hello', 1000)
