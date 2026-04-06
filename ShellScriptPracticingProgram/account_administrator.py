# account_administrator

import sqlite3

class DatabaseAdministrator :
    def __init__(self, DB_NAME = 'accounts.db') :
        print("DB Access Approved")
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_table()
        self.insert_admin()

    def create_table(self) :
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_admin(self) :
        default_admin = ("admin", "1234")
        try :
            self.cursor.execute("INSERT INTO accounts (account_id, password) VALUES (?, ?)", default_admin)
            self.conn.commit()
        except sqlite3.IntegrityError :
            pass

    def check_credentials(self, user_id, password) :
        if not user_id or not password :
            return False  # 빈 값이면 무조건 False
        try :
            self.cursor.execute("SELECT * FROM accounts WHERE account_id = ? AND password = ?", (user_id, password))
            return self.cursor.fetchone() is not None
        except sqlite3.Error as e :
            print(f"[DB Error] {e}")
            return False

    def create_account(self, user_id, password) :
        try :
            self.cursor.execute("INSERT INTO accounts (account_id, password) VALUES (?, ?)", (user_id, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError :
            return False

    def close(self) :
        self.conn.close()

if __name__ == "__main__" :
    dba = DatabaseAdministrator()
    dba.close()
