import mysql.connector
from starlette.responses import RedirectResponse
from fastapi.responses import JSONResponse
from fastapi import Form, Cookie, APIRouter, Request, Path, HTTPException, Query
from typing import Annotated
import jwt
import time
from datetime import datetime
import os
from backend.utils.db import get_db_instance, User
from backend.utils.decoder import decode_token
from backend.routers.websocket import cm
import datetime
from ..utils.decoder import decode_token
rooms_router = APIRouter()

secret_key_router = os.getenv("PRIVATE_fastapi_token")

db = get_db_instance()

@rooms_router.get("/create_room")
async def create_room(request: Request, roomname: Annotated[str | None, Query()], authtoken: Annotated[str | None, Cookie()] = None):
    if authtoken is None:
        raise HTTPException(401, "Token not passed")
    if not roomname:
        raise HTTPException(400, "Bah la ca marche pas y'a pas la roomname")
    try:
        userid = decode_token(authtoken)
    except:
        return JSONResponse(content={"non": "non ca marche pas"})

    roomid = db.execute_query("INSERT INTO rooms (roomname, creatorID) VALUES (%s,%s)", (roomname,userid["user_id"]))
    db.execute_query("INSERT INTO roomusers (userid, roomID) VALUES (%s, %s)", (userid['user_id'], roomid))
    db.execute_query("INSERT INTO roomusers (userid, roomID) VALUES (%s, %s)", (99, roomid)) # Le compte admin  !
    return JSONResponse(content={"room_id": roomid}, status_code=200)

@rooms_router.get("/leave_room")
async def leave_room(request: Request, roomid: Annotated[str |  None, Query()] = None, authtoken: Annotated[str | None, Cookie()] = None):
    if authtoken is None:
        raise HTTPException(401, "Not authenticated")
    if roomid is None:
        raise HTTPException(400, "Roomname n'est pas présent (bad req)")
    uid = decode_token(authtoken)["user_id"]
    db.execute_query("DELETE FROM `roomusers` WHERE roomID = %s AND userid = %s", (roomid,uid))
    return JSONResponse(content={"success": "ok"}, status_code=200)

@rooms_router.get("/join_room")
async def leave_room(request: Request, roomid: Annotated[int |  None, Query()] = None, authtoken: Annotated[str | None, Cookie()] = None):
    if authtoken is None:
        raise HTTPException(401, "Not authenticated")
    if roomid is None:
        return JSONResponse(content={"error": "Room not valid"}, status_code=400)
    if len(db.execute_query("SELECT * FROM `rooms` WHERE roomid = %s;", (roomid,))) != 1:
        return JSONResponse(content={"error": "Room not found"}, status_code=404)
    uid = decode_token(authtoken)["user_id"]
    db.execute_query("INSERT INTO `roomusers` (roomID, userid) VALUES (%s, %s)", (roomid,uid))
    return JSONResponse(content={"success": "ok", "roomid": roomid}, status_code=200)


@rooms_router.get("/getrooms")
async def get_rooms(request: Request, authtoken: Annotated[str | None, Cookie()] = None):
    if not authtoken:
        return RedirectResponse(url="/auth/login")
    data = db.get_rooms(decode_token(authtoken)["user_id"])
    return JSONResponse(content={"rooms": list(data.keys())}, status_code=200)


@rooms_router.get("/{room_id}/messages")
async def get_rooms(request: Request, room_id: Annotated[str | None, Path()], authtoken: Annotated[str | None, Cookie()] = None):
    print(request.cookies)
    if not authtoken:
        return RedirectResponse(url="/auth/login")
    data = db.get_rooms(decode_token(authtoken)["user_id"], room_id)
    current_user = User().load_user(id=decode_token(authtoken)["user_id"])
    if current_user and current_user.group == "admin":
        data["isAdmin"] = "admin"
    return data

@rooms_router.get("/{room_id}/sendmessage")
async def sendmessagetoroom(request: Request, room_id: Annotated[str | None, Path()], content: Annotated[str | None, Query()], authtoken: Annotated[str | None, Cookie()] = None):
    if authtoken is None:
        raise HTTPException(401, "Token not passed")
    uid = decode_token(authtoken)
    uid:int = uid["user_id"]
    if content.startswith("/") and User().load_user(uid).group == "admin":
        if content.split("/")[1].split(" ")[0] == "dmsg":
            db.execute_query("DELETE FROM `messages` WHERE id = %s", (content.split("/")[1].split(" ")[1],))
            return await cm.emit_event("server:UpdateDB")
        elif content.split("/")[1].split(" ")[0] == "sysmsg":
            db.execute_query("INSERT INTO messages (author, body, timestamp, roomID) VALUES (%s, %s, %s, %s)", (99, " ".join(content.split("/")[1].split(" ")[1:]), datetime.datetime.now(), room_id))
            return await cm.emit_event("server:UpdateDB")
        elif content.split("/")[1].split(" ")[0] == "kick":
            db.execute_query("DELETE FROM `roomusers` WHERE roomID = %s AND userid = %s", (room_id, content.split("/")[1].split(" ")[1]))
            return await cm.emit_event("server:UpdateDB")
    if len(db.execute_query("SELECT users.id FROM users JOIN roomusers ON roomusers.userid = users.id WHERE userid = %s AND roomID = %s;", (uid, room_id))) > 0:
        db.execute_query("INSERT INTO messages (author, body, timestamp, roomID) VALUES (%s, %s, %s, %s)", (uid, content, datetime.datetime.now(), room_id))
        await cm.emit_event("server:UpdateDB")
    else:
        raise HTTPException(401, "Unauthorized")
