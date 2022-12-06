#Carolina Caicedo Pasiminio - 2067815
#Cristhian Camilo Lozano Gómez - 2067818
#Germán David Estrada Holguin - 2013122
#Manuel Alejandro Perdomo Londoño - 2067575
#Nicolás Felipe Victoria Rodríguez - 1767315

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
            #print("Periodo: ", i) #imprime el periodo
            periodo = i
            break #Termina la ejecucion, ya que si encontro un key en el diccionario, es porque
            #Se empiezan a repetir los numeros
        except:
            #en el caso del error            
            generatedNumbers[Rn] = 1 #Crear un registro con Rn como key
    return list(generatedNumbers.keys()), periodo #Retorna el listado de numeros generados

randoms = execute(0, 5, 7, 16384, 16000)[0]
print(len(randoms))

f = [
    0.0013,
    0.0228,
    0.1586,
    0.5,
    0.8413,
    0.9772,
    0.9987
]

def getValues(r):
    for i in range(len(f)):
        if r <= f[i]:
            if i == 0 :
                return 0, 0, 0
            fx1 = f[i]
            fx0 = f[i-1]            
            return (fx1-r)/(fx1-fx0), i-3, (i-4)
    return 1, i-3, i-4

def getNormalValue(r, mu, rho):
    l, x1, x0 = getValues(r)
    a = (l*x0)+((1-l)*x1)
    return a*rho+mu

i = 0
def U(a, b):
    global i
    r = randoms[i] * (b - a) + a
    i = (i + 1)%(len(randoms)-1)
    return r        

def N(mu, rho):
    return getNormalValue(U(0,1), mu, rho)