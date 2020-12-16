import os
from functools import reduce
import sys
sys.path.append('/'.join(__file__.split("/")[:-2]))
from standalone.udfs import *

fh = inputFileHandler(__file__, "Input.txt")
lines_list = fh.readlines()
delimiter = "\n"

unique_ans = list(map(lambda x: len(set(list(x))), lineSepGroupFormatter(lines_list, delimiter, '')))

print('Total number of answers --> ' + str(reduce(lambda x, y: x+y, unique_ans)))