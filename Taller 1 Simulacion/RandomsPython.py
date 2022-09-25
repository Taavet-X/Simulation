import random
import X2
import KolmogorovSmirnov
import Corridas
import Series
import Poker

randoms = []

def execute(limit):
    for i in range(limit):
        Rn = random.random() #Genera el numero Rn
        randoms.append(Rn) #Adiciona Rn A la lista
    return randoms

'''
execute(1000)

X2.execute(randoms)
print("-----------------------")
KolmogorovSmirnov.execute(randoms)
print("-----------------------")
Corridas.execute(randoms)
print("-----------------------")
Series.execute(randoms)
print("-----------------------")
Poker.execute(randoms,5)
'''