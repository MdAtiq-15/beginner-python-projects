import random

moves = {
    "r": "🪨", 
    "p": "📄", 
    "s": "✂️"
    }

round_counter = 1
player_round_wins = 0
computer_round_wins = 0

while round_counter <= 3:
    print(f"ROUND {round_counter}")
    user = input("Rock, Paper or Scissors? (r/p/s): ").strip().lower()
    computer = random.choice(list(moves.keys()))

    print(f"\nYou chose {moves[user]}")
    print(f"Computer chose {moves[computer]}")

    if user == computer:
        print("It's a tie!")

    elif (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        print("You win!\n")
        player_round_wins += 1

    else:
        print("You lose!\n")
        computer_round_wins += 1

    # Check winner
    if player_round_wins == 2:
        print("Player wins the game!")
        break
    elif computer_round_wins == 2:
        print("Computer wins the game!")
        break
    elif round_counter == 3:  # Only reaches here if it's 1-1 going into last round
        if player_round_wins > computer_round_wins:
            print("Player wins the game!")
        elif computer_round_wins > player_round_wins:
            print("Computer wins the game!")
        else:
            print("Round tied!")



    # play_again = input("Continue? (y/n): ")
    print("+", "-" * 30, "+")
    # if play_again != "y":
    #     break

    round_counter += 1
    
