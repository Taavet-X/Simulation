import tkinter as tk
import X2

class X2Table:

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
        btnExecute.bind('<Button-1>', self.executeX2)

    def createTable(self):
        frmTable = tk.Frame(master = self.master)
        frmTable.grid( row = 1, column = 0, sticky="news", padx = 5, pady = 5)

        #Se configuran las 4 columnas de la tabla para que tengan igual tamaño
        for i in range(4):
            frmTable.grid_columnconfigure(i, weight = 1)
        
        #Se crean los headers
        headers = ["Rango", "FO", "FE", "X^2i"]
        for i in range(len(headers)):
            lblHeader = tk.Label(master = frmTable,  text = headers[i], width=10, relief=tk.RAISED, borderwidth=1)
            lblHeader.grid(row = 0, column = i, sticky="news")

        #Se crean las celdas
        self.lblFOs = []
        self.lblFEs = []
        self.lblX2s = []

        for i in range(10):
            row = i+1
            ri = str(i/10)
            rs = str((i+1)/10)
            lblRange = tk.Label(master = frmTable, text = ri + " - " + rs, relief=tk.GROOVE, borderwidth=1)
            lblRange.grid(row = row, column = 0, sticky="news")

            lblFO = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)
            self.lblFOs.append(lblFO)
            lblFO.grid(row = row, column = 1, sticky="news")

            lblFE = tk.Label(master = frmTable,  text = "", relief=tk.GROOVE, borderwidth=1)
            self.lblFEs.append(lblFE)
            lblFE.grid(row = row, column = 2, sticky="news")

            lblX2 = tk.Label(master = frmTable,  text = "", relief=tk.GROOVE, borderwidth=1)
            self.lblX2s.append(lblX2)
            lblX2.grid(row = row, column = 3, sticky="news")

        label1 = tk.Label(master = frmTable, text = "x^2 calc", relief=tk.RAISED, borderwidth=1)
        label1.grid(row = 11, column = 2, sticky="news")

        self.lblX2Total = tk.Label(master = frmTable, text = "", relief=tk.GROOVE, borderwidth=1)
        self.lblX2Total.grid(row = 11, column = 3, sticky="news")

        self.txtResult = tk.Text(master = self.master)
        self.txtResult.grid(row = 2, column=0, sticky = "news", padx=5, pady=5)

    def setFOs(self, fos):
        for i in range(len(fos)):
            self.lblFOs[i].config(text = str(fos[i]))

    def setFEs(self, fe):
        for i in range(len(self.lblFEs)):
            self.lblFEs[i].config(text = str(fe))

    def setX2s(self, x2s):
        for i in range(len(x2s)):
            self.lblX2s[i].config(text = str(x2s[i]))

    def setX2(self, x2):
        self.lblX2Total.config(text = x2)

    def setRes(self, strRes):
        self.txtResult.delete('1.0', tk.END)
        self.txtResult.insert(tk.INSERT, strRes)

    def executeX2(self, event):
        numbers = self.numbers
        if len(numbers) == 0:
            print("No hay numeros generados")
        elif len(self.entAlpha.get()) == 0:
            print("Debe indicar un nivel de confianza")          
        else:
            try:
                nc = float(self.entAlpha.get())
                fos, fe, x2s, x2, strRes = X2.execute(numbers, nc)
                self.setFOs(fos)
                self.setFEs(fe)
                self.setX2s(x2s)
                self.setX2(x2)
                self.setRes(strRes)
            except NameError:
                print(NameError)
                print("El nivel de confianza debe ser un double")
            
            
    