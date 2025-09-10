import random

colours = ["Red", "Green", "Blue"]
num_colours = len(colours)
spin_counter = 0
results = {}

def update_results(colour):
    # check if the colour exists in the dictionary
    if colour not in results:
        results[colour] = 1
        return
    
    results[colour] = results.get(colour) + 1

print("\nHello! Welcome to Wheel of Colours.")
#tells the user of the default colours on the wheel
print(f"Current colours on the wheel are: {', '.join(colours)} \n")
print("To spin the wheel type 'spin'")
print("And to stop type 'stop'\n")

user_command = input("spin/stop:  ")

while user_command != "stop":
    # '-1' to prevent it from getting index out of range
    # as indexing in list starts from 0 i.e. first value
    random_colour_index = random.randint(0, num_colours - 1)

    spin_counter += 1
    update_results(colours[random_colour_index])

    print(f"🎉 {colours[random_colour_index]} 🎉")
    print(f"\nNumber of spins = {spin_counter}\n")
    user_command = input("spin/stop:  ")

print("\n Results: \n")
for key, value in results.items():
    print(f"{key} : {value}")
print("\nThank you using Wheel of Colours!")