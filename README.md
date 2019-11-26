
## Implementation

Utilising built in functionality of os.walk, starting from the current working directory (ignoring the files)
  - check each directory contained in the CWD
  - list all files in the directory
  - for each file, find occurrence of "TODO" by iterating through the file contents
  - if pattern is found, print the file name

Run the below command to execute the program (Python 2.7 onwards)

```
python todo_finder.py
```

## Test Data

  - create directories 5 levels down, where the number of directories in each level is randomly picked (between 2 to 7)
  - test data is generated by creating a file of 1 MB each
  - the file is constructed by a sequence random characters, which in some cases might have "TODO", for example "aKdaXJKSDGKTODOnaluw" (these files will be tracked for verification purposes)
  - each file is put in each created directories

### Example
To simplify, assume the level is 2 instead of 5, and the random numbers generated were [2, 3],
```
/path/to/your/dir
  - testrun_1
    - f1
    - testrun_01
      - f2
    - testrun_02
      - f3
    - testrun_03
      - f4
  - testrun_2
    - f5
    - testrun_01
      - f6
    - testrun_02
      - f7
    - testrun_03
      - f8
```

where testrun_* depicts directory, and f* depicts file.


Run the below command to generate random data (Python 2.7 onwards)

```
python gen_test_data.py
```