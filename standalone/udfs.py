import os

def inputFileHandler(script_file_name, input_file_name):
    dir_path = os.path.dirname(os.path.realpath(script_file_name))
    file_name = dir_path + "/" + input_file_name
    ifh = open(file_name, "r")

    return ifh