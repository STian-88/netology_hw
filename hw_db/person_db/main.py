import psycopg2

def create_person_bd():
    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("""
            DROP TABLE IF EXISTS phone;
            DROP TABLE IF EXISTS person;
            """)

    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS person(
                person_id SERIAL PRIMARY KEY,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(30) NOT NULL,
                email VARCHAR(30) NOT NULL
            ); 
            """)

            cur.execute("""
            CREATE TABLE phone(
                number BIGINT PRIMARY KEY,
                fk_person_id INTEGER REFERENCES person(person_id)
            );
            """)
    conn.commit()

def find_person_id():
    find = input('Введите имя, фамилию или email для поиска: ').lower()
    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT person_id FROM person
                    WHERE person.first_name = %s OR person.last_name = %s OR person.email = %s;
                    """,
                    (find.capitalize(), find.capitalize(), find)
                )
                res = cur.fetchall()
                while len(res) == 0:
                    print('Запись отсутствует.')
                    find = input('Введите имя, фамилию или email для поиска: ').lower()
                    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
                        with conn.cursor() as cur:
                            cur.execute(
                                """
                                SELECT person_id FROM person
                                WHERE person.first_name = %s OR person.last_name = %s OR person.email = %s;
                                """,
                                (find.capitalize(), find.capitalize(), find)
                                )
                            res = cur.fetchall()
                return str(res[0][0])

def get_person_info():
    name = input('Введите фамилию и имя: ')
    while ' ' not in name.strip():
        name = input('Ввод должен состоять из двух слов(Фамилия и Имя)')
    email = input('Введите email: ')
    phone = int(input('Введите номер телефона(0 - нет номера телефона): '))
    if phone != 0:
        return name.split()[0].capitalize(), name.split()[1].capitalize(), email, phone
    else:
         return name.split()[0], name.split()[1], email

def add_person():
    info = get_person_info()
    if len(info) > 3:
        first_name, last_name, email, phone = info
        with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO person(first_name, last_name, email)
                VALUES (%s, %s, %s) RETURNING person_id;
                """, (first_name, last_name, email))
                person_id = cur.fetchone()
                cur.execute("""
                INSERT INTO phone(number, fk_person_id)
                VALUES (%s, %s); 
                """, (phone, person_id))
    else:
        first_name, last_name, email = info
        with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO person(first_name, last_name, email)
                VALUES (%s, %s, %s);
                """, (first_name, last_name, email))
    input('Запись добавлена!')

def add_phone():
    person_id = find_person_id()
    phone = int(input('Введите номер телефона: '))
    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO phone(number, fk_person_id)
                    VALUES(%s, %s)
                    """,
                    (phone, person_id)
                )
    input('Номер телефона записан!')

def change_info():
    person_id = find_person_id()
    new_person_info = get_person_info()
    if len(new_person_info) == 3: 
        with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE person SET first_name = %s WHERE person_id = %s
                        """, (new_person_info[0], person_id)
                    )
                    cur.execute(
                        """
                        UPDATE person SET last_name = %s WHERE person_id = %s
                        """, (new_person_info[1], person_id)
                    )
                    cur.execute(
                        """
                        UPDATE person SET email = %s WHERE person_id = %s
                        """, (new_person_info[2], person_id)
                    )
        conn.commit()
    else:
        with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE person SET first_name = %s WHERE person_id = %s
                        """, (new_person_info[0], person_id)
                    )
                    cur.execute(
                        """
                        UPDATE person SET last_name = %s WHERE person_id = %s
                        """, (new_person_info[1], person_id)
                    )
                    cur.execute(
                        """
                        UPDATE person SET email = %s WHERE person_id = %s
                        """, (new_person_info[2], person_id)
                    )
                    cur.execute(
                        """
                        INSERT INTO phone(number, fk_person_id)
                        VALUES(%s, %s)
                        """, (new_person_info[3], person_id)
                )
        conn.commit()
    input('Данные изменены!')

def show_person_info():
    person_id = find_person_id()
    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM person WHERE person_id = %s
                    """, 
                    (person_id)
                )
                res = cur.fetchall()
    if len(res) == 0:
        print('Запись отсутствует.')
    else:
        person_id, first_name, last_name, email = res[0]
        print(f'Фамилия: {first_name}\n'
              f'Имя: {last_name}\n'
              f'Email: {email}')
    phones_list = show_person_phones(person_id)
    for phone in phones_list:
        print(phone)
    input()

def show_person_phones(person_id):
    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM phone WHERE fk_person_id = %s
                    """, 
                    (person_id,)
                )
                res = cur.fetchall()
    phones_list= []
    for item in res:
        phones_list.append(item[0])
    return phones_list

def delete_person():
    person_id = find_person_id()
    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM phone 
                WHERE phone.fk_person_id = %s
                """, (person_id)
            )
            cur.execute(
                """
                DELETE FROM person 
                WHERE person_id = %s
                """, (person_id)
            )
    input('Нет человека - нет проблем!)')

def delete_phone():
    person_id = find_person_id()
    with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT number 
                FROM phone
                WHERE fk_person_id = %s
                """,
                (person_id)
            )
            phones = cur.fetchall()
    print('Существующие номера: ')
    for i in range(len(phones)):
        print(f'{i+1} --> {phones[i][0]}')
    choice = int(input(f'Выберите номер для удаления(0 - {len(phones)})\n'
                   f'0 - удалить все номера: ' ))
    if choice == 0:
        with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM phone 
                    WHERE phone.fk_person_id = %s
                    """, (person_id)
                )
    else:
        ch = phones[choice-1][0]
        with psycopg2.connect(database='person_info', user='postgres', password='postgres') as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM phone 
                    WHERE phone.number = %s
                    """, (ch,)
                )
    input('"Жили как-то без телефонов и ничо"')

def get_choice():
    print(
        """
        ---------Меню---------- 
        1 --> Добавить запись
        2 --> Добавить номер телефона к существующей записи
        3 --> Изменить запись
        4 --> Удалить запись
        5 --> Удалить номера телефона
        6 --> Найти запись
        7 --> Выйти
        """
    )
    choice = int(input('Введите номер(1-7): '))
    while 7 < choice < 1:
        choice = int(input('Введите номер(1-7): '))
    print()
    return choice
    
def main():
    choice = 0
    while choice != 7:
        choice = get_choice()
        if choice == 1:
            add_person()
        if choice == 2:
            add_phone()
        if choice == 3:
            change_info()
        if choice == 4:
            delete_person()
        if choice == 5:
            delete_phone()
        if choice == 6:
            show_person_info()
        if choice == 7:
            print('Пока')
    
if __name__ == '__main__':
    main()
    