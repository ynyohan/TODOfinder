import glob
import os
import random
import string
import shutil

test_dir_pattern = "testrun"

# clear all testdir from previous run
for path in glob.glob(test_dir_pattern + "_*"):
    shutil.rmtree(path)

dirs = [] # track all dirs created
num_folders_each_level = [random.randint(2,7) for _ in range(5)] # create 5 level nested dirs, each level between 2 to 7 dirs
print("Number of directories to be created at each level: " + str(num_folders_each_level))

num_folders_each_level = [2, 3]

parent_dirs = ["."] # track immediate parent dirs
for iter, n_level in enumerate(num_folders_each_level):
    cur_dirs = []
    for i in range(1, n_level+1):
        for parent in parent_dirs:
            dirname = test_dir_pattern + "_" + iter*"0" + str(i)
            dirpath = os.path.join(parent, dirname)
            os.mkdir(dirpath)
            cur_dirs.append(dirpath)
    parent_dirs = cur_dirs # the current dirs become parent dirs for next level
    dirs += parent_dirs

size = 1 * 1024 * 1024
counter = 0
file_counter = 0

print("Listing file generated that contains TODO....")

for iter, dir in enumerate(dirs):
    file_counter += 1
    chars = ''.join([random.choice(string.letters) for i in range(size)])
    # print(str(iter))
    filepath = os.path.join(dir, "f" + str(iter))

    with open(filepath, 'wb') as fout:
        if "TODO" in chars:
            counter += 1
            print(filepath)
        fout.write(chars)

print("Total files generated: " + str(file_counter))
print("Total files containing TODO: " + str(counter))
