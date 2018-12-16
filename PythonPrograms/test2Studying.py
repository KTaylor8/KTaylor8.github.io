list1 = [1]
list1.extend([2, 3])
print(list1)

# .appends() adds the argument as a single element to the list (will nest lists)
# .extend() iterates over elements in argument and adds them to the end of the list individually #THROWS ERROR UNLESS ARGUMENT ITERABLE (EX: UNLESS LIST)
# {string}.find("{element}") returns the index of the first instance of the element in the string (or -1 if not found)
# {string}.swapcase() swaps the uppercase and lower case states of the letters
# "{separator}".join({list}) joins the contents of a list into a string
# {list}.remove({element}) removes the first occurance of that element
# {list}.count({element}) returns integer for number of occurances of elem
# {list}.reserve() reverses list order
# {list}.sort() sorts list in place by ascii (doesn't return any value)
# try-except-else form:
#   try:
#   except {optional errorType}: {code that runs if error}
#   else: {code that runs if error}
#   or finally (cannot use with else): {code that runs no matter what}
# raise {exception}     to cause exception
# unpacking is when you assign elements in an object direct to variables:
# ex: a, b, c, = [1, 2, 3]
# look at and understand dice.py file
