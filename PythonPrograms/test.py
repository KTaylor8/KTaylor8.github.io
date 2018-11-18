# lists = []
# for i in range(1, 7):
#     lists.append(i)
# for x in range(len(lists)):
#     print("{}\t".format(lists[x]), end=" ")
import json

moodDataDict = {"I love cats": "positive"}

f = open("moodTrackerData.json", "a+")
json.dump(moodDataDict, f)
