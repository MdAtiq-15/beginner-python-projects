import random

def guess_the_number():
    rand_number = random.randint(1, 100)
    user_attempts = 0

    print("Hello\n")
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