from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    email = Column(String, nullable=True)
    pass_hash = Column(String, nullable=True)


class Category(Base):
    __tablename__ = 'Categories'

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), index=True)
    type = Column(Boolean)


class Transaction(Base):
    __tablename__ = 'Transactions'

    transaction_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), index=True)
    category_id = Column(Integer, ForeignKey('Categories.category_id'), index=True)
    amount = Column(Integer)
    description = Column(String, nullable=True)
    datetime = Column(DateTime)
    
    user = relationship("User", back_populates="Transactions")
    category = relationship("Category", back_populates="Transactions")


class Budget(Base):
    __tablename__ = 'Budgets'

    budget_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), index=True)
    category_id = Column(Integer, ForeignKey('Categories.category_id'), index=True)
    amount = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime, nullable=True)
