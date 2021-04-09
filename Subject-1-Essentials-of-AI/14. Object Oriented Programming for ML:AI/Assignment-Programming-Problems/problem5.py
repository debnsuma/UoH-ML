# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/np-eye-and-identity

import fileinput
import numpy as np
np.set_printoptions(legacy='1.13')
# ## Raw Data from STDIN/File - FOR Hacker Rank
# input_data = []
# for line in fileinput.input():
#     input_data.append(line)
# input_data = [ d.rstrip().split()  for d in input_data]

## Raw Data from STDIN/File  - FOR LAPTOP
with open("input5.txt") as f:
    input_data = f.readlines()
input_data = [ d.rstrip().split()  for d in input_data]

def np_dot_cross(input_data):
    N = int(input_data[0][0])
    my_arr_1 = np.array(input_data[1:N+1], dtype=int)
    my_arr_2 = np.array(input_data[N+1:], dtype=int)

    result = np.dot(my_arr_1, my_arr_2)

    return result

print(np_dot_cross(input_data))