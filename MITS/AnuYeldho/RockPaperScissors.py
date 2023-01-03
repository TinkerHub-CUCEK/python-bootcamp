import random

print("*** ROCK PAPER SCISSORS ***")

print("\nMOVES : \n")
print(" r  :  ROCK")
print(" p  :  PAPER")
print(" s  :  SCISSORS")
moves = ['r','p','s']
compScore = 0
yourScore = 0
n = int(input("\nEnter number of rounds: "))

for i in range(n):
  you = input("\nEnter your move(r/p/s): ")
  comp = random.choice(moves)
  print("Computer's move:",comp)
  if(you=='r' and comp=='p'):
    compScore += 1
  elif(you=='p' and comp=='r'):
    yourScore += 1
  elif(you=='p' and comp=='s'):
    compScore += 1
  elif(you=='s' and comp=='p'):
    yourScore += 1
  elif(you=='s' and comp=='r'):
    compScore += 1
  elif(you=='r' and comp=='s'):
    yourScore += 1
  else:
    pass

print("\nSCORE BOARD : \n")
print("Computer \t You")
print(compScore,' \t\t',yourScore)
if(compScore == yourScore):
  print("\n--- DRAW MATCH --- ")
elif(compScore > yourScore):
  print("\n--- COMPUTER WON --- ")
else:
  print("\n--- YOU WON --- ")
