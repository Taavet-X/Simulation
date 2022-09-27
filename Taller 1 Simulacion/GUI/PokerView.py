import tkinter as tk
import Poker

class PokerView:

    def __init__(self, master, numbers):
        self.numbers = numbers
        self.master = master
        self.createOptions()
        self.createTable()

    def createOptions(self):
        frmOptions = tk.Frame(master = self.master, relief=tk.GROOVE, borderwidth=1)
        frmOptions.grid(row = 0, column=0, sticky="news")
        frmOptions.grid_columnconfigure(4, weight = 1)

        lblAlpha = tk.Label(master = frmOptions, text = "Nivel de Confianza:")
        lblAlpha.grid(row = 0, column = 0, sticky = "news", padx = 5, pady = 5)

        self.entAlpha = tk.Entry(master = frmOptions)
        self.entAlpha.grid(row = 0, column = 1, sticky = "news", padx = 5, pady = 5)
        self.entAlpha.insert(0, "0.05")

        lblDecimals = tk.Label(master = frmOptions, text = "Decimales:")
        lblDecimals.grid(row = 0, column = 2, sticky = "news", padx = 5, pady = 5)

        self.entDecimals = tk.Entry(master = frmOptions)
        self.entDecimals.grid(row = 0, column = 3, sticky = "news", padx = 5, pady = 5)
        self.entDecimals.insert(0, "5")

        btnExecute = tk.Button(master = frmOptions, text = "Ejecutar Prueba")
        btnExecute.grid(row = 0, column = 4, sticky="news", padx = 5, pady = 5)
        btnExecute.bind('<Button-1>', self.execute)

    def createTable(self):
        frmTable = tk.Frame(master = self.master)
        frmTable.grid( row = 1, column = 0, sticky="news", padx = 5, pady = 5)

        #Se configuran las 4 columnas de la tabla para que tengan igual tamaño
        for i in range(5):
            frmTable.grid_columnconfigure(i, weight = 1)
        
        #Se crean los headers
        headers = ["Categoría", "FO", "PO", "E", "x2_i"]
        for i in range(len(headers)):
            lblHeader = tk.Label(master = frmTable,  text = headers[i], width=10, relief=tk.RAISED, borderwidth=1)
            lblHeader.grid(row = 0, column = i, sticky="news")

        #Se crean las celdas
        self.lblCats = []
        self.lblFOs = []
        self.lblPOs = []
        self.lblEs = []
        self.lblX2s = []

        for i in range(7):
            row = i+1

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 0, sticky="news")
            self.lblCats.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 1, sticky="news")
            self.lblFOs.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 2, sticky="news")
            self.lblPOs.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 3, sticky="news")
            self.lblEs.append(lblCell)

            lblCell = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)            
            lblCell.grid(row = row, column = 4, sticky="news")
            self.lblX2s.append(lblCell)

        lblTitleTotal = tk.Label(master = frmTable, text = "X2calc", relief=tk.RAISED, borderwidth=1)
        lblTitleTotal.grid(row = 11, column = 3, sticky="news")

        self.lblTotal = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)
        self.lblTotal.grid(row = 11, column = 4, sticky="news")

        self.txtResult = tk.Text(master = self.master)
        self.txtResult.grid(row = 2, column=0, sticky = "news", padx=5, pady=5)

    def setCats(self, list):
        for i in range(len(list)):
            self.lblCats[i].config(text = str(list[i]))

    def setFOs(self, list):
        for i in range(len(list)):
            self.lblFOs[i].config(text = str(list[i]))

    def setPOs(self, list):
        for i in range(len(list)):
            self.lblPOs[i].config(text = str(list[i]))
    
    def setEs(self, list):
        for i in range(len(list)):
            self.lblEs[i].config(text = str(list[i]))

    def setX2s(self, list):
        for i in range(len(list)):
            self.lblX2s[i].config(text = str(list[i]))

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
        elif len(self.entDecimals.get()) == 0:
            print("Debe indicar un nivel de confianza")         
        else:
            try:
                nc = float(self.entAlpha.get())
            except:
                print("El nivel de confianza debe ser un double")
                return
            try:
                decimals = int(self.entDecimals.get())
                if decimals != 5 and decimals != 3:
                    print("Los decimales deben ser 5 o 3")    
                    return
            except:
                print("Los decimales deben ser un numero entero")
                return
            cats, fos, pos, es, x2s, x2calc, strRes = Poker.execute(numbers, decimals, nc)
            self.setCats(cats)
            self.setFOs(fos)
            self.setPOs(pos)
            self.setEs(es)
            self.setX2s(x2s)
            self.setTotal(x2calc)
            self.setRes(strRes)