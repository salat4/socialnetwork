# This is a sample Python script.
from dal.model.user import User
from dal.repository.user_repository import UserRepository

user = User(1, "Vova", "Nemalik", "POSTGRESQL", "vovasql@gmail.com", "nesalatik18", "vova_avatar")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    repo = UserRepository()

