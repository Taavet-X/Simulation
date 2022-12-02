import threading
import time
import generador

class event:

    def __init__(self, clock, type, status, queue):
        self.clock = clock
        self.type = type
        self.status = status
        self.queue = queue

clock = 0
futureEventsList = []
inspectorAvailable = True
timeUnit = 1
coldDown = 120
simulationTime = 1440 #24 hours

products = 0

for i in range(120, 1440):
    products 
    adjustingTime = generador.U(5, 10)

    futureEventsList.append[]


'''
2 type of events S and E
S: start of an inspection
E: end of an inspection
'''




'''
timeUnit = 1 #min

products = 0
inspectorStatus = "available"

def updateProducts():
    global products
    products += (timeUnit * 60) / 3

inspectionWait = 120 #min = 2 hours
inspectionColdown = 120
def inspect():
    global products
    selection = products * 0.25
    print("Selection ", selection)
    products = 0

def execute():
    global inspectionColdown    
    for i in range(1000):
        updateProducts()
        if inspectionColdown == 0:            
            inspectionColdown = inspectionWait
            inspectorThread = threading.Thread(target=inspect)
            inspectorThread.start()
        inspectionColdown -= 1

execute()
'''