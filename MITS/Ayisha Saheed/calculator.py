while True:

    a = int(input("Enter the first number a= "))
    b = int(input("Enter the second number b= "))

    op = input(
        "choose from the following operations: +,-,*,/,% =   "
    )
    print("RESULT: ")
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    elif op == '%':
        print(a % b)
    else:
        print("invalid input")

    c = input("CONTINUE CALCULATION? Y or N:   ")
    if c == 'N':
        break
