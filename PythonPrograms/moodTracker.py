import nltk  # natural language toolkit
import json


def classifyResp(resp):
    """
    Function prepares sentiment classifier based on examples (to determine if text is overall positive or negative in meaning), prints overall sentiment of response, and returns {resp, mood}
    >>> classifyResp("I love my best friend")
    {"I love my best friend" : positive}
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

    # match possibly polar words to sentiment
    for (words, sentiment) in posResps + negResps:
        for el in words.split():
            if len(el) >= 3:  # shorter words neutral
                filteredWords.append(el.lower())
        resps.append((filteredWords, sentiment))
    wordFeatures = getWordFeatures(getRespsWords(resps))

    # compiles training (response, sentiment) pairs and prepares classifier
    extractedFeatures = extractFeatures(wordFeatures, resp.split())
    trainingData = nltk.classify.apply_features(extractedFeatures, resps)
    classifier = nltk.NaiveBayesClassifier.train(trainingData)

    # response's overall sentiment will eventually affect how program responds
    # but for now it just prints the overall sentiment
    mood = classifier.classify(extractedFeatures)
    print(f'Your response was overall {mood}')
    moodData = {resp: mood}
    return moodData


def getRespsWords(resps):
    """
    Function separates [(words filtered to be > 3 characters), sentiment] list of pairs into list of those words only
    >>> getRespsWords([("love", "best", "friend"), "positive"])
    ["love","best","friend"]
    """
    allWords = []
    for (words, sentiment) in resps:
        # extend() adds each individual element, not whole list
        allWords.extend(words)
    return allWords


def getWordFeatures(wordlist):
    """
    Function reorders list of filtered words by decreasing frequency
    """
    wordlist = nltk.FreqDist(wordlist)
    wordFeatures = wordlist.keys()
    return wordFeatures


def extractFeatures(featuresList, document):
    """
    Function is a feature extractor that compares words in response to words in list of possible words so unused words can be ignored and response can be tested against the training data
    """
    documentWords = set(document)
    features = {}
    for word in featuresList:
        features[f"contains{word}"] = (word in documentWords)
    return features


def storeMood(moodData):
    """
    Function writes dictionaries of {resp: mood} to json file
    """
    f = open("moodTrackerData.json", "a")
    f.write(f"\n{moodData}")
    # CURRENTLY NOT STORED IN CORRECT FORMAT


def main():
    """
    Program's main process: asks user about their day to determine their mood, with the option to repeat
    """
    repeat = ''
    while repeat != "yes":
        userInput = input(
            "Please describe your day and how you feel about it.\n"
        ).lower()
        print(classifyResp(userInput))
        # storeMood(classifyResp(userInput))
        # repeat = input("Do you want to make another entry?\n").lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
