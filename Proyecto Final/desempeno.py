#Carolina Caicedo Pasiminio - 2067815
#Cristhian Camilo Lozano Gómez - 2067818
#Germán David Estrada Holguin - 2013122
#Manuel Alejandro Perdomo Londoño - 2067575
#Nicolás Felipe Victoria Rodríguez - 1767315

import inspeccion

def getOutput(nInspectores, pSeleccion, pAjuste, a, b, mu, rho, timeBetweenInspections, simulationTime):

    strOutput, simulacion = inspeccion.ejecutar(
        nInspectors = nInspectores,
        pSelection = pSeleccion,
        pAdjust = pAjuste,
        aValue = a,
        bValue = b,
        muValue = mu,
        rhoValue = rho,
        tiempoEntreInspecciones = timeBetweenInspections,
        tiempoSimulacion = simulationTime)

    #Manuel
    #--Numero de inspecciones realizadas y tiempo promedio de espera
    numeroInspeccionesRealizadas = 0
    llegadas = []
    salidas = []
    for reg in simulacion:
        e = reg[0] 
        if e.eventType == "S":
            numeroInspeccionesRealizadas += 1
            salidas.append(e)
        else:
            llegadas.append(e)

    tiemposEspera = []
    tiempoTotal = 0

    while len(salidas)>0:
        llegada = llegadas.pop(0)
        salida = salidas.pop(0)
        tiempo = salida.time - llegada.time
        tiemposEspera.append(tiempo)
        tiempoTotal += tiempo

    tiempoPromedio = tiempoTotal / numeroInspeccionesRealizadas

    strOutput += "Numero de inspecciones realizadas: " + str(numeroInspeccionesRealizadas) +"\n"
    strOutput += "Tiempos de Espera: " + str(tiemposEspera)+"\n"
    strOutput += "Tiempo total: " + str(tiempoTotal)+"\n"
    strOutput += "Tiempo promedio: " + str(tiempoPromedio)+"\n"

    '''eventos = simulacion.pop()
    cantidadSalidas = eventos.pop(0)
    Espera = eventos.pop(0) / cantidadSalidas
    print("Numero de inspecciones atendidas: ",cantidadSalidas)
    print("Promedio de espera: ",Espera)
    '''
    #Carolina
    #--Tamaño maximo de la cola
    max = -1
    for registro in simulacion:
        tamanoCola = registro[3]
        if tamanoCola > max:
            max = tamanoCola
    strOutput += "Tamaño maximo de la cola: " + str(max) +"\n"

    #Nicolas
    #--Comportamiento de la cola
    X = []
    Y = []
    for reg in simulacion:    
        x = reg[0].time
        y = reg[3]    
        X.append(x)
        Y.append(y)        
    #plt.plot(X, Y, color="blue")
    #plt.grid()
    #plt.show()


    #Christian
    #--Porcentaje de ocupacion del inspector
    prevTime = 0
    prevStatus = 0
    data = {}
    for reg in simulacion:
        time = reg[0].time
        estado = reg[2]
        value = time - prevTime
        try:
            data[prevStatus] += value
        except:
            data[prevStatus] = value
        prevTime = time
        prevStatus = estado

    strOutput += str(data)+"\n"
    maxTime = simulacion[-1][0].time
    for reg in data:
        data[reg] = round(data[reg]/maxTime, 2)
    strOutput += str(data)
    return X, Y, strOutput

'''
print(getOutput(
    nInspectores=1,
    pSeleccion=15,
    pAjuste=5,
    a=5,
    b=10,
    mu=30,
    rho=5,
    timeBetweenInspections=120,
    simulationTime = 1440
)[2])
#'''
'''
'''