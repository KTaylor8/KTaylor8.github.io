import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

def average(numList):
    sum = 0
    for i in range(len(numList)):
        sum += numList[i]
    average = sum/len(numList)
    return average

# Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)

polList = []
subList = []

for tweet in tweetData: #for every tweet in tweetData
    tb = TextBlob(tweet["text"])
    polList.append(tb.polarity)
    subList.append(tb.subjectivity)

print(average(polList))
print(average(subList))
print(subList)

#make polarity histogram
# plt.hist(polList, bins = [-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
# plt.xlabel('Polarity')
# plt.ylabel('Number of Tweets')
# plt.title('Histogram of Tweet Polarity')
#plt.grid(True)
# plt.show()

#make subjectivity histogram
plt.hist(subList, bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
plt.xlabel('Subjectivity')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Subjectivity')
plt.grid(True)
plt.show()

#plt.plot makes a line graph

#make pol v sub scatter plot
# plt.scatter(subList, polList)
# plt.xlabel('Subjectivity')
# plt.ylabel('Polarity')
# plt.title('Tweet Polarity vs Subjectivity')
# plt.grid(True)
# #makes line of best fit
# plt.plot(np.unique(subList), np.poly1d(np.polyfit(subList, polList, 1))(np.unique(subList)))
# plt.show()

#combine all tweets into one large string
#tweets_str = ' '.join(map(str, list))
