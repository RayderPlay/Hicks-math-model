import numpy as np
from builtins import range
import matplotlib.pyplot as plt

leftLim = -2.0
rightLim = 2.0
iteration = 0.01

firstCoefficient = 1
secondCoefficient = 1
accelerator = 1
nationalIncome = [
    1,
    1
]

#Processing of the model Hicks
def personalInvestition(arr, firstCoefficient, secondCoefficient, accelerator):
    personalMoney = 0
    inducedInvestment = 0
    investition = []
    investition.append(arr[0])
    investition.append(arr[1])
    for i in range(2, 20):
        personalMoney = firstCoefficient * investition[i - 1] + secondCoefficient * investition[i - 2]
        inducedInvestment = accelerator * (investition[i - 1] - investition[i - 2])
        investition.append(round(personalMoney + inducedInvestment, 4))
    return investition

#Сhecking of coefficients
def checkFunction(c1, c2):
    arr = personalInvestition(nationalIncome, c1, c2, accelerator)

    if arr[18] != 0:
        return False
    else:
        return True

res = []
dataY = [[] for i in np.arange(leftLim, rightLim, iteration)]
dataX = [[] for i in np.arange(leftLim, rightLim, iteration)]
stage = 0
res = [[], []]

for i in np.arange(leftLim, rightLim, iteration):
    for j in np.arange(leftLim, rightLim, iteration):
        if checkFunction(i, j):
            dataY[stage].append(round(i * 10, 2))
            dataX[stage].append(round(j * 10, 2))
            res[1].append(round(i * 10, 2))
            res[0].append(round(j * 10, 2))
    stage += 1

f1 = open('dataX.txt', 'w')
f2 = open('dataY.txt', 'w')

f1.write(str(res[0]))
f2.write(str(res[1]))
f2.close()
f1.close()

print(dataX)
print(dataY)

plt.scatter(res[0], res[1], s = 1)
plt.show()
