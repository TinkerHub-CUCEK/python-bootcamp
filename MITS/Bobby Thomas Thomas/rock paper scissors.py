import random

player = input("Enter your choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)
print(f"\nYou chose {player}, computer chose {computer}.\n")

if player == computer:
    print(f"Both players selected {player}. It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif player == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose.")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose.")
else:
    print("try again")

