from core.features.order.model import Model
from core.features.order.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)

    def fillContactnames(self):
        customers = self.model.fillContactnames()

        return customers

    def fetchCustomerid(self, contactname):
        customerid = self.model.fetchCustomerid(contactname)

        return customerid

    def sendOrder(self):
        self.model.sendOrder()