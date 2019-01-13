# aimldl/python3
This is my personal repository of Python scripts from various sources such as online courses, package tutorials, and so on.
I started this for productivity and code reuse purposes.

# To-dos
- Change the repository name from python to python3
- Change the appropriate changes from python to python3 within Dockerfile

# Disclaimer
Most of the scripts are from other sources either on the web or books. I don't intend to violate copyright issue or cause problems. Please let me know if any violation or inconvenience is found.

# Conventions
## README.md
A repository should have a README.md which includes:
* An identifier
** The identifier has the full information to find the repository.
** / # python/packages/numpy         (Wrong)
** / # aimldl/python/packages/numpy  (Correct)

* To-dos
** The next task to follow up the previous work is given here.
** / # To-dos

* References
** The sources of the scripts are here.
/ # References

## Directory name convention
A directory name is a meaningful cluster of files.

## File name convention
* The title is the file name(spaces are replaced by _).
  For example,
    1.Reading_CSV_files_in_Python.py
      is for a web article "Reading CSV files in Python" at https://pythonprogramming.net/reading-csv-files-python-3/.
* Note the file name is indexed so the order of the files can become obvious.
* 1.reading_cvs_files_in_python.py (Wrong)
* 1.Reading_CSV_files_in_Python.py (Correct)

* If chapters and sub-chapters exist, this hierarchy is also indexed.
  For example, 1.Quickstart_tutorial-1.The_Basics-1.An_eample.py
  In this way, the order of the files is easy to grasp.

## Reference
* Each reference is numbered in the order that the scripts are created.
* The index number and the title is identical to the file name of a script (spaces are replaced by _).
  For example,
    References
    1.Reading CSV files in Python, https://pythonprogramming.net/reading-csv-files-python-3/

## Within the file
/# 1.Quickstart_tutorial-1.The_Basics-1.An_eample.py
/#
/# https://docs.scipy.org/doc/numpy/user/quickstart.html
/# The Basics - An example
