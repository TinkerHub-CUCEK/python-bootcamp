import random

def play_game():
  print("Rock-Paper-Scissors!!!")
  print("To play, enter one of the following options:")
  print(" 'R' for Rock")
  print(" 'P' for Paper")
  print(" 'S' for Scissors")
  print("Enter 'Q' to quit the game.\n")
  count=compcount=0
  while True:
    player= input("Enter your move: ")
    player= player.upper()
    if player== 'Q':
      if count>compcount:
          print("You win!")
      elif count==0 and compcount==0:
          print("Exit")
          break
      elif count==compcount:
          print("It's a tie!")
      else:
          print("The computer wins!")
      print("Your score is",count,"and computer score is",compcount)
      print("Thank you for playing! Exit.")
      break
    
    computer_move = random.choice(['R', 'P', 'S'])
    print("Computer move=",computer_move)
    if player != 'R' and player != 'P' and player != 'S':
      print("Invalid move. Please try again.\n")
      continue
    if player == computer_move:
          print("It's a tie!\n")
    elif (player == 'R' and computer_move == 'S') or (player == 'P' and computer_move == 'R') or (player == 'S' and computer_move == 'P'):
          print("you score 1\n")
          count+=1
    else:
          print("computer score 1\n")
          compcount+=1

play_game()
