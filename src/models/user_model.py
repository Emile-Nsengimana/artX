from sqlalchemy import Column, String, Boolean, BIGINT, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError

from src.helpers.database import Base
from src.helpers.database import db_session
from src.models.art_model import Art
from src.models.payment_model import Payment
from src.models.art_order_model import Order
from src.utils.utility import Utility


class User(Base, Utility):
    __tablename__ = 'users'
    user_id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True)
    dob = Column(DateTime, nullable=False)
    role = Column(String, nullable=False)
    phone_no = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    status = Column(String, default="active")
    city = Column(String, nullable=False)
    street_no = Column(String)
    post_code = Column(String)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    art = relationship("Art")
    payment = relationship("Payment")
    order = relationship("Order")

    @staticmethod
    def save_user(**kwargs):
        result = ''
        try:
            register_user = User(**kwargs)
            register_user.save()
            result = register_user

        except IntegrityError as err:
            error_message = err.orig.args[0]
            index_start = error_message.find('Key')
            result = error_message[index_start+3:-1].replace(
                '(', '').replace(')', '')
            db_session.close()

        return result
