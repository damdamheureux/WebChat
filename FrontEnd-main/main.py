import flask
from flask import request, abort, render_template, redirect, Response, make_response, send_file
from functools import wraps
import requests
from flask_cors import CORS
app = flask.Flask(__name__)
from os import environ

CORS(app)
# login verify
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "authtoken" not in request.cookies:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return redirect("/login")

@app.route("/static/loginbg.png")
def loginbg():
    return send_file("./static/PeacefulLake.webp")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/notverified")
def notverified():
    return "not verified page"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/account/verify")
def verify_account():
    return "verify account page"

@app.route("/rooms")
@login_required
def room():
    room = requests.get(f"{environ.get("API_URL")}/rooms/getrooms", cookies=request.cookies)
    if room.status_code == 401:
        return abort(401, "Invalid token")
    print(room.json())
    return render_template("rooms.html", rooms=room.json()["rooms"])

@app.route('/create_room', methods=["GET"])
def create_room():
    response = requests.get(f"{environ.get("API_URL")}/rooms/create_room", params=request.args, cookies=request.cookies)
    print(response.status_code)
    if response.status_code != 200:
        return abort(response.status_code)
    return {"room_id": response.json().get("room_id")}

@app.route("/leave_room", methods=["GET"])
@login_required
def leave_room():
    response = requests.get(f"{environ.get("API_URL")}/rooms/leave_room", params=request.args, cookies=request.cookies)
    print(response.status_code)
    if response.status_code != 200:
        return abort(response.status_code)
    return {"status": 'ok'}

@app.route("/join_room", methods=["GET"])
@login_required
def join_room():
    print("join room")
    response = requests.get(f"{environ.get("API_URL")}/rooms/join_room", params=request.args, cookies=request.cookies)
    if response.status_code != 200:
        print(response.status_code)
        return abort(response.status_code, response.text)
    print(response.json())
    return {"room_id": response.json().get("roomid")}

@app.route("/rooms/<room_id>")
@login_required
def room_show_id(room_id):
    messages_on_room = requests.get(f"{environ.get("API_URL")}/rooms/{room_id}/messages", cookies=request.cookies)
    print(messages_on_room.content)
    if "error" in messages_on_room.json():
        return redirect("/rooms") # Empeche de se login a une room qui est pas la sienne
    return render_template("messages.html", roomid=room_id, messages=messages_on_room.json()["room"], isAdmin = ("isAdmin" in messages_on_room.json()), wsurl = environ.get("WS_URL"))

@app.route("/transmitregister", methods=["GET"])
def transmitregister():
    response = requests.get(f"{environ.get("API_URL")}/auth/register", params=request.args, cookies=request.cookies)
    if response.status_code != 200:
        return abort(response.status_code, response.text)
    a = make_response(redirect("/rooms"))
    a.set_cookie("authtoken", response.cookies.get("authtoken"))
    return a

@app.route('/transmitlogin', methods=["GET"])
def transmit_login():
    response = requests.get(f"{environ.get("API_URL")}/auth/login", params=request.args, cookies=request.cookies)
    print(response.status_code)
    if response.status_code != 200:
        return abort(response.status_code, response.text)
    a = make_response(redirect("/rooms"))
    a.set_cookie("authtoken", response.cookies.get("authtoken"))
    return a

@app.route("/rooms/<room_id>/sendmessage", methods=["GET"])
def sendmessage(room_id):
    response = requests.get(f"{environ.get("API_URL")}/rooms/{room_id}/sendmessage", params=request.args, cookies=request.cookies)
    if response.status_code != 200:
        return abort(response.status_code, response.text)
    return redirect(f"/rooms/{room_id}")


if __name__ == '__main__':
    app.run(debug=True, port=40120, host="0.0.0.0", load_dotenv=True)