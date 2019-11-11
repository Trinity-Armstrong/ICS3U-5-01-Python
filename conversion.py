#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This program converts Celsius to Farenheight


def conversion():
    # This function converts Celsius to Farenheight

    # Input
    Tc = int(input("Enter a temperature in Celsius to convert: "))

    # Process
    Tf = (9/5)*Tc+32

    # Output
    print("This temperature in Farenheight is: {0}°".format(Tf))


def main():
    # This function calls other functions

    # Call function
    conversion()


if __name__ == "__main__":
    main()
