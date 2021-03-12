# Problem 2
# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/find-the-second-largest-element-in-an-list

'''

Given a list of integers as input, return the second largest number.

Input Format

Comma seperated list of integers

Constraints

Number of elements in the list is >2 and <=100,000

Output Format

Print the second largest number

'''

import fileinput

# ## Raw Data from STDIN/File - FOR Hacker Rank
# input_data = []
# for line in fileinput.input():
#     input_data.append(line)
#
# input_data = input_data[0].split(",")
# input_data = [int(d) for d in input_data]

## Raw Data from STDIN/File  - FOR LAPTOP
with open("input2.txt") as f:
    input_data = f.readlines()

input_data = input_data[0].split(",")
input_data = [int(d) for d in input_data]

def get_second_largest(elements):
    if len(elements) <= 1:
        return None
    largest = elements[0]
    second_largest = elements[1]

    for i in elements[1:]:
        if i > largest:
            largest, second_largest = i, largest
    if largest == second_largest:
        second_largest = "Error"
    return second_largest

print(get_second_largest(input_data))
