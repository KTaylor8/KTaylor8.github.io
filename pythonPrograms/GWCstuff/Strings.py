bob ="cat" != "dog"
print (bob)
doublesingle = "'Hi'"
#when listing strings connected by and, only the last string will print
print (doublesingle and "rawr" and "boop" and "dog")
#three consecutive same-type quotations (on both sides) allow for indenting
double3 = """Hi
    hi
        hi
            hi
                hi
                    hi
                        hi
                            hi"""
print (double3)
single3 = '''Hi
    hi!''' + " hip hip hooray!" * 3
#when listing strings connected by or, only the first string will print
print (single3 or "meow" and """
    ow""")
i = -1
while True:
    i += 1

    if (i > 20):
        #break ends the current function and continues on with program
        break

    #checks if i is odd
    if (i % 2 != 0):
        print ("restart. it's an odd number")
        #continue moves on to the next iteration of loop and skips anything below in the current iteration
        continue

    if (i % 2 == 0):
        print ("even number:" + i)
        print (i)
