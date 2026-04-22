from nicegui import ui
from fastapi.responses import RedirectResponse
from services.auth_service import auth_service

def create_dashboard_page():
    @ui.page('/dashboard')
    def dashboard():
        if not auth_service.is_authenticated():
            return RedirectResponse('/admin')

        def logout():
            auth_service.logout()
            ui.navigate.to('/admin')

        with ui.column().classes('absolute-center items-center'):
            ui.label('Welcome to the Dashboard!').classes('text-2xl')
            ui.button('Log out', on_click=logout)
