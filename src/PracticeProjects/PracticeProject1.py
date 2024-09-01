from math import *
import random 


#Game Function 
def Game(State, playersStats):
    print_header("IT'S GAME TIMEEEE!") 

    #Player Selection  
    while(State):
        user_input = input("Lets play guess the number. Are you player 1, 2, or 3? ")
        if user_input in ['1','2','3']: 
            player = int(user_input) - 1 #-1 is so it fits the proper range as we start with 0 not 1 in a list 
            print(f"{playersStats[player][0]} your current score is: {playersStats[player][1]}") 
            State = False
        else:
                print("\nPlease either type 1, 2, or 3. No strings or other numbers")  
    
    State = True
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
                print(f"Player {str(player+1)} your new score is: {str(playersStats[player][1])}")
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

# Rockpaperscissors Game Funtion
def rockpaperscissors(State, playersStats):
    gamePieces = ["rock", "paper", "scissor"]

    print_header("Time to play ROCK PAPER SCISSORS!!!")

    while(State):
        user_input = input("This game has 2 players. First player, are you player 1, 2, or 3? ")
        if user_input in ['1','2','3']: 
            firstPlayer = int(user_input) - 1 #-1 is so it fits the proper range as we start with 0 not 1 in a list
            print(f"{playersStats[firstPlayer][0]} your current score is: {playersStats[firstPlayer][1]}") 
            State = False
        else:
                print("\nPlease either type 1, 2, or 3. No strings or other numbers") 

    State = True
    #This while statement finds our who are the 2 players playing
    while(State):
        user_input = input("Second player, are you player 1, 2, or 3? ")
        if user_input in ['1','2','3']: 
            secondPlayer = int(user_input) - 1 #-1 is so it fits the proper range as we start with 0 not 1 in a list
            print(f"{playersStats[secondPlayer][0]} your current score is: {playersStats[secondPlayer][1]}") 
            State = False
        else:
                print("\nPlease either type 1, 2, or 3. No strings or other numbers")
    
    State = True
    #This while statement allows the players to choose rock, paper, scissors to see who wins
    while(State):
        firstPlayerGuess = input(f"\nPlayer {firstPlayer+1} please type rock, paper, or scissor: ")
        secondPlayerGuess = input(f"Player {secondPlayer+1} please type rock, paper, or scissor: ")
        if firstPlayerGuess.lower() in gamePieces and secondPlayerGuess.lower() in gamePieces:
            winner = rChecker(firstPlayerGuess, secondPlayerGuess) 
            if winner == "firstPlayer":
                playersStats[firstPlayer][1] += 1
                #firstPlayer += 1
                print (f"\nPlayer {firstPlayer+1} you won!!!")
                print(f"Player {str(firstPlayer+1)} your new score is: {str(playersStats[firstPlayer][1])}")
            elif winner == "secondPlayer":
                print (f"\nPlayer {secondPlayer+1} you won!!!")
                playersStats[secondPlayer][1] += 1
                print(f"Player {str(secondPlayer+1)} your new score is: {str(playersStats[secondPlayer][1])}")
            State = False
        else:
            print("Wrong input by either player 1 or 2, please try again.")
    return playersStats

#This Function checks to see who won
def rChecker(firstPlayerGuess, secondPlayerGuess):
    if firstPlayerGuess == secondPlayerGuess:
        print("Tied!!!")
    elif firstPlayerGuess == "rock" and secondPlayerGuess == "paper":
        return "secondPlayer"
    elif firstPlayerGuess == "paper" and secondPlayerGuess == "scissor":
        return "secondPlayer"
    elif firstPlayerGuess == "scissor" and secondPlayerGuess == "rock":
        return "secondPlayer"
    else:
        return "firstPlayer" 

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
        user_input= input("Do you want to play a guessing game, RockPaperScissors, or use calculator? Type G, R or C:  ") 
        if user_input == "G":
            Game("True",playersStats)
            print_divider
        elif user_input == "R":
            rockpaperscissors("True",playersStats)
        elif user_input == "C":
            Calculator()


main()
