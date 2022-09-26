import tkinter as tk
import KolmogorovSmirnov

class KolmogorovSmirnovTable:

    def __init__(self, master, numbers):
        self.numbers = numbers
        self.master = master
        self.createOptions()
        self.createTable()

    def createOptions(self):
        frmOptions = tk.Frame(master = self.master, relief=tk.GROOVE, borderwidth=1)
        frmOptions.grid(row = 0, column=0, sticky="news")
        frmOptions.grid_columnconfigure(2, weight = 1)

        lblAlpha = tk.Label(master = frmOptions, text = "Nivel de Confianza:")
        lblAlpha.grid(row = 0, column = 0, sticky = "news", padx = 5, pady = 5)

        self.entAlpha = tk.Entry(master = frmOptions)
        self.entAlpha.grid(row = 0, column = 1, sticky = "news", padx = 5, pady = 5)
        self.entAlpha.insert(0, "0.05")

        btnExecute = tk.Button(master = frmOptions, text = "Ejecutar Prueba")
        btnExecute.grid(row = 0, column = 2, sticky="news", padx = 5, pady = 5)
        btnExecute.bind('<Button-1>', self.execute)

    def createTable(self):
        frmTable = tk.Frame(master = self.master)
        frmTable.grid( row = 1, column = 0, sticky="news", padx = 5, pady = 5)

        #Se configuran las 4 columnas de la tabla para que tengan igual tamaño
        for i in range(6):
            frmTable.grid_columnconfigure(i, weight = 1)
        
        #Se crean los headers
        headers = ["Rango", "FO", "FOA", "POA", "PEA", "|PEA-POA|"]
        for i in range(len(headers)):
            lblHeader = tk.Label(master = frmTable,  text = headers[i], width=10, relief=tk.RAISED, borderwidth=1)
            lblHeader.grid(row = 0, column = i, sticky="news")

        #Se crean las celdas
        self.lblFOs = []
        self.lblFOAs = []
        self.lblPOAs = []
        self.lblPEAs = []
        self.lblDifs = []

        for i in range(10):
            row = i+1
            ri = str(i/10)
            rs = str((i+1)/10)
            lblRange = tk.Label(master = frmTable, text = ri + " - " + rs, relief=tk.GROOVE, borderwidth=1)
            lblRange.grid(row = row, column = 0, sticky="news")

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 1, sticky="news")
            self.lblFOs.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 2, sticky="news")
            self.lblFOAs.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 3, sticky="news")
            self.lblPOAs.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 4, sticky="news")
            self.lblPEAs.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 5, sticky="news")
            self.lblDifs.append(lblCell)

        lblTitleTotal = tk.Label(master = frmTable, text = "DMcalc", relief=tk.RAISED, borderwidth=1)
        lblTitleTotal.grid(row = 11, column = 4, sticky="news")

        self.lblTotal = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)
        self.lblTotal.grid(row = 11, column = 5, sticky="news")

        self.txtResult = tk.Text(master = self.master)
        self.txtResult.grid(row = 2, column=0, sticky = "news", padx=5, pady=5)

    def setFOs(self, list):
        for i in range(len(list)):
            self.lblFOs[i].config(text = str(list[i]))

    def setFOAs(self, list):
        for i in range(len(list)):
            self.lblFOAs[i].config(text = str(list[i]))

    def setPOAs(self, list):
        for i in range(len(list)):
            self.lblPOAs[i].config(text = str(list[i]))
    
    def setPEAs(self, list):
        for i in range(len(list)):
            self.lblPEAs[i].config(text = str(list[i]))

    def setDifs(self, list):
        for i in range(len(list)):
            self.lblDifs[i].config(text = str(list[i]))

    def setTotal(self, total):
        self.lblTotal.config(text = total)

    def setRes(self, strRes):
        self.txtResult.delete('1.0', tk.END)
        self.txtResult.insert(tk.INSERT, strRes)

    def execute(self, event):
        numbers = self.numbers
        if len(numbers) == 0:
            print("No hay numeros generados")
        elif len(self.entAlpha.get()) == 0:
            print("Debe indicar un nivel de confianza")          
        else:
            try:
                nc = float(self.entAlpha.get())
            except:
                print("El nivel de confianza debe ser un double")
                return
            print("1")
            fos, foas, poas, peas, difs, DMcalc, strRes = KolmogorovSmirnov.execute(numbers, nc)
            print("122")
            self.setFOs(fos)
            self.setFOAs(foas)
            self.setPOAs(poas)
            self.setPEAs(peas)
            self.setDifs(difs)
            self.setTotal(DMcalc)
            self.setRes(strRes)

            
            
    