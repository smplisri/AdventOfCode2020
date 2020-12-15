import os
import math

def treeTraverser(input_file_name, output, position, position_inc, line_inc, display=False):
    line_start, open_spaces, tree_spaces = 1, 0, 0
    repeat = 1 + ((len(open(input_file_name).readlines()) - 1) * position_inc)
    with open(input_file_name, "r") as fh:
        for line in fh:
            elongated_line = line.strip() * math.ceil(repeat / len(line.strip()))
            if line_start == 1:
                if display:
                    print(elongated_line)
            elif (line_start + 1) % line_inc == 0:
                position = position + position_inc
                if elongated_line[position] == '#':
                    tree_spaces = tree_spaces + 1
                    char = 'X'
                elif elongated_line[position] == '.':
                    open_spaces = open_spaces + 1
                    char = 'O'

                if display:
                    print(elongated_line[:position] + char + elongated_line[position+1:])
            else:
                if display:
                    print(elongated_line)

            line_start = line_start + 1
    
    return open_spaces, tree_spaces

dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_name = dir_path + "/Input.txt"
output_file_name = dir_path + "/Output.txt"
input_list, traversers = [], []
position, line_start, multiplier = 0, 1, 1

routers = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

for route in routers:
    O, X = treeTraverser(input_file_name, output_file_name, position, route[0], route[1])
    traversers.append((O, X))

    print(f"For the set of {route}")
    print(" Number of Open spaces --> " + str(O))
    print(" Number of Tree spaces --> " + str(X))

for (O, X) in traversers:
    multiplier = multiplier * X

print("Multiplied value at the end with all the trees transversed --> " + str(multiplier))
