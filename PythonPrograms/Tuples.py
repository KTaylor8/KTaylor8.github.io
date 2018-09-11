print("""
A tuple is a sequence of immutable (unchangeable) Python objects.
Tuples are sequences, just like lists.
However, unlike lists, tuples cannot be changed.
Also, lists use square brackets, while tuples use parentheses.
Creating a tuple is as simple as putting different comma-separated values.
""")

tuple1 = ("a", "b", "c", 1, 2, 3)
print ("For example: tuple1:", tuple1)

tuple2 = ("Wow",)
print ("If a tuple only has 1 item, you have to end it w/ a comma, ex: tuple2 =", tuple2)
print("""
Since you can't change tuples directly,
you can only make new tuples
and set them to include altered versions of already-existing tuples,
such as sums of already-existing tuples, as shown below.
""")

tuple3 = tuple1 + tuple2
print("tuple3 = tuple1 + tuple2")
print ("tuple3 then prints as", tuple3)
