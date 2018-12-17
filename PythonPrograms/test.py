# lists = []
# for i in range(1, 7):
#     lists.append(i)
# for x in range(len(lists)):
#     print("{}\t".format(lists[x]), end=" ")
import json
import os


def testMergeDicts():
    date_info = {'year': "2020", 'month': "01", 'day': "01"}
    track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
    all_info = {**date_info, **track_info}
    print(all_info)


def testForLoopInList():
    string = "I am a happy person with lots of food and a good home"
    filteredWords = [el.lower() for el in string.split()]
    print(filteredWords)


def testFileEmpty():  # FOR SOME REASON ALWAYS THINKS FILE EMPTY
    with open("answers.json", "w+") as dataFile:
        print(os.stat("answers.json").st_size)
        print(os.path.getsize("answers.json"))
        if os.stat("answers.json").st_size == 0:  # file empty
            # if os.path.getsize("answers.json") == 0:  # file empty
            print("file empty")
        else:
            print("file occupied")


def testJson():
    entry = {"n": "positive"}
    # entry1 = {"key": "value"}
    # entry2 = {**entry, **entry1}
    # print(entry2)
    # dataFile = open("moodTrackerData.json", "r+")
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


def testForLoop():
    list1 = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    for (num1, num2) in list1:
        print(num1+num2)

    for i in range(10):
        print(i, end=" ")


def testSlicing():
    list1 = [1, 2, 3, 4, 5]
    print(list1[1:4])  # slice has inclusive start and exclusive end
    for i in range(3):  # range starts at 0 and has exclusive end
        print(i, end=": ")
        print(list1[i])


def testUnpacking():
    list1 = [1, 2, [3, 4]]
    a, b, c = list1
    print(c, b, a)


def testReferencingNests():
    list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    for el in list1:
        print(el)


def testKeys():
    dict = {'Name': 'Zara', 'Age': 7, 8.0: 'cat'}
    print(dict.keys())


def main():
    testKeys()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()


# for receivingN in range(self.layerSizes[layer]):
#             neuronOutList = []  # outputs from a neuron when fed all inputs
#             # for each input that the receiving neuron receives:
#             for inNum in range(len(inList)):
#                 # for neuron in range(self.layerSizes[layerI+1]): don't think needed
#                 neuronWs = self.w[layer][receivingN]
#                 neuronBs = self.b[layer][receivingN][0]
#                 print(
#                     f'receiving neuron #: {receivingN}'
#                     f'\t1 hidden w for 1 connection: {neuronWs}'
#                     f'\t1 hidden b for 1 connection: {hiddenB}')
#                 neuronOutArr = self.sigmoid(
#                     np.dot(hiddenW, inList)+hiddenB
#                 )
#                 neuronOutList.append(neuronOutArr[0])
#             inList.append(neuronOutList)
#             append(neuronInList)
#             # print('hiddenOutputList: ', hiddenOutputList)  # debugging

#         rawExpOut = inList
#         # # for loop not really necessary since we only have 1 output neuron
#         # for neuron in range(self.layerSizes[layerI+1]):
#         #     print(f"Initial weights = {self.w}\n")
#         #     print(f'output layer weights: {self.w[layerI][0]}')
#         #     outputW = self.w[layerI][0][neuron]
#         #     # print(f"Initial biases = {self.b}\n")
#         #     # print(f'output layer bias: {self.b[layerI][0][0]}')
#         #     # doesn't change throughout feedforward() b/c there's only 1 output neuron that all connections go through
#         #     outputB = self.b[layerI][0][0]
#         #     print(
#         #         f'neuron #: {neuron}'
#         #         f'\t1 hidden w for 1 connection: {hiddenW}'
#         #         f'\t1 hidden b for 1 connection: {hiddenB}')
#         #     finalNeuronOutputArr = self.sigmoid(
#         #         np.dot(outputW, hiddenOutputList)+outputB
#         #     )
#         #     finalNeuronOutput = finalNeuronOutputArr[0]
