# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/np-shape-reshape

import fileinput
import numpy as np

# ## Raw Data from STDIN/File - FOR Hacker Rank
# input_data = []
# for line in fileinput.input():
#     input_data.append(line)


## Raw Data from STDIN/File  - FOR LAPTOP
with open("input1.txt") as f:
    input_data = f.readlines()

def get_np_array(a):
    a = np.array(list(map(int, a.split())))
    a.shape = (3, 3)

    return a

result = get_np_array(input_data[0])

print(result)