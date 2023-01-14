def addition ():

    print("Addition")

    n = float(input("Enter the number: "))
    b = float(input("Enter the second number: "))

    return n+b

def subtraction ():

    print("Subtraction");

    n = float(input("Enter the number: "))
    b = float(input("Enter the second number: "))

    return n-b

def multiplication ():

    print("Multiplication")

    n = float(input("Enter the number: "))
    b = float(input("Enter the second number: "))

    return n*b
def division():

    
    n = float(input("Enter the number: "))
    b = float(input("Enter the second number: "))

    return n/b

# main...

while True:

    res = []

    print(" My calculator")

    print(" Enter 'a' for addition")

    print(" Enter 's' for substraction")

    print(" Enter 'm' for multiplication")

    print(" Enter 'd' for division")

    print(" Enter 'q' for quit")

    c = input(" ")

    if c != 'q':

        if c == 'a':

            res = addition()

            print("Ans = ", res)

        elif c == 's':

            res = subtraction()

            print("Ans = ", res)

        elif c == 'm':

            res = multiplication()

            print("Ans = ", res)

        elif c == 'd':

            res = division()

            print("Ans = ", res)

    else:

        print ("Quitting...")