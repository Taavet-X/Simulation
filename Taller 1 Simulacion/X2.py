import math
import Values

def execute(numbers, nc):
    '''
    #Lectura de los datos desde txt
    file = open(url, "r")
    lines = file.readlines()
    numbers = []
    #conversion de los datos a double
    for i in lines:
        try:
            numbers.append(float(i))
        except:
            print("Imposible to convert line #", i, "for", lines[i])
    '''
    #x^2
    counters = [
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
    for number in numbers:
        counters[math.ceil(number*10)-1] += 1


    

    fe = len(numbers) / len(counters)

    x2sPartials = []
    x2 = 0
    for counter in counters:    
        x2Partial = (fe - counter)**2 / fe
        x2 += x2Partial
        x2sPartials.append(x2Partial)

    #print(counters)
    #print(x2sPartials)
    #print(x2)

    gl = len(counters) - 1
    xcrit = Values.get(gl, nc)
    strRes = "gl: " + str(gl) + "\nNivel de confianza: " + str(nc) + "\nX2calc: " + str(x2) + "\nX2crit: " + str(xcrit)
    if x2 <= xcrit:
        strRes += "\nX2calc <= X2crit -> Los datos tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador es bueno en cuanto a uniformidad"
    else:
        strRes += "\nX2calc > X2crit -> Los datos NO tienen distribución U(0, 1)"
        strRes += "\n\nConclusión:\nEl generador NO es bueno en cuanto a uniformidad"
    return counters, fe, x2sPartials, x2, strRes
    '''
    for i in range(10):
        if number <=
    if number <= 0.1:
        counters[0] += 1
    elif number <= 0.2:
        counters[1] += 1
    elif number <= 0.2:
        counters[1] += 1
    elif number <= 0.2:
        counters[1] += 1
    elif number <= 0.2:
        counters[1] += 1
    elif number <= 0.2:
        counters[1] += 1
    elif number <= 0.2:
        counters[1] += 1
    elif number <= 0.2:
        counters[1] += 1
    '''