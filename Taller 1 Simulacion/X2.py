import math
import Values

def execute(numbers, nc):

    fos = [ #FOs
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

    for number in numbers: #Recorrer todos los numeros generados
        index = math.ceil(number*10)-1 #Se convierte el numero al indice que corresponde en el listado fos
        fos[index] += 1 #Suma 1 a esa posicion

    #se divide la cantidad de numeros, en la cantidad de rangos
    fe = len(numbers) / len(fos) #Se calcula la frecuencia esperada para cada rango

    x2sPartials = [] #El listado de los x2 individuales es decir por fila, o rango
    x2calc = 0 #Acomulador de los x2 individuales
    for fo in fos: #se recorren todas las frecuencias obtenidas
        x2Partial = (fe - fo)**2 / fe #se calcula el x2 individual es decir el de la fila
        x2calc += x2Partial #se acomula el resultado en el x2calc
        x2sPartials.append(x2Partial) #se adiciona el resultado a la lista

    gl = len(fos) - 1 #Grados de libertad, cantidad de clases - 1
    xcrit = Values.get(gl, nc) #Se obtiene el xcritico de la tabla de probabilidades
    strRes = "gl: " + str(gl) + "\nNivel de confianza: " + str(nc) + "\nX2calc: " + str(x2calc) + "\nX2crit: " + str(xcrit)
    if x2calc <= xcrit: #En el caso de que se acepte
        strRes += "\nX2calc <= X2crit -> Los datos tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador es bueno en cuanto a uniformidad"
    else: #Caso de no aceptacion
        strRes += "\nX2calc > X2crit -> Los datos NO tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador NO es bueno en cuanto a uniformidad"
    return fos, fe, x2sPartials, x2calc, strRes