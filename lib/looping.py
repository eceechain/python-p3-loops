#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    
    while countdown > 0:
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    squared_numbers = [x**2 for x in int_list]
    return squared_numbers

def fizzbuzz():
    # code goes here!
    """
    Prints numbers from 1 to 100.
    For multiples of three, prints "Fizz".
    For multiples of five, prints "Buzz".
    For numbers which are multiples of both three and five, prints "FizzBuzz".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

