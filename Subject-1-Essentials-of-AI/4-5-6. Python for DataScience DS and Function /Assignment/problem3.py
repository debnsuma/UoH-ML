# Problem 2
# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/find-the-second-largest-element-in-an-list

import fileinput

# ## Raw Data from STDIN/File - FOR Hacker Rank
# input_data = []
# for line in fileinput.input():
#     input_data.append(line)

## Raw Data from STDIN/File  - FOR LAPTOP
with open("input3.txt") as f:
    input_data = f.readlines()

num = int(input_data[0].strip())
result = []

for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(i)
result = [str(i) for i in result]
print(",".join(result))
