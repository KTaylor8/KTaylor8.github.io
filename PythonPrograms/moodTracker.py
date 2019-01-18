import nltk  # natural language toolkit
import json
import os
from matplotlib import pyplot as plt


def getRespData():
    """
    The function prepares lists of text string and sentiment data tuples from multiple csv files of data (mostly imported) to improve the accuracy of the program's sentiment classifications.

    posStrings = list of strings with positive sentiment read from data file
    neutStrings = list of strings with neutral sentiment read from data file
    negStrings = list of strings with negative sentiment read from data file
    posResps = list of tuples (text string, "positive")
    neutResps = list of tuples (text string, "neutral")
    negResps = list of tuples (text string, "negative")
    files = list of file names from which I import string-sentiment data
    dataFile = current file with data being imported
    string = the polarized text from a line in the data file

    Note: no parameters, so no doctest
    """

    posStrings = []
    neutStrings = []
    negStrings = []
    files = [
        "stanfordSentiment140TweetData.csv",
        "dataHubTweetDataFull.csv",
    ]
    for i in range(10):  # adds custom data many times to outweigh other data
        files.append("customData.csv")

    for i in range(len(files)):
        with open(files[i], "r", encoding="utf8") as dataFile:
            # w/o this encoding some characters are undefined
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
        dataFile.close()

    posResps = [(string, "positive") for string in posStrings]
    neutResps = [(string, "neutral") for string in neutStrings]
    negResps = [(string, "negative") for string in negStrings]

    # print(f"{posResps[230:]}")  # if list too long to show: it'll cut off end
    return posResps, neutResps, negResps


def initClassifier(posResps, neutResps, negResps):
    """
    The function first matches the filtered possibly polar words to their sentiment, then it prepares the sentiment classifier based on the training response examples to determine if a new given text response is overall positive, neutral or negative in tone.

    posResps = list of (text string, "positive")
    neutResps = list of tuples (text string, "neutral")
    negResps = list of (text string, "negative")
    filteredWords = changing list of words longer than 2 characters
    resps = list of (list of polar words in a string, sentiment)
    sortedWords = list of filtered words ordered by decreasing frequency
    sentimentTrainingList = list of every sentiment (for tracking num of resps)
    wordsTrainingList = list of every individual filtered word
    ignoreWordsList = list of neutral words that are most likely accompanied                     by polarized words (I don't want too many neutral words 
                    to overload an actually polarized statement.)
    el = current word (element) in a list of words from a split string
    sortedWords = list of filtered words ordered by decreasing frequency
    trainingData = list of labeled feature sets [a list of tuples ({dict of                   each resp's extracted features}, resp sentiment string)]
    classifier = object that maps each feature to the probability of it having              a positive or negative sentiment

    Note: not doing a doc test run because I'm not sure how to make the classifier return a value in the right format without it being super long
    """

    resps = []
    filteredWords = []
    sentimentTrainingList = []
    wordsTrainingList = []
    ignoreWordsList = [
        "feel",
        "need",
        "want",
    ]
    # match filtered (possibly polar) words to sentiment for each string:
    for (string, sentiment) in posResps + neutResps + negResps:
        # for el in string.split():
        #     if len(el) >= 3:  # shorter words neutral
        #         filteredWords.append(el.lower())
        filteredWords = []
        for el in string.split():
            if len(el) >= 3 and el not in ignoreWordsList and el[0] != "@":
                filteredWords.extend(el.lower())
        resps.append((filteredWords, sentiment))
        sentimentTrainingList.append(sentiment)
        wordsTrainingList.append((filteredWords))
        # filteredWords.clear()
    sortedWords = getWordFeatures(getRespsWords(resps))

    # compiles training (response, sentiment) pairs and prepares classifier
    # trainingData = nltk.classify.apply_features(extractFeatures, resps)
    trainingData = [
        (
            extractFeatures(
                sortedWords,
                wordsTrainingList[i]
            ),
            sentimentTrainingList[i]
        ) for i in range(len(sentimentTrainingList))
    ]
    classifier = nltk.NaiveBayesClassifier.train(trainingData)
    return sortedWords, classifier


def classifyResp(sortedWords, classifier, userResp):
    """
    This function classifies the overall sentiment of the user's response, prints it, and returns the dictionary of the mood data in the form {resp, mood}.

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
    The function separates a list in the paired form [(filtered words), sentiment] into a list of the filtered words only.

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
    The function reorders the list of filtered words by decreasing frequency.

    sigWords = list of all filtered individual words from the string
    sigWordsAndFreq = dictionary of filtered words with their frequencies
    sortedWords = list of filtered words wordered by decreasing frequency
    """
    sigWordsAndFreq = nltk.FreqDist(sigWords)
    sortedWords = sigWordsAndFreq.keys()  # gets dict keys
    return sortedWords


def extractFeatures(sortedWords, userResp):
    """
    The function is a feature extractor that compares words in response to words in list of possible words so unused words can be ignored and response can be tested against the training data.

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
    The function adds dictionaries in the form {resp: mood} to the json file.

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
        # (you can't open the same file w/ w within with statement code block)
        dataFile.seek(0)
        dataFile.truncate()
        dataFile.write(json.dumps(moodData))


def graphSentiments():
    """
    The function graphs sentiment of entries (negatuve, neutral, or positive) vs entry number so that the user can see the general trend of their mood.

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
    This simple function overwrites the json file storing the entry data in order to clear it.
    """
    open("moodTrackerData.json", "w").close()


def main():
    """
    The function serves as the program's main menus and loops in asking the user to chose between a variety of actions (make a new entry, graph your mood data, delete all entries, or quit the program) and calling the function for that functionality until the user quits.

    repeat = whether the user wants to repeat the program or not
    userResp = user's response about their day
    sortedWords = list of filtered words ordered by decreasing frequency
    classifier = object that maps each feature to the probability of it having              a positive or negative sentiment
    yesList = list of possible responses to the repeat program question used             to determine whther the user wants to perform further actions
    """
    yesList = [
        'yes', 'yeah', 'sure', 'okay', 'ok', 'why not', 'yeet', 'yep', 'yup', 'si', 'affirmative', 'of course', 'always'
    ]
    repeat = 'yes'
    posResps, neutResps, negResps = getRespData()
    sortedWords, classifier = initClassifier(posResps, neutResps, negResps)
    while repeat == "yes":
        userResp = input(
            "\nTo make a new entry, type 'entry',\n"
            "to make a graph of your mood over the course of your entries so far, type 'graph',\n"
            "to delete all of your entries, type 'delete',\n"
            "or to exit the program, type 'quit'.\n"
        ).strip().lower()
        if userResp == "entry":
            userResp = input(
                "\nPlease describe your day and how you feel about it.\n"
            ).lower()
            storeMood(classifyResp(sortedWords, classifier, userResp))
            repeat = input(
                "\nDo you want to do another action?\n"
            ).lower()
        elif userResp == "graph":
            graphSentiments()
        elif userResp == "delete":
            deleteEntries()
        elif userResp == "quit":
            repeat = "no"
        else:
            print("Error! Try again.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
