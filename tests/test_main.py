import pytest
import logging
from kivy.clock import Clock
from app.main import MyApp

@pytest.fixture
def app():
    return MyApp()

def test_label_text(app):
    app.build()
    assert app.title == 'What\'s This?', "App name does not match 'What\'s This?'"
