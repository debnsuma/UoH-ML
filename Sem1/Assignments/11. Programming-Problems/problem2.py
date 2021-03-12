# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/np-min-and-max

import fileinput
import numpy as np

# ## Raw Data from STDIN/File - FOR Hacker Rank
# input_data = []
# for line in fileinput.input():
#     input_data.append(line)
# input_data = [ d.rstrip().split()  for d in input_data]

## Raw Data from STDIN/File  - FOR LAPTOP
with open("input2.txt") as f:
    input_data = f.readlines()
input_data = [ d.rstrip().split()  for d in input_data]

def get_np_arr_min_max(input_data):

    #N, M = list(map(int, input_data[0]))
    my_arr = np.array(input_data[1:], dtype=int)
    my_arr_max = max(np.min(my_arr, axis=1))

    return my_arr_max

print(get_np_arr_min_max(input_data))
