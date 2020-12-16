import os
import re
import sys
sys.path.append('/'.join(__file__.split("/")[:-2]))
from standalone.udfs import *

fh = inputFileHandler(__file__, "Input.txt")
lines_list = fh.readlines()
delimiter = "\n"
passport_info, interim_data = [], {}
invalid, valid = 0, 0
key_lst = [
    { 'key': 'byr', 'required': True, 'qc': {'low': '1920', 'up': '2002'} },
    { 'key': 'iyr', 'required': True, 'qc': {'low': '2010', 'up': '2020'} },
    { 'key': 'eyr', 'required': True, 'qc': {'low': '2020', 'up': '2030'} },
    { 'key': 'hgt', 'required': True, 'qc': {'cm': {'low': '150', 'up': '193'}, 'in': {'low': '59', 'up': '76'}} },
    { 'key': 'hcl', 'required': True, 'qc': {'pattern': r'^#[0-9a-f]{6}$'} },
    { 'key': 'ecl', 'required': True, 'qc': {'choice': ['amb','blu','brn','gry','grn','hzl','oth']} },
    { 'key': 'pid', 'required': True, 'qc': {'pattern': r'^\d{9}$'} },
    { 'key': 'cid', 'required': False }
]

for line in lineSepGroupFormatter(lines_list, delimiter, ' '):
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
            if 'qc' in item.keys():
                if item['key'] != 'hgt' and 'low' in item['qc'].keys() and 'up' in item['qc'].keys():
                    if interim_data[item['key']] < item['qc']['low'] or interim_data[item['key']] > item['qc']['up']:
                        inv_flag = True
                        break
                elif item['key'] == 'hgt':
                    hgt = interim_data[item['key']][:-2]
                    unit = interim_data[item['key']][-2:]
                    if unit not in item['qc'].keys():
                        inv_flag = True
                        break
                    elif hgt < item['qc'][unit]['low'] or hgt > item['qc'][unit]['up']:
                        inv_flag = True
                        break
                elif 'pattern' in item['qc'].keys():
                    if re.match(item["qc"]["pattern"], interim_data[item['key']]) == None:
                        inv_flag = True
                        break
                elif 'choice' in item['qc'].keys():
                    if interim_data[item['key']] not in item['qc']['choice']:
                        inv_flag = True
                        break
                else:
                    print('Empty quality control seems suspicious')
                    raise "Error"
    invalid = invalid+1 if inv_flag else invalid+0
    valid = valid+0 if inv_flag else valid+1
    interim_data = {}

print(f"Number of Invalid passports --> {invalid}")
print(f"Number of Valid passports --> {valid}")