print(f"Welcome to Tokyo revengers quiz!")

playing = input(f"Do you wanna play? ")

while True:

    if playing.lower() != 'yes':
        quit()

    print(f"Lets start the Tokyo revengers quiz! ")

    name = input(f"please enter your name : ")
    print(f"player {name.lower()},lets start the game")

    score = 0

    Ans1 = input(f"Who was the leader of 'Tokyo manji gang': ")
    if Ans1.lower() == 'mikey':
        print(f"{Ans1} is the right answer!")
        score += 5
    else:
        print(f"Incorrect!")

    Ans2 = input(f"Who was the childhood friend of 'Mikey': ")
    if Ans2.lower() == 'draken':
        print(f"{Ans2} is the right answer!")
        score += 5
    else:
        print(f"Incorrect!")

    Ans3 = input(f"who was the main character in tokyo revengers anime: ")
    if Ans3.lower() == 'takemitchy':
        print(f"{Ans3} is the right answer!")
        score += 5
    else:
        print(f"Incorrect!")

    Ans4 = input(f"Madhava's favourite dialogue from 'Tokyo Revengers': ")
    if Ans4.lower() == 'toman did not lose leader!':
        print(f"{Ans4} is the right answer!")
        score += 5
    else:
        print(f"Incorrect!")

    Ans5 = input(f"which character was overpowered at the last season: ")
    if Ans5.lower() == 'angry':
        print(f"{Ans5} is the right answer!")
        score += 5
    else:
        print(f"Incorrect!")

    print(f"congratulations!,the quiz has completed and you have scored {score} points!")

    ask = input(f"do you play again: ")
    if ask.lower() == 'no':
        print(f"Game has ended!")
        quit()


   

   
        
    

    









    



