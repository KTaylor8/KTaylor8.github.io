import json
answersData = open('answers.json', 'r')
readData = json.load(answersData)
print(readData)
