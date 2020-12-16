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

formatted_seats = list(map(lambda x: seatIdentifier(x.strip()), lines_list))
min_seat_id = str(reduce(lambda x,y: x if x < y else y, formatted_seats))
max_seat_id = str(reduce(lambda x,y: x if x > y else y, formatted_seats))
print("The MIN seat ID --> " + min_seat_id)
print("The MAX seat ID --> " + max_seat_id)

formatted_seats.sort()

missing_seats = [x for x in range(int(min_seat_id), int(max_seat_id)) if x not in formatted_seats]
print(f"Missing seat number are --> {missing_seats}")