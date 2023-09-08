from dal.model.user import User
from dal.repository.user_repository import UserRepository
import bcrypt
import jwt
import uuid


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def registration(self, register_user):
        salt = bcrypt.gensalt()

        payload_data = {
            'sub': register_user['surname'],
            'name': register_user['name'],
            'email': register_user['email']
        }
        token = jwt.encode(
            payload=payload_data,
            key="secret"
        )
        hash_password = bcrypt.hashpw(register_user['password'].encode('utf-8'), salt)
        user_dal = User(
            email=register_user['email'],
            password=hash_password,
            surname=register_user['surname'],
            name=register_user['name'],
            avatar=register_user['avatar'],
            salt=salt,
            jwt=token
        )

        self.user_repository.create_user(user_dal)

    def login(self, user):
        login_user = self.user_repository.read_user(user['email'])
        print(login_user)
        # if user['password'] == login_user.password:
        #     print("all good")
