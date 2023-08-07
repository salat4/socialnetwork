from dal.model.user import User
from dal.repository.user_repository import UserRepository
from socialnetwork.login.forms import RegistrationForm


def register_user(request):
    rep = UserRepository()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = User(_id=None,  # Якщо у вас є автоматична генерація ідентифікаторів в DAL, вкажіть None
                        name=user_data['username'],
                        surname='',  # Ви можете також додати інші поля з форми реєстрації тут
                        login=user_data['username'],
                        email=user_data['email'],
                        password=user_data['password'],
                        avatar='path_to_avatar'
                        )
            rep.create_user(user)  # Збереження даних про користувача за допомогою вашого DAL
            return True
    return False
