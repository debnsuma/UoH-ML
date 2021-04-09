# Problem 2:
# https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/find-any-of-the-peak-elements


# Raw Data from STDIN/File - FOR Hacker Rank
import fileinput

input_data = []
for line in fileinput.input():
    input_data.append(line)
input_data = [d.rstrip().split() for d in input_data]

## Raw Data from STDIN/File  - FOR LAPTOP
# with open("input2.txt") as f:
#     input_data = f.readlines()
# input_data = [ d.rstrip().split()  for d in input_data]


arr = [int(i) for i in input_data[0][0].split(",")]


def find_peak(arr, low, high):
    mid = (low + high) // 2

    # If the mid is the peak
    if ((mid == 0 or arr[mid - 1] < arr[mid]) and
            (mid == len(arr) - 1 or arr[mid + 1] < arr[mid])):
        return mid

    # If right side of the mid is bigger than the mid
    elif mid + 1 < len(arr) and arr[mid + 1] > arr[mid]:
        low = mid + 1
        return find_peak(arr, low, high)

    # If left side of the mid is bigger than the mid
    else:
        high = mid - 1
        return find_peak(arr, low, high)

    return mid


print(find_peak(arr, 0, len(arr) - 1))
