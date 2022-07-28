import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    publisher_id = sqla.Column(sqla.Integer, primary_key=True)
    publisher_name = sqla.Column(sqla.String(length=30), unique=True, nullable=False)

    def __str__(self):
        return f'Publisher {self.publisher_id}: {self.publisher_name}'

class Book(Base):
    __tablename__ = 'book'
    book_id = sqla.Column(sqla.Integer, primary_key=True)
    book_title = sqla.Column(sqla.String(length=60), unique=True, nullable=False)
    fk_publisher_id = sqla.Column(sqla.Integer, sqla.ForeignKey('publisher.publisher_id'), nullable=False)
    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'Book {self.book_id}: {self.book_title}'

class Shop(Base):
    __tablename__ = 'shop'
    shop_id = sqla.Column(sqla.Integer, primary_key=True)
    shop_name = sqla.Column(sqla.String(length=30), unique=True, nullable=False)

    def __str__(self):
        return f'Shop {self.shop_id}: {self.shop_name}'

class Stock(Base):
    __tablename__ = 'stock'
    stock_id = sqla.Column(sqla.Integer, primary_key=True)
    fk_book_id = sqla.Column(sqla.Integer, sqla.ForeignKey('book.book_id'), nullable=False)
    fk_shop_id = sqla.Column(sqla.Integer, sqla.ForeignKey('shop.shop_id'), nullable=False)
    stock_count = sqla.Column(sqla.Integer, nullable=False)
    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

class Sale(Base):
    __tablename__ = 'sale'
    sale_id = sqla.Column(sqla.Integer, primary_key=True)
    sale_price = sqla.Column(sqla.String(length=10), nullable=False)
    sale_date = sqla.Column(sqla.String, nullable=False)
    sale_count = sqla.Column(sqla.Integer, nullable=False)
    fk_stock_id = sqla.Column(sqla.Integer, sqla.ForeignKey('stock.stock_id'), nullable=False)
    stock = relationship(Stock, backref='sale')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)