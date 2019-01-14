import nltk  # natural language toolkit
import json
import os
from matplotlib import pyplot as plt

# sentiment is the connotation of a word (positive or negative)


def getRespData():
    """
    Function prepares lists of text string and sentiment data tuples from imported csv file Twitter data to improve accuracy of sentiment classifications.

    posStrings = list of strings with positive sentiment read from data file
    neutStrings = list of strings with neutral sentiment read from data file
    negStrings = list of strings with negative sentiment read from data file
    posResps = list of tuples (text string, "positive")
    neutResps = list of tuples (text string, "neutral")
    negResps = list of tuples (text string, "negative")

    Note: no parameters, so no doctest
    """

    posStrings = []
    neutStrings = []
    negStrings = []

    # training data: (response, sentiment)
    # ADD MORE TRAINING DATA AND MAKE IT WORK W/ DIFFERENT SOURCES & FORMATS (ORDERS AND QUOTES OR NO QUOTES)
    numDataSources = 3
    fileName = "stanfordSentiment140TweetData.csv"
    # !!!! for some reason the positive scan of the Stanford ends at line 235 (neutral and neg finish fully) but I couldn't figure out how to fix it

    # for i in range(numDataSources):
    with open(fileName, "r") as dataFile:
        for line in dataFile:
            # strip \n, convert to list of str, split at 1st comma:
            line = line.strip().split(",", 1)
            line.sort()  # puts num before str in list
            string = line[1].strip('"')  # removes " from start & end
            if line[0] == '4':
                posStrings.append(string)
            elif line[0] == '2':
                neutStrings.append(string)
            elif line[0] == '0':
                negStrings.append(string)
    # if i == 0:
    #     fileName = "dataHubTweetData.csv"
    # elif i == 1:
    #     fileName = "customData.csv"

    posResps = [(string, "positive") for string in posStrings]
    neutResps = [(string, "neutral") for string in neutStrings]
    negResps = [(string, "negative") for string in negStrings]
    # NEED TO ADD EVEN MORE DATA SOURCES

    print(posResps)  # debug
    return posResps, neutResps, negResps


def initClassifier(posResps, neutResps, negResps):
    """
    Function prepares sentiment classifier based training response examples (to determine if text is overall positive or negative in meaning),

    posResps = list of (text string, "positive")
    neutResps = list of tuples (text string, "neutral")
    negResps = list of (text string, "negative")
    filteredWords = changing list of words longer than 2 characters
    resps = list of (list of polar words in a string, sentiment)
    sortedWords = list of filtered words ordered by decreasing frequency
    sentimentTrainingList = list of every sentiment (for tracking num of resps)
    wordsTrainingList = list of every individual filtered word
    sortedWords = list of filtered words ordered by decreasing frequency
    trainingData = list of labeled feature sets [a list of tuples ({dict of                   each resp's extracted features}, resp sentiment string)]
    classifier = object that maps each feature to the probability of it having              a positive or negative sentiment

    Note: not doing a doc test run because I'm not sure how to make the classifier returned value in the right format without it being super long
    """

    resps = []
    filteredWords = []
    sentimentTrainingList = []
    wordsTrainingList = []

    # match filtered (possibly polar) words to sentiment for each string
    for (string, sentiment) in posResps + neutResps + negResps:
        # for el in string.split():
        #     if len(el) >= 3:  # shorter words neutral
        #         filteredWords.append(el.lower())
        filteredWords = [el.lower() for el in string.split() if len(
            el) >= 3]  # CURRENTLY NOT FILTERING OUT THE @s
        resps.append((filteredWords, sentiment))
        sentimentTrainingList.append(sentiment)
        wordsTrainingList.append((filteredWords))
        # filteredWords.clear()
    sortedWords = getWordFeatures(getRespsWords(resps))

    # compiles training (response, sentiment) pairs and prepares classifier
    # trainingData = nltk.classify.apply_features(extractFeatures, resps)
    trainingData = [
        (extractFeatures(sortedWords,
                         wordsTrainingList[i]),
         sentimentTrainingList[i]) for i in range(len(sentimentTrainingList))
    ]
    classifier = nltk.NaiveBayesClassifier.train(trainingData)
    return sortedWords, classifier


def classifyResp(sortedWords, classifier, userResp):
    """
    Classifies overall sentiment of user response, prints this, and returns dict {resp, mood}
    sortedWords = list of filtered words ordered by decreasing frequency
    userResp = user's response about their day and feelings
    extractedFeatures = dict with booleons for whether or not a sorted word is                     in the user's response
    classifier = object that maps each feature to the probability of it having              a positive or negative sentiment
    mood = classified sentiment for user response
    moodDataDict = dict of user response string and mood string

    Note: not doing a doc test run because I'm not sure how to make the classifier argument in the right format without it being super long
    """
    # response's overall sentiment will eventually affect how program responds
    # but for now it just prints the overall sentiment
    extractedFeatures = extractFeatures(sortedWords, userResp.split())
    mood = classifier.classify(extractedFeatures)
    print(f'Your response was overall {mood}.')
    moodDataDict = {userResp: mood}
    return moodDataDict


