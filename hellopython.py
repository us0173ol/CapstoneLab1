import random
numOfGuesses = 0
#get users name for interaction
print('Hello, what is your name? ')
name = input()
#computer generates a random number in the range specified
number = random.randint(1,20)
print('I am thinking of a number between 1 and 20 ' ,name, '. ')
print("I'll give you 5 guesses. ")
#limit the number of guesses the user can make
while numOfGuesses < 5:
    print ('Take a guess. ')
    guess = input()
    #make sure guess is an integer
    guess = int(guess)
    #not the greatest error handling here but will improve over time
    #keep count of the guesses, give hints
    numOfGuesses = numOfGuesses +1
    if guess < number:
        print('Too low ')
    if guess > number:
        print('Too high ')
    if guess == number:
        break
#congratulate user if they guess correctly
if guess == number:
    numOfGuesses = str(numOfGuesses)
    print('Great job ', name,', you guessed the number in ', numOfGuesses, 'guesses.')
#give the answer if they dont guess it
if guess != number:
    number = str(number)
    print('Wrong, better luck next time! The number was ', number, '. ')
