import random
while True:

 player_score=0
 computer_score=0
 ties=0

 print("choices are : 1. rock , 2. paper , 3.scissors")
 choice =int(input("enter your chioce from 1-3: "))
 if choice ==1:
    player_choice ="rock"
 elif choice ==2:
    player_choice ="paper"    
 else:
    player_choice ="scissor"    
 print("player's choice is:" ,player_choice)   



 print( "now it's computer choice")
 computer =random.randint(0,2)
 if computer ==1:
    computer_choice="rock"
 elif computer ==2:
    computer_choice="paper"    
 else :
    computer_choice ="scissor"
 print("computer's choice is",computer_choice)



 if(player_choice == computer_choice):
  print("it's a tie!")
  result="ties"

 elif((player_choice =="paper"and computer_choice =="rock")or(player_choice =="rock"and computer_choice =="paper")):
  print("paper win !")
  result ="paper"

 elif ((player_choice =="scissor"and computer_choice =="rock")or(player_choice =="rock"and computer_choice =="scissor")):
  print("rock wins!")
  result ="rock"

 else :
    print("scissor win!") 
    result="scissor"

 if result =="ties":
    ties +=1
 elif result ==player_choice:
    player_score +=1
    print("player win!")
 else :
    computer_score +=1
    print("computer win!")


 print("score are")
 print("player's  score is: ",player_score)
 print("computer's score is: ",computer_score)
 print("ties are: ",ties)


 repeat =input("Do you want to play again ?")
 if repeat == "NO"or repeat =="no" :
   break

  
print("Game over!")  
print("Thanks for playing")
