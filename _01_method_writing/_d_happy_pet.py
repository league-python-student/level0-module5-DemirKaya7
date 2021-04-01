"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


def Walk(petType, petHappiness):
    if petType == "Dog":
        petHappiness += 4
    elif petType == "Cat":
        petHappiness += 1
    elif petType == "Fish":
        petHappiness -= 5
    elif petType == "Bird":
        petHappiness -= 1
    return petHappiness


def Feed(petType, petHappiness):
    if petType == "Dog":
        petHappiness += 3
    elif petType == "Cat":
        petHappiness += 3
    elif petType == "Fish":
        petHappiness += 3
    elif petType == "Bird":
        petHappiness += 3
    return petHappiness


def Pet(petType, petHappiness):
    if petType == "Dog":
        petHappiness += 2
    elif petType == "Cat":
        petHappiness += 2
    elif petType == "Fish":
        petHappiness -= 1
    elif petType == "Bird":
        petHappiness += 2
    return petHappiness


def Bathe (petType, petHappiness):
    if petType == "Dog":
        petHappiness += 1
    elif petType == "Cat":
        petHappiness -= 7
    elif petType == "Fish":
        petHappiness += 4
    elif petType == "Bird":
        petHappiness -= 6
    return petHappiness

if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    window = Tk()
    window.withdraw
    petHappiness = 0
    petType = simpledialog.askstring(title="Select pet type", prompt="Would you like a: Dog, Cat, Fish, or Bird?")
    while (petHappiness < 10):
        print("Your pet is at happiness level: " + str(petHappiness) + " out of 10. Choose the right interactions to "
                                                                       "make them happier")
        action = simpledialog.askstring(title="Select interaction", prompt="Would you like to: Walk, Feed, "
                                                                           "Pet, or Bathe?")
        if action == "Walk":
            petHappiness = Walk(petType, petHappiness)
        elif action == "Feed":
            petHappiness = Feed(petType, petHappiness)
        elif action == "Pet":
            petHappiness = Pet(petType, petHappiness)
        elif action == "Bathe":
            petHappiness = Bathe(petType, petHappiness)
        else:
            print("Walk, Feed, Pet, or Bath?")

    print("Your pet is at happiness level: " + str(petHappiness) + " - nice job!")


