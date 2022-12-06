#Carolina Caicedo Pasiminio - 2067815
#Cristhian Camilo Lozano Gómez - 2067818
#Germán David Estrada Holguin - 2013122
#Manuel Alejandro Perdomo Londoño - 2067575
#Nicolás Felipe Victoria Rodríguez - 1767315

import math
import generador

class evento:

    def __init__(self, time, eventType):
        self.eventType = eventType
        self.time = time

    def toString(self):
        return str(self.time) + self.eventType

clock = 0
LEF = []
queue = 0
server = 0
servers = 1
products = 0
a = 5
b = 10
mu = 30
rho = 5
timeBetweenInspections = 120
pSeleccion = 15
pAjuste = 5
productosInspeccionados = 0

def reset():
    global clock, LEF, queue, server, products
    clock = 0
    LEF = []
    queue = 0
    server = 0
    products = 0


def insert(event):
    if len(LEF) == 0:
        LEF.append(event)
    else:
        for i in range(len(LEF)):
            if  event.time <= LEF[i].time:
                LEF.insert(i, event)
                return
        LEF.append(event)

def llegada():
    global queue, server
    #generar tiempo entre llegadas
    tiempoEntreLlegadas = timeBetweenInspections
    #calcular el tiempo de la proxima llegada
    tiempoProximaLlegada = clock + tiempoEntreLlegadas
    e = evento(tiempoProximaLlegada, "L")
    #colocarla en la lista de eventos futuros
    insert(e)
    #si el inspector esta desocupado    
    if server < servers:
        generarSalida()
        #poner el inspector en ocupado
        server += 1
    #sino
    else:
        #aumentar el numero de inspecciones en la cola en 1
        queue += 1

def salida():
    global queue, server
    #poner inspector en desocupado    
    server -= 1
    #si la cola no esta vacia
    if queue != 0:
        #reducir el numero de inspecciones en la cola en 1
        queue -= 1
        generarSalida()
        #poner el inspector en ocupado
        server += 1

def generarSalida():
    global products, productosInspeccionados
    #generar tiempo de servicio
    time = 0
    fifteenPercent =  math.ceil(products * pSeleccion / 100) #15%
    productosInspeccionados += fifteenPercent
    for i in range(fifteenPercent):
        time += generador.N(mu, rho) / 60.0
    fivePercent = math.ceil(fifteenPercent * pAjuste / 100) #5%
    for i in range(fivePercent):
        time += generador.U(a, b)
        time += generador.N(mu, rho) / 60.0      
    ts = round(time)
    products = 0
    #calcular tiempo de la proxima salida
    tiempoProximaSalida = clock + ts
    #y colocar el evento de salida en la LEF
    e = evento(tiempoProximaSalida, "S")
    insert(e)


def ejecutar(nInspectors, pSelection, pAdjust, aValue, bValue, muValue, rhoValue, tiempoEntreInspecciones, tiempoSimulacion):
    global clock, products, productosInspeccionados
    global servers, pSeleccion, pAjuste, a, b, mu, rho,  timeBetweenInspections
    reset()
    servers = nInspectors
    pSeleccion = pSelection
    pAjuste = pAdjust
    a = aValue
    b = bValue
    mu = muValue
    rho = rhoValue
    timeBetweenInspections =tiempoEntreInspecciones
    simulacion = []
    strSimulacion = ""
    LEF.append(evento(timeBetweenInspections,"L"))
    while clock < tiempoSimulacion:  
        e = LEF.pop(0)    
        oldClock = clock
        clock = e.time
        products += (clock - oldClock)*20
        if e.eventType == "L":
            llegada()
        else:
            salida()
        simulacion.append([e, LEF[:], server, queue])        
        strSimulacion += str(clock) + " " + e.eventType + " " +str(list(map(lambda e:e.toString(),LEF))) + " " + str(server) + " " + str(queue) + "\n"
    strSimulacion += "Cantidad de productos Inspeccionados: " + str(productosInspeccionados) + "\n"
    return strSimulacion, simulacion

#ejecutar(1,15,5,5,10,30,5,120, 1440)