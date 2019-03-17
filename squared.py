def square(x):
    square = x * x
    return square

squared = square(2)

print("Squared = " + str(squared))

while True:
    squares = int(input("Type a number to square: "))
    print(square(squares))

