from mysql.connector import Error, pooling
import time
from os import environ as varenv
import ast
import json
import datetime

class User:
    def __init__(self,firstname=None, name=None,id=None, email=None, group=None):
        self.firstname = firstname
        self.name = name
        self.id = id
        self.email = email
        self.group = group
    
    def complete_name(self):
        return " ".join([self.firstname, self.name])
    def load_user(self, id):
        d = get_db_instance().execute_query("SELECT prenom, nom, email, `group` FROM `users` WHERE id = %s;", (id,))[0]
        self.firstname = d[0]
        self.name = d[1]
        self.email= d[2]
        self.group = d[3]
        self.id = id
        return self
    
class Message:
    def __init__(self, content, author:User, timestamp, id):
        self.content = content
        self.author:User = author
        self.timestamp:datetime.datetime = timestamp
        self.id = id
    def __repr__(self):
        return "A message sent by "+ self.author.complete_name() + " w content "+self.content+" at date "+self.timestamp.strftime("%d/%m/%Y - %H:%M:%S")
    


class MySQLDatabase:
    def __init__(self, host, user, password, database, port, pool_size=5, max_retries=3, retry_delay=5):
        self.db_config = {
            "host": host,
            "user": user,
            "port": port,
            "password": password,
            "database": database,
        }
        self.pool_size = pool_size
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.pool = None
        self.initialize_db()
    
    def initialize_db(self):
        """Initialize the connection pool."""
        try:
            self.pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=self.pool_size, **self.db_config)
            print("Database pool initialized successfully.")
        except Error as e:
            print(f"Error initializing database pool: {e}")
    
    def get_connection(self):
        """Retrieve a connection from the pool, with automatic reconnection on failure."""
        retries = 0
        while retries < self.max_retries:
            try:
                connection = self.pool.get_connection()
                if connection.is_connected():
                    return connection
            except Error as e:
                print(f"Connection attempt {retries + 1} failed: {e}")
                retries += 1
                time.sleep(self.retry_delay)
        raise Exception("Failed to connect to MySQL after multiple attempts")
    def execute_query(self, query, params=None):
        """Execute a query with automatic reconnection handling."""
        connection = None
        cursor = None
        try:
            connection = self.get_connection()
            cursor = connection.cursor(buffered=True)
            cursor.execute(query, params or ())
            connection.commit()
    
            if cursor.description:  # Query returns data (SELECT)
                return cursor.fetchall()
            elif query.strip().upper().startswith("INSERT"):  # Query is an INSERT
                return cursor.lastrowid  # Return last inserted ID
            else:
                return None  # For UPDATE/DELETE, return nothing
        except Error as e:
            print(f"MySQL Error: {e}")
            if e.errno in [2006, 2013, 2055]:  # Lost connection, timeout, etc.
                print("Reconnecting to MySQL...")
                return self.execute_query(query, params)  # Retry execution
            else:
                raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_rooms(self, user_id, room_id=None):
        assert isinstance(user_id, int) and user_id > 0 # Ensure user_id is a positive integer
        print(room_id)
        rmes = {}
        if not room_id:
            rooms = self.execute_query("SELECT * FROM roomusers WHERE userid = %s", (user_id,))

            for room in rooms:
                print(room)
                room_name = self.execute_query("SELECT roomname FROM `rooms` WHERE roomid = %s", (room[1],))
                print(room_name)
                room_mess = self.execute_query("SELECT author,body,timestamp, id FROM messages WHERE roomid = %s", (room[1],))
                rmes2 = [Message(content=mdata[1], author=User().load_user(id=mdata[0]), timestamp=mdata[2], id=mdata[3]) for mdata in room_mess]
                print(rmes2)
                rmes[room_name[0][0] + " - "+ str(room[1])] = rmes2
            return rmes
        else:
            room = self.execute_query("SELECT * FROM roomusers WHERE userid = %s AND roomid = %s", (user_id, room_id))
            if len(room) <= 0:
                return {"error": "user is not part of the room"}
            # print(room)
            room_name = self.execute_query("SELECT roomname FROM `rooms` WHERE roomid = %s", (room_id,))[0]
            room_mess = self.execute_query("SELECT author,body,timestamp,id FROM messages WHERE roomid = %s", (room_id,))
            rmes2 = [Message(content=mdata[1], author=User().load_user(id=mdata[0]), timestamp=mdata[2], id=mdata[3]) for mdata in room_mess]
            rmes["room"] = rmes2
            return rmes
    def close_pool(self):
        """Close all connections in the pool."""
        if self.pool:
            self.pool._remove_connections()
            print("Database pool closed.")

def create_db(host: str, user: str, password: str, database: str, port: int):
    retry_count = 0
    max_retries = 5
    db = None
    while retry_count < max_retries:
        try:
            db = MySQLDatabase(host = host,user=user,password=password,database=database,port=port)
            if db.pool is not None and db.pool.get_connection().is_connected():
                print("Connected to the SQL Pool.")
                break
        except Exception as e:
            print(f"Connection attempt {retry_count + 1} failed: {e}")
        retry_count += 1
        print("Retrying connection...")
        time.sleep(2)
    if db is None:
        raise Exception("Failed to connect to the database after multiple attempts.")
    return db

ma_ptn_de_db = create_db(
        host=varenv.get("DB_HOST"),
        user=varenv.get("DB_USER"),
        password=varenv.get("DB_PASSWORD"),
        database=varenv.get("DB_NAME"),
        port=int(varenv.get("DB_PORT"))
)


def get_db_instance():
    return ma_ptn_de_db