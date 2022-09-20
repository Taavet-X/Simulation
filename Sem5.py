import numpy as np
#a = -1/lambda * ln(r)
# r es un aleatori en (0,1]
#lambda es un margen de error

rs = [
    0.998011,
    0.802474,
    0.865982,
    0.025413,
    0.497639,
    0.614659,
    0.180718,
    0.733765,
    0.327262,
    0.853182,
    0.481597,
    0.430662,
    0.886753,
    0.910834,
    0.441091
]

#distribucion exponencial
l = 1.5
print("")
for r in rs:
    a = -1/l * np.log(r)
    print(a)  


#acomulada
#a = (B-A)r+A
A = 10
B = 20
print("Acomulada")
for r in rs:
    a = (B-A)*r+A
    print(a)

#normal estandarizada
dic = {
    "-3":0.0013,
    "-2":0.0228,
    "-1":0.1586,
    "0":0.5,
    "1":0.8413,
    "2":0.9772,
    "3":0.9987
}
print("Normal")
x1 = 0
x2 = 1
for r in rs:
    l = (r-dic[str(x2)])/(dic[str(x1)]-dic[str(x2)])
    a = (l*x1+(1-l)*x2)
    print("l",l,"a",a)
