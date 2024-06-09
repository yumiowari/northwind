import psycopg

class Model:
    def __init__(self):
        self.orderid = None
        self.customerid = None
        self.employeeid = None
        self.orderdate = None
        self.requireddate = None
        self.shippeddate = None
        self.freight = None
        self.shipname = None
        self.shipaddress = None
        self.shipcity = None
        self.shipregion = None
        self.shippostalcode = None
        self.shipcountry = None
        self.shipperid = None

    def fillContactnames(self):
        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "SELECT contactname FROM northwind.customers"
                session.execute(query)
                result = session.fetchall()
                contactnames = [registro[0] for registro in result] # remove os parênteses

                return contactnames

    def fetchCustomerid(self, contactname):
        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "SELECT customerid FROM northwind.customers WHERE contactname = '{}'".format(contactname)
                session.execute(query)
                result = session.fetchone()
                customerid = result[0]

                return customerid

    def fillLastnames(self):
        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "SELECT lastname FROM northwind.employees"
                session.execute(query)
                result = session.fetchall()
                lastnames = [registro[0] for registro in result]

                return lastnames

    def fetchEmployeeid(self, lastname):
        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "SELECT employeeid FROM northwind.employees WHERE lastname = '{}'".format(lastname)
                session.execute(query)
                result = session.fetchone()
                employeeid = result[0]

                return employeeid

    def fillShipnames(self):
        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "SELECT DISTINCT shipname FROM northwind.orders"
                session.execute(query)
                result = session.fetchall()
                shipnames = [registro[0] for registro in result]

                return shipnames

    def fetchShip(self, shipname):
        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "SELECT shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid FROM northwind.orders WHERE shipname = '{}'".format(shipname)
                session.execute(query)
                result = session.fetchone()
                ship = {
                    'name': shipname,
                    'address': result[0],
                    'city': result[1],
                    'region': result[2],
                    'postalcode': result[3],
                    'country': result[4],
                    'id': result[5]
                }

                return ship

    def sendOrder(self, customerid, employeeid, orderdate, requireddate, shippeddate, freight, ship):
        self.customerid = "'" + customerid + "'"
        self.employeeid = employeeid
        self.orderdate = "'" + orderdate + "'"
        self.requireddate = "'" + requireddate + "'"
        self.shippeddate = shippeddate
        if self.shippeddate != None:
            self.shippeddate = "'" + self.shippeddate + "'"
        else:
            self.shippeddate = "null"
        self.freight = float(freight)
        self.shipname = ship['name']
        self.shipname = "'" + self.shipname + "'"
        self.shipaddress = ship['address']
        self.shipaddress = "'" + self.shipaddress + "'"
        self.shipcity = ship['city']
        self.shipcity = "'" + self.shipcity + "'"
        self.shipregion = ship['region']
        if self.shipregion != None:
            self.shipregion = "'" + self.shipregion + "'"
        else:
            self.shipregion = "null"
        self.shippostalcode = ship['postalcode']
        if self.shippostalcode == None:
            self.shippostalcode = "null"
        self.shipcountry = ship['country']
        self.shipcountry = "'" + self.shipcountry + "'"
        self.shipperid = ship['id']
        if self.shipperid != None:
            self.shipperid = "'" + self.shipperid + "'"
        else:
            self.shipperid = "null"

        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "SELECT MAX(orderid) FROM northwind.orders"
                session.execute(query)
                result = session.fetchone()
                self.orderid = result[0] + 1

        with psycopg.connect( host='localhost', dbname='northwind', user = 'postgres', password = 'postgres') as northwind:  
            with northwind.cursor() as session:
                query = "INSERT INTO northwind.orders VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(self.orderid,
                                                                                                                              self.customerid,
                                                                                                                              self.employeeid,
                                                                                                                              self.orderdate,
                                                                                                                              self.requireddate,
                                                                                                                              self.shippeddate,
                                                                                                                              self.freight,
                                                                                                                              self.shipname,
                                                                                                                              self.shipaddress,
                                                                                                                              self.shipcity,
                                                                                                                              self.shipregion,
                                                                                                                              self.shippostalcode,
                                                                                                                              self.shipcountry,
                                                                                                                              self.shipperid)
                session.execute(query)