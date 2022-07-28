from fileinput import filename
import json
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
    filename = '/home/stian88/main_docs/projects/netology_hw/db/hw_orm/test_data.json'
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
            'book': Book,
            'stock': Stock,
            'shop': Shop,
            'sale': Sale
        }[item.get('model')]
        session.add(model(**item.get('fields')))
        session.commit()

    find_name = input('Введите искомое: ')
    for record in session.query(Book).filter(Book.book_title.like(f'%{find_name}%')).all():
        print(record)

    subq = session.query(Book).filter(Book.book_title.like(f'%{find_name}%')).subquery()
    for item in session.query(Publisher).join(subq, subq.c.fk_publisher_id == Publisher.publisher_id).all():
        print(item)

    session.close()

if __name__  == '__main__':
    main()


