import math

def execute(x0, a, m, limit):
    generatedNumbers = {}
    q = math.floor(m / a)
    r = m % a
    #m = a * q + r
    x = x0
    for i in range(limit):
        Rn = x / m
        try:
            generatedNumbers[Rn]
            print("Periodo: ", i)
            break
        except:
            generatedNumbers[Rn] = 1    
        x = a * (x % q) - (r * math.floor(x / q))        
        if x < 0:
            x += m
    return list(generatedNumbers.keys())

'''
def save():
    file = open("GEM.txt", "w")
    for key in generatedNumbers.keys():
        file.write(str(key) + "\n")
    file.close()
'''

#Seleccionar un m muy grande, preferiblemente que sea potencia de dos por eficiencia 
#Seleccionar un c, tal que c y m sean primos relativos; c preferiblemente impar y a = 1 + 4k (k es cualquier entero)
#execute(x0 = 72, a = 10, m = 73)
#execute(x0 = 1, a = 5, m = 2**15)
#save()