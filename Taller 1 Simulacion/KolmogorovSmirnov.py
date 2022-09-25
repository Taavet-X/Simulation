import math
import numpy as np

def execute(numbers):
    '''
    file = open(url, "r")
    lines = file.readlines()
    numbers = []

    for i in lines:
        try:
            numbers.append(float(i))
        except:
            print("Imposible to convert line #", i, "for", lines[i])
    '''
    fos = [
        0, #[0, 0.1]
        0, #(0.1, 0.2]
        0, #(0.2, 0.3]
        0, #(0.3, 0.4]
        0, #(0.4, 0.5]  
        0, #(0.5, 0.6]
        0, #(0.6, 0.7]
        0, #(0.7, 0.8]
        0, #(0.8, 0.9]
        0, #(0.9, 1]
    ]
    for number in numbers:
        fos[math.ceil(number*10)-1] += 1


    print(fos)

    foas = []
    poas = []
    peas = []
    difs = []
    foa = 0
    DMcalc = 0 #The max from difs
    n = len(numbers)
    for i in range(len(fos)):
        foa += fos[i]
        foas.append(foa)
        poas.append(foa/n)
        peas.append((i+1)/10)        
        difference = round(abs(peas[i]-poas[i]),3)
        difs.append(difference)
        if difference >= DMcalc:
            DMcalc = difference

    print("FO",foas)
    print("FOA",poas)
    print("POA",peas)
    print("|PEA-POA|", difs)
    print("DMcalc",DMcalc)

    a  = 0.05
    c = math.sqrt(-np.log(a/2)*1/2)
    DMcrit = round(c/math.sqrt(n),3)

    print("DMcrit", DMcrit)
    print(DMcalc <= DMcrit)

    return fos, foas, poas, peas, difs, DMcalc