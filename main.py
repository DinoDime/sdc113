import random


# Random is imported to allow use of randint for random number generation

def title():
    print("This program plays Guess the Number with the user. A random number between "
          "1 and 10 will be generated. The user will guess the number. "
          "If the guess is too low or too high, a message indicating so will be printed. "
          "If the user guesses correctly, 'You guessed it' will be printed.")


# The title function exists to outline the purpose of the assignment

def play_game():
    number = random.randint(1, 10)
    while True:
        guess = input("Guess a number between 1 and 10: ")
        guess = int(guess)
        if guess == number:
            print("You guessed it!")
            break
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")


# This function is the actual game play. Randint is used to generate a random number between 1 and 10, inclusive of
# both 1 and 10. The guess variable gathers input from the user. This input is a string. guess = (int)guess turns the
# string into an int so it can be compared to the random number. Break is used to end the while loop. Without it,
# it would be a never ending loop.

def main():
    title()
    go_again = "yes"
    while True:
        play_game()
        play_again = input("Do you want to play again? Enter 'yes' or 'no' , I")
        if play_again == go_again:
            continue
        else:
            print("Thank you for playing!")
            break


# The main function puts together the other functions and some logic to allow a user to play multiple times.
# Continue is used if a user enters "yes" when prompted, which which has the code go to line 33 and carry onwards
# break is used if a user enters any character(s) other than "yes", which ends the program.

main()
# main is called initiate the game. If main were not called, nothing would print out and the user would be unable to
# play.
