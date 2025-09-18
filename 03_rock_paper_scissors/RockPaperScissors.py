import random

moves = {
    "r": "🪨", 
    "p": "📄", 
    "s": "✂️"
    }

while True:
    user = input("Rock, Paper or Scissors? (r/p/s): ").strip().lower()
    computer = random.choice(list(moves.keys()))

    print(f"You chose {moves[user]}")
    print(f"Computer chose {moves[computer]}")

    if user == computer:
        print("It's a tie!")

    elif (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        print("You win!")

    else:
        print("You lose!")
