import tkinter as tk
from tkinter import ttk
from tkcalendar.calendar_ import Calendar

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Realizar Pedido")
        self.root.geometry("400x400")

        # nome do cliente
        self.customerid = tk.StringVar()
        self.contactnames = self.controller.fillContactnames()
        
        self.customersCombobox = ttk.Combobox(self.root, values=self.contactnames)
        self.customersCombobox.bind("<<ComboboxSelected>>", self.fetchCustomerid)

        self.customersCombobox.pack()
        #

        # nome do empregado
        self.employeeid = tk.IntVar()
        self.lastnames = self.controller.fillLastnames()

        self.employeesCombobox = ttk.Combobox(self.root, values=self.lastnames)
        self.employeesCombobox.bind("<<ComboboxSelected>>", self.fetchEmployeeid)

        self.employeesCombobox.pack()
        #

        # datas
        self.orderdateCalendar = Calendar(self.root, date_pattern="yyyy-MM-dd") # usa .get_date() para recupear a data
        self.orderdateCalendar.pack()

        self.requireddateCalendar = Calendar(self.root, date_pattern="yyyy-MM-dd")
        self.requireddateCalendar.pack()

        self.shippeddateCalendar = Calendar(self.root, date_pattern="yyyy-MM-dd")
        self.shippeddateCalendar.pack()
        #

        # frete
        self.freight = tk.StringVar()
        self.freight.trace_add("write", self.checkFreight)
        self.freightEntry = tk.Entry(self.root, textvariable=self.freight)
        self.freightEntry.pack()
        #

        # barco
        self.ship = {}
        self.shipname = tk.StringVar()
        self.shipnames = self.controller.fillShipnames()
        self.shipsCombobox = ttk.Combobox(self.root, values=self.shipnames)
        self.shipsCombobox.bind("<<ComboboxSelected>>", self.fetchShip)
        self.shipsCombobox.pack()
        # 

        self.confirm = tk.Button(self.root, text="Enviar", command=self.controller.sendOrder)
        self.confirm.pack()

    def fetchCustomerid(self, event):
        contactname = self.customersCombobox.get()

        customerid = self.controller.fetchCustomerid(contactname)

        self.customerid.set(customerid)

    def fetchEmployeeid(self, event):
        lastname = self.employeesCombobox.get()

        employeeid = self.controller.fetchEmployeeid(lastname)

        self.employeeid.set(employeeid)

    def checkFreight(self, var, index, mode):
        freight = self.freight.get()

        flag = False

        aux = ""

        for digit in freight:
            if digit.isdigit() or (digit == '.' and flag == False):
                aux += digit
                if digit == '.':
                    flag = True

        self.freight.set(aux)

    def fetchShip(self, event):
        shipname = self.shipsCombobox.get()

        self.shipname.set(shipname)

        self.ship = self.controller.fetchShip(shipname)