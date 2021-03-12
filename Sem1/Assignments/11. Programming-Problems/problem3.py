# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/np-concatenate

import fileinput
import numpy as np

# ## Raw Data from STDIN/File - FOR Hacker Rank
# input_data = []
# for line in fileinput.input():
#     input_data.append(line)
# input_data = [ d.rstrip().split()  for d in input_data]

## Raw Data from STDIN/File  - FOR LAPTOP
with open("input3.txt") as f:
    input_data = f.readlines()
input_data = [ d.rstrip().split()  for d in input_data]

def concat_arr(input_data):
    N, M, P = list(map(int, input_data[0]))
    my_arr_1 = np.array(input_data[1:N+1], dtype=int)
    my_arr_2 = np.array(input_data[N+1:], dtype=int)

    result = np.concatenate((my_arr_1, my_arr_2), axis=0)

    return result

print(concat_arr(input_data))