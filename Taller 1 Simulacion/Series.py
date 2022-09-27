import math
import Values

def execute(numbers, nc):
    matrix = [ #Matriz para las frecuencias (Contadores o FOs)
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    matrix2 = [ #Matriz para los X2s
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    #Se aplica la funcion techo, para el caso de que no sea un numero par
    #entonces el resultado sea un numero entero
    for i in range(math.ceil(len(numbers)/2)): #se recorre el listado de 2 en 2
        try:
            pair = (numbers[i*2], numbers[i*2 + 1]) #Se intenta formar parejas de numeros generados
            #El primer elemento corresponde a la fila, el segundo a la columna que corresponde
            rowIndex = math.ceil(pair[0]/2*10)-1 # Se convierte el numero, a la fila correspondiente
            columnIndex = math.ceil(pair[1]/2*10)-1 #Se convierte el numero, a la columna correspondiente
            matrix[rowIndex][columnIndex] += 1 #Suma uno en dicha posicion de la matriz de FOs
        except:
            #El error surge cuando se intenta formar una pareja pero la cantidad de numeros
            #no es par
            print("The list lenght wasn't odd, the last number is not included")            

    n = len(numbers) #La cantidad de numeros
    FE = (n/2) / 25 #Frecuencia esperada (cantidad de parejas / cantidad de clases o celdas)

    X2calc = 0 #total (La suma de todas las celdas)
    for i in range(len(matrix)): #recorre el numero de filas
        for j in range(len(matrix[i])): #recorre el numero de columnas
            FO = matrix[i][j] #se almacena temporalmente la frecuencia obtenida
            X2i = round( (FE-FO)**2 /FE, 2) #Se calcula el X2 correspondiente a la celda o clase
            matrix2[i][j] = X2i #se almacena el resultado del X2 en la segunda matriz
            X2calc += matrix2[i][j] #acomula el resultado del X2i, en el X2total

    gl = len(matrix)*len(matrix[0]) - 1 #Grado de libertad (Cantidad de celdas - 1)
    xcrit = Values.get(gl, nc) #Se trae el valor X2Critico de la tabla de probabildades
    strRes = "gl: " + str(gl)
    strRes += "\nNivel de confianza: " + str(nc)
    strRes += "\nX2calc: " + str(X2calc)
    strRes += "\nX2crit: " + str(xcrit)
    if X2calc <= xcrit:
        strRes += "\nX2calc <= X2crit"
        strRes += "\n\nConclusión:\nEl resultado no permite rechazar la hipotesis de independencia"
    else:
        strRes += "\nX2calc > X2crit"
        strRes += "\n\nConclusión:\nSe rechaza la hipotesis de independencia"

    return matrix, matrix2, strRes