# Problem 1
# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/sum-of-given-n-numbers

'''

Given n: the number of integers that need to be input, we need to input the integers and print the sum of these "n" integers.

Input Format

The first line will consist of the number(n) of integers to read from the next line. The next line will conssit of n intregers seperated by space.

Constraints

0<=n<=100

'''
import fileinput

# ## Raw Data from STDIN/File - FOR Hacker Rank
# input_data = []
# for line in fileinput.input():
#     input_data.append(line)
# input_data = [ d.rstrip().split()  for d in input_data]

## Raw Data from STDIN/File  - FOR LAPTOP
with open("input1.txt") as f:
    input_data = f.readlines()
input_data = [ d.rstrip().split()  for d in input_data]


# Saving the elements
num = int(input_data[0][0])
if num == 0:
    elements = []
else:
    elements = [int(n) for n in input_data[1]]

# Sum Function
def _sum(elements):
    result = 0
    if elements:
        for i in elements:
            result += i

    return result

print(_sum(elements=elements))





