from fastapi import WebSocket, APIRouter
from fastapi.websockets import WebSocketDisconnect
from fastapi import FastAPI, Cookie, Header, Query
from typing import Annotated
from json import dumps, loads
from ..utils.decoder import decode_token
from ..utils.db import get_db_instance
db = get_db_instance()


router = APIRouter()


class connectionManager:
    def __init__(self):
        self.active_connections:list[WebSocket] = []

    async def emit_event(self, event:str):
        for connection in self.active_connections:
            try:
                await connection.send_json({"event": event})
            except:
                pass
    def connect(self, websocket: WebSocket):
        self.active_connections.append(websocket)
    def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except:
            pass

cm = connectionManager()
@router.websocket("/keepalive")
async def websocket_endpoint(websocket: WebSocket, authtoken: Annotated[str | None, Query()] = None):
    await websocket.accept()
    if not authtoken:
        return await websocket.close(reason="Token non passé")
    cm.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text() # Ici on va juste dire qu'on est pret a recevoir n'importe quelle data, dans le rooms/sendmessage on a cm:emit_event pour signaler l'ajout de message !
    except WebSocketDisconnect:
        cm.disconnect(websocket)
# @router.websocket("/keepalive")
# async def websocket_endpoint(websocket: WebSocket, authtoken: Annotated[str | None, Query()] = None):
#     print("authtoken from websocket is", authtoken)
#     await websocket.accept()
#     if not authtoken:
#         print("CLOSING: TOKEN NON PASSE")
#         await websocket.close(reason="Token non passe")

#     token = decode_token(authtoken)

#     if not token: # A passer dans le try block
#         print("CLOSING: TOKEN INVALIDE")
#         await websocket.close(reason="Invalid token")
#         return
#     print("TOKEN TOUJOURS BON, ON CONTINUE")
#     cm.connect(websocket)
#     try:
#         while True:
#             print("WEBSOCKET BOUCLE")
#             data = await websocket.receive_text()
#             print("data received")
#             if data:
#                 print("emit")
#                 await cm.emit_event("updateDB")
#     except WebSocketDisconnect:
#         print("CLOSING: WEBSOCKET_DISCONNECT")
#         await websocket.close()
