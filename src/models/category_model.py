from sqlalchemy import Column, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from src.helpers.database import Base
from src.utils.utility import Utility


class Category(Base, Utility):
    __tablename__ = 'categories'
    no = Column(String, Sequence('cat_no_seq', start=1, increment=1),
                primary_key=True)
    category = Column(String, ForeignKey('arts.no'), nullable=False)
    art = relationship("Art")
