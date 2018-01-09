import random
numOfGuesses = 0

print('Hello, what is your name? ')
name = input()

number = random.randint(1,20)
print('I am thinking of a number between 1 and 20 ' ,name, '. ')
print("I'll give you five guesses. ")

while numOfGuesses < 5:
    print ('Take a guess. ')
    guess = input()
    guess = int(guess)

    numOfGuesses = numOfGuesses +1
    if guess < number:
        print('Too low ')
    if guess > number:
        print('Too high ')
    if guess == number:
        break

if guess == number:
    numOfGuesses = str(numOfGuesses)
    print('Great job ', name,', you guessed the number in ', numOfGuesses, 'guesses.')

if guess != number:
    number = str(number)
    print('Wrong, better luck next time! The number was ', number, '. ')
