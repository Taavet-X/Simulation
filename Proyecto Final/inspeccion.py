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
timeBetweenInspections = 120


def insert(event):
    if len(LEF) == 0:
        LEF.append(event)
    else:
        for i in range(len(LEF)):
            if  event.time <= LEF[i].time:
                LEF.insert(i, event)
                return
        LEF.append(event)

table = []
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
    global products
    #generar tiempo de servicio
    time = 0
    fifteenPercent =  math.ceil(products * 15 / 100)    
    for i in range(fifteenPercent):
        time += generador.N(30, 5) / 60.0
    fivePercent = math.ceil(fifteenPercent * 4.1 / 100)
    for i in range(fivePercent):
        time += generador.U(5, 10)
        time += generador.N(30, 5) / 60.0      
    ts = round(time)
    products = 0
    #calcular tiempo de la proxima salida
    tiempoProximaSalida = clock + ts
    #y colocar el evento de salida en la LEF
    e = evento(tiempoProximaSalida, "S")
    insert(e)

simulacion = []
LEF.append(evento(timeBetweenInspections,"L"))
while clock < 1440:  
    e = LEF.pop(0)    
    oldClock = clock
    clock = e.time
    products += (clock - oldClock)*20
    if e.eventType == "L":
        llegada()
    else:
        salida()
    simulacion.append([e, LEF[:], server, queue])
    print(clock, e.eventType, list(map(lambda e:e.toString(),LEF)), server, queue)