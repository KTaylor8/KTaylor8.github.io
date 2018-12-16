import random


def calculateRolls():
    numDice = int(input(f"number of dice? "))
    numRolls = int(input(f"number of rolls? "))
    allRolls = []
    for roll in range(numRolls):
        diceSum = numDice * random.randint(1, 6)
        allRolls.append(diceSum)
    # print(f"allRolls: {allRolls}")
    return allRolls
    # print(allRolls)


def sortNums(rollsList):
    rolls = []
    rollsList.sort()
    # print(f"rollsList: {rollsList}")
    for checkingNum in rollsList:
        numNew = True
        for [num, freq] in rolls:
            if checkingNum == num:
                numNew = False
        if numNew == True:
            freq = rollsList.count(checkingNum)
            rolls.append([checkingNum, freq])
    # print(f"rolls: {rolls}")
    return rolls


def makeHistogram(rollsList):
    freqList = []
    for [num, freq] in rollsList:
        freqList.append(freq)
    freqList.sort()
    # print(f"freqList: {freqList}")
    step = round(50/freqList[0])  # scales freq for max # of * of 50
    for [num, freq] in rollsList:
        print("{}".format(num), end=" ")
        for step in range(freq):
            print("*", end="")
        print(" {}".format(freq))


def main():
    while True:
        rollNums = calculateRolls()
        sortedNums = sortNums(rollNums)
        makeHistogram(sortedNums)
        reply = input("Type 'done' to end program. ").lower().strip()
        if reply == "done":
            break
    print("Program done")


if __name__ == "__main__":
    import doctest
    doctest.testmod
    main()
