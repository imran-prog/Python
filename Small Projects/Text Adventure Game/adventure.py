# Setup
Option = ["yes", "no"]
direction = ["forward", "backward", "left", "right"]

# Introduction
name = input("Enter Your name, Adventurer: ")
print("Greetings "+ name + ", Let's Get into the Quest")
print("You Find Yourself into the Dark Forest.")
print("Can You find your way through the forest")

# Start Game
response = ""
while response not in Option:
    response = input("Would you like to step into the forest (yes\\no): ")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this adventure, Goodbye", name)
    else:
        print("I didn't understand")

# Second part
response = ""
while response not in Option:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward: ")
    response = response.lower()
    if response == "left":
        print("The bear eats you, farewell " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the forest.")
        quit()
    elif response == "forward":
        print("You can not scale the wall")
        response = ""
    elif response == "backward":
        print("You leave the forest, Goodbye " + name + ".")
        quit()
    else:
        print("I didn't understand")