#!/usr/bin/python3
"""
importing modules
"""
from math import *
from cs50 import *


def main():
    # prompting user for change owed
    while True:
        coins = float(input("Change owed: "))
        total = floor(coins * 100)
        # checks if user input is greater than zero otherwise repeats step one
        if total > 0:
            return 0
            break

    makeChange(coins, total)


def makeChange(coins, total):
    # calculates quaters
    quarter = total // 25
    # calculates dimes
    dime = (total % 25) // 10
    # calculates nickels
    nickel = ((total % 25) % 10) // 5
    # calculates pennies
    pennie = ((total % 25) % 10) % 5
    # prints the change owed
    print(f"{quarter + dime + nickel + pennie}")


if __name__ == "__main__":
    main()
