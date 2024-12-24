import random
print("*********************************************************")
print("*********************************************************")
print("***                                                   ***")
print("***              WELCOME STRANGER                     ***")
print("***                   TO A                            ***")
print("***              NUMBER GUESSING                      ***")
print("***                   GAME                            ***")
print("***                                                   ***")
print("*********************************************************")
print("*********************************************************")

answer= random.randint(0,25)

print(answer)

def easy_mode():
    print("PLEASE GUESS A NUMBER BELOW 25")

    try:

        user_guess = int(input("> "))

        if user_guess == answer:
             print("\n***You have won, but at what cost???")

        elif user_guess > answer:
             print("@@@You went higher than the actual answer@@@\n")
             easy_mode()

        elif user_guess < answer:
             print("@@@You went lower than the actual answer@@@\n")
             easy_mode()


    except ValueError:
         print("!!!Please enter a number!!!")
         easy_mode()

def hard_mode():
    print("PLEASE GUESS A NUMBER BELOW 25")

    try:
        tries = 0
        while tries < 5:
             user_guess = int(input("> "))

             if user_guess == answer:
                print() 
                print("\n***You have won, but at what cost???")
                break

             elif user_guess > answer:
                print("@@@You went higher than the actual answer@@@\n")
                tries += 1
                if tries == 5:
                    print(f"\n@@@You failed at guessing the correct number. You had {tries} tries@@@")
                else:
                    print("PLEASE GUESS THE NUMBER: ")
            
             elif user_guess < answer:
                print("@@@You went lower than the actual answer@@@\n")
                tries += 1
                if tries == 5:
                    print(f"\n@@@You failed at guessing the correct number. You had {tries} tries@@@")
                else:
                    print("PLEASE GUESS THE NUMBER: ")


    except ValueError:
         print("!!!Please enter a number!!!")
         hard_mode()



def pre_game():
    print("How would you like to play? EASY or HARD?")
    print("Press 1 for EASY and 2 for HARD and 3 for HELP")
    operation = input(">")

    if operation == "1":
        easy_mode()

    elif operation =="2":
        hard_mode()

    elif operation == "3":
        print("\n***In EASY mode you have unlimited tries.***\n***And in HARD mode, you have only five tries")
        pre_game()

pre_game()



