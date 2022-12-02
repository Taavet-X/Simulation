class evento:

    def __init__(self, time, eventType):
        self.eventType = eventType
        self.time = time

    def toString(self):
        return str(self.time) + self.eventType

#####################################################
tls = [7, 8, 2, 11, 1, 7, 1, 7, 2, 7, 3, 41, 22]
c1 = -1
def getTL():
    global c1 
    c1 += 1
    return tls[c1]

tss = [6, 11, 18, 9, 15, 45]
c2 = -1
def getTS():
    global c2
    c2 += 1
    return tss[c2]
#####################################################

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

table = []
def llegada():
    global queue, server, products
    #generar tiempo entre llegadas
    tiempoEntreLlegadas = 120
    #calcular el tiempo de la proxima llegada
    tiempoProximaLlegada = clock + tiempoEntreLlegadas
    products += 4
    e = evento(tiempoProximaLlegada, "L")
    #colocarla en la lista de eventos futuros
    insert(e)
    #si el inspector esta desocupado    
    if server == 0:
        #generar tiempo de servicio
        ts = products * 1
        products = 0
        #calcular tiempo de la proxima salida****
        tiempoProximaSalida = clock + ts
        #y colocar el evento de salida en la LEF
        e = evento(tiempoProximaSalida, "S")
        insert(e)
        #poner el inspector en ocupado
        server = 1
    #sino
    else:
        #aumentar el numero de inspecciones en la cola en 1
        queue += 1

def salida():
    global queue, server, products
    #poner inspector en desocupado
    server = 0
    #si la cola no esta vacia
    if queue != 0:
        #reducir el numero de inspecciones en la cola en 1
        queue -= 1
        #generar tiempo de servicio
        ts = products * 1
        products = 0
        #calcular tiempo de la proxima salida****
        tiempoProximaSalida = clock + ts
        #y colocar el evento de salida en la LEF
        e = evento(tiempoProximaSalida, "S")
        insert(e)
        #poner el inspector en ocupado
        server = 1

LEF.append(evento(120,"L"))
while clock < 500:  
    e = LEF.pop(0)
    clock = e.time
    if e.eventType == "L":
        llegada()
    else:
        salida()
    
    print(clock, e.eventType, list(map(lambda e:e.toString(),LEF)), server, queue)