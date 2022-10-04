import math

#Metodo transformada inversa para distribucion exponencial
def exponencial(randoms, l):
    result = []
    for i in range(len(randoms)):
        a = -(1/l) * math.log(randoms[i])
        result.append(round(a, 4))
    return result

#Metodo de la transformada inversa para la distribucion uniforme u(A, B)
def uniforme(numbers, A, B):
    dif = B - A
    result = []
    for i in range(len(numbers)):
        a = numbers[i] * A + dif
        result.append(a)
    return result 

#Transformada inversa Normal Estandarizada
dict = {
    -3: 0.0013,
    -2: 0.0228,
    -1: 0.1586,
    0:  0.5,
    1: 0.8413,
    2: 0.9772,
    3: 0.9987
}

def normal(numbers, x0, x1):
    result = []
    for r in numbers:
        l = (dict[x1] - r)/(dict[x1]-dict[x0])
        a = l*x0 + (1-l)*x1
        result.append(a)
    return result

#normal centralizada
def centralizada(numbers,x0n, x1n, mu, s):
    result = []
    for r in numbers:
        l = (dict[x1n] - r)/(dict[x1n]-dict[x0n])
        a = l*x0n + (1-l)*x1n
        a = a * s + mu
        result.append(a)
    return result

randoms = [
    0.5520,
    0.4881,
    0.7512,
    0.3124,
    0.5696,
    0.7238,
    0.9438
]
#print(*exponencial(randoms, 1.5), sep = "\n")
print(*centralizada(randoms, 0, 1, 10, 2), sep = "\n")