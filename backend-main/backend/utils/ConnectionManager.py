from fastapi.websockets import WebSocket
from backend.utils.db import get_db_instance
db = get_db_instance()
# Websocket connection manager
class Room:
    def __init__(self, name, room_id, max_users,owner, verified=0, password=None):
        self.name = name
        self.room_id = room_id
        self.max_users = max_users
        self.owner = owner
        self.verified = verified
        self.password = password
        self.connected_users = []
        self.users = []
        self.messages = []
  
    def connect_to_room(self, websocket: WebSocket):
        self.connected_users.append(websocket)
        self.users.append(websocket.headers.get("user_id"))

    def disconnet_from_room(self, websocket: WebSocket):
        self.connected_users.remove(websocket)
        self.users.remove(websocket.headers.get("user_id"))
        

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
        self.rooms = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def join_room(self, room_id, websocket: WebSocket):
        for room in self.rooms:
            if room.room_id == room_id:
                room.connected_users.append(websocket)
                return room
        room = self.create_room("Ma chambre", room_id=room_id, max_users=-1, owner=websocket.headers.get("user_id"))
        room.connected_users.append(websocket)
        return room
    
    def create_room(self, name, room_id, max_users, owner, verified=0, password=None):
        room = Room(name, room_id, max_users, owner, verified, password)
        self.rooms.append(room)
        return room

    # async def connect(self, websocket: WebSocket, room_name:str):
    #     await websocket.accept()
    #     self.active_connections.append(websocket)
    #     self.add_to_channel(websocket, room_name)

    # def create_room(self):
    #     pass

    # def disconnect(self, websocket: WebSocket):
    #     self.active_connections.remove(websocket)
    
    # def add_to_channel(self, websocket: WebSocket, roomName:str):
    #     if not roomName in self.active_rooms:
    #         self.active_rooms[roomName] = []
    #     self.active_rooms[roomName].append(websocket)

    # async def send_personal_message(self, message: str, websocket: WebSocket):
    #     await websocket.send_text(message)

    # async def broadcast(self, message: str):
    #     for connection in self.active_connections:
    #         await connection.send_text(message)