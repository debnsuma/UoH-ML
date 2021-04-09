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
with open("input4.txt") as f:
    input_data = f.readlines()
input_data = [ d.rstrip().split()  for d in input_data]

def ey_identity(input_data):
    N, M = list(map(int, input_data[0]))

    result = np.eye(N,M)

    return result

print(ey_identity(input_data))