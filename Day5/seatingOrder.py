import os
from functools import reduce
import sys
sys.path.append('/'.join(__file__.split("/")[:-2]))
from standalone.udfs import *

fh = inputFileHandler(__file__, "Input.txt")
lines_list = fh.readlines()

def rowConversion(input):
    return int(
        input.replace('F', '0').replace('B', '1'),
        2
    )

def seatConversion(input):
    return int(
        input.replace('L', '0').replace('R', '1'),
        2
    )

def seatIdentifier(input):
    row = input[:-3]
    seat = input[-3:]
    return (rowConversion(row) * 8) + seatConversion(seat)

formatted_seats = map(lambda x: seatIdentifier(x.strip()), lines_list)

print("The MAX seat ID --> " + str(reduce(lambda x,y: x if x > y else y, formatted_seats)))