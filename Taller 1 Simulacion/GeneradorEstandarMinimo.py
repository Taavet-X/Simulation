import math

def execute(x0, a, m, limit): #Ya no se utiliza la C
    generatedNumbers = {} #Un diccionario, se usa por eficiencia
    q = math.floor(m / a) #Segun el algorimo GEM
    r = m % a #Segun el algorimo GEM
    x = x0 #Se define inicialmente a X como la semilla
    periodo = None
    for i in range(limit): #Se recorre operando desde la semilla hasta llegar al limite
        Rn = x / m #Se calcula el numero aleatorio
        try: 
            generatedNumbers[Rn]#Se intenta acceder al diccionario
            #con un key que es igual al Rn generado, si no existe dicho key
            #en el diccionario, esto arroja error, por lo que se va al except
            #pero en caso de que exista, no hay error y siguen las siguientes lineas
            print("Periodo: ", i) #imprime el periodo
            periodo = i
            break #Termina la ejecucion, ya que si encontro un key en el diccionario, es porque
            #Se empiezan a repetir los numeros
        except:
            #en el caso del error 
            generatedNumbers[Rn] = 1 #Crear un registro con Rn como key

        x = a * (x % q) - (r * math.floor(x / q)) #Se calcula el nuevo x, de acuerdo al GEM  
        if x < 0: #Se valida el caso de que el nuevo x sea menor a m de acuerdo con el GEM
            x += m
    return list(generatedNumbers.keys()), periodo