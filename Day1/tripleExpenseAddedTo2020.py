import os
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_name = dir_path + "/Input.txt"
input_list = []
triple_set_list = []
iter, sampling = 0, 3

with open(input_file_name, "r") as fh:
    for line in fh:
        input_list.append(int(line.strip()))

for item in list(itertools.combinations(input_list, sampling)):
    if sum(item) == 2020:
        print(item[0] * item[1] * item[2])
        break
