import random

def guessing_game():
    number_to_guess = random.randint(1, 100) 
    attempts = 0
    print(" Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.\n")
            elif guess > number_to_guess:
                print("Too high! Try again.\n")
            else:
                print(f"\n Congratulations! You guessed the number.")
                print(f" Total attempts: {attempts}")
                break
        except ValueError:
            print(" Invalid input. Please enter a number.\n")

guessing_game()
