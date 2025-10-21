import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input(f"Type Rock/Paper/Scissors or 'Q' to quit: ").lower()
    if user_input == 'q':
        print(f'exiting the game!')
        break
       

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock = 0,paper = 1,scissors = 2
    computer_pick = options[random_number]
    print("computer_picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print(f"you won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print('you won!')
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print('you won!')

    elif user_input == 'paper' and computer_pick == 'paper':
        print(f"its same,pick again!")

    elif user_input == 'scissors' and computer_pick == 'scissors':
        print(f"its same,pick again!")

    elif user_input == 'rock' and computer_pick == ' rock':
        print(f"its same,pick again!")

    else:
        print(f"you lost!")
        computer_wins += 1


print(f"user score = {user_wins},computer score = {computer_wins} ")
    
print("Good Bye!")


        