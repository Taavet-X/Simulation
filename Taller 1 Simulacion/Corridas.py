import math
import Values
#Cinco decimales
#mostrar la tabla chi cuadrado
#3 y de 5 decimales
def execute(numbers, alpha):
    #para el diccionario la estructura se contempla asi:
    #{"longitud de corrida": veces que aparece}
    counters = {}
    res = "*"
    last = "*"
    counter = 1
    lastValue = numbers[0]
    total = 0
    for value in numbers[1:]:
        behavior = ""
        if value > lastValue:            
            behavior = "+"
        elif value < lastValue:
            behavior = "-"

        if last != behavior:
            try:
                counters[counter] += 1
            except:
                counters[counter] = 1
            counter = 1
            total += 1
        else:
            counter +=1
        
        res += behavior
        last = behavior
        lastValue = value

    n = len(numbers)
    mu = (2*n - 1)/3
    s = (16*n-29)/90
    Zobs = (total - mu)/math.sqrt(s)
    halfAlpha = alpha/2
    Zcrit = Values.getZ(halfAlpha)

    strRes = str(counters)
    strRes += "\nNivel de confianza: " + str(alpha) 
    strRes += "\nMedia: " + str(mu) 
    strRes += "\nVarianza: " + str(s) 
    strRes += "\nZobs: " + str(Zobs)
    strRes += "\nZcrit: " + str(Zcrit)
    if Zobs >= -Zcrit and Zobs <= Zcrit:
        strRes += "\nZobs pertenece al rango [-Zcrit, Zcrit]"
        strRes += "\n\nConclusión:\nNo hay evidencia para rechazar la hipótesis de independencia"
    else:
        strRes += "\nZobs NO pertenece al rango [-Zcrit, Zcrit]"
        strRes += "\n\nConclusión:\nSe rechaza la hipótesis de independencia"
    return res, strRes
    '''
    print(res)
    print(total)
    print(counters)
    print(Zobs)
    '''
#numbers = [0.1, 0.0, 0.1, 0.2, 0.1, 0.0, 0.1, 0.2, 0.3, 0.2, 0.3]

numbers = [
  0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27,
  0.19, 0.72, 0.75, 0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28,
  0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53,
  0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29
  ]


#execute(numbers)

#Como se conoce el valor de Zcrit 