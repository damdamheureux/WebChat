from dotenv import load_dotenv
from os import environ as varenv
load_dotenv(".env")
from backend import create_app
from backend.utils.db import ma_ptn_de_db
print(ma_ptn_de_db)
from backend.routers.websocket import router as websocket_routes
from backend.routers import auth as auth_router
from backend.routers.rooms import rooms_router
app = create_app()

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(websocket_routes, prefix="/ws", tags=["ws"])
app.include_router(rooms_router, prefix="/rooms", tags=["rooms"])