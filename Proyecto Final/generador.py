from random import random

f = [
    0.0013,
    0.0228,
    0.1586,
    0.5,
    0.8413,
    0.9772,
    0.9987
]

def getValues(r):
    for i in range(len(f)):
        if r <= f[i]:
            fx1 = f[i]
            fx0 = f[i-1]            
            return (fx1-r)/(fx1-fx0), i-3, (i-4)

def getNormalValue(r, mu, rho):
    l, x1, x0 = getValues(r)
    a = (l*x0)+((1-l)*x1)
    return a*rho+mu

def U(a, b):
    random(a, b)

def N(mu, rho):
    getNormalValue(U(0,1), mu, rho)



'''
R = [
    0.5520,
    0.4881,
    0.7512,
    0.3124,
    0.5696,
    0.7238,
    0.9438
]

for r in R:
    a = getNormalValue(r, 10, 2)
    print(a)
'''
