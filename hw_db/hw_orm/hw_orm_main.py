import json
from socket import PACKET_BROADCAST
import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker

from hw_orm_models import Publisher, Book, Sale, Shop, Stock, create_tables

def get_dsn():
    # dialect = input('Драйвер подключения: ')
    dialect = 'postgresql'
    # user_ligin = input('Логин: ')
    user_login = 'postgres'
    # user_passord = input('Пароль: ')
    user_password = 'postgres'
    # host = input('Хост: ')
    host = 'localhost'
    # port = input('Порт: ')
    port = '5432'
    # dbname = input('База данных: ')
    dbname = 'books_shop'

    return f'{dialect}://{user_login}:{user_password}@{host}:{port}/{dbname}'

def get_json_test_data():
    filename = 'hw_db/hw_orm/test_data.json'
    with open(filename) as infile:
        json_data = json.load(infile)
    return json_data

def main():
    engine = sqla.create_engine(get_dsn())
    create_tables(engine=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = get_json_test_data()
    for item in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,}[item.get('model')]
        session.add(model(id=item.get('pk'), **item.get('fields')))
    session.commit()

    user_input = input('Введите искомое: ')
    subq_1 = session.query(Publisher).filter(Publisher.name.like(f'%{user_input}%')).subquery()
    subq_2 = session.query(Book).join(subq_1, subq_1.c.id == Book.fk_publisher_id).subquery()
    subq_3 = session.query(Stock).join(subq_2, subq_2.c.id == Stock.fk_book_id).subquery()
    for item in session.query(Shop).join(subq_3, subq_3.c.fk_shop_id == Shop.id).all():
        print(item)

    session.close()

if __name__  == '__main__':
    main()