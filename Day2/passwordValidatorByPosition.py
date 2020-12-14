import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_name = dir_path + "/Input.txt"
input_list = []
valid_pwd = 0
invalid_pwd = 0

with open(input_file_name, "r") as fh:
    for line in fh:
        input_list.append(line.strip().split())

for item in input_list:
    [pos1Val, pos2Val] = item[0].split('-')
    char = item[1].strip(':')
    secr_pwd = item[2]

    if bool(secr_pwd[int(pos1Val)-1] == char) ^ bool(secr_pwd[int(pos2Val)-1] == char):
        valid_pwd = valid_pwd + 1
    else:
        invalid_pwd = invalid_pwd + 1

print("Number of valid passwords --> " + str(valid_pwd))
print("Number of invalid passwords --> " + str(invalid_pwd))
