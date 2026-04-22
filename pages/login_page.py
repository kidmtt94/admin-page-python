from nicegui import ui
from fastapi.responses import RedirectResponse
from services.auth_service import auth_service

def create_login_page():
    @ui.page('/admin')
    def login_page():
        # If already logged in, go straight to dashboard
        if auth_service.is_authenticated():
            return RedirectResponse('/dashboard')

        def try_login() -> None:
            if auth_service.authenticate(username.value, password.value):
                ui.navigate.to('/dashboard')
            else:
                ui.notify('Wrong username or password', color='negative')

        with ui.column().classes('w-full h-screen items-center justify-center bg-gray-100'):
            with ui.card().classes('w-96 p-8 shadow-md'):
                ui.label('Login Form').classes('text-3xl font-bold self-center mb-6')
                
                ui.label('Username:').classes('font-bold')
                username = ui.input(placeholder='Enter your username').classes('w-full mb-4')
                
                ui.label('Password:').classes('font-bold')
                password = ui.input(placeholder='Enter your password', password=True).classes('w-full mb-4').on('keydown.enter', try_login)
                                
                ui.button('Login', on_click=try_login).classes('w-full bg-blue-500 text-white')

