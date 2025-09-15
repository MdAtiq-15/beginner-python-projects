import random

def guess_the_number():
    print("Hello!\n")
    print("Please choose your range of numbers to guess.\n")

    min_value = int(input("Minimum value:  "))
    max_value = int(input("Maximum value:  "))

    rand_number = random.randint(min_value, max_value)
    user_attempts = 1
    max_attempts = 5
    
    print(f"You have {max_attempts} attempts")
    user_guess = int(input(f"Guess the number (between {min_value} and {max_value}):  "))

    while (user_guess != rand_number) and user_attempts != max_attempts:
        
        if user_guess < rand_number:
            print(f"Too Low! Try again.")
            print(f"{max_attempts - user_attempts} attempts left.\n")
        else:
            print("Too High! Try again.")
            print(f"{max_attempts - user_attempts} attempts left.\n")
        
        user_guess = int(input(f"Guess the number (between {min_value} and {max_value}):  "))
        user_attempts += 1

    if user_attempts == max_attempts:
        print("Game Over!. You ran out of attempts.")
    else:
        print(f"\nCongratulations! You guessed the number in {user_attempts} attempts.\n")

#RUN
guess_the_number()