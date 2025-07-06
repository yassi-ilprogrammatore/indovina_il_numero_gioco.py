import random
import time
number = random.randint(1, 50)
tentative = 0
start_time = time.time()
while True:
    try:
        guess = int(input("Guess a number between 1 and 50: "))
        tentative += 1
        if guess < 1 or guess > 50:
            print("Please guess a number between 1 and 50.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            if tentative == 1:
                print("You guessed it on your first try!")
            else:
                print(f"It took you {tentative} attempts.")
            risposta = input("Do you want to play again? (yes/no): ").strip().lower()
            if risposta == 'yes':
                 number = random.randint(1, 50)
                 tentative = 0
            else:
                print("Thanks for playing!")
                end_time = time.time()
                print(f"You played for {end_time - start_time:.2f} seconds.")
                print("Goodbye!")
                break
    except ValueError:
        print("That's not a valid number. Please enter an integer between 1 and 10.")
        continue

