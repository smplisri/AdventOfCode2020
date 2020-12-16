import os
from functools import reduce
import sys
sys.path.append('/'.join(__file__.split("/")[:-2]))
from standalone.udfs import *

fh = inputFileHandler(__file__, "Input.txt")
lines_list = fh.readlines()
delimiter = "\n"    

formatted_lines = lineSepGroupFormatter(lines_list, delimiter, '')

answers = list(map(lambda x: list(x), formatted_lines))
unique_answers = list(map(lambda x: set(list(x)), formatted_lines))

unique_answers_count = reduce(lambda x, y: len(set(x)) + len(set(y)) if type(x) is list else x + len(set(y)), answers)
print(f'Total number of answers --> {unique_answers_count}')

common_answers_count = 0
dict_format_lines = lineSepGroupFormatterDict(lines_list, delimiter, '')
for iterator in range(1, len(dict_format_lines)+1):
    group_counts = len(dict_format_lines["group" + str(iterator)])
    unique_charset = set(list(''.join(dict_format_lines["group" + str(iterator)])))
    for char in unique_charset:
        if sum(char in item for item in dict_format_lines["group" + str(iterator)]) == group_counts:
            common_answers_count = common_answers_count + 1

print(f"Total number of common answers --> {common_answers_count}")