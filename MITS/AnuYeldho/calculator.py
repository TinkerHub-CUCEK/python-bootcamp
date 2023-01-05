def add(a,b):
    sum = a+b
    print("Sum: ",sum)

def sub(a,b):
    diff = a-b
    print("Difference: ",diff)

def mul(a,b):
    pro = a*b
    print("Product: ",pro)

def div(a,b):
    if(b==0):
        print("Undefined")
    else:
        quo = a//b
        rem = a%b
        print("Quotient: ",quo)
        print("Remainder: ",rem)

print('*** CALCULATOR ***')

print("\nOPERATIONS : \n")
print(" +   ADDITION ")
print(" -   SUBTRACTION ")
print(" *   MULTIPLICATION ")
print(" /   DIVISION ")
c = 'y'
while(c == 'y'):
    ch = input("\nEnter your choice( + - * / ): ")
    if(ch == '+'):
        x = int(input("Enter operand 1: "))
        y = int(input("Enter operand 2: "))
        add(x,y)
    elif(ch == '-'):
        x = int(input("Enter operand 1: "))
        y = int(input("Enter operand 2: "))
        sub(x,y)
    elif(ch == '*'):
        x = int(input("Enter operand 1: "))
        y = int(input("Enter operand 2: "))
        mul(x,y)
    elif(ch == '/'):
        x = int(input("Enter operand 1: "))
        y = int(input("Enter operand 2: "))
        div(x,y)
    else:
        print(" WRONG OPERATION !")
    c = input("\nDo you want to continue ? (y/n): ")
    if(c == 'n'):
        break
