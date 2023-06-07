#!/usr/bin/python3

def fizzbuzz():

    """Print the numbers from the range of 1 to 100 separated by a space.


    For the multiples of three, print Fizz and not the number.

    For multiples of five, print Buzz instead of the number.

    For the multiples of three and five, print FizzBuzz instead of the number.

    """

    for number in range(1, 101):

        if number % 3 == 0 and number % 5 == 0:

            print("FizzBuzz ", end="")

        elif number % 3 == 0:

            print("Fizz ", end="")

        elif number % 5 == 0:

            print("Buzz ", end="")

        else:

            print("{} ".format(number), end="")
