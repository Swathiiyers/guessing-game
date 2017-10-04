"""A number-guessing game."""

# Put your code here
import random

print "Welcome to the game!"
name = raw_input("What's your name? ")

print"Choose a random number, %s" % (name)

# secret_num = random.randint(1, 100)
#print " the secret number is %d" % (secret_num)

# guess = None
# too_high = 100
# too_low = 0
# count = 0


def continue_game(): 
    user_choice = raw_input("Would you like to play again? Say 'yes' or 'no'").lower()
    if user_choice == 'yes':
        guessing_game()
    elif user_choice == 'no':
        return



def guessing_game():
    secret_num = random.randint(1, 100)
    guess = None
    too_high = 100
    too_low = 0
    best_count = 100
    count = 0
    
    while guess != secret_num:
        count = count + 1
        try:
            guess = int(raw_input("Guess the number: "))
            if guess > 100 or guess < 1:
                print "invalid input, WHAT WERE YOU THINKING?! Enter a number between 1 and 100"
                #guess = int(raw_input("Guess the number: ")) 

            elif guess > secret_num:
                too_high = guess
                print "%d too high, guess again" % (guess)

            elif guess < secret_num:
                too_low = guess
                print "%d too low, guess again" % (guess)

        except ValueError:
            print "Enter a valid number!"

    print "You got it! The number is %d"%(guess)
    print "The number of guesses is %d" %(count)
    continue_game()

    if count < best_count:
        best_count = count
        print "The best number of guesses you gave was %d" %(best_count)
       
        
    



guessing_game()

    