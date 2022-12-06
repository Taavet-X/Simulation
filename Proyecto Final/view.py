#Carolina Caicedo Pasiminio - 2067815
#Cristhian Camilo Lozano Gómez - 2067818
#Germán David Estrada Holguin - 2013122
#Manuel Alejandro Perdomo Londoño - 2067575
#Nicolás Felipe Victoria Rodríguez - 1767315

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import desempeno

numbers = []


window = tk.Tk()
window.title("Taller 1")


frmParameters = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)

lblCantidadInspectores = tk.Label(master = frmParameters, text = "No. Inspectores")
lblCantidadInspectores.grid(row = 0, column = 0, padx=5, pady=5)
entCantidadInspectores = tk.Entry(frmParameters)
entCantidadInspectores.grid(row = 0, column = 1, sticky="news", padx=5, pady=5)

lblPSeleccion = tk.Label(master = frmParameters, text = "% Seleccion")
lblPSeleccion.grid(row = 1, column = 0, padx=5, pady=5)
entPSeleccion = tk.Entry(frmParameters)
entPSeleccion.grid(row = 1, column = 1, sticky="news", padx=5, pady=5)

lblPAjuste = tk.Label(master = frmParameters, text = "% Ajuste")
lblPAjuste.grid(row = 2, column = 0, padx=5, pady=5)
entPAjuste = tk.Entry(frmParameters)
entPAjuste.grid(row = 2, column = 1, sticky="news", padx=5, pady=5)

lbla = tk.Label(master = frmParameters, text = "a en U(a, b)")
lbla.grid(row = 3, column = 0, padx=5, pady=5)
enta = tk.Entry(frmParameters)
enta.grid(row = 3, column = 1, sticky="news", padx=5, pady=5)

lblb = tk.Label(master = frmParameters, text = "b en U(a, b)")
lblb.grid(row = 4, column = 0, padx=5, pady=5)
entb = tk.Entry(frmParameters)
entb.grid(row = 4, column = 1, sticky="news", padx=5, pady=5)

lblMu = tk.Label(master = frmParameters, text = "Mu en N(mu, rho)")
lblMu.grid(row = 5, column = 0, padx=5, pady=5)
entMu = tk.Entry(frmParameters)
entMu.grid(row = 5, column = 1, sticky="news", padx=5, pady=5)

lblRho = tk.Label(master = frmParameters, text = "rho en N(mu, rho)")
lblRho.grid(row = 6, column = 0, padx=5, pady=5)
entRho = tk.Entry(frmParameters)
entRho.grid(row = 6, column = 1, sticky="news", padx=5, pady=5)

lblTiempoEntreInspecciones = tk.Label(master = frmParameters, text = "T entre Inspecciones")
lblTiempoEntreInspecciones.grid(row = 7, column = 0, padx=5, pady=5)
entTiempoEntreInspecciones = tk.Entry(frmParameters)
entTiempoEntreInspecciones.grid(row = 7, column = 1, sticky="news", padx=5, pady=5)

lblTiempoDeSimulacion = tk.Label(master = frmParameters, text = "Tiempo de Simulacion")
lblTiempoDeSimulacion.grid(row = 8, column = 0, padx=5, pady=5)
entTiempoDeSimulacion = tk.Entry(frmParameters)
entTiempoDeSimulacion.grid(row = 8, column = 1, sticky="news", padx=5, pady=5)

btnExecute = tk.Button(frmParameters, text="Ejecutar",command='')
btnExecute.grid(row=9, column=0, columnspan=2, sticky="news", padx=5, pady=5)

frmParameters.grid(row = 0, column = 0, sticky = "news", padx=5, pady=5)

#Output
frmOutput = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)
txtOutput = tk.Text(frmOutput, width=50, height=50)
txtOutput.grid(column=0, row=0, sticky="news")
frmOutput.grid(row = 0, column = 1, sticky="news" ,padx=5, pady=5)
frmOutput.grid_rowconfigure(0, weight=1)
frmOutput.grid_columnconfigure(0, weight=1)

##########
# the figure that will contain the plot
frmGraphic = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)
fig = Figure( dpi = 100)
canvas = FigureCanvasTkAgg(fig, master = frmGraphic)  
plot1 = fig.add_subplot(111)
fig.suptitle("Comportamiento de la Cola", fontsize=20)
canvas.draw()

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()
toolbar = NavigationToolbar2Tk(canvas, frmGraphic)
toolbar.update()

# placing the toolbar on the Tkinter window
canvas.get_tk_widget().pack()
frmGraphic.grid(row = 0, column = 2, sticky="news" ,padx=5, pady=5)
frmGraphic.grid_rowconfigure(0, weight=1)
frmGraphic.grid_columnconfigure(0, weight=1)
##########

entCantidadInspectores.insert(0, "1")
entPSeleccion.insert(0, "15")
entPAjuste.insert(0, "5")
enta.insert(0, "5")
entb.insert(0, "10")
entMu.insert(0, "30")
entRho.insert(0, "5")
entTiempoEntreInspecciones.insert(0, "120")
entTiempoDeSimulacion.insert(0, "1440")
####################

def Execute(event):

    nInspectores = int(eval(entCantidadInspectores.get()))
    pSeleccion= int(eval(entPSeleccion.get()))
    pAjuste= int(eval(entPAjuste.get()))
    a= int(eval(enta.get()))
    b= int(eval(entb.get()))
    mu= int(eval(entMu.get()))
    rho= int(eval(entRho.get()))
    timeBetweenInspections= int(eval(entTiempoEntreInspecciones.get()))
    simulationTime = int(eval(entTiempoDeSimulacion.get()))

    print(nInspectores, pSeleccion, pAjuste, a, b, mu, rho, timeBetweenInspections, simulationTime)
    
    txtOutput.delete('1.0', tk.END)
    X, Y, strOutput = desempeno.getOutput(
        nInspectores, pSeleccion, pAjuste, a, b, mu, rho, timeBetweenInspections, simulationTime
    )
    txtOutput.insert(tk.END, strOutput) 
    
    #
    #for item in canvas.get_tk_widget().find_all():
    #canvas.get_tk_widget().delete("all")
    #plot1.clf()
    plot1 = fig.add_subplot(111)
    fig.suptitle("Comportamiento de la Cola", fontsize=20)
    for i in range(len(X)):
        plot1.plot(X[i],Y[i], marker = "o", color = "blue")
    X = np.array(X)
    Y = np.array(Y)
    plot1.plot(X, Y, color="blue")
    plot1.grid()
    #y = [i**2 for i in range(101)]
    
    #plot1.plot(y)
    canvas.draw()

btnExecute.bind('<Button-1>', Execute)

window.mainloop()