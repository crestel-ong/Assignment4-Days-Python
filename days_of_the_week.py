#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: October 2021
# This is days of the week program


def main():
    # this function displays the day a number entered represents

    # telling them what they are doing
    print("Everyday has a corresponding number.")
    print("For example, 1 is Sunday.")
    print("")

    # input
    user_input_as_string = input("Enter a number of a day of the week: ")

    try:
        # convert string to integer
        user_input_as_integer = int(user_input_as_string)

        # process and output
        if user_input_as_integer >= 0:
            if user_input_as_integer == 1:
                print("Sunday")
            elif user_input_as_integer == 2:
                print("Monday")
            elif user_input_as_integer == 3:
                print("Tuesday")
            elif user_input_as_integer == 4:
                print("Wednesday")
            elif user_input_as_integer == 5:
                print("Thursday")
            elif user_input_as_integer == 6:
                print("Friday")
            elif user_input_as_integer == 7:
                print("Saturday")
            else:
                print("Invalid number.")
        else:
            print("You did not enter a positive integer.")
    except Exception:
        print("{0} is not an integer.".format(user_input_as_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
