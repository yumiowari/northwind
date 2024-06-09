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

    def fillLastnames(self):
        lastnames = self.model.fillLastnames()

        return lastnames

    def fetchEmployeeid(self, lastname):
        employeeid = self.model.fetchEmployeeid(lastname)

        return employeeid

    def fillProductnames(self):
        productnames = self.model.fillProductnames()

        return productnames

    def fetchProduct(self, productname):
        product = self.model.fetchProduct(productname)

        return product

    def fillShipnames(self):
        shipnames = self.model.fillShipnames()

        return shipnames

    def fetchShip(self, shipname):
        ship = self.model.fetchShip(shipname)

        return ship

    def sendOrder(self):
        customerid = self.view.customerid.get()
        employeeid = self.view.employeeid.get()
        product = self.view.product
        qty = self.view.qty.get()
        discount = self.view.discount.get()
        orderdate = self.view.orderdateCalendar.get_date()
        orderdate += ' 00:00:00' # to do
        requireddate = self.view.requireddateCalendar.get_date()
        requireddate += ' 00:00:00'
        shippeddate = self.view.shippeddateCalendar.get_date()
        shippeddate += ' 00:00:00'
        freight = self.view.freight.get()
        ship = self.view.ship

        self.model.sendOrder(customerid, employeeid, product, qty, discount, orderdate, requireddate, shippeddate, freight, ship)