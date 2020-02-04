from sqlalchemy import Column, String, BIGINT, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError

from src.models.payment_model import Payment
from src.helpers.database import Base
from src.utils.utility import Utility
from src.helpers.database import db_session


class Art(Base, Utility):
    __tablename__ = 'arts'
    no = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    image = Column(String)
    details = Column(Text)
    price = Column(Float)
    owner = Column(BIGINT, ForeignKey('users.user_id'), nullable=False)
    category = Column(String, nullable=False)
    status = Column(String, nullable=False, default='available')
    payment = relationship('Payment', uselist=False)

    @staticmethod
    def save_art(**kwargs):
        result = ''
        try:
            register_art = Art(**kwargs)
            register_art.save()
            result = register_art

        except IntegrityError as err:
            error_message = err.orig.args[0]
            index_start = error_message.find('Key')
            result = error_message[index_start+3:-1].replace(
                '(', '').replace(')', '')
            db_session.close()

        return result
