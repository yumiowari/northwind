from core.features.order.model import Model
from core.features.order.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)

    def sendOrder(self):
        print("Pedido enviado!") # teste