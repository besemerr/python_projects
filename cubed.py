def cube(x):
    return x * x * x

cubed = cube(3)

print("Cube = " + str(cubed))

while True:
    cubes = int(input("Type a number to cube: "))
    print(cube(cubes))
