import random
while True:
    
    ch1 = input("SELECT ROCK, PAPER, OR SCISSOR:   ")
    print("you chose:")
    print(ch1)
    lst = ["ROCK","PAPER","SCISSOR"]
    
    ch2 = random.choice(lst)
    print("my choice:")
    print(ch2)
    if ch1=="ROCK" and ch2=="PAPER":
        print("YOU LOST...")
    elif ch1=="PAPER" and ch2=="SCISSOR":
        print("YOU LOST...")
    elif ch1=="SCISSOR" and ch2=="ROCK":
        print("YOU LOST...")
    elif ch1=="PAPER" and ch2=="ROCK":
        print("YOU WON!!!!")
    elif ch1=="SCISSOR" and ch2=="PAPER":
        print("YOU WON!!!!")
    elif ch1=="ROCK" and ch2=="SCISSOR":
        print("YOU WON!!!!")
    elif ch1==ch2:
        print("IT'S A TIE")
    else:
        print("try again")
        
    c = input("CONTINUE?? YES or NO: ")
    if c == "NO":
        break
