import os
import json
import sys
sys.path.append('/'.join(__file__.split("/")[:-2]))
from standalone.udfs import *

def passportFormatter(lines_list, delimiter):
    formatted_list = map(lambda x: x.strip() if x != delimiter else x, lines_list)
    return ' '.join(formatted_list).split(' \n ')


fh = inputFileHandler(__file__, "Input.txt")
lines_list = fh.readlines()
delimiter = "\n"
passport_info, interim_data = [], {}
invalid, valid = 0, 0
key_lst = [
    { 'key': 'byr', 'required': True },
    { 'key': 'iyr', 'required': True },
    { 'key': 'eyr', 'required': True },
    { 'key': 'hgt', 'required': True },
    { 'key': 'hcl', 'required': True },
    { 'key': 'ecl', 'required': True },
    { 'key': 'pid', 'required': True },
    { 'key': 'cid', 'required': False }
]

print(passportFormatter(lines_list, delimiter))

for line in passportFormatter(lines_list, delimiter):
    for item in line.strip().split():
        key = item.split(":")[0]
        value = item.split(":")[1]
        interim_data[key] = value
    
    passport_info.append(interim_data)
    inv_flag = False
    for item in key_lst:
        if item['required']:
            if item['key'] not in interim_data.keys():
                inv_flag = True
                break
    invalid = invalid+1 if inv_flag else invalid+0
    valid = valid+0 if inv_flag else valid+1
    interim_data = {}

print(f"Number of Invalid passports --> {invalid}")
print(f"Number of Valid passports --> {valid}")