"""A number-guessing game."""

# Put your code here
import random

print "Welcome to the game!"
name = raw_input("What's your name?")
print"Choose a random number"
secret_num = random.randint(1, 100)
print " the secret number is %d" %(secret_num)
guess = None
too_high = 100
too_low = 0
while guess != secret_num:
    guess = (too_high + too_low) / 2
    if guess > secret_num:
        too_high = guess
        print "%d too high, guess again" % (guess)
    if guess < secret_num:
        too_low = guess
        print "%d too low, guess again" % (guess)


print "The guessed number is %d"%(guess)

