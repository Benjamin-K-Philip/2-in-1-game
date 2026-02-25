



while True:
    print("\nWelcome to the 2 in 1 game")
    print("\nMenu Of 2 different games")
    print("1.Mad Libs Generator")
    print("2.Rock Paper Scissors")
    choice=input("\nEnter which game you want to play(1/2):")

    if choice=='1':   
        print('\n----Mad Libs Generator----')
        verb_1 = input("Enter a verb of choice,and press enter:")
        adj_1 = input("Enter a adjective of choice, and press enter:")
        verb_2 = input("Enter second verb of choice, and press enter:")
        body_part = input("Enter a body part name of choice, and press enter:")
        adverb = input("Enter an adverb of choice for eg:- extremly,swiftly,lazily, and press enter:")
        body_part_2 = input("Enter any body name of your choice,and press enter:")
        noun = input("Enter a noun of choice, and press enter:")
        verb_3 = input("Enter the third verb of choice, and press enter:")
        animal = input("Enter name of any animal of choice, and press enter:")
        noun_2 = input("Enter an noun of choice , and press enter:")
        verb_4 = input("Enter the fourth verb of choice, and press enter:")
        adj_2 = input("Enter an adjective of chioce, and press enter:")
        color = input("Enter any color name, and press enter:")
        story='\nMost doctors agree that bicycles of ' +verb_1+ ' is a/an ' +adj_1+ ' form of exercise '+verb_2+' a bicycle enables you to develop your '+body_part+' muscles as well as '+adverb+' increase the rate of a '+body_part_2+' beat.More '+noun+' around the world '+verb_3+' bicycles than drive '+animal+' no matter what kind of '+noun_2+' you '+verb_4+' always be sure to wear a/an '+adj_2+' helmet.Make sure to have '+color+" reflectors too! "
        print(story)

    elif choice=='2':
        import random
        print(" \n---------------------")
        print("| Rock Paper Scissors |")
        print(" ---------------------")
        listch = ["R", "P", "S"]
        user_score = 0
        computer_score = 0
        i = 1
        chance = int(input("\nHow many time you want to play (no. of chances): "))

        while i <= chance:
            computer = str(random.choice(listch))
            user = input("\nEnter Rock, Paper, Scissors (key to press: R,P,S): ").upper()
            if user == computer:
                print("\n Entries entered are same")
            elif user == "R":
                print("Entry done by the computer: ", computer)
                if computer == "P":
                    print("\n You lose! Paper covers Rock")
                    computer_score += 1
                else:
                    print("\n You win! Rock smashes Scissors")
                    user_score += 1
            elif user == "P":
                print("Entry done by the computer: ", computer)
                if computer == "S":
                    print("\n You lose! Scissor cuts Paper")
                    computer_score += 1
                else:
                    print("\n You win! Paper covers Rock")
                    user_score += 1
            elif user== "S":
                print("Entry done by the computer: ", computer)
                if computer == "R":
                    print("\n You lose! Rock smashes Scissors")
                    computer_score += 1
                else:
                    print("\n You win! Scissor cut Paper")
                    user_score += 1
            else:
                print("Invalid entry")

            print("\n\t******ScoreBoard******")
            print(f"\t You: {user_score} | Computer: {computer_score}")
            print("\t**********************")
            print(f"Game No:[{i}]")
            print("========================================================")
            i += 1
        print("\n\n##### Game Over #####")
        print("*******************************************")
        if user_score < computer_score:
            print(
                "\n Sorry You lose the game and the computer wins the game with a score of ", computer_score
            )
        elif user_score == computer_score:
            print("\n The Game is tied ")
        else:
            print("\n You Win the Game with a score of ", user_score, "")
    else:
        print("\n Worng choice")
    

    repeat=input("\n Do you want to continue? (y/n):")
    if repeat=='n'or repeat=='N' or repeat=='No' or repeat=='NO' or repeat=='no':
       print("\n Thank you for playing the game")
       break
 
    
