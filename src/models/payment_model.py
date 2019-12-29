from sqlalchemy import (Column, Sequence, BIGINT, String,
                        Float, DateTime, ForeignKey)
from sqlalchemy.orm import relationship

from src.helpers.database import Base
from src.utils.utility import Utility


class Payment(Base, Utility):
    __tablename__ = 'payments'

    no = Column(String, Sequence('pay_no', start=1, increment=1),
                primary_key=True)
    amount = Column(Float)
    payment_method = Column(String, nullable=False)
    transfer_no = Column(String, nullable=False)
    item = Column(String, ForeignKey('arts.no'), nullable=False)
    owner = Column(BIGINT, ForeignKey('users.user_id'), nullable=False)
    art = relationship("Art")
