#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Nov 8, 2023
# This program will ask the user for a number
# between 0 and 9 and it will tell them
# if they guessed my number correctly or not with try catch
import random


def main():
    # generate random number
    correct_guess = random.randint(0, 9)

    while True: 
        # Get the user number as a string and display message about program
        print(
            "This program will ask the user for a number between 0 and 9 and it will tell them"
        )
        print("if they guessed my number correctly or not.")
        user_guess_str = input("Please enter a number between 0 and 9: ")

        # Catch if the user number is something wrong
        try:
            # Convert user number as a string to int
            user_guess_int = int(user_guess_str)

            if user_guess_int < 0:
                # Message for negative user number
                print("\n{} is not a positive int.".format(user_guess_int))

            elif user_guess_int > 9:
                # Message for user number greater than 9
                print("\n{} is greater than 9.".format(user_guess_int))

            # check if user did not enter the correct guess
            elif user_guess_int != correct_guess:
                print("\n{} is not correct.".format(user_guess_int, correct_guess))
            
            # if user entered the right guess
            else:
                break

        except Exception:
            # Message for invalid user number
            print("\n{} is not a valid whole number.".format(user_guess_str))

    print("\nCongratulations! {} is the correct guess.".format(user_guess_int))


if __name__ == "__main__":
    main()
