import nltk  # natural language toolkit
import json
import os
from matplotlib import pyplot as plt
import string
from collections import Counter
# it has to be significantly weighted toward negative in order for it to predict negative


def getRespData():
    """
    The function prepares lists of text string and sentiment data tuples from multiple csv files of data (mostly imported) to improve the accuracy of the program's sentiment classifications.

    posResps = list of tuples (text string, "positive")
    neutResps = list of tuples (text string, "neutral")
    negResps = list of tuples (text string, "negative")
    allResps = complete list of (response, sentiment) tuples from sample data
    files = list of file names from which I import string-sentiment data
    dataFile = current file with data being imported
    text = the polarized text from a line in the data file

    Note: no parameters, so no doctest
    """

    posResps = []
    # consider removing neutral option because it's overpowering others
    neutResps = []
    negResps = []
    files = [
        # http://help.sentiment140.com/for-students
        "stanfordSentiment140TweetData.csv",

        # # https://old.datahub.io/dataset/twitter-sentiment-analysis/resource/091d6b4b-22e9-4a64-85c4-bdc8028183ac
        # "dataHubTweetsFull.csv",

        # https://www.kaggle.com/crowdflower/twitter-airline-sentiment/version/2
        # "airlineTweets2.csv"
    ]
    for i in range(20):  # adds custom data many times to outweigh other data
        files.append("customData.csv")

    for i in range(len(files)):
        with open(files[i], "r", encoding="utf8") as dataFile:
            # w/o this encoding some characters are undefined
            for line in dataFile:
                # strip \n, convert to list of str, split at 1st comma:
                line = line.strip().split(",", 1)
                # There are a bunch of lines in the data file that are a portion of a string that got moved to a new line and it would take too long to find and remove all of them:
                try:
                    text = line[1].strip('"').lower()
                    if line[0] == '4':
                        posResps.append((text, "positive"))
                    elif line[0] == '2':
                        neutResps.append((text, "neutral"))
                    elif line[0] == '0':
                        negResps.append((text, "negative"))
                except IndexError:
                    pass
        dataFile.close()

    allResps = posResps + neutResps + negResps
    # print(f"{negResps[230:]}")  # if list too long to show: it'll cut off end
    return allResps


def initClassifier(allResps):
    """
    The function first matches the filtered possibly polar words (with punctuation removed) to their sentiment, then it prepares the sentiment classifier based on the training response examples to determine if a new given text response is overall positive, neutral or negative in tone.

    allResps = complete list of (response, sentiment) tuples from sample data
    filteredWords = changing list of words from a string that are filtered to 
                    be useful (at least three characters long, not int the ignoreWordsList not a username (@), and not a url)
    resps = list of (list of individual polar words, sentiment) tuples
    sortedWords = list of filtered words ordered by decreasing frequency
    sentimentTrainingList = list of every sentiment (for tracking num of resps)
    wordsTrainingList = list of all filteredWords lists
    ignoreWordsList = list of common, neutral words that are most likely                         accompanied by polarized words (I don't want too many                      neutral words to overload an actually polarized                            statement.)
    text = sample response string from a tuple in allResps
    textWordsList = text split into individual words in a list
    sentiment = sample sentiment string from a tuple in allResps
    word = current word (element) in a list of words from textWordsList
    trainingData = list of labeled feature sets [a list of tuples ({dict of                   each resp's extracted features}, resp sentiment string)]
    classifier = object that maps each feature to the probability of it having              a positive or negative sentiment

    Note: not doing a doc test run because I'm not sure how to make the classifier return a value in the right format without it being super long
    """

    resps = []
    filteredWords = []
    sentimentTrainingList = []
    wordsTrainingList = []
    ignoreWordsList = [  # must be lowercase
        "feel", "need", "want", "and", "then", "day", "night", "had", "has", "have", "make", "makes", "made", "was", "are", "were", "will", "afternoon", "evening", "morning", "get", "got", "receive", "received", "the", "went", "its", "his", "her", "their", "our", "they", "this", "that", "im", "mr", "mrs", "ms", "for", "you", "with", "only", "essentially", "basically", "from", "but", "just", "also", "too", "out", "today", "tonight", "tomorrow", "about", "around", "watch", "watched", "see", "saw", "hear", "heard", "now", "currently", "all", "what", "who", "where", "when", "how", "why", "some", "lots", "very", "really", "much", "many", "someone", "something"
    ]

    # match filtered (possibly polar) words to sentiment for each string:
    for i in range(len(allResps)):
        filteredWords = []
        text = allResps[i][0]  # it throws tuple error if I don't make new var
        textWordsList = text.split()
        sentiment = allResps[i][1]
        for word in textWordsList:
            if len(word) >= 3 and (word not in ignoreWordsList) and \
                    word != "@" and word[0:4] != "http":
                word = word.translate(
                    str.maketrans('', '', string.punctuation))
                filteredWords.append(word)
        resps.append((filteredWords, sentiment))
        sentimentTrainingList.append(sentiment)
        wordsTrainingList.append((filteredWords))
    # print(wordsTrainingList)
    sortedWords = getWordFeatures(getRespsWords(resps))

    # compiles training (response, sentiment) pairs and prepares classifier:
    trainingData = [
        (
            extractFeatures(sortedWords, wordsTrainingList[example]),
            sentimentTrainingList[example]
        ) for example in range(len(sentimentTrainingList))
    ]
    classifier = nltk.NaiveBayesClassifier.train(trainingData)
    return sortedWords, classifier


