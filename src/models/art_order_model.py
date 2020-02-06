from sqlalchemy import (Column, String, Float, Text,
                        Sequence, BIGINT, ForeignKey)
from sqlalchemy.exc import IntegrityError

from src.helpers.database import Base
from src.helpers.database import db_session
# from src.models.art_model import Art
from src.utils.utility import Utility


class Order(Base, Utility):
    __tablename__ = 'orders'
    no = Column(String, Sequence('pay_no', start=1, increment=1),
                primary_key=True)
    item_no = Column(String, ForeignKey('arts.no'), nullable=False)
    label = Column(String, nullable=False)
    image = Column(String)
    details = Column(Text)
    price = Column(Float)
    orderedBy = Column(BIGINT, ForeignKey('users.user_id'), nullable=False)

    @staticmethod
    def save_order(**kwargs):
        result = ''
        try:
            add_order = Order(**kwargs)
            add_order.save()
            result = add_order

        except IntegrityError as err:
            error_message = err.orig.args[0]
            index_start = error_message.find('Key')
            result = error_message[index_start+3:-1].replace(
                '(', '').replace(')', '')
            db_session.close()

        return result
