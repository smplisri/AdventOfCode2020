import os
import sys
sys.path.append('/'.join(__file__.split("/")[:-2]))
from standalone.udfs import *

fh = inputFileHandler(__file__, "Input.txt")
input_list = []
iter = 0

for line in fh:
    input_list.append(int(line.strip()))

while iter < len(input_list):
    for internal_iter in range(0,len(input_list)):
        if internal_iter != iter:
            if input_list[iter] + input_list[internal_iter] == 2020:
                print(input_list[iter] * input_list[internal_iter])
                break
    iter = iter + 1
