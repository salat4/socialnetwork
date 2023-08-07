class User:
    def __init__(self, _id, name, surname, login, email, password, avatar):
        self._id = _id
        self.name = name
        self.surname = surname
        self.login = login
        self.email = email
        self.password = password
        self.avatar = avatar

    def __str__(self):
        return f"User(id={self._id}, name='{self.name}', surname='{self.surname}', login='{self.login}', email='{self.email}', password='{self.password}', avatar='{self.avatar}')"

