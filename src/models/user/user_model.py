from sqlalchemy import Column, String, Boolean, BIGINT, DateTime
from sqlalchemy.orm import relationship

from src.helpers.database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(DateTime, nullable=False)
    role = Column(String, nullable=False)
    phone_no = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    state = Column(String, default="active")
    city = Column(String, nullable=False)
    address_1 = Column(String)
    address_2 = Column(String)
    post_code = Column(String)
    is_admin = Column(Boolean, default=False)
    art = relationship("Art")
    payment = relationship("Payment")

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.dob = kwargs['dob']
        self.role = kwargs['role']
        self.phone_no = kwargs['phone_no']
        self.country = kwargs['country']
        self.state = kwargs['state']
        self.statecity = kwargs['city']
        self.stateaddress_1 = kwargs['address_1']
        self.stateaddress_2 = kwargs['address_2']
        self.statepost_code = kwargs['post_code']
        self.is_admin = kwargs['is_admin']
