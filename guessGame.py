# Guess the number woohoo

import random
import time

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

print('The number is ' + str(secretNumber))

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
# TODO: only print too low/high if guesses remain
    if guess < secretNumber:
        print('Too low.')
    elif guess > secretNumber:
        print('Too high.')
    else:
        break # correct guess

if guess == secretNumber:
    print('Good job ' + name + '!')
else:
    print('Correct!')
    time.sleep(3)
    print('NOT.')
    time.sleep(1)
    print('The number I was thinking of was ' + str(secretNumber))


print('That was ' + ('only ' if guessesTaken<5 else '') + str(guessesTaken)+ ' guesses.')
