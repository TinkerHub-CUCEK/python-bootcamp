print("Calculator")
print("----------")
print("Operations provided are:")
print(" '+' for Addition")
print(" '-' for Subtraction")
print(" '*' for Multiplication")
print(" '/' for Division\n")



n=1
while(n==1):
    a=int(input("Enter the first number:"))
    b=int(input("Enter second number:"))
    c=input("Enter the operator(+,-,*,/):")
    if c=='+':
        print("Addition undergoes")
        print("Sum is",a+b,"\n")
    elif c=='-':
        print("Subtraction undergoes")
        print("Difference is",a-b,"\n")
    elif c=='*':
        print("Multiplication undergoes")
        print("Product is",a*b,"\n")
    elif c=='/':
        print("Division undergoes")
        print("Result is",a/b,"\n")
    else:
        print("Invalid Operator!!")
    s=input("Do you want to continue(y/n):")
    if s=='y':
        n=1
    else:
        n=0
        print("Exit")
