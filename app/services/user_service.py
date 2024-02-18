from app.models.user import User


class UserService:
    def __init__(self):
        # For the sake of example, we'll pretend this is a database of users.
        self.users = [
            User(1, "John Doe", "john.doe@example.com", "password"),
            User(2, "Jane Doe", "jane.doe@example.com", "password"),
        ]

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def authenticate(self, user_id, password):
        user = self.get_user_by_id(user_id)
        if user and user.password == password:
            return user
        return None
