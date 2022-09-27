import math
import numpy as np

def execute(numbers, nc):
    fos = [ #Acomuladores para las frecuencias obtenidas
        0, #[0, 0.1]
        0, #(0.1, 0.2]
        0, #(0.2, 0.3]
        0, #(0.3, 0.4]
        0, #(0.4, 0.5]  
        0, #(0.5, 0.6]
        0, #(0.6, 0.7]
        0, #(0.7, 0.8]
        0, #(0.8, 0.9]
        0, #(0.9, 1]
    ]
    for number in numbers: #se recorren todos los numeros
        index = math.ceil(number*10)-1 #Se convierte el numero al indice que corresponde en el listado fos
        fos[index] += 1 #Suma 1 a esa posicion

    foas = [] #Listado para las frecuencias obtenidas ACOMULADAS
    poas = [] #Listado para las probabilidades obtenidas ACOMULADAS
    peas = [] #Listado para las probabilidades esperadas ACOMULADAS
    difs = [] #Listado para las diferencias |PEA-POA| 
    foa = 0 #Acomulador para crear progresivamente el listado foas
    DMcalc = 0 #La diferencia Mayor (Resultado)
    n = len(numbers) #cantidad de numeros
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