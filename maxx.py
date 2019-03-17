import sys

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

def maxx(a, b, c):

    if a > b and a > c:
        sys.stdout.write(a)
        if b > c:
            sys.stdout.write(", " + int(b))
            sys.stdout.write(", " + int(c))
        else:
            sys.stdout.write(", " + int(c))
            sys.stdout.write(", " + int(b))
    elif b > a and b > c:
        sys.stdout.write(b)
        if a > c:
            sys.stdout.write(", " + int(a))
            sys.stdout.write(", " + int(c))
        else:
            sys.stdout.write(", " + int(c))
            sys.stdout.write(", " + int(a))
    elif c > a and c > b:
        sys.stdout.write(c)
        if a > b:
            sys.stdout.write(", " + int(a))
            sys.stdout.write(", " + int(b))

        else:
            sys.stdout.write(", " + int(b))
            sys.stdout.write(", " + int(a))


maxx(a, b, c)
