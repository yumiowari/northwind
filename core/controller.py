import tkinter as tk

from core.model import Model
from core.view import View
from core.features.order.controller import Controller as OrderController

class Controller:
    def __init__(self):
        self.root = tk.Tk()

        self.model = Model()
        self.view = View(self.root, self)

        self.root.mainloop()

    def newOrder(self):
        self.ordercontroller = OrderController(self.root)

    def reportRanking(self):
        pass