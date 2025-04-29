from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)
    # Add any additional fields you need for your expense tracking
    def __repr__(self):
        return f"<Expense(id={self.id}, amount={self.amount}, category={self.category}, date={self.date}, description={self.description}, user_id={self.user_id})>"
    # Add any additional methods you need for your expense tracking
    