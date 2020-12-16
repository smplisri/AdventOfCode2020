import os

def inputFileHandler(script_file_name, input_file_name):
    dir_path = os.path.dirname(os.path.realpath(script_file_name))
    file_name = dir_path + "/" + input_file_name
    ifh = open(file_name, "r")

    return ifh

def lineSepGroupFormatter(lines_list, delimiter, join_char):
    formatted_list = map(lambda x: x.strip() if x != delimiter else x, lines_list)
    return join_char.join(formatted_list).split(join_char + delimiter + join_char)

def lineSepGroupFormatterDict(lines_list, delimiter, join_char):
    iterator, answerset, interim_data = 1, {}, []
    formatted_list = list(map(lambda x: x.strip() if x != delimiter else x, lines_list))
    formatted_list.append(delimiter)
    for item in formatted_list:
        if item.strip() == "":
            answerset["group" + str(iterator)] = interim_data
            interim_data = []
            iterator = iterator + 1
        else:
            interim_data.append(item)
    
    return answerset