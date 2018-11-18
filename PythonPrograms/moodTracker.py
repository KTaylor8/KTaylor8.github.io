import nltk  # natural language toolkit
import json
import os
# sentiment is the connotation of a word (positive or negative)


def classifyResp(userResp):
    """
    Function prepares sentiment classifier based on examples (to determine if text is overall positive or negative in meaning), prints overall sentiment of response, and returns {resp, mood}

    userResp = user's response about their day
    posResps = list of (text string, "positive")
    negResps = list of (text string, "negative")
    filteredWords = list of words longer than 2 characters (filtered words)
    resps = list of (list of polar words in a string, sentiment)
    sortedWords = list of filtered words ordered by decreasing frequency

    >>> classifyResp("My best friend is amazing")
    {"My best friend is amazing" : positive}
    """

    pos = "positive"
    neg = "negative"

    # training data: (response, sentiment)
    # limited now but will add more later
    posResps = [("I love my new car", pos),
                ("The view from my house is amazing", pos),
                ("I feel great this morning", pos),
                ("I am so excited about the concert", pos),
                ("He is my best friend", pos)]
    negResps = [("I hate my new car", neg),
                ("The view from my house is horrible", neg),
                ("I feel tired this morning", neg),
                ("I am dreading the concert", neg),
                ("He is my worst enemy", neg)]

    resps = []
    filteredWords = []

    # match filtered (possibly polar) words to sentiment for each string
    for (string, sentiment) in posResps + negResps:
        for el in string.split():
            if len(el) >= 3:  # shorter words neutral
                filteredWords.append(el.lower())
        resps.append(filteredWords, sentiment)
        filteredWords.clear()
    sortedWords = getWordFeatures(getRespsWords(resps))

    # compiles training (response, sentiment) pairs and prepares classifier
    # ISSUE: apply_features should be returning a list-like obj but apparently it's a dict
    extractedFeatures = extractFeatures(sortedWords, userResp.split())
    trainingData = nltk.classify.apply_features(extractedFeatures, resps)
    classifier = nltk.NaiveBayesClassifier.train(trainingData)

    # response's overall sentiment will eventually affect how program responds
    # but for now it just prints the overall sentiment
    mood = classifier.classify(extractedFeatures)
    print(f'Your response was overall {mood}')
    moodDataDict = {userResp: mood}
    return moodDataDict


def getRespsWords(resps):
    """
    Function separates [(filtered words), sentiment] list of pairs into list of those words only

    resps = list of (list of polar words in a string, sentiment)
    sigWords = list of all filtered individual words from the string

    >>> getRespsWords([("love", "best", "friend"), "positive"])
    ["best","friend","amazing"]
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
    userResp = user's response about their day
    features = dictionary of {"contains(polar word)": whether or not user input string contains polar word}

    """
    userRespWords = set(userResp)
    features = {}
    for word in sortedWords:
        features[f"contains{word}"] = (word in userRespWords)
    return features


def storeMood(moodDataDict):
    """
    Function writes dictionaries of {resp: mood} to json file

    moodData = (user input string, sentiment)

    """
    moodDataStr = ("{\n" +
                   f"{moodDataDict.key()}" +
                   ":" +
                   f"{moodDataDict.value()}" +
                   "\n}")
    f = open("moodTrackerData.json", "a+")
    if os.stat(f).st_size == 0:  # if file empty
        f.write("{\n" +
                f"{moodDataStr}" +
                "\n}"
                )
    else:
        f.seek(-1, os.SEEK_END)
        f.truncate()  # delete ending } in file
        # convert from dict {userResp: mood} to string {\n dict \n}
        f.write(f"\n{moodDataStr}" +
                "\n}"
                )

    f.close()


def main():
    """
    Program's main process: asks user about their day to determine their mood, with the option to repeat

    repeat = whether the user wants to repeat the program or not
    userResp = user's response about their day

    """
    repeat = ''
    while repeat != "yes":
        userResp = input(
            "Please describe your day and how you feel about it.\n"
        ).lower()
        print(classifyResp(userResp))
        # storeMood(classifyResp(userInput))
        # repeat = input("Do you want to make another entry?\n").lower()
        # DEBUGGING


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
