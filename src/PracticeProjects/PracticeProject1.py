from math import *
import random 


#Game Function 
def Game(State, playersStats):
    print_header("IT'S GAME TIMEEEE!")

    #Player Selection
    user_input = input("Lets play guess the number. Are you player 1, 2, or 3? ")
    if user_input in ['1','2','3']: 
        player = int(user_input) - 1 #-1 is so it fits the proper range as we start with 0 not 1 in a list
        print(f"{playersStats[player][0]} your current score is: {playersStats[player][1]}") 
    else:
            print("\nPlease either type 1, 2, or 3. No strings or other numbers") 
    

    #Number Range Selection
    while (State): 
        user_input = input("\nBetween what range of numbers do you want to guess from? Exp: Range of 18 is numbers between 1 - 18. \nType a 1-2 digit number: ")
        if user_input in ('1','2'):
            print ("Sorry, you can't use 0, 1, or any negative numbers")
            State = True
        else:
            State = False
        
    #Pick a random number from the range the user gave.
    randomNum = random.randrange(1,int(user_input))
    print(f"We have a picked random number generated between 1 to {randomNum} with our advance technology")
    print(randomNum)
    State = True
    guess_count = 3
    while (State):
        if guess_count == 0:
            print()
        else:
            print(f"\nTotal Guesses left: {guess_count}")
            user_input = input("Please pick a number: ")
            if int(user_input) == randomNum:
                print("That is correct!!!!\n")
                playersStats[player][1] += 1 
                print("Player " + str(player) + " your new score is: " + str(playersStats[player][1])  )
                State = False
                #Checking if your guess is less than or greater than the actual number. 
            elif int(user_input) > randomNum:
                print("You guess is higher than the actual random number")
                guess_count -= 1
            elif int(user_input) < randomNum:
                print("You guess is lower than the actual random number")
                guess_count -= 1
            else:
                print("Incorrect try again\n")
                guess_count -= 1


    print_divider()
    return playersStats


#Calculator Function
def Calculator():
    # Custom lists for different categories
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numerics = "0123456789"
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/\\"
    math_symbols = "+,-,*,/"

    print_header("Are you ready to calculate!?")
    State = True
    while State:
        State = False
        #user_input = input("Please type either +, -, *, or /: ")
        #if user_input 
        user_input = input("Please put the math equation you want solved, like 2 * 12: ")
        
        if user_input[0] in alphabets and user_input[0] in special_characters:
            State = True
        else:
            for i in user_input:
                if i not in numerics and i not in math_symbols:
                #if i = user-input:
                #elif i in "+, -, *, /":
                    State = True
        if State == True:
            print("Incorrect statement")
        elif State == False:
            math = eval(user_input)
            print(f"{user_input} is {math}")
        return


#Utility Function
def print_divider():
    print("\n" + "*" * 110 + "\n")
    return

def print_header(header_text):
    print("\n" + "=" * 110)
    print(header_text.center(110))
    print("=" * 110 + "\n")
    return 


#Main Function
def main():
    playersStats = [
            ["Player 1",0],
            ["Player 2",0],
            ["Player 3",0]
            ]

    State = True 
    print_header("Salaam")
    while(State):
        user_input= input("Do you want to play a game or use calculator? Type G or C:  ") 
        if user_input == "G":
            Game("True",playersStats)
            print_divider
        elif user_input == "C":
            Calculator()


main()
