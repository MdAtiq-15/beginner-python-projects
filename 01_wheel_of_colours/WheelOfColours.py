import random

colours = ["Red", "Green", "Blue", "Orange", "Yellow", "White"]
num_colours = len(colours)

def wheel_of_colours():
    spin_counter = 0
    results = {}

    print("\nHello! Welcome to Wheel of Colours.")
    print(f"Current colours on the wheel are: {', '.join(colours)} \n") #tells the user of the default colours on the wheel
    print("To spin the wheel type 'spin'")
    print("And to stop type 'stop'\n")

    while True:
        user_command = input("spin/stop:  ").strip().lower()
        if user_command == "stop":
            break
        if user_command != "spin":
            print("❌ Invalid input! Please type 'spin' or 'stop'.")
            continue
        
        spin_counter += 1
        random_colour = random.choice(colours)
        results[random_colour] = results.get(random_colour, 0) + 1

        print(f"🎉 {random_colour} 🎉")
        print(f"Number of spins so far: {spin_counter}\n")

    print("\n--- Spin Results ---\n")
    for key, value in sorted(results.items(), key=lambda item: item[1], reverse=True):
        print(f"{key}: {value}")
    print("\nThank you for using Wheel of Colours!")


# Run the program
wheel_of_colours()