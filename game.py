"""A number-guessing game."""

# Put your code here
import random

print "Welcome to the game!"
name = raw_input("What's your name? ")

print"Choose a random number, %s" % (name)

secret_num = random.randint(1, 100)
#print " the secret number is %d" % (secret_num)

guess = None
too_high = 100
too_low = 0
count = 0

while guess != secret_num:
    count = count + 1
    guess = int(raw_input("Guess the number: "))
    if guess > 100 or guess < 0:
        print "invalid input, WHAT WERE YOU THINKING?! Enter a number between 1 and 100"
        #guess = int(raw_input("Guess the number: ")) 

    elif guess > secret_num:
        too_high = guess
        print "%d too high, guess again" % (guess)

    elif guess < secret_num:
        too_low = guess
        print "%d too low, guess again" % (guess)


print "The guessed number is %d"%(guess)
print "The number of guesses is %d" %(count)