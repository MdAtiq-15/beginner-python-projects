import random

def guess_the_number():
    print("Hello!\n")
    print("Please choose your range of numbers to guess.\n")

    min_value = int(input("Minimum value:  "))
    max_value = int(input("Maximum value:  "))

    rand_number = random.randint(min_value, max_value)
    user_attempts = 0
    
    user_guess = int(input("Guess the number (between 1 and 100):  "))

    while user_guess != rand_number:
        user_attempts += 1

        if user_guess < rand_number:
            print("Too Low! Try again.")
        else:
            print("Too High! Try again.")

        user_guess = int(input("Guess the number (between 1 and 100):  "))

    print(f"\nCongratulations! You guessed the number in {user_attempts} attempts.\n")

#RUN
guess_the_number()