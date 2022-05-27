#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, finding the minimum number in random numbers

import random


def smallest_number(list_of_numbers):
    # This function finds the maximum value
    minimum = list_of_numbers[0]
    for a_single_number in list_of_numbers:
        if a_single_number < minimum:
            minimum = a_single_number
    return minimum


def main():
    # This function does random and output
    random_number = []

    # input
    print("Here is a list of random numbers: \n")
    for loop_counter in range(0, 10):
        single_number = random.randint(1, 100)
        random_number.append(single_number)
        print("The random number is {}".format(single_number))

    # process & output
    answer = smallest_number(random_number)
    print("\nThe smallest number is {}".format(answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
