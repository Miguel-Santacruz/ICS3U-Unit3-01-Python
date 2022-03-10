#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: March 2022
# This program calculates the sum of two integers
#   inputted by the user and shows the calculation


def main():
    # This function calculates the sum of two integers

    # Input
    Integer_1 = int(input("Enter the first number to add (Integer): "))
    Integer_2 = int(input("Enter the second number to add (Integer): "))

    # Process
    Sum = Integer_1 + Integer_2

    # Output
    print("")
    print("{0} + {1} = {2}".format(Integer_1, Integer_2, Sum))

    print("\nDone.")


if __name__ == "__main__":
    main()
