import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_name = dir_path + "/Input.txt"
input_list = []
iter = 0

with open(input_file_name, "r") as fh:
    for line in fh:
        input_list.append(int(line.strip()))

while iter < len(input_list):
    for internal_iter in range(0,len(input_list)):
        if internal_iter != iter:
            if input_list[iter] + input_list[internal_iter] == 2020:
                print(input_list[iter] * input_list[internal_iter])
                break
    iter = iter + 1
