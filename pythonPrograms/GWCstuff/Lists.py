#{} indicate that you need to replace w/ your own stuff; don't type the {}
#len({listName}) returns lenght of list
#{ListLength} (len) = last index + 1
#tuples are like lists that you set by using () instead of [] and separating items using commas, but you can't change the items
girlList = 'Katie', "'Beiza'", '"Locksley"', "Madeleine", '''Rebecca''', """Victoria"""
numList = 1, 0, 9, 1, 1, 36,
#make an empty variable using ""; you can print it as a blank
noList = ""
print (noList)
print (girlList)
print (len(numList))
#{listname}[{#1}:{#2}]  returns all values in range [{#1},{#2}] inclusive
print (numList[1:4])
print ("bob", "bobette")
#del (girlList[2])
#in is an operator, returns boolean of existance/nonexistance, not actual item in list
print ("Bloop:", 0 in numList)
print ("rawr" in numList)
#commas in print output multiple listed items in same line w/ spaces in between but no quotation marks (unless you nested different quotation marks)/parentheses/brackets
print(girlList[0] + " " + girlList[1], girlList[2], girlList[3], girlList[4], girlList[5])
print(numList[0] + numList[1], numList[2], numList[3], numList[4], numList[5])
#for {variable} in {listName}:      &      for {variable} in range(len({listName})):
#   print({variable})               &           print({listname}[{variable}])
#^^are loops that print all of the items in the list; i usually = index
#the variable exists only for the purposes inside the loop and changes based on the iteration
#for loops w/ print output multiple strings in column w/o quotation marks/parentheses/brackets
#you can make the items printed horizontally in the same line by adding commas in between them
print("for x in numList:")
for i in numList:
    print (i)
print ("for i in range (len(numList)):")
for i in range (len(numList)):
    #python automatically adds a space between different types of data separated by commas
    print("i:", i)
    print(numList[i])
#w/ nested lists w/ different item types, + combines the lists
nestList1 = girlList + numList
print(nestList1)
#w/ nested lists of different item types, separating commas in print still return the lists as separate items within a big list
nestList2 = girlList, numList
print(nestList2)
noList = []
print ("noList:")
#print an empty list using a for loop (to not return the brackets); print 0 times loop
for x in noList:
    print (x)
