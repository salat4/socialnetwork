
from connect_to_db.connect import connect
from dal.model.user import User


class UserRepository:
    def __init__(self):
        self.connection = connect()
        self.create_table_user()

    def create_table_user(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                surname VARCHAR NOT NULL,
                login VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                avatar VARCHAR
            );
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        self.connection.commit()

    def create_user(self, user):
        query = '''
            INSERT INTO users (name, surname, login, email, password, avatar)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id;
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user.name, user.surname, user.login, user.email, user.password, user.avatar))
            user_id = cursor.fetchone()[0]
            user.id = user_id
        self.connection.commit()

    def read_user(self, user_id):
        query = '''
            SELECT * FROM users WHERE id = %s;
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()
            if row:
                _id, name, surname, login, email, password, avatar = row
                return User(_id, name, surname, login, email, password, avatar)
            return None

    def update_user(self, user_id, new_data):
        user = self.read_user(user_id)
        if not user:
            return False

        update_query = '''
            UPDATE users SET name = %s, surname = %s, login = %s, email = %s, password = %s, avatar = %s
            WHERE id = %s;
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(update_query, (
                new_data.get('name', user.name),
                new_data.get('surname', user.surname),
                new_data.get('login', user.login),
                new_data.get('email', user.email),
                new_data.get('password', user.password),
                new_data.get('avatar', user.avatar),
                user_id
            ))
        self.connection.commit()
        return True

    def delete_user(self, user_id):
        query = '''
            DELETE FROM users WHERE id = %s;
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user_id,))
        self.connection.commit()
        return True
