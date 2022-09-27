import math
import Values

def execute(numbers, alpha):
    #para el diccionario la estructura se contempla asi:
    #{"longitud de corrida": veces que aparece}
    counters = {}

    res = "*" #La cadena de texo o patron de corridas ++-++-+...
    last = "*" #El ultimo suceso o comportamiento, es * o + o -
    counter = 1 #inicia en 1 porque siempre se cuenta algo y se incrementa (longitud de corrida actual)
    lastValue = numbers[0] #el ultimo numero recorrido, se inicializa como el primero del listado
    total = 0 #Cantidad de corridas
    for value in numbers[1:]: #Se recorre el listado de numeros a partir de la primer posicion
        behavior = "" #Se define una variable que corresponde al comportamiento
        if value > lastValue: #en caso de que el valor actual, sea mayor al ultimo
            behavior = "+" #se define al comportamiento como de incremento
        elif value < lastValue: #en caso contrario
            behavior = "-" #se define como decremento

        if last != behavior: #Si el ultimo comportamiento es diferente al actual,
            #quiere decir que la corrida termina alli
            try: #entonces se intenta sumar 1 al registro
                #del diccionario que tiene la longitud de la corrida como key
                #esto arroja error, si no existe, de lo contrario lo incrementa en 1
                counters[counter] += 1
            except:
                #en caso de que el error sea arrojado, entonces crea el registro
                # con la longituda de corrida como key, y lo inicializa en 1
                counters[counter] = 1
            counter = 1 #Reiniciar el contador en 1 (Longitud de corrida)
            total += 1 #Acomular una corrida en el total
        else: #En caso de que el ultimo comportamiento sea igual al actual
            counter +=1 #entonces la Longitud de corrida se incrementa en 1.
        
        res += behavior #Adicionar el comportamiento a la cadena de texto
        last = behavior #define el ultimo comportamiento como el comportamiento actual
        lastValue = value #define el ultimo valor como el valor actual (valor = numero)

    n = len(numbers) #cantidad de numeros
    mu = (2*n - 1)/3 #media
    s = (16*n-29)/90 #varianza
    Zobs = (total - mu)/math.sqrt(s) #Zobs segun algoritmo de corridas
    halfAlpha = alpha/2 #Segun algoritmo de corridas
    Zcrit = Values.getZ(halfAlpha) #Se obtiene de la tabla de distribucion normal.

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