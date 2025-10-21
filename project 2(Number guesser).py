import random

top_of_range = input(f"please enter the range: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print(f"please enter a number greater than 0")
        quit()

else:
    print(f"please enter a number next time!")
    quit()


random_number = random.randrange( 0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input(f"please enter a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else :
        print(f"please enter a number next time!")
        continue

    if user_guess == random_number:
        print(f"You guesses it right!")
        break
        
    elif user_guess > random_number:
        print(f"Think a bit lower!")

    else:
        print(f"think a bit higher!")

    if guesses == 1:
        print(f"you got it in a single guess!")

    else:
        print(f"you got it right in {guesses} guessess!")



    





    