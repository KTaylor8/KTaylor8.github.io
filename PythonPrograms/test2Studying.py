# .appends() adds the argument as a single element to the list (will nest lists)
# .extend() iterates over elements in argument and adds them to the end of the list individually #THROWS ERROR UNLESS ARGUMENT ITERABLE (EX: UNLESS LIST)
# {string}.find("{element}") returns the index of the first instance of the element in the string (or -1 if not found)
# {string}.swapcase() swaps the uppercase and lower case states of the letters
# "{separator}".join({list}) joins the contents of a list into a string
# {list}.remove({element}) removes the first occurance of that element
# {list}.count({element}) returns integer for number of occurances of elem
# {list}.reverse() reverses list order
# {list}.sort() sorts list in place by ascii (doesn't return any value)
# try-except-else form:
#   try:
#   except {optional errorType}: {code that runs if error}
#   else: {code that runs if error}
#   or finally (cannot use with else): {code that runs no matter what}
# unpacking is when you assign elements in an object direct to variables:
# ex: a, b, c, = [1, 2, 3]
# String formatting:
# { (index in .format()):(flags)(width).(decimal precision)(type) }
# default float decimal precision is 6
# flags (most may be combined):
# < align left (default), > align right, ^: align center,
# 0 width filled by 0s preceding num,
# , either used alone or separating numbers and letters (ex: {0:=3,d}) includes commas as thousands separators,
# = places the padding between sign and digits
# if width not specified, it will remain that # for all
# types: d = integer, s = string, f = float
# look at and understand dice.py file
