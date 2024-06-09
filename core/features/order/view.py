import tkinter as tk
from tkinter import ttk

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Realizar Pedido")
        self.root.geometry("400x400")

        # nome do cliente
        self.customerid = tk.StringVar()
        self.contactnames = self.controller.fillContactnames()
        
        self.combobox = ttk.Combobox(self.root, values=self.contactnames)
        self.combobox.bind("<<ComboboxSelected>>", self.fetchCustomerid)

        self.combobox.pack()
        #

        self.orderid = tk.StringVar()
        self.orderid.trace_add("write", self.checkOrderid)
        self.orderidEntry = tk.Entry(self.root, textvariable=self.orderid)
        self.orderidLabel = tk.Label(self.root, text="Número do pedido:")
        self.orderidLabel.pack()
        self.orderidEntry.pack()

        self.orderdate = tk.StringVar()
        self.orderdate.trace_add("write", self.checkOrderdate)
        self.orderdateEntry = tk.Entry(self.root, textvariable=self.orderdate)
        self.orderdateLabel = tk.Label(self.root, text="Data do pedido:")
        self.orderdateLabel.pack()
        self.orderdateEntry.pack()

        self.employee = tk.StringVar()
        self.employee.trace_add("write", self.checkEmployee)
        self.employeeEntry = tk.Entry(self.root, textvariable=self.employee)
        self.employeeLabel = tk.Label(self.root, text="Nome do vendedor:")
        self.employeeLabel.pack()
        self.employeeEntry.pack()

        self.productname = tk.StringVar()
        self.productname.trace_add("write", self.checkProductname)
        self.productnameEntry = tk.Entry(self.root, textvariable=self.productname)
        self.productnameLabel = tk.Label(self.root, text="Produto:")
        self.productnameLabel.pack()
        self.productnameEntry.pack()

        self.productqty = tk.StringVar()
        self.productqty.trace_add("write", self.checkProductqty)
        self.productqtyEntry = tk.Entry(self.root, textvariable=self.productqty)
        self.productqtyLabel = tk.Label(self.root, text="Quantidade:")
        self.productqtyLabel.pack()
        self.productqtyEntry.pack()

        self.confirm = tk.Button(self.root, text="Enviar", command=self.controller.sendOrder)
        self.confirm.pack()

    def fetchCustomerid(self, event):
        contactname = self.combobox.get()

        customerid = self.controller.fetchCustomerid(contactname)

        print(customerid)
        self.customerid.set(customerid)

    def checkOrderid(self, var, index, mode):
        orderid = self.orderid.get()

        aux = ""

        for digit in orderid:
            if digit.isdigit():
                aux += digit

        self.orderid.set(aux)

    def checkOrderdate(self, var, index, mode):
        orderdate = self.orderdate.get()

        aux = ""

        for digit in orderdate:
            if digit.isdigit():
                aux += digit

        self.orderdate.set(aux)

    def checkEmployee(self, var, index, mode):
        employee = self.employee.get()

        aux = ""

        for digit in employee:
            if not digit.isdigit():
                aux += digit

        self.employee.set(aux)

    def checkProductname(self, var, index, mode):
        productname = self.productname.get()

        aux = ""

        for digit in productname:
            if not digit.isdigit():
                aux += digit

        self.productname.set(aux)

    def checkProductqty(self, var, index, mode):
        productqty = self.productqty.get()

        aux = ""

        for digit in productqty:
            if digit.isdigit():
                aux += digit

        self.productqty.set(aux)