def classifyResp(sortedWords, classifier, userResp):
    """
    This function removes punctuation (except from the user's response, classifies the overall sentiment of the user's response, prints it, and returns the dictionary of the mood data in the form {resp, mood}.

    sortedWords = list of filtered words ordered by decreasing freq
    userResp = user's response about their day and feelings
    extractedFeatures = dict with booleons for whether or not a sorted word is                     in the user's response
    classifier = object that maps each feature to the probability of it having              a positive or negative sentiment
    mood = classified sentiment for user response
    moodDataDict = dict of user response string and mood string

    Note: not doing a doc test run because I'm not sure how to make the classifier argument in the right format without it being super long
    """

    # remove punctuation from string and split string into list:
    userRespEdited = userResp.translate(
        str.maketrans('', '', string.punctuation)
    )
    userRespEdited = userRespEdited.split()
    for word in userRespEdited:
        if len(word) < 3:
            # remove first (not all) matching value
            userRespEdited.remove(word)

    extractedFeatures = extractFeatures(sortedWords, userRespEdited)

    mood = classifier.classify(extractedFeatures)
    print(f'Your response was overall {mood}.')
    moodDataDict = {userResp: mood}
    return moodDataDict


def getRespsWords(resps):
    """
    The function separates a list in the paired form [(filtered words), sentiment] into a list of the filtered words only.

    resps = full list of (list of polar words in a string, sentiment)
    sigWords = list of all individual filtered words from resps

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

    >>> getWordFeatures(['sky', 'like', 'pie', 'like', 'like', 'pie'])
    ['like', 'pie', 'sky']
    """
    sortedWords = []
    # wouldn't maintain sorted order from nltk.DistFreq when talking .keys(); Counter is my alternative:
    sigWordsAndFreq = Counter(sigWords).most_common()
    for (word, freq) in sigWordsAndFreq:
        sortedWords.append(word)
    return sortedWords


def extractFeatures(sortedWords, words):
    """
    The function is a feature extractor that compares words in response to words in list of possible words so unused words can be ignored and response can be tested against the training data.

    sortedWords = dict keys list of filtered words ordered by decreasing freq
    words = all (filtered) response words split individually into a list
    features = dictionary of {'contains(polar word)': boolean whether or not user input string contains polar word}

    >>> extractFeatures(['like', 'pie', 'fly', 'sky'], ['I', 'like', 'pie'])
    {'contains(like)': True, 'contains(pie)': True, 'contains(fly)': False, 'contains(sky)': False}

    """
    wordSet = set(tuple(words))
    features = {}
    for word in sortedWords:
        features[f'contains({word})'] = (word in wordSet)
    return features


def storeMood(entry):
    """
    The function adds dictionaries in the form {resp: mood} to the json file.

    entry = new user entry
    dataFile = read file of json mood data
    moodData = updated json mood data to store
    oldMoodData = json mood data (user entries) stored

    Note: nothing is printed because it just writes to a file, so no doctest
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

    Note: no parameters, so no doctest
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

    Note: no parameters, so no doctest
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

    Note: no parameters, so no doctest
    """
    yesList = [
        'yes', 'yeah', 'sure', 'okay', 'ok', 'why not', 'yeet', 'yep', 'yup', 'si', 'affirmative', 'of course', 'always'
    ]
    repeat = 'yes'
    print("Please wait while the sentiment classifier is initialized.")
    allResps = getRespData()
    sortedWords, classifier = initClassifier(allResps)

    while repeat == "yes":
        # userResp = input(
        #     "\nTo make a new entry, type 'entry',\n"
        #     "to make a graph of your mood over the course of your entries so far, type 'graph',\n"
        #     "to delete all of your entries, type 'delete',\n"
        #     "or to exit the program, type 'quit'.\n"
        # ).strip().lower()
        userResp = "entry"
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
