import tkinter as tk

from core.model import Model
from core.view import View
import core.features.order

class Controller:
    def __init__(self):
        self.root = tk.Tk()

        self.model = Model()
        self.view = View(self.root, self)

        self.root.mainloop()

    def newOrder(self):
        self.orderview = core.features.order.View(self.view.root)

    def reportRanking(self):
        pass