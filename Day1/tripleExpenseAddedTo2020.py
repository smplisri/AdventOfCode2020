import os
import itertools
import sys
sys.path.append('/'.join(__file__.split("/")[:-2]))
from standalone.udfs import *

fh = inputFileHandler(__file__, "Input.txt")
input_list = []
triple_set_list = []
iter, sampling = 0, 3

for line in fh:
    input_list.append(int(line.strip()))

for item in list(itertools.combinations(input_list, sampling)):
    if sum(item) == 2020:
        print(item[0] * item[1] * item[2])
        break
