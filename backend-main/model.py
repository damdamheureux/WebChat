from .main import db
class User:
    def __init__(self, user_id=None, email=None):
        self.user_id = user_id
        self.email = email
        self.nom = None
        self.prenom = None
        self.ins_date = None
        self.group = None
        self.password = None
        if self.user_id or self.email:
            self.load_user()

    def load_user(self):
        """Load user data from the database based on user_id or email."""
        cursor = db.cursor()

        try:
            if self.user_id:
                cursor.execute("SELECT * FROM users WHERE id = %s", (self.user_id,))
            elif self.email:
                cursor.execute("SELECT * FROM users WHERE email = %s", (self.email,))
            user_data = cursor.fetchone()

            if user_data:
                self.user_id = user_data[0]
                self.nom = user_data[1]
                self.prenom = user_data[2]
                self.email = user_data[3]
                self.ins_date = user_data[4]
                self.group = user_data[5]
                self.password = user_data[6]
            else:
                print("User not found.")
        finally:
            print("User loaded", repr(self))

    def __repr__(self):
        return f"<User(user_id={self.user_id}, email='{self.email}', name='{self.nom}')>"
