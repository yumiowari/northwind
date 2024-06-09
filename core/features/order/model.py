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

    def sendOrder(self):
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