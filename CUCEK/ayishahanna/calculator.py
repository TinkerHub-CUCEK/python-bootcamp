print("_MINI CALCULATOR_")
while True:
  print("select an option")    
  print("1.add")
  print("2.subtrat")
  print("3.multiply")
  print("4.divide")
  print("5.exit")


  choice = input("enter the choice : ")
  if choice =="5":
    print("sorry! EXIT")
    break
  
  
  a =float(input("enter number 1: "))
  b =float(input("enter number 2: "))

  if choice =="1":
    print(a, "+", b ,"=", (a+b))

  elif choice =="2":
    print(a, "-" , b ,"=", (a-b))

  elif choice =="3":
    print(a, "*", b ,"=",(a*b))

  elif choice =="4":
    if b == 0:
        print("divide by zero is error")
    else:
        print(a,"/", b ,"=",(a/b))  
  
   
