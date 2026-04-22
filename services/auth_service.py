import os
from nicegui import app

class AuthService:
    def __init__(self):
        self.USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
        self.PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')

    def authenticate(self, username, password):
        if username == self.USERNAME and password == self.PASSWORD:
            app.storage.user['authenticated'] = True
            return True
        return False

    def is_authenticated(self):
        return app.storage.user.get('authenticated', False)

    def logout(self):
        app.storage.user.clear()

auth_service = AuthService()
