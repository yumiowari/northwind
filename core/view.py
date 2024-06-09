import tkinter as tk

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Northwind")
        self.root.geometry("400x400")

        self.menubar = tk.Menu(self.root)

        self.ordermenu = tk.Menu(self.menubar, tearoff=0)
        self.ordermenu.add_command(label="Cadastrar", command=self.controller.newOrder)
        self.menubar.add_cascade(label="Pedidos", menu=self.ordermenu)

        self.printmenu = tk.Menu(self.menubar, tearoff=0)
        self.printmenu.add_command(label="Ranking", command=self.controller.reportRanking)
        self.menubar.add_cascade(label="Imprimir", menu=self.printmenu)

        self.root.config(menu=self.menubar)