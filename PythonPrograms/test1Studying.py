# modules:
# a module is a file consisting of Python code.
# It can define functions, classes and variables & may include runnable code.
# include module names followed by a . when calling functions from modules (rather than importing all attributes using * in case the function name exists in multiple modules)
# You can shorten module names using: import {module} as {name}
# recommended to use the following when possible instead of importing all attributes of modules: from {modules} import {attribute}
# to assign a value to a global variable within a function without passing it in as a parameter, you must use "global {var}" before the assignment (within the function)
# dir() returns a list of strings of names contained by the module
# globals() and locals() returns all of the variable names in that scope
# reload({modu(le}) re-imports the module

# files i/o:
# {fileObject} = open({fileNameString}, {accessModeString})
# w = write only, OVERWRITES FILE IF EXISTS
# w+ = read and write, OVERWRITES FILE IF EXISTS
# access modes:
# r+ = read AND write but doesn't overwrite file
# r = read only
# a = append only
# a+ = read and append
# using .close() to close the file after done writing is good habit
# .write({string}) and .read()  (.read() can take a # of bytes too)
# .tell() retuns the position in the file in bytes
# .seek(offset in bytes {, from byte position})
# python os module: .rename({oldName}, {newName}) & . remove({name})

# date & time:
# time.time() returns # ticks since midnight 1/1/1970 (epoch)
# calendar module can generate calendars
# readable time specifications: time.asctime( time.localtime( time.time() ) )

# tuples:
# single element tuples won't be treated as such unless they have , before )
# access tuple elements like a dictionary or list (and use : to show a range)
# when using a slicing operator (:) to access a range of elements in the tuple, THE ENDING INDEX IS EXCLUSIVE, WHICH IS THE SAME FOR LISTS AND DICTS, except a single element tuple will be returned with a ,
# when only one number is included w/ the slicing operator (:), the other number is assumed to be the start (0) or end
# negative indices start from the right

# exceptions handling:
# using assertions to sanity check that something is true and through an error if not: assert {expression}
# try-except-else form:
#   try:
#   except {optional errorType}: {code that runs if error}
#   else: {code that runs if error}
#   or finally (cannot use with else): {code that runs no matter what}
# raise {exception}     to cause exception

# string.format():     (put the whole thing within the print())
# mid-string substitutions:
# { (index in .format()):(flags)(width).(decimal precision)(type) }
# default float decimal precision is 6
# flags (most may be combined):
# < align left (default), > align right, ^: align center,
# 0 width filled by 0s preceding num,
# , either used alone or separating numbers and letters (ex: {0:=3,d}) includes commas as thousands separators,
# = places the padding between sign and digits
# if width not specified, it will remain that # for all
# types: d = integer, s = string, f = float


def main():
    # """
    # >>> main()
    # -000,032,532 and 111.0 or cat

    # """
    # print("{:0=12,d} and {:3.1f} or {:s}".format(-32532, 111, "cat"))

    print("{:d} rawr {:f} and {:f}".format(
        2560, 32532, 1))
    print(float(4))
    print("{:f}".format(400000000))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
