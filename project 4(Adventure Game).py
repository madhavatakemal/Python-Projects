name = input(f"Please enter your name: ")
print(f"welcome {name} to this adventure!")

answer = input(f"you are on a scerene road, two of the people are waiting for you on either sides whom you choose to follow(plz enter right or left or 'q' to exit the game!): ").lower()
if answer == 'left':
    answer = input(f"you started travelling with the person standing on left,found a river you can cross it by swimming or walk aroung with the guy!(enter swim or walk or 'q' to exit!): ").lower()
    
    if answer == 'swim':
        print(f"In the mid way an alligator attacked you and you lost!")

    elif answer == 'walk':
        answer = input(f"by walking a while you reached a kinddom,its of the man you choose and now he decided to offer you his kingdom or his daughter(Enter kingdom or princess or press q to exit): ").lower()

        if answer == 'kingdom':
            answer = input(f"you choose the kingdom and happily living as a king but after five years the person standing on right approached you for inner wisdom(enter wisdom or kingdom or press 'q' to exit): ").lower()

            if answer == 'wisdom':
                print(f"The person took you on a spiritual path")

            elif answer == 'kingdom':
                print(f"you continued to rule the kingdom throughout the life!")
            elif answer == 'q':
                print(f"Quitting the game!")
                quit()

            else:
                print(f"its and invalid answer,please enter a valid one!")

        elif answer == 'princess':
            print(f"you got married to the beautifull princess and liveed a happy life with her!,though bounded by the responsibilities you never discovered the path of inner wisdom!") 

        elif answer == 'q':
            print(f"Quitting the game!")
            quit()

        else:
            print(f"Invalid answer,choose it correctly!")

    elif answer.lower() == 'q':
        print('Quitting the game!')
        quit()
        
    else:
        print(f"Invalid answer,please enter a valid answer!")

elif answer == 'right':
    answer = input(f"you choose to follow the person standing on right,travelling with him you arrived at a tree and he offered you to become his disciple(enter yes to become and no to let go! or press 'q' to exit): ").lower()

    if answer == 'yes':
        print(f"you became his disciple and followed a path of an ascetic and finally at a point your life you realized the self!")

    elif answer == 'no':
        answer = input(f"for now you felt you are not worthing of becoming his disciple and wanted to become worthy! enter meditate or leave or 'q' to exit!: ").lower()


        if answer == 'meditate':
            print(f"finally you became worthy and followed the foot steps of the person you choose to follow!")
            print(f"The person finally made you his disciple!")

        elif answer == 'leave':
            print(f"you got indulged in the illustions of life and regretted that you better have chosen the life of an ascetic!")
            answer = input(f"the same person came for you again and wanted to make you his disciple(press yes to become or no to leave or 'q to quit): ").lower()

            if answer == 'yes':
                print(f"you  became his disciple and after all of the wordly suffering,and tremendous hard work you realized the self!")

            elif answer == 'no':
                print(f"Not listening to your gut feeling you continued to indulge in illustions forever!")

            elif answer == 'q':
                print(f"Quitting the game!")
                quit()

            else:
                print(f"Invalid answer,enter a valid one!")

        elif answer == 'q':
            print(f"quitting the game!")
            quit()
        

        else:
            print(f"invaild answer,please enter a valid one!")

    elif answer == 'q':
        print(f"Quitting the game!")
        quit()

    else:
        print(f"its an invalid answer please enter a valid one!")

elif answer == 'q':
    print(f"Quitting the game!")
    quit()

else:
    print(f"its an invalid answer please enter a valid one!")

