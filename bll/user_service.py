from dal.repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def registration(self, user):
        self.user_repository.create_user(user)
