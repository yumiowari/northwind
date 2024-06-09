import tkinter as tk
from tkinter import ttk
from tkcalendar.calendar_ import Calendar

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Inserir Pedido")
        self.root.geometry("800x600")

        self.top = tk.Frame(self.root)
        self.base = tk.Frame(self.root)

        # nome do cliente
        self.customerid = tk.StringVar()
        self.contactnames = self.controller.fillContactnames()
        
        self.customersLabel = tk.Label(self.top, text="Nome do cliente:")
        self.customersCombobox = ttk.Combobox(self.top, values=self.contactnames, state='readonly')
        self.customersCombobox.bind("<<ComboboxSelected>>", self.fetchCustomerid)

        self.customersLabel.pack()
        self.customersCombobox.pack()
        #

        # nome do empregado
        self.employeeid = tk.IntVar()
        self.lastnames = self.controller.fillLastnames()

        self.employeesLabel = tk.Label(self.top, text="Sobrenome do empregado:")
        self.employeesCombobox = ttk.Combobox(self.top, values=self.lastnames, state='readonly')
        self.employeesCombobox.bind("<<ComboboxSelected>>", self.fetchEmployeeid)

        self.employeesLabel.pack()
        self.employeesCombobox.pack()
        #

        # nome do produto
        self.product = {}
        self.productnames = self.controller.fillProductnames()

        self.productsLabel = tk.Label(self.top, text="Nome do produto:")
        self.productsCombobox = ttk.Combobox(self.top, values=self.productnames, state='readonly')
        self.productsCombobox.bind("<<ComboboxSelected>>", self.fetchProduct)

        self.productsLabel.pack()
        self.productsCombobox.pack()
        #

        # quantidade
        self.qty = tk.StringVar()
        self.qty.trace_add("write", self.checkQty)

        self.qtyLabel = tk.Label(self.top, text="Quantidade:")
        self.qtyEntry = tk.Entry(self.top, textvariable=self.qty)

        self.qtyLabel.pack()
        self.qtyEntry.pack()
        #

        # desconto
        self.discount = tk.StringVar()
        self.discount.trace_add("write", self.checkDiscount)

        self.discountLabel = tk.Label(self.top, text="Desconto:")
        self.discountEntry = tk.Entry(self.top, textvariable=self.discount)

        self.discountLabel.pack()
        self.discountEntry.pack()
        #

        ### datas
        self.datas = tk.Frame(self.top)

        # data do pedido
        self.orderdateFrame = tk.Frame(self.datas)
        self.orderdateLabel = tk.Label(self.orderdateFrame, text="Data do pedido:")
        self.orderdateCalendar = Calendar(self.orderdateFrame, date_pattern="yyyy-MM-dd") # usa .get_date() para recupear a data

        self.orderdateLabel.pack()
        self.orderdateCalendar.pack()
        self.orderdateFrame.pack(side=tk.LEFT)
        #

        # data limite para entrega
        self.requireddateFrame = tk.Frame(self.datas)
        self.requireddateLabel = tk.Label(self.requireddateFrame, text="Data limite para entrega:")
        self.requireddateCalendar = Calendar(self.requireddateFrame, date_pattern="yyyy-MM-dd")

        self.requireddateLabel.pack()
        self.requireddateCalendar.pack()
        self.requireddateFrame.pack(side=tk.LEFT)
        #

        # data do envio
        self.shippeddateFrame = tk.Frame(self.datas)
        self.shippeddateLabel = tk.Label(self.shippeddateFrame, text="Data do envio:")
        self.shippeddateCalendar = Calendar(self.shippeddateFrame, date_pattern="yyyy-MM-dd")

        self.shippeddateLabel.pack()
        self.shippeddateCalendar.pack()
        self.shippeddateFrame.pack(side=tk.LEFT)
        #

        self.datas.pack()
        ###

        # frete
        self.freight = tk.StringVar()
        self.freight.trace_add("write", self.checkFreight)

        self.freightLabel = tk.Label(self.top, text="Frete:")
        self.freightEntry = tk.Entry(self.top, textvariable=self.freight)

        self.freightLabel.pack()
        self.freightEntry.pack()
        #

        # barco
        self.ship = {}
        self.shipnames = self.controller.fillShipnames()

        self.shipsLabel = tk.Label(self.top, text="Embarcação:")
        self.shipsCombobox = ttk.Combobox(self.top, values=self.shipnames, state='readonly')
        self.shipsCombobox.bind("<<ComboboxSelected>>", self.fetchShip)

        self.shipsLabel.pack()
        self.shipsCombobox.pack()
        #

        # botão de confirmação
        self.confirm = tk.Button(self.base, text="Enviar", command=self.controller.sendOrder)

        self.confirm.pack()
        #

        self.top.pack(side=tk.TOP)
        self.base.pack(side=tk.BOTTOM)

    def fetchCustomerid(self, event):
        contactname = self.customersCombobox.get()

        customerid = self.controller.fetchCustomerid(contactname)

        self.customerid.set(customerid)

    def fetchEmployeeid(self, event):
        lastname = self.employeesCombobox.get()

        employeeid = self.controller.fetchEmployeeid(lastname)

        self.employeeid.set(employeeid)

    def fetchProduct(self, event):
        productname = self.productsCombobox.get()

        self.product = self.controller.fetchProduct(productname)

    def checkQty(self, var, index, mode):
        qty = self.qty.get()

        aux = ""

        for digit in qty:
            if digit.isdigit():
                aux += digit

        self.qty.set(aux)

    def checkDiscount(self, var, index, mode):
        discount = self.discount.get()

        flag = False

        aux = ""

        for digit in discount:
            if digit.isdigit() or (digit == '.' and flag == False):
                aux += digit
                if digit == '.':
                    flag = True

        self.discount.set(aux)

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

        self.ship = self.controller.fetchShip(shipname)