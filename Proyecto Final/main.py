import threading
import time

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
