import nltk  # natural language toolkit
import json
import os
from matplotlib import pyplot as plt
from matplotlib import axes as axes
import string
from collections import Counter
import numpy as np
# it thinks everything is positive with only the custom data and it thinks sad and bad are neutral unless they're together (very similar to moodTracker.py); don't forget to add the dataHub data back in


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
    neutResps = []
    negResps = []
    files = [
        # http://help.sentiment140.com/for-students
        "stanfordSentiment140TweetData.csv",

        # # https://old.datahub.io/dataset/twitter-sentiment-analysis/resource/091d6b4b-22e9-4a64-85c4-bdc8028183ac
        # "dataHubTweetsFull.csv",

        # # crashes the program b/c it's too much data or takes too long to load; "MemoryError  Exception: No Description": https://www.kaggle.com/crowdflower/twitter-airline-sentiment/version/2
        # "airlineTweets2.csv"
    ]
    # + custom data 20 times to outweigh specific words' tone in other files:
    for i in range(20):
        files.append("customData.csv")

    for i in range(len(files)):
        with open(files[i], "r", encoding="utf8") as dataFile:
            # w/o utf8 encoding some characters, are undefined
            for line in dataFile:
                line = line.strip().split(",", 1)
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
    return allResps


def initClassifier(allResps, ignoreWordsList):
    """
    The function first matches the filtered possibly polar words (with punctuation removed) to their sentiment, then it prepares the sentiment classifier based on the training response examples to determine if a new given text response is overall positive, neutral or negative in tone.

    allResps = complete list of (response, sentiment) tuples from sample data

    filteredWords = changing list of words from a string that are filtered to be useful (at least three characters long, not int the ignoreWordsList not a username (@), and not a url)

    resps = list of (list of individual polar words, sentiment) tuples

    sortedWords = list of filtered words ordered by decreasing frequency

    sentimentTrainingList = list of every sentiment (for tracking num of responses)

    wordsTrainingList = list of all filteredWords lists

    ignoreWordsList = list of common, neutral (or very context dependent) words that are most likely accompanied by polarized words (I don't want too many neutral words to overload an actually polarized statement.)

    text = sample response string from a tuple in allResps

    textWordsList = text split into individual words in a list

    sentiment = sample sentiment string from a tuple in allResps

    word = current word (element) in a list of words from textWordsList

    trainingData = list of labeled feature sets [a list of tuples ({dict of each resp's extracted features}, resp sentiment string)]

    classifier = object that maps each feature to the probability of it having a positive or negative sentiment

    Note: not doing a doc test run because I'm not sure how to make the classifier return a value in the right format without it being super long
    """

    resps = []
    filteredWords = []
    sentimentTrainingList = []
    wordsTrainingList = []

    # filter and organize words from sample data:
    for i in range(len(allResps)):
        filteredWords = []
        sentiment = allResps[i][1]
        text = allResps[i][0]  # throws tuple error if I don't make new var
        textWordsList = text.split()

        # remove usernames:
        wordsToRemove = []
        for word in textWordsList:
            if word[0] == "@":
                wordsToRemove.append(word)
        textWordsList = [
            el for el in textWordsList if el not in wordsToRemove
        ]

        # join, remove punctuation (as str, not str-split list), re-split:
        text2 = ' '.join(textWordsList)
        text2 = text2.translate(str.maketrans('', '', string.punctuation))
        textWordsList2 = text2.split()

        # filter other unhelpful words:
        for word in textWordsList2:
            if len(word) >= 3 and (word not in ignoreWordsList) and \
                    word[0:4] != "http":
                filteredWords.append(word)

        resps.append((filteredWords, sentiment))
        sentimentTrainingList.append(sentiment)
        wordsTrainingList.append((filteredWords))
    sortedWords = getWordFeatures(getRespsWords(resps))

    # compiles training pairs (response, sentiment) and prepares classifier:
    trainingData = [
        (
            extractFeatures(sortedWords, wordsTrainingList[example]),
            sentimentTrainingList[example]
        ) for example in range(len(sentimentTrainingList))
    ]
    classifier = nltk.NaiveBayesClassifier.train(trainingData)
    return sortedWords, classifier


def classifyResp(sortedWords, classifier, userResp, ignoreWordsList):
    """
    This function removes punctuation (except from the user's response, classifies the overall sentiment of the user's response, prints it, and returns the dictionary of the mood data in the form {resp, mood}.

    sortedWords = list of filtered words ordered by decreasing freq

    userResp = user's response about their day and feelings

    ignoreWordsList = list of common, neutral (or very context dependent) words that are most likely accompanied by polarized words (I don't want too many neutral words to overload an actually polarized statement.)

    extractedFeatures = dict with booleons for whether or not a sorted word is in the user's response

    classifier = object that maps each feature to the probability of it having a positive or negative sentiment

    mood = classified sentiment for user response

    moodDataDict = dict of user response string and mood string

    Note: not doing a doc test run because I'm not sure how to make the classifier argument in the right format without it being super long
    """

    # remove punctuation from string and split string into list:
    userRespEdited = userResp.translate(
        str.maketrans('', '', string.punctuation)
    )

    # remove short/unhelpful words:
    userRespEdited = userRespEdited.split()
    wordsToRemove = []
    for word in userRespEdited:
        if len(word) < 3 or word in ignoreWordsList:
            wordsToRemove.append(word)
    userRespEdited = [el for el in userRespEdited if el not in wordsToRemove]

    extractedFeatures = extractFeatures(sortedWords, userRespEdited)

    mood = classifier.classify(extractedFeatures)
    print(f'\nYour response was overall {mood}.')
    respond(userRespEdited, mood)
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
        sigWords.extend(words)
    return sigWords


def getWordFeatures(sigWords):
    """
    The function reorders the list of filtered words by decreasing frequency.

    sigWords = list of all filtered individual words from the string

    sigWordsAndFreq = list of tuples in the form (filtered word, frequency)

    sortedWords = list of filtered words ordered by decreasing frequency

    >>> getWordFeatures(['sky', 'like', 'pie', 'like', 'like', 'pie'])
    ['like', 'pie', 'sky']
    """
    sortedWords = []
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


def respond(userRespWords, mood):
    """
    The function searches for key words in the user's response in order to provide a response to the user's entry  that is helpful for certain situations.

    userRespWords = list of useful individual words filtered from user response

    mood = predicted sentiment of 

    sleepTipKW = list of key words to trigger sleep tips

    selfCareKW = list of key words to trigger affirmation of a positive experience

    sickKW = list of key words to trigger suggestions regarding sickness

    >>> respond(["tired","not","sleep"], "negative")
    The average adult needs to sleep for 7-9 hours. If you find yourself laying awake at night, there are several things you can do to help you sleep.
    Eat foods with melatonin around bedtime, such as cherries.
    To relax, you can try the 4-7-8 breathing technique: breathe in for 4 seconds, hold your breath for 7 seconds, and breathe out for 8 seconds.
    You can also flex all of your muscles, starting at your feet and gradually working your way up to your head, then gradually relax them, again, starting from your feet and working your way up to your head.
    """

    sleepTipKW = ["sleepy", "sleep", "drowsy"]
    selfCareKW = ["holiday", "vacation", "relax", "party", "festival"]
    sickKW = ["sick", "illness", "unwell", "sickness", "fever"]

    if mood == "negative" and (set(userRespWords) & set(sleepTipKW)):
        print(
            "The average adult needs to sleep for 7-9 hours. "
            "If you find yourself laying awake at night, there are several things you can do to help you sleep."
            "\nEat foods with melatonin around bedtime, such as cherries."
            "\nTo relax, you can try the 4-7-8 breathing technique: "
            "breathe in for 4 seconds, hold your breath for 7 seconds, and breathe out for 8 seconds."
            "\nYou can also flex all of your muscles, starting at your feet and gradually working your way up to your head, "
            "then gradually relax them, again, starting from your feet and working your way up to your head."
        )
    elif mood == "positive" and (set(userRespWords) & set(selfCareKW)):
        print(
            "Yay! Life is too short to not enjoy yourself. "
            "Always remember that you ARE worth it."
        )
    elif mood == "negative" and (set(userRespWords) & set(sickKW)):
        print(
            "If you need to take a sick day tomorrow to rest, don't be afraid to do it. "
            "It will keep the sickness from spreading to others and will allow your body to fight it, so it's a win-win. "
            "\nAnd if you worry that you are seriously ill, then visit the doctor, rather than trying to diagnose and treat yourself."
        )
    elif mood == "negative":
        print(
            "Your struggles and pain are valid. "
            "Nevertheless, choose to believe that that you will get through this and make the future brighter. "
            "Choose positivity and gratitude simply because it feels better."
        )
    elif mood == "positive":
        print("Yay! Happy days are the best days!")


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
        if os.path.getsize("moodTrackerData.json") == 0:  # file empty
            moodData = entry
        else:  # file occupied
            oldMoodData = json.load(dataFile)
            moodData = {**oldMoodData, **entry}  # consolidates duplicate pairs
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

    try:
        with open("moodTrackerData.json", "r+") as dataFile:
            entries = json.load(dataFile)
            entriesCount = [entry for entry in range(1, len(entries)+1)]
            sentimentList = [mood for mood in entries.values()]

        plt.plot(entriesCount, sentimentList, 'bo-')  # x, y, marker
        plt.yticks(sentimentList, sentimentList)
        plt.xticks(np.arange(min(entriesCount), max(entriesCount)+1, 1.0))
        plt.ylabel('Sentiment')
        plt.xlabel('Entry Number')
        plt.title('Sentiment vs Entry Number Graph')
        plt.show()

    except json.decoder.JSONDecodeError:
        print(
            "Sorry. There's not enough data to graph. Make a new entry first."
        )


def deleteEntries():
    """
    This simple function overwrites the json file storing the entry data in order to clear it.

    Note: no parameters, so no doctest
    """
    open("moodTrackerData.json", "w").close()
    print("You have deleted all of your entries.")


def main():
    """
    The function serves as the program's main menus and loops in asking the user to chose between a variety of actions (make a new entry, graph your mood data, delete all entries, or quit the program) and calling the function for that functionality until the user quits.

    ignoreWordsList = list of common, neutral (or very context dependent) words that are most likely accompanied by polarized words (I don't want too many neutral words to overload an actually polarized statement.)

    yesList = list of possible responses to the repeat program question used to determine whther the user wants to perform further actions

    repeat = whether the user wants to repeat the program or not

    userResp = user's response about their day

    sortedWords = list of filtered words ordered by decreasing frequency

    classifier = object that maps each feature to the probability of it having a positive or negative sentiment

    Note: no parameters, so no doctest
    """
    ignoreWordsList = [  # must be lowercase and w/o punctuation
        "feel", "need", "want", "and", "then", "day", "night", "had", "has", "have", "make", "makes", "made", "was", "are", "were", "will", "afternoon", "evening", "morning", "get", "got", "receive", "received", "the", "went", "its", "his", "her", "their", "our", "they", "them", "this", "that", "im", "mr", "mrs", "ms", "for", "you", "with", "only", "essentially", "basically", "from", "but", "just", "also", "too", "out", "today", "tonight", "tomorrow", "about", "around", "watch", "watched", "see", "saw", "hear", "heard", "now", "currently", "all", "what", "who", "where", "when", "how", "why", "some", "lots", "very", "really", "much", "many", "someone", "something", "since", "because", "which", "there", "did", "more", "less"
    ]

    yesList = [
        'yes', 'yeah', 'sure', 'okay', 'ok', 'why not', 'yeet', 'yep', 'yup', 'si', 'affirmative', 'of course', 'always'
    ]
    repeat = 'yes'
    print(
        "Welcome to Katie's Mood Tracker!\n"
        "Please wait while the sentiment classifier initializes."
    )
    allResps = getRespData()
    sortedWords, classifier = initClassifier(allResps, ignoreWordsList)

    graphSentiments()  # debugging
    while repeat == "yes":
        userResp = input(
            "\nTo make a new entry, type 'entry',\n"
            "to make a graph of your mood over the course of your entries so far, type 'graph',\n"
            "to delete all of your entries, type 'delete',\n"
            "or to exit the program, type 'quit'.\n"
        ).strip().lower()
        if userResp == "entry":
            userResp = input(
                "\nPlease describe your day and how you feel about it."
                "\n(Stick to one general tone in your entry, please, or "
                "this version of the mood tracker will get confused)\n"
            ).lower()
            storeMood(classifyResp(
                sortedWords, classifier, userResp, ignoreWordsList
            ))
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
