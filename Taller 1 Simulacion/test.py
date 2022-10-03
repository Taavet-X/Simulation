'''
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
#print(dict2[str(alpha)][gl])

l = [1,2,3,4,5]
#print(max(l))
'''
'''
import math
pair = (0.41, 0.68)
rowIndex = math.ceil(pair[0]/2*10)-1
columnIndex = math.ceil(pair[1]/2*10)-1
print(rowIndex)
print(columnIndex)

try:
    value = int("s")
except:
    print("No se puede")

import math
import Values

def execute(numbers, nc):

    fos = [ #FOs
        53, #[0, 0.1]
        67, #(0.1, 0.2]
        66, #(0.2, 0.3]
        59, #(0.3, 0.4]
        58, #(0.4, 0.5]  
        57, #(0.5, 0.6]
        65, #(0.6, 0.7]
        54, #(0.7, 0.8]
        64, #(0.8, 0.9]
        67, #(0.9, 1]
    ]

    #se divide la cantidad de numeros, en la cantidad de rangos
    fe = 610 / 10 #Se calcula la frecuencia esperada para cada rango

    x2sPartials = [] #El listado de los x2 individuales es decir por fila, o rango
    x2calc = 0 #Acomulador de los x2 individuales
    for fo in fos: #se recorren todas las frecuencias obtenidas
        x2Partial = (fe - fo)**2 / fe #se calcula el x2 individual es decir el de la fila
        x2calc += x2Partial #se acomula el resultado en el x2calc
        x2sPartials.append(x2Partial) #se adiciona el resultado a la lista

    gl = len(fos) - 1 #Grados de libertad, cantidad de clases - 1
    xcrit = 0.5#Values.get(gl, nc) #Se obtiene el xcritico de la tabla de probabilidades
    strRes = "gl: " + str(gl) + "\nNivel de confianza: " + str(nc) + "\nX2calc: " + str(x2calc) + "\nX2crit: " + str(xcrit)
    if x2calc <= xcrit: #En el caso de que se acepte
        strRes += "\nX2calc <= X2crit -> Los datos tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador es bueno en cuanto a uniformidad"
    else: #Caso de no aceptacion
        strRes += "\nX2calc > X2crit -> Los datos NO tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador NO es bueno en cuanto a uniformidad"
    return fos, fe, x2sPartials, x2calc, strRes

print(execute([],0.2))
'''
import math
import numpy as np

def execute(numbers, nc):
    fos = [ #Acomuladores para las frecuencias obtenidas
        53, #[0, 0.1]
        67, #(0.1, 0.2]
        66, #(0.2, 0.3]
        59, #(0.3, 0.4]
        58, #(0.4, 0.5]  
        57, #(0.5, 0.6]
        65, #(0.6, 0.7]
        54, #(0.7, 0.8]
        64, #(0.8, 0.9]
        67, #(0.9, 1]
    ]

    foas = [] #Listado para las frecuencias obtenidas ACOMULADAS
    poas = [] #Listado para las probabilidades obtenidas ACOMULADAS
    peas = [] #Listado para las probabilidades esperadas ACOMULADAS
    difs = [] #Listado para las diferencias |PEA-POA| 
    foa = 0 #Acomulador para crear progresivamente el listado foas
    DMcalc = 0 #La diferencia Mayor (Resultado)
    n = 610 #cantidad de numeros
    for i in range(len(fos)): #se recorren todas las frecuencias obtenidas
        foa += fos[i] #Acomula la FOi 
        foas.append(foa) #Adiciona el valor actual en el acomulador foa al listado foas
        poas.append(foa/n) #Adiciona la probabilidad acomulada al listado poas
        peas.append((i+1)/10) #Adiciona la probabilidad esperada al peas
        difference = round(abs(peas[i]-poas[i]),3) #Calcula la diferencia |PEA-POA|
        difs.append(difference) #Adiciona el resultado de la diferencia al listado difs
        if difference >= DMcalc: #Valida si es la mayor diferencia hasta el momento
            DMcalc = difference #en caso de ser mayor, soobrescribe el valor DMcalc

    c = math.sqrt(-np.log(nc/2)*1/2) #subtotal para calcular el DMcrit   
    gl = len(numbers) - 1 #Grados de libertad, cantidad de numeros - 1
    DMcrit = round(c/math.sqrt(n),3) #Se calcula el valor del DMcrit
    strRes = "gl: " + str(gl) + "\nNivel de confianza: " + str(nc) + "\nDMcalc: " + str(DMcalc) + "\nDMcrit: " + str(DMcrit)
    if DMcalc <= DMcrit:
        strRes += "\nDMcalc <= DMcrit -> Los datos tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador es bueno en cuanto a uniformidad"
    else:
        strRes += "\nDMcalc > DMcrit -> Los datos NO tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador NO es bueno en cuanto a uniformidad"

    return fos, foas, poas, peas, difs, DMcalc, strRes

print(execute([],0.05))