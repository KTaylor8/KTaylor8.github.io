import json
usersDict = {}
talk = True
edit = 'yes'
nameList = []

while talk == True:
    answers = {}
    survey = [
        """
What is your name?""",
        "How old are you?",
        "What's your hometown?",
        "What's your date of birth? (DD/MM/YYYY)"]

    keys = ["name", "age", "hometown", "DOB"]

    for i in range(len(survey)):
        response = input(survey[i] + ": ")
        answers[keys[i]] = response
        if i == 0:
            name = response
            nameList.append(name)

    print(answers)

    while edit == 'yes':
        edit = input("""
Do you want to edit one of your previous answers? ('yes' or 'no'): """)
        if edit == 'yes':
            print(usersDict)
            print(keys)
            question_edit = input("""
From the list above, which answer do you want to edit? """ )
            #need to select answer to edit
    edit = 'yes'


    #need to figure out how to put each key-value pair on a new line
    usersDict[name] = answers


    thing = input("""
Do you want to keep collecting data? ('yes' or 'no'): """)
    thing = thing.lower()
    if thing != "yes":
        talk = False

print("Here is the data that has been collected so far:")
# print(usersDict)
for i in range(len(usersDict)):
    print(usersDict[nameList[i]])

#write to text file
myFile = open("survey.txt", 'w')
myFile.write('\n')
myFile.write(json.dumps(usersDict))
myFile.write('\n')
myFile.write("************")
#write to json file
myFile = open("surveyData.json", 'w')
myFile.write('[\n')
for i in range(len(usersDict)):
    #to reference a specific key-value pair in a dictionary,
    #you have to reference the key name, not the entry number
    myFile.write(json.dumps(usersDict[nameList[i]]))
    if i != len(usersDict)-1:
        myFile.write(',\n')
myFile.write('\n]')
#read file
# currently the entries in each dict aren't on separate lines so it can't read them
# answersData = open('surveyData.json', 'r')
# readData = json.load(answersData)
# print(readData)
