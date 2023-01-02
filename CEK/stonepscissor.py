import random
c1=0
c2=0
score=0
c='y'
while c=='y':
    rps=["rock","paper","scissor"]
    print("0:rock")
    print("1:paper")
    print("2:scissor")
    i=random.randint(0,2)
    a=rps[i]
    b=input("Choose from the list")
    print("Computer opts:")
    print(i)
    if a==rps[0]:
        c1=0
    elif a==rps[1]:
        c1=1
    elif a==rps[2]:
        c1=2
    if b==rps[0]:
        c2=0
    elif b==rps[1]:
        c2=1
    elif b==rps[2]:
        c2=2
    if c1>c2:
        print("Computer wins with score:")
        print(c1)
        score=score+c1
    elif c1<c2:
        print("User wins with score:")
        print(c2)
        score=score+c2
    elif c1==c2:
        print("Both have same score")    
    c=input("Continue?(y/n)")
print("score:")
print(score)