import GeneradorLinealCongruente
import GeneradorEstandarMinimo
import RandomsPython
import X2
import KolmogorovSmirnov
import Series

import tkinter as tk
from tkinter import ttk

numbers = []


window = tk.Tk()
window.title("Taller 1")


frmGenerator = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)

lblX0 = tk.Label(master = frmGenerator, text = "X0")
lblX0.grid(row = 0, column = 0, padx=5, pady=5)
entX0 = tk.Entry(frmGenerator)
entX0.grid(row = 0, column = 1, sticky="news", padx=5, pady=5)

lbla = tk.Label(master = frmGenerator, text = "a")
lbla.grid(row = 1, column = 0, padx=5, pady=5)
enta = tk.Entry(frmGenerator)
enta.grid(row = 1, column = 1, sticky="news", padx=5, pady=5)

lblc = tk.Label(master = frmGenerator, text = "c")
lblc.grid(row = 2, column = 0, padx=5, pady=5)
entc = tk.Entry(frmGenerator)
entc.grid(row = 2, column = 1, sticky="news", padx=5, pady=5)

lblm = tk.Label(master = frmGenerator, text = "m")
lblm.grid(row = 3, column = 0, padx=5, pady=5)
entm = tk.Entry(frmGenerator)
entm.grid(row = 3, column = 1, sticky="news", padx=5, pady=5)

lblLimit = tk.Label(master = frmGenerator, text = "Limite")
lblLimit.grid(row = 4, column = 0, padx=5, pady=5)
entLimit = tk.Entry(frmGenerator)
entLimit.grid(row = 4, column = 1, sticky="news", padx=5, pady=5)

label1 = tk.Label(master=frmGenerator, text="Generador:")
label1.grid(row = 5, column = 0, padx=5, pady=5)

strvGenerator = tk.StringVar()
cbGenerator = ttk.Combobox(frmGenerator, textvariable=strvGenerator)
cbGenerator['values'] = ["Lineal Congruente", "Estandar Minimo", "Python"]
cbGenerator['state'] = 'readonly'
cbGenerator.grid(row = 5, column = 1, padx=5, pady=5)
cbGenerator.current(0)

oldx0 = 0
olda = 0
oldc = 0
oldm = 0

def on_field_change(index, value, op):
    global oldx0, olda, oldc, oldm
    gen = cbGenerator.get()
    if gen == "Lineal Congruente":
        entX0.config(state= "normal")
        enta.config(state= "normal")
        entc.config(state= "normal")
        entm.config(state= "normal")
        if(entX0.get() == ""):
            entX0.insert(0, oldx0)
        if(enta.get() == ""):
            enta.insert(0, olda)
        if(entc.get() == ""):
            entc.insert(0, oldc)
        if(entm.get() == ""):
            entm.insert(0, oldm)
    elif gen == "Estandar Minimo":
        if(entc.get()!= ""):
            oldc = entc.get()
            entc.delete(0, 'end')
        entX0.config(state= "normal")
        enta.config(state= "normal")
        entc.config(state= "disabled")
        entm.config(state= "normal")
        if(entX0.get() == ""):
            entX0.insert(0, oldx0)
        if(enta.get() == ""):
            enta.insert(0, olda)
        if(entm.get() == ""):
            entm.insert(0, oldm)
    else:
        if(entX0.get()!= ""):
            oldx0 = entX0.get()
            entX0.delete(0, 'end')
        if(enta.get()!= ""):
            olda = enta.get()
            enta.delete(0, 'end')
        if(entc.get()!= ""):
            oldc = entc.get()
            entc.delete(0, 'end')
        if(entm.get()!= ""):
            oldm = entm.get()
            entm.delete(0, 'end')
        entX0.config(state= "disabled")
        enta.config(state= "disabled")
        entc.config(state= "disabled")
        entm.config(state= "disabled") 
strvGenerator.trace('w',on_field_change)

btnGenerate = tk.Button(frmGenerator, text="Ejecutar",command='')
btnGenerate.grid(row=6, column=0, columnspan=2, sticky="news", padx=5, pady=5)



frmGeneratedNumbers = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)
txtGeneratedNumbers = tk.Text(frmGeneratedNumbers, width=28)
txtGeneratedNumbers.grid(column=0, row=0, sticky="news")


frmGenerator.grid(row = 0, column = 0, sticky = "news", padx=5, pady=5)

frmGeneratedNumbers.grid(row = 1, column = 0, sticky="news" ,padx=5, pady=5)
frmGeneratedNumbers.grid_rowconfigure(0, weight=1)
frmGeneratedNumbers.grid_columnconfigure(0, weight=1)

#TABS
tabControl = ttk.Notebook(window, width=700)
tab1 = tk.Frame(tabControl)
tab1.grid_columnconfigure(0, weight = 1)
tab1.grid_rowconfigure(2, weight = 1)

tab2 = tk.Frame(tabControl)
tab2.grid_columnconfigure(0, weight = 1)
tab2.grid_rowconfigure(2, weight = 1)

tab3 = tk.Frame(tabControl)
tab4 = tk.Frame(tabControl)
tab5 = tk.Frame(tabControl)
  
tabControl.add(tab1, text ='X2')
tabControl.add(tab2, text ='Kolmogorov-Smirnov')
tabControl.add(tab3, text ='Corridas')
tabControl.add(tab4, text ='Serie')
tabControl.add(tab5, text ='Poker')
tabControl.grid(row = 0, column=2, rowspan= 2, sticky="news", padx=5, pady=5)
#(expand = 1, fill ="both")

entX0.insert(0, "5")
enta.insert(0,"106")
entc.insert(0,"1283")
entm.insert(0,"6075")
entLimit.insert(0, "1000")
####################
#Tablas

#TABLA X2 ###############################
import GUI.X2View
GUI.X2View.X2Table(tab1, numbers)
#FIN TABLA X2 ###############################
#TABLA KOLMOGOROV ###############################
import GUI.KolmogorovSmirnovView
GUI.KolmogorovSmirnovView.KolmogorovSmirnovTable(tab2, numbers)
'''
frmKolmogorovTableOptions = tk.Frame(master = tab2, relief=tk.GROOVE, borderwidth=1)
btnRunKolmogorov = tk.Button(master = frmKolmogorovTableOptions, text = "Ejecutar Prueba")
btnRunKolmogorov.grid(row = 0, column = 0)


frmKolmogorovTableOptions.grid(row = 0, column=0)

frmKolmogorov = tk.Frame(master = tab2)
frmKolmogorov.grid( row = 1, column = 0)

label1 = tk.Label(master = frmKolmogorov, width= 10, text = "Rango", relief=tk.RAISED, borderwidth=1)
label1.grid(row = 0, column = 0)

label2 = tk.Label(master = frmKolmogorov, width= 10, text = "FO", relief=tk.RAISED, borderwidth=1)
label2.grid(row = 0, column = 1)

label3 = tk.Label(master = frmKolmogorov, width= 10, text = "FOA", relief=tk.RAISED, borderwidth=1)
label3.grid(row = 0, column = 2)

label4 = tk.Label(master = frmKolmogorov, width= 10, text = "POA", relief=tk.RAISED, borderwidth=1)
label4.grid(row = 0, column = 3)

label5 = tk.Label(master = frmKolmogorov, width= 10, text = "PEA", relief=tk.RAISED, borderwidth=1)
label5.grid(row = 0, column = 4)

label6 = tk.Label(master = frmKolmogorov, width= 10, text = "|PEA - POA|", relief=tk.RAISED, borderwidth=1)
label6.grid(row = 0, column = 5)


lblFOsKolmogorov = []
lblFOAsKolmogorov = []
lblPOAsKolmogorov = []
lblPEAsKolmogorov = []
lblDifsKolmogorov = []

for i in range(10):
    row = i+1
    ri = str(i/10)
    rs = str((i+1)/10)
    lblRange = tk.Label(master = frmKolmogorov, width= 10, text = ri + " - " + rs, relief=tk.GROOVE, borderwidth=1)
    lblRange.grid(row = row, column = 0)

    lblFO = tk.Label(master = frmKolmogorov, width= 10, text = "", relief=tk.GROOVE, borderwidth=1)
    lblFOsKolmogorov.append(lblFO)
    lblFO.grid(row = row, column = 1)

    lblFOA = tk.Label(master = frmKolmogorov, width= 10, text = "", relief=tk.GROOVE, borderwidth=1)
    lblFOAsKolmogorov.append(lblFOA)
    lblFOA.grid(row = row, column = 2)

    lblPOA = tk.Label(master = frmKolmogorov, width= 10, text = "", relief=tk.GROOVE, borderwidth=1)
    lblPOAsKolmogorov.append(lblPOA)
    lblPOA.grid(row = row, column = 3)

    lblPEA = tk.Label(master = frmKolmogorov, width= 10, text = "", relief=tk.GROOVE, borderwidth=1)
    lblPEAsKolmogorov.append(lblPEA)
    lblPEA.grid(row = row, column = 4)

    lblDif = tk.Label(master = frmKolmogorov, width= 10, text = "", relief=tk.GROOVE, borderwidth=1)
    lblDifsKolmogorov.append(lblDif)
    lblDif.grid(row = row, column = 5)

label1 = tk.Label(master = frmKolmogorov, width= 10, text = "DM calc", relief=tk.RAISED, borderwidth=1)
label1.grid(row = 11, column = 4)

lblDMTotal = tk.Label(master = frmKolmogorov, width= 10, text = "", relief=tk.GROOVE, borderwidth=1)
lblDMTotal.grid(row = 11, column = 5)


def setFOsKolmogorov(fos):
    for i in range(len(fos)):
        lblFOsKolmogorov[i].config(text = str(fos[i]))

def setFOAsKolmogorov(foas):
    for i in range(len(foas)):
        lblFOAsKolmogorov[i].config(text = str(foas[i]))

def setPOAsKolmogorov(poas):
    for i in range(len(poas)):
        lblPOAsKolmogorov[i].config(text = str(poas[i]))

def setPEAsKolmogorov(peas):
    for i in range(len(peas)):
        lblPEAsKolmogorov[i].config(text = str(peas[i]))
    
def setDifsKolmogorov(difs):
    for i in range(len(difs)):
        lblDifsKolmogorov[i].config(text = str(difs[i]))

def setDM(dm):
    lblDMTotal.config(text = dm)

def executeKolmogorov(event):
    if len(numbers) == 0:
        print("No hay numeros generados")
    else:
        fos, foas, poas, peas, difs, dm = KolmogorovSmirnov.execute(numbers)
        setFOsKolmogorov(fos)
        setFOAsKolmogorov(foas)
        setPOAsKolmogorov(poas)
        setPEAsKolmogorov(peas)
        setDifsKolmogorov(difs)
        setDM(dm)        
        
btnRunKolmogorov.bind('<Button-1>', executeKolmogorov)
'''
#FIN TABLA KOLMOGOROV ###############################
#TABLA SERIES ###############################
frmSeriesTable1Options = tk.Frame(master = tab4, relief=tk.GROOVE, borderwidth=1)
btnRunSeries = tk.Button(master = frmSeriesTable1Options, text = "Ejecutar Prueba")
btnRunSeries.grid(row = 0, column = 0)
frmSeriesTable1Options.grid(row = 0, column=0)

frmSeries1 = tk.Frame(master = tab4)
frmSeries1.grid( row = 1, column = 0)

for i in range(5):
    li = str(i/10*2)
    ls = str((i+1)/10*2)
    label = tk.Label(master = frmSeries1, width= 10, text = li + " - " + ls, relief=tk.RAISED, borderwidth=1)
    label.grid(row = 0, column = i+1)
    label = tk.Label(master = frmSeries1, width= 10, text = li + " - " + ls, relief=tk.RAISED, borderwidth=1)
    label.grid(row = i+1, column = 0)

lblsMatrix = []

for i in range(5):
    lblsCells = []
    for j in range(5):
        label = tk.Label(master = frmSeries1, width= 10, relief=tk.GROOVE, borderwidth=1)
        label.grid(row = i+1, column = j+1)
        lblsCells.append(label)
    lblsMatrix.append(lblsCells)

frmSeries2 = tk.Frame(master = tab4)
frmSeries2.grid( row = 2, column = 0)

for i in range(5):
    li = str(i/10*2)
    ls = str((i+1)/10*2)
    label = tk.Label(master = frmSeries2, width= 10, text = li + " - " + ls, relief=tk.RAISED, borderwidth=1)
    label.grid(row = 0, column = i+1)
    label = tk.Label(master = frmSeries2, width= 10, text = li + " - " + ls, relief=tk.RAISED, borderwidth=1)
    label.grid(row = i+1, column = 0)

lblsMatrix2 = []

for i in range(5):
    lblsCells = []
    for j in range(5):
        label = tk.Label(master = frmSeries2, width= 10, relief=tk.GROOVE, borderwidth=1)
        label.grid(row = i+1, column = j+1)
        lblsCells.append(label)
    lblsMatrix2.append(lblsCells)

def setMatrixSeries(matrix, matrix2):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            lblsMatrix[i][j].config(text = matrix[i][j])
            lblsMatrix2[i][j].config(text = matrix2[i][j])

def executeSeries(event):
    if len(numbers) == 0:
        print("No hay numeros generados")
    else:
        matrix, matrix2 = Series.execute(numbers)
        setMatrixSeries(matrix, matrix2)
                
btnRunSeries.bind('<Button-1>', executeSeries)

'''
def executeX2(event):
    if len(numbers) == 0:
        print("No hay numeros generados")
    else:
        fos, fe, x2s, x2 = X2.execute(numbers)
        setFOs(fos)
        setFEs(fe)
        setX2s(x2s)
        setX2(x2)
        
        
btnRunX2.bind('<Button-1>', executeX2)
'''

'''
fos = [91, 102, 113, 110, 87, 95, 98, 104, 117, 83]
setFOs(fos)

fe = 100
setFEs(fe)

x2s = [0.81, 0.04, 1.69, 1.0, 1.69, 0.25, 0.04, 0.16, 2.89, 2.89]
setX2s(x2s)

x2 = 11.46
setX2(x2)
'''
#FIN TABLA X2 ###############################

####################

def generateNumbers(event):
    global numbers
    gen = cbGenerator.get()

    if gen == "Lineal Congruente":
        try:
            x0 = int(entX0.get())
            a = int(enta.get())
            c = int(entc.get())
            m = int(entm.get())
            limit = int(entLimit.get())
            numbers.clear()
            numbers.extend(GeneradorLinealCongruente.execute(x0, a, c, m, limit))
            txtGeneratedNumbers.delete('1.0', tk.END)
            for number in numbers:
                txtGeneratedNumbers.insert(tk.END, str(number)+"\n") 
        except NameError:            
            print(NameError)  

    elif gen == "Estandar Minimo":
        try:
            x0 = int(entX0.get())
            a = int(enta.get())
            m = int(entm.get())
            limit = int(entLimit.get())
            numbers.clear()
            numbers.extend(GeneradorEstandarMinimo.execute(x0, a, m, limit))
            txtGeneratedNumbers.delete('1.0', tk.END)
            for number in numbers:
                txtGeneratedNumbers.insert(tk.END, str(number)+"\n")

        except NameError:            
            print(NameError)  

    elif gen == "Python":
        try:
            limit = int(entLimit.get())
            numbers.clear()
            numbers.extend(RandomsPython.execute(limit))
            txtGeneratedNumbers.delete('1.0', tk.END)
            for number in numbers:
                txtGeneratedNumbers.insert(tk.END, str(number)+"\n")
        except:
            print("Dato no valido")

btnGenerate.bind('<Button-1>', generateNumbers)

window.mainloop()