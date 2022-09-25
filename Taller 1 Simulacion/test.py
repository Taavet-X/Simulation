dict = {
    "key1": 1,
    "key2": 2
}

try:
    dict["key3"] #Se intenta acceder posicion que no existe y arroja error
except: 
    dict["key3"] = 3 #entonces se crea el nuevo registro

for key in dict.keys():
    print(key) #imprime la llave
    print(dict[key]) #imprime el dato almacenado con dicha llave


dict2 = {
    "0.5" : [0.45, 1.39, 2.37],
    "0.25" : [0.32, 2.77, 4.11, 5.39]
}

alpha = 0.25
gl = 3
gl -= 1
print(dict2[str(alpha)][gl])

l = [1,2,3,4,5]
print(max(l))