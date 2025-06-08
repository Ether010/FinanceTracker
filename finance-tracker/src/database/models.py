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

class Income(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    source = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)
    # Add any additional fields you need for your income tracking
    def __repr__(self):
        return f"<Income(id={self.id}, amount={self.amount}, source={self.source}, date={self.date}, description={self.description}, user_id={self.user_id})>"
    # Add any additional methods you need for your income tracking
class Budget(Base): 
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, nullable=False)
    # Add any additional fields you need for your budget tracking
    def __repr__(self):
        return f"<Budget(id={self.id}, category={self.category}, amount={self.amount}, date={self.date}, user_id={self.user_id})>"
    # Add any additional methods you need for your budget tracking
class User(Base):   
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    # Add any additional fields you need for your user tracking
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    # Add any additional methods you need for your user tracking
    