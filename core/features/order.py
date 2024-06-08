import tkinter as tk

class View():
    def __init__(self, root):
        self.root = tk.Toplevel(root)

        self.root.title("Realizar Pedido")
        self.root.geometry("400x300")

        self.orderidEntry = tk.Entry(self.root)
        self.orderidLabel = tk.Label(self.root, text="Número do pedido:")
        self.orderidLabel.pack()
        self.orderidEntry.pack()

        self.orderdateEntry = tk.Entry(self.root)
        self.orderdateLabel = tk.Label(self.root, text="Data do pedido:")
        self.orderdateLabel.pack()
        self.orderdateEntry.pack()

        self.customerEntry = tk.Entry(self.root)
        self.customerLabel = tk.Label(self.root, text="Nome do cliente:")
        self.customerLabel.pack()
        self.customerEntry.pack()

        self.employeeEntry = tk.Entry(self.root)
        self.employeeLabel = tk.Label(self.root, text="Nome do vendedor:")
        self.employeeLabel.pack()
        self.employeeEntry.pack()

        self.productnameEntry = tk.Entry(self.root)
        self.productnameLabel = tk.Label(self.root, text="Produto:")
        self.productnameLabel.pack()
        self.productnameEntry.pack()

        self.productqtyEntry = tk.Entry(self.root)
        self.productqtyLabel = tk.Label(self.root, text="Quantidade:")
        self.productqtyLabel.pack()
        self.productqtyEntry.pack()