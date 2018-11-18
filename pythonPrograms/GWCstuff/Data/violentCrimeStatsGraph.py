#https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt
import state_crime
list_of_report = state_crime.get_all_crimes()

def average(numList):
    sum = 0
    for i in range(len(numList)):
        sum += numList[i]
    average = sum/len(numList)
    average = int(average)
    return average

list4Average = []
numRapes = []

#average number of rapes in washington
for row in list_of_report:
    if row["State"] == "Washington":
        list4Average.append(row["Data"]["Totals"]["Violent"]["Rape"])
        numRapes.append(row["Data"]["Totals"]["Violent"]["Rape"])

#What was the average number of rapes per year from 1960-2012?
print("Average number of rapes in Washington for 1960-2012: ", average(list4Average))

#How did the number of rapes in Washington change over time?
#makes a list of years to go on the x-axis
yearList = []
year = 1960
for i in range(53):
    yearList.append(year)
    year = year + 1

#make Washington rapes vs years graph
plt.plot(yearList, numRapes, 'r^')
plt.plot(yearList, numRapes, 'k')
plt.xlabel('Year')
plt.ylabel('Number of Rapes')
plt.title('Rapes vs Years in Washington')
plt.grid(True)
plt.show()
