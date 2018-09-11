import json

#small tweet data:
# tweetFile = open("tweets_small.json", "r")
# tweetData = json.load(tweetFile)
# tweetFile.close()

#big tweet data:
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

langList = []
langFreqList = []
# locList = []

#for the length of tweetData, using a variable i as an integer, so you can access the specific indices
for i in range(len(tweetData)):
#     print("Tweet id: ", tweetData[i]["id"])
#     print("Tweet text: ", tweetData[i]["text"])
    if tweetData[i]["lang"] not in langList:
        langList.append(tweetData[i]["lang"])
        langFreqList.append(1)
    else: #if there have already been tweets in that language, count up by one in the freqList
        #what is the repeated language found in this iteration?
        langFreqList[i] = langFreqList[i] + 1
#ISSUE: need same index in langFreqList as index of the tweetData[i]["lang"]'s language that is in langList

#each tweet is a dictionary within the bigger dictionary tweetData
#can't access the indices of the tweets using this loop
#for tweet in tweetData: #for every tweet in tweetData
     # print("Tweet id: ", tweet["id"])
     # print("Tweet text: ", tweet["lang"])
    # if tweet["lang"] not in langList:
    #    langList.append(tweet["lang"])
    # if tweet["location"] not in locList:
    #    locList.append(tweet["location"])

print("Tweet languages: ", langList)
print("Tweet language frequencies: ", langList)
# print("Tweet locations: ", locList)
