from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.app import App
import logging


class LoginScreen(BoxLayout):
    user_id_input = NumericProperty()
    password_input = StringProperty()

    def login(self, user_id, password):
        app = App.get_running_app()
        logging.debug(f"login_view.login: {app.title}")
        app.controller.authenticate_user(user_id, password)
        logging.debug(f"authenicating user from inputs: {user_id, password}")
