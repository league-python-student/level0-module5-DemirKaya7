"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    window = Tk()
    window.withdraw

    originalName = simpledialog.askstring(title="Name", prompt="Enter your name")
    alteredName = ""
    for i in range(len(originalName)):
        if i % 2 == 0:
            alteredName = alteredName + originalName[i].upper()
        else:
            alteredName = alteredName + originalName[i].lower()
    messagebox.showinfo(title="Goofy name", message=alteredName)