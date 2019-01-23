# doesn't go through inside the for loop and idk why
sentimentsList = ["0", "2", "4"]
with open("airlineTweets2.csv", "a+", encoding="utf8") as dataFile:
    for line in dataFile:
        if line[0] in sentimentsList:  # if line starts w/ sentiment num
            dataFile.write(line)
            print(f"line printed: {line}")
        else:
            print(f"line not printed: {line}")
        print(line)
