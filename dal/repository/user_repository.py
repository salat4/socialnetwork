
from connect_to_db.connect import connect
from dal.model.user import User


class UserRepository:
    def __init__(self):
        self.connection = connect()
        self.create_table_user()

    def create_table_user(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
                _id SERIAL PRIMARY KEY,
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
            RETURNING _id;
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user.name, user.surname, user.login, user.email, user.password, user.avatar))
            user_id = cursor.fetchone()[0]
            user.id = user_id
        self.connection.commit()

    def read_user(self, user_id):
        query = '''
            SELECT * FROM users WHERE _id = %s;
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
        # print(new_data)
        update_query = '''
            UPDATE users SET name = %s, surname = %s, login = %s, email = %s, password = %s, avatar = %s
            WHERE _id = %s;
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(update_query, (
                new_data.name,
                new_data.surname,
                new_data.login,
                new_data.email,
                new_data.password,
                new_data.avatar,
                user_id
            ))
        self.connection.commit()
        return True

    def delete_user(self, user_id):
        query = '''
            DELETE FROM users WHERE _id = %s;
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, (user_id,))
        self.connection.commit()
        return True

    def get_user_by_email(self, email):
        query = '''
                    SELECT * FROM users WHERE email = %s;
                '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            if row:
                _id, name, surname, login, email, password, avatar = row
                return User(_id, name, surname, login, email, password, avatar)
            return None
