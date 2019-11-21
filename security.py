from models.user import UserModel


def authenticate(username, password):
    user = UserModel.search_be_username(username)
    if user and user.password == password:
        return user


def identity(paylode):
    user_id = paylode["identity"]
    return UserModel.search_by_id(user_id)
