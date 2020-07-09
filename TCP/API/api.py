from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from API.Models.product import Product
import json


class Api:
    engine = None
    session = None

    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:p@ssw0rd@localhost:3306/merida-optics')
        self.session = Session(self.engine)

    def insert(self, pk: int, data: int):
        """
        :param pk:
        :param data:
        :return:
        """
        product = self.session.query(Product).get(pk)
        product.stock += data
        self.session.commit()
        return self.show_all()

    def get_all(self):
        """
        :return:
        """
        return self.show_all()

    def remove(self, pk: int, data: int):
        """
        :param pk:
        :param data:
        :return:
        """
        product = self.session.query(Product).get(pk)
        product.stock -= data
        self.session.commit()
        return self.show_all()

    def show_all(self):
        """
        :return:
        """
        # return self.session.query(Product).all()
        data = list()
        products = self.session.query(Product).all()
        for p in products:
            data.append({"id": p.id, "cod": p.cod, "description": p.description, "brand": p.brand, "type": p.type, "price": p.price, "stock": p.stock})
        return data
