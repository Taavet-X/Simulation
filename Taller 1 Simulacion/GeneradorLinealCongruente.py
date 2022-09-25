generatedNumbers = {}

def execute(x0, a, c, m, limit):
    x = x0
    for i in range(limit):        
        x = (a * x + c) % m
        Rn = x / m
        try:
            generatedNumbers[Rn]
            print("Periodo: ", i)
            break
        except:
            generatedNumbers[Rn] = 1 #Adiciona un registro con el Rn
        
        
    saveGeneratedNumbers()
        
def saveGeneratedNumbers():
    file = open("GLC.txt", "w")
    for key in generatedNumbers.keys():
        file.write(str(key) + "\n")
    file.close()


#Seleccionar un m muy grande, preferiblemente que sea potencia de dos por eficiencia 
#Seleccionar un c, tal que c y m sean primos relativos; c preferiblemente impar y a = 1 + 4k (k es cualquier entero)
#execute(x0 = 1, a = 5, c = 7, m = 1024)
#execute(x0 = 5, a = 106, c = 1283, m = 6075)
#saveGeneratedNumbers()

#Se debe tomar el random generado con la semilla?