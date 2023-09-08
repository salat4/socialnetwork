import uuid


class User:
    def __init__(self, name, surname, email, password, avatar, salt, jwt, _id=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.avatar = avatar
        self.salt = salt
        self.jwt = jwt
        self._id = _id

    def __str__(self):
        return f"User(id={self._id}, name='{self.name}', surname='{self.surname}',  email='{self.email}', password='{self.password}', avatar='{self.avatar}, jwt = '{self.jwt}', salt = '{self.salt}'')"
