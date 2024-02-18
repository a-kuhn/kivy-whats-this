from app.models.user import User
from app.services.user_service import UserService


class UserController:
    def __init__(self, view):
        self.view = view
        self.service = UserService()

    def show_user(self, user_id):
        user = self.service.get_user_by_id(user_id)
        if user:
            self.view.display_user(user)
        else:
            print("User not found.")

    def authenticate_user(self, user_id, password):
        user = self.service.authenticate(user_id, password)
        if user:
            print("Login successful!")
            # Proceed to the main part of the application
        else:
            print("Login failed. Please check your credentials.")
