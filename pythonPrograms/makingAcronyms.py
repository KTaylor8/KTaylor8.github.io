#line = ' What AboutMe '
#str = "What"
#filter(str.isupper, line)
#print(line.upper())
#list = ["a", "b", "c", "d"]
#print(" ".join(list))

#name_string = "IDontKnow"
#print(filter(name_str.lower(), name_str))
#print(name_str)
names = 'Vincent Vega Jules Winnfield'
print(''.join(x[0] for x in names.split()))
