from sqlalchemy import Column, String, BIGINT, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.helpers.database import Base


class Art(Base):
    __tablename__ = 'arts'
    no = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    image = Column(String)
    details = Column(Text)
    price = Column(Float)
    owner = Column(BIGINT, ForeignKey('users.user_id'), nullable=False)
    category = Column(String, ForeignKey('category.no'), nullable=False)
    status = Column(String, nullable=False, default='available')
    payment = relationship('payment', uselist=False)
    category = relationship('Category', uselist=False)

    def __init__(self, **kwargs):
        self.no = kwargs['no']
        self.category = kwargs['category']
        self.label = kwargs['label']
        self.image = kwargs['image']
        self.details = kwargs['details']
        self.status = kwargs['status']
        self.price = kwargs['price']
        self.owner = kwargs['owner']
