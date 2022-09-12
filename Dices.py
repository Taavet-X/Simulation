from ast import Global
from random import randint
import matplotlib.pyplot as plt

def throwDices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1 + dice2

counter = {}
for i in range(10000):
    result = throwDices()
    if result in counter:
        counter[result] += 1
    else:
        counter[result] = 1    
counter = dict(sorted(counter.items()))

plt.plot(list(counter.keys()),list(counter.values()))
plt.show()
