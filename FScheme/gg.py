#Guessing game
import random

number = random.randint(1, 10)

player_name = input("Hello there, what is your name?")

print('okay! ' + player_name+ ' I am guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('You have guessed the number in ' + str(number_of_guesses) + 'tries!')
else:
    print('You did not guess the number, The number was ' + str(number))

    