import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from nicegui import ui

from pages.login_page import create_login_page
from pages.dashboard_page import create_dashboard_page
from services.auth_service import auth_service

app = FastAPI(title="My Main API Server")

# GET /hello endpoint
@app.get('/hello')
def hello():
    return {"message": "Hello, World!"}

create_login_page()
create_dashboard_page()

# Run nicegui with the custom FastAPI app
ui.run_with(app, storage_secret='super-secret-key-for-session')

if __name__ in {"__main__", "__mp_main__"}:
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
