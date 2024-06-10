# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import StaleDataError
import uuid
from core.features.order.DAO import *
from core.features.order.mapeamento import *

import json
import requests
from datetime import datetime

# Criação do engine e base declarativa
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/northwind', echo=True)
Base = declarative_base()

class Model:
    def __init__(self):
        self.session = session

    def __init__(self):
        self.orderid = None
        self.customerid = None
        self.employeeid = None
        self.productid = None
        self.unitprice = None
        self.qty = None
        self.discount = None
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
        contactnames = self.session.query(Customer.contactname).all()
        return [contactname[0] for contactname in contactnames]

    def fetchCustomerid(self, contactname):
        customer = self.session.query(Customer).filter(Customer.contactname == contactname).one()
        return customer.customerid

    def fillLastnames(self):
        lastnames = self.session.query(Employee.lastname).all()
        return [lastname[0] for lastname in lastnames]

    def fetchEmployeeid(self, lastname):
        employee = self.session.query(Employee).filter(Employee.lastname == lastname).one()
        return employee.employeeid

    def fillProductnames(self):
        productnames = self.session.query(Product.productname).all()
        return [productname[0] for productname in productnames]
                
    def fetchProduct(self, productname):
        product = self.session.query(Product).filter(Product.productname == productname).one()
        return {
            'name': product.productname,
            'id': product.productid,
            'unitprice': product.unitprice
        }

    
    def fillShipnames(self):
        shipnames = self.session.query(Order.shipname).distinct().all()
        return [shipname[0] for shipname in shipnames]

    def fetchShip(self, shipname):
        order = self.session.query(Order).filter(Order.shipname == shipname).first()
        return {
            'name': order.shipname,
            'address': order.shipaddress,
            'city': order.shipcity,
            'region': order.shipregion,
            'postalcode': order.shippostalcode,
            'country': order.shipcountry,
            'id': order.shipperid
        }

    def sendOrder(self, customerid, employeeid, product, qty, discount, orderdate, requireddate, shippeddate, freight, ship):
        # Criação do pedido
        order = Order(
            customerid=customerid,
            employeeid=employeeid,
            orderdate=orderdate,
            requireddate=requireddate,
            shippeddate=shippeddate,
            freight=freight,
            shipname=ship['name'],
            shipaddress=ship['address'],
            shipcity=ship['city'],
            shipregion=ship['region'],
            shippostalcode=ship['postalcode'],
            shipcountry=ship['country'],
            shipperid=ship['id']
        )
        self.session.add(order)
        self.session.commit()  # Commit para gerar o orderid

        # Criação dos detalhes do pedido
        order_detail = OrderDetail(
            orderid=order.orderid,
            productid=product['id'],
            unitprice=product['unitprice'],
            qty=qty,
            discount=discount
        )
        self.session.add(order_detail)
        self.session.commit()