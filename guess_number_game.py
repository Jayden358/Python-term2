#Jayden Williams
#10/28/2019
#Guess my number game

#imports
import random

#functions

#gets a number and makes sure its a number and with in the range and returns the number
guesses=0

def get_num_in_range(rmin,rmax):
    num = input("pick a number between " + str(rmin) +" and "+str(rmax)+"\n")
    if num.isdigit():
        num = int(num)
        if num >= rmin and num <= rmax:
            return num
        print("Not a good value")

#menu
def menu():
    #this is my menu to choose difficulty
    print("""

    Welcome to GUESS MY NUMBER game
    please choose an option
    from the list below

    1: Easy
    2: Normal
    3: Hard
    4: Impossible(really hard!!!)
    5: COMPUTER GUESS
    6: Quit
    """)
    #this allows choices
    while True:
        choice = input("")
        if choice == "1":
            return easy()
        elif choice == "2":
            return normal()
        elif choice == "3":
            return hard()
        elif choice == "4":
            return impossible()
        elif choice == "5":
            computer()
        elif choice == "6":
            quit()
        else:
            print("Sorry that is not an option.")





#easy
def easy():
    guesses = 0
    #gets random number 1 through 10
    y = random.randint(1, 10)
    while True:
        #tells user guess a number between 1 through 10
        guess = get_num_in_range(1, 10)

        if guess>y:
            print("guess lower")
        else:
            print("guess higher")

        guesses+=1
        #if user guesses the number
        if guess == y:
            print("you guessed it,Play again? (y or n)")
            answer = input()
            #allows user to play again or quit
            if answer == "y":
                menu()
            elif answer == "n":
                quit()
            else:
                print("Please enter y(yes) or n(no)")

        elif guesses==7:
            print("you lose, Play again? (y or n)")
            answer = input()
            if answer == "y":
                menu()
            elif answer == "n":
                quit()
            else:
                print("Please enter y(yes) or n(no)")

#normal
def normal():
    guesses = 0
    y = random.randint(1, 50)
    while True:
        guess = get_num_in_range(1, 50)

        if guess>y:
            print("guess lower")
        else:
            print("guess higher")

        guesses+=1
        if guess == y:
            print("you guessed it,Play again? (y or n)")
            answer = input()
            if answer == "y":
                menu()
            elif answer == "n":
                quit()
            else:
                print("Please enter y(yes) or n(no)")

        elif guesses==30:

            print("you lose, Play again? (y or n)")
            answer = input()
            if answer == "y":
                menu()
            elif answer == "n":
                quit()
            else:
                print("Please enter y(yes) or n(no)")



#hard
def hard():
    guesses = 0
    y = random.randint(1, 100)
    while True:
        guess = get_num_in_range(1, 100)

        if guess>y:
            print("guess lower")
        else:
            print("guess higher")

        guesses+=1
        if guess == y:
            print("you guessed it,Play again? (y or n)")
            answer = input()
            if answer == "y":
                menu()
            elif answer == "n":
                quit()
            else:
                print("Please enter y(yes) or n(no)")

        elif guesses==50:

            print("you lose, Play again? (y or n)")
            answer = input()
            if answer == "y":
                menu()
            elif answer == "n":
                quit
            else:
                print("Please enter y(yes) or n(no)")

#impossible
def impossible():
    guesses = 0
    y = random.randint(1, 1000)
    while True:
        guess = get_num_in_range(1, 1000)

        if guess > y:
            print("guess lower")
        else:
            print("guess higher")

        guesses += 1
        if guess == y:
            print("you guessed it,Play again? (y or n)")
            answer=input()
            if answer=="y":
                menu()
            elif answer =="n":
                quit()
            else:
                print("Please enter y(yes) or n(no)")

        elif guesses == 500:
            print("you lose, Play again? (y or n)")
            answer = input()
            if answer == "y":
                menu()
            elif answer == "n":
                quit()
            else:
                print("Please enter y(yes) or n(no)")


def computer():
    min=1
    max=100
    guesses=0
    playernum=int(input("Enter a number between 1 and 100 for a computer to guess"))


    guess=random.randint(min,max)

    print("computer guess",guess)
    print("your Number",playernum)
    guesses+=1
    while guess != playernum:
        print("guessing")
        if guess>playernum:
            print("lower")
            max = guess
        elif guesses == 50:
            print("Computer lost")
            quit()
        else:
            print("higher")
            max = guess+1
        print("retrying")
        guess = random.randint(min, max)
        guesses += 1
        print("computer guess",guess)
        print("guess number",guesses)
    print("computer wins")






menu()