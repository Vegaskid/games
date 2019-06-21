import random

number = random.randint(1, 100)
correct_guess = False
guesses = []

print("I've thought of a random number between 1-100")
print("Can you guess it?")

while correct_guess == False:
    guess = int(input('Please have a guess: '))
    if guess in guesses:
        print("You've already guessed that, try again!")
    elif 1 <= guess <= 100:
        guesses.append(guess)
        if guess < number:
            print("Go higher")
        elif guess > number:
            print("Go lower")
        else:
            correct_guess = True

print("Congrats, you correctly guessed the number, " + str(number))
print("It took you " + str(len(guesses)) + " guesses.")
