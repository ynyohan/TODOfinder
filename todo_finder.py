import os

import sys
print(sys.version)

CWD = os.path.dirname(os.path.abspath(__file__))

def list_files_containing_string(root_path, search_string):
    counter = 0

    for dirpath, dirnames, filenames in os.walk(CWD):
        if dirpath == CWD: continue # ignore the files on current working directory

        for fname in filenames:
            filepath = os.path.join(dirpath, fname)
            with open(filepath, 'r') as file_handler:
                for line in file_handler:
                    if search_string in line:
                        print(filepath)
                        counter += 1
                        break

    print("Total files containing TODO: " + str(counter))

list_files_containing_string(CWD, "TODO")
