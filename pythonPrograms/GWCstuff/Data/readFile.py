import json
answersData = open('read.json', 'r+')
readData = json.load(answersData)
print(readData)