def getRespsWords(resps):
    """
    Function separates [(filtered words), sentiment] list of pairs into list of those words only

    resps = list of (list of polar words in a string, sentiment)
    sigWords = list of all filtered individual words from the string

    >>> getRespsWords([(['love', 'best', 'friend'], 'positive')])
    ['love', 'best', 'friend']
    """
    sigWords = []
    for (words, sentiment) in resps:
        # extend() adds each individual element, not whole list
        sigWords.extend(words)
    return sigWords


def getWordFeatures(sigWords):
    """
    Function reorders list of filtered words by decreasing frequency

    sigWords = list of all filtered individual words from the string
    sigWordsAndFreq = dictionary(?) of filtered words with their frequencies
    sortedWords = list of filtered words wordered by decreasing frequency
    """
    sigWordsAndFreq = nltk.FreqDist(sigWords)
    sortedWords = sigWordsAndFreq.keys()  # gets dict keys
    return sortedWords


def extractFeatures(sortedWords, userResp):
    """
    Function is a feature extractor that compares words in response to words in list of possible words so unused words can be ignored and response can be tested against the training data

    sortedWords = list of filtered words wordered by decreasing frequency
    userResp = user's response string about their day split into list
    features = dictionary of {'contains(polar word)': boolean whether or not user input string contains polar word}
    >>> extractFeatures(['like', 'pie', 'fly', 'sky'], ['I', 'like', 'pie'])
    {'contains(like)': True, 'contains(pie)': True, 'contains(fly)': False, 'contains(sky)': False}

    """
    userRespTup = tuple(userResp)
    # userRespWords = {userRespTup[i] for i in userRespTup}
    userRespWords = set(userRespTup)
    features = {}
    for word in sortedWords:
        features[f'contains({word})'] = (word in userRespWords)
    return features


def storeMood(entry):
    """
    Function writes dictionary {resp: mood} to json file

    entry = new user entry
    dataFile = read file of json mood data
    moodData = updated json mood data to store
    oldMoodData = json mood data (user entries) stored
    """
    with open("moodTrackerData.json", "r+") as dataFile:
        # if os.stat("moodTrackerData.json").st_size == 0:  # file empty
        if os.path.getsize("moodTrackerData.json") == 0:  # file empty
            moodData = entry
        else:  # file occupied
            # throws docoder error if file empty
            oldMoodData = json.load(dataFile)
            moodData = {**oldMoodData, **entry}  # consolidates duplicate pairs
        # (you can't open the same file w/ w within the with statement code block)
        dataFile.seek(0)
        dataFile.truncate()
        dataFile.write(json.dumps(moodData))


def graphSentiments():
    """
    Function graphs sentiment of entries vs entry number.

    dataFile = read file of json mood data
    entries = user entries stored (dictionary)
    entriesCount = list of number of entries (used for x-axis tick labels)
    entry = each entry in the dictionary of entries
    sentimentList = list of sentiments (used for y-axis tick labels)
    mood = values in dictionary of entries
    subplot = graph created (plot as part of new figure)
    """
    with open("moodTrackerData.json", "r+") as dataFile:
        entries = json.load(dataFile)
        entriesCount = [entry for entry in range(len(entries))]
        sentimentList = [mood for mood in entries.values()]
    subplot = plt.figure().add_subplot(111)  # 1x1 grid, 1 (sub)plot in figure
    subplot.plot(entriesCount, sentimentList)  # x, y, marker
    subplot.set_yticklabels(["negative", "neutral", "positive"])  # order ticks
    plt.ylabel('Sentiment')
    plt.xlabel('Entry Number')
    plt.title('Sentiment vs Entry Number Graph')
    plt.show()


def deleteEntries():
    """
    This simple function overwrites the json file storing the entry data to clear it.
    """
    open("moodTrackerData.json", "w").close()


def main():
    """
    Program's main process: asks user about their day to determine their mood, with the option to repeat, quit, or delete all of the stored mood data

    repeat = whether the user wants to repeat the program or not
    userResp = user's response about their day
    sortedWords = list of filtered words ordered by decreasing frequency
    classifier = object that maps each feature to the probability of it having              a positive or negative sentiment
    yesList = list of possible responses to the repeat program question used             to determine whther the user wants to perform further actions
    """
    yesList = ['yes', 'yeah', 'sure', 'okay', 'ok', 'why not', 'yeet', 'yep', 'yup',
               'si', 'affirmative', 'of course', 'always']
    repeat = 'yes'
    posResps, neutResps, negResps = getRespData()
    # sortedWords, classifier = initClassifier(posResps, neutResps, negResps)
    # while repeat == "yes":
    #     userResp = input(
    #         "\nTo make a new entry, type 'entry',\n"
    #         "to make a graph of your mood over the course of your entries so far, type 'graph',\n"
    #         "to delete all of your entries, type 'delete',\n"
    #         "or to exit the program, type 'quit'.\n"
    #     ).strip().lower()
    #     if userResp == "entry":
    #         userResp = input(
    #             "\nPlease describe your day and how you feel about it.\n"
    #         ).lower()
    #         storeMood(classifyResp(sortedWords, classifier, userResp))
    #         repeat = input(
    #             "\nDo you want to do another action?\n"
    #         ).lower()
    #     elif userResp == "graph":
    #         graphSentiments()
    #     elif userResp == "delete":
    #         deleteEntries()
    #     elif userResp == "quit":
    #         repeat = "no"
    #     else:
    #         print("Error! Try again.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
