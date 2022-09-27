import tkinter as tk
import Corridas

class View:

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
        self.txtResult1 = tk.Text(master = self.master, height=15)
        self.txtResult1.grid( row = 1, column = 0, sticky="news", padx = 5, pady = 5)
       
        self.txtResult2 = tk.Text(master = self.master)
        self.txtResult2.grid(row = 2, column=0, sticky = "news", padx=5, pady=5)

    def setRes(self, strRes1, strRes2):
        self.txtResult1.delete('1.0', tk.END)
        self.txtResult1.insert(tk.INSERT, strRes1)
        self.txtResult2.delete('1.0', tk.END)
        self.txtResult2.insert(tk.INSERT, strRes2)

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
            strRes1, strRes2 = Corridas.execute(numbers, nc)
            self.setRes(strRes1, strRes2)