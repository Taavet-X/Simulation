def execute(x0, a, c, m, limit): #El limite se utiliza ya que no afecta el algoritmo, mientras que m si.
    generatedNumbers = {} #Diccionario, se usa por eficiencia.
    x = x0 #se define inicialmente como la semilla
    periodo = None
    for i in range(limit): #Se recorre operando desde la semilla hasta llegar al limite
        x = (a * x + c) % m #Se calcula el nuevo valor de la x con el algoritmo del GLC
        Rn = x / m #Se calcula numero pseudoaleatorio    
        try:
            generatedNumbers[Rn] #Se intenta acceder al diccionario
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
    return list(generatedNumbers.keys()), periodo #Retorna el listado de numeros generados