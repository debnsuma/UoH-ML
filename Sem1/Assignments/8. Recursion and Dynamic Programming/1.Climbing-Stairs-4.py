# Problem 1 : Climbing Stairs 4
# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/climbing-stairs-4-4


## Raw Data from STDIN/File - FOR Hacker Rank
import fileinput

input_data = []
for line in fileinput.input():
    input_data.append(line)
input_data = [ d.rstrip().split()  for d in input_data]

# ## Raw Data from STDIN/File  - FOR LAPTOP
# with open("input1.txt") as f:
#     input_data = f.readlines()
# input_data = [ d.rstrip().split()  for d in input_data]


num = int(input_data[0][0])


def count_possibility(num):
    total = 0
    if num == 2:
        return 2
    elif num == 1:
        return 1
    else:
        total = total + count_possibility(num - 1) + count_possibility(num - 2)

    return total

print(count_possibility(num))
