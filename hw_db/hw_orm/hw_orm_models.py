import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(length=30), unique=True, nullable=False)

    def __str__(self):
        return f'Publisher {self.id}: {self.name}'

class Book(Base):
    __tablename__ = 'book'
    id = sqla.Column(sqla.Integer, primary_key=True)
    title = sqla.Column(sqla.String(length=60), unique=True, nullable=False)
    fk_publisher_id = sqla.Column(sqla.Integer, sqla.ForeignKey('publisher.id'), nullable=False)
    
    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'Book {self.id}: {self.title}'

class Shop(Base):
    __tablename__ = 'shop'
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(length=30), unique=True, nullable=False)

    def __str__(self):
        return f'Shop {self.id}: {self.name}'

class Stock(Base):
    __tablename__ = 'stock'
    id = sqla.Column(sqla.Integer, primary_key=True)
    fk_book_id = sqla.Column(sqla.Integer, sqla.ForeignKey('book.id'), nullable=False)
    fk_shop_id = sqla.Column(sqla.Integer, sqla.ForeignKey('shop.id'), nullable=False)
    count = sqla.Column(sqla.Integer, nullable=False)

    books = relationship(Book, backref='stocks')
    shops = relationship(Shop, backref='stocks')

class Sale(Base):
    __tablename__ = 'sale'
    id = sqla.Column(sqla.Integer, primary_key=True)
    price = sqla.Column(sqla.String(length=10), nullable=False)
    date = sqla.Column(sqla.String, nullable=False)
    count = sqla.Column(sqla.Integer, nullable=False)
    fk_stock_id = sqla.Column(sqla.Integer, sqla.ForeignKey('stock.id'), nullable=False)

    stock = relationship(Stock, backref='sale')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)