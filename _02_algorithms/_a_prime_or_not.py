"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


def is_prime(value):
    prime = True
    for i in range(100000):
        if i != 0 and i != 1 and i != value:
            if value % i == 0:
                prime = False
    return prime

if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    window = Tk()
    window.withdraw

    num = simpledialog.askinteger(title="Enter number", prompt="Enter an integer to see if it's prime")
    if is_prime(num):
        print(str(num) + " is prime")
    else:
        print(str(num) + " is not prime")

