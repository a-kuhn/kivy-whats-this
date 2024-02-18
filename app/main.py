from kivy.app import App
from app.views.login_view import LoginScreen
from app.views.user_view import UserView
from app.controllers.user_controller import UserController


class MyApp(App):
    def build(self):
        self.title = "What's This?"
        self.controller = UserController(UserView())
        return LoginScreen()


if __name__ == "__main__":
    MyApp().run()
