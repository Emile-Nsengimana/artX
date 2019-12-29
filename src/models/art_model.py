from sqlalchemy import Column, String, BIGINT, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.models.payment_model import Payment
from src.models.category_model import Category
from src.helpers.database import Base
from src.utils.utility import Utility


class Art(Base, Utility):
    __tablename__ = 'arts'
    no = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    image = Column(String)
    details = Column(Text)
    price = Column(Float)
    owner = Column(BIGINT, ForeignKey('users.user_id'), nullable=False)
    category = Column(String, ForeignKey('category.no'), nullable=False)
    status = Column(String, nullable=False, default='available')
    payment = relationship('Payment', uselist=False)
    category = relationship('Category', uselist=False)
