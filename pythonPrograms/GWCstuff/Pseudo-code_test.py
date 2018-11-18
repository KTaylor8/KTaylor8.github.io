ages = [5, 12, 3, 56, 24, 78, 1, 15 ,44]
#sum = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8]
#sum(ages)
sum = 0
for i in ages:
    sum += ages[i]
print (sum/len(ages))
