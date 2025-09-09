import random

colours = ["Red", "Green", "Blue"]
num_colours = len(colours)

print("\nHello! Welcome to Wheel of Colours.")
#tells the user of the default colours on the wheel
print(f"Current colours on the wheel are: {', '.join(colours)} \n")
print("To spin the wheel type 'spin'")
print("And to stop type 'stop'")

user_command = input("spin/stop:  ")

while user_command != "stop":
    # '-1' to prevent it from getting index out of range
    # as indexing in list starts from 0 i.e. first value
    random_colour = random.randint(0, num_colours - 1)
    print(colours[random_colour])
    user_command = input("spin/stop:  ")

print("\nThank you using Wheel of Colours!")