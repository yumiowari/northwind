from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from core.features.order.mapeamento import *\

class DAO():
    # Conexão com o banco
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/northwind")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    # Função de inserção no banco
    def insert(session, obj):
        session.add(obj)