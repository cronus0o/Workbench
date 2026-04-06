import sqlite3
import json
import pandas
import matplotlib.pyplot as plt

class DatabaseAdministrator :
    def __init__(self, DB_NAME = 'shopDatabase.db') :
        print("DB Access Approved")
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_tables()

    # Checking DB Status when Running Program
    def create_tables(self) :
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS shopList (
                shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
                shop_name TEXT NOT NULL UNIQUE,
                location TEXT NOT NULL UNIQUE
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS menuList (
                menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
                shop_id INTEGER NOT NULL,
                menu_name TEXT NOT NULL,
                FOREIGN KEY (shop_id) REFERENCES shopList (shop_id)
            )
        """)
        self.conn.commit()

    # Insert Data into DB
    def insert_data(self, json_path) :
        with open(json_path, 'r', encoding = 'utf-8') as f :
            data = json.load(f)


# -----------------------------------------------------------------------------------------------------------------------------
        # Determine by .json Data Sturcture
        for shop in data :
            name = shop["name"]
            location = shop["location"]
            menus = shop.get("menu", [])

            self.cursor.execute("SELECT shop_id FROM shopList WHERE shop_name = ? AND location = ?", (name, location))
            res = self.cursor.fetchone()

            if res :
                shop_id = res[0]
            else :
                self.cursor.execute("INSERT INTO shopList (shop_name, location) VALUES (?, ?)", (name, location))
                shop_id = self.cursor.lastrowid

            for menu in menus:
                self.cursor.execute("SELECT menu_id FROM menuList WHERE shop_id = ? AND menu_name = ?", (shop_id, menu))
                if not self.cursor.fetchone():
                    self.cursor.execute("INSERT INTO menuList (shop_id, menu_name) VALUES (?, ?)", (shop_id, menu))
        self.conn.commit()
# ------------------------------------------------------------------------------------------------------------------------------


    # Other Functions
    def get_shops(self) :
        self.cursor.execute("SELECT * FROM shopList")
        return self.cursor.fetchall()

    def get_menu(self, shop_id) :
        self.cursor.execute("SELECT menu_name FROM menuList WHERE shop_id = ?", (shop_id,))
        return [row[0] for row in self.cursor.fetchall()]

    def update_shop_location(self, shop_name, new_location) :
        self.cursor.execute("UPDATE shopList SET location = ? WHERE shop_name = ?", (new_location, shop_name))
        self.conn.commit()

    def delete_shop(self, shop_name) :
        self.cursor.execute("SELECT shop_id FROM shopList WHERE shop_name = ?", (shop_name,))
        res = self.cursor.fetchone()
        if res :
            shop_id = res[0]
            self.cursor.execute("DELETE FROM menuList WHERE shop_id = ?", (shop_id,))
            self.cursor.execute("DELETE FROM shopList WHERE shop_id = ?", (shop_id,))
            self.conn.commit()


# ---------------------------------------------------------------------------------------------------------------------
    # Determine by .json Data Sturcture
    # Group (Category)
    def visualize_shops(self):
        df = pandas.read_sql_query("SELECT * FROM shopList", self.conn)
        print("SHOP LIST")
        print(df)

        # 예시 차트 (가게 수 분포)
        plt.bar(df['shop_name'], [1] * len(df))  # 가게당 1개씩
        plt.xticks(rotation=45, ha='right')
        plt.title("Shops in DB")
        plt.tight_layout()
        plt.show()

    def close(self):
        self.conn.close()
# ---------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__" :
    print("DBA Testing")

    # .db filename Parameter
    # default = 'shopDatabase.db'
    dba = DatabaseAdministrator()
    dba.create_tables()

    # Path/filename.json
    dba.insert_data("scraped.json")


    # dba.visualize_shops()



# json()	문자열을 JSON으로 파싱함
# json_object(k1, v1, ...)	키-값 쌍으로 JSON 객체 생성
# json_array(v1, v2, ...)	값들로 JSON 배열 생성
# json_extract(json, path)	경로에 있는 값을 추출
# json_set(json, path, value)	지정 경로에 값 설정 (있으면 덮어씀)
# json_insert(json, path, value)	경로가 없을 경우만 값 추가
# json_replace(json, path, value)	경로가 있을 경우만 값 변경
# json_remove(json, path)	경로에 있는 값 삭제
# json_type(json, path)	경로에 있는 값의 JSON 타입 반환
# json_valid(json)	유효한 JSON인지 확인 (1 또는 0)
# json_each(json)	JSON 객체의 각 요소를 행으로 나눔 (virtual table)

# cursor.execute()
# cursor.executemany()

# cursor.execute("INSERT INTO shopList (shop_id, shop_name, location) VALUES (?, ?, ?)", (4, "IndiaFood", ddd-ddd))
# cursor.execute("SELECT shop_name FROM shopList WHERE")
# cursor.execute("UPDATE shopList SET location = ? WHERE shop_name = ?", (, ))
# cursor.execute("DELETE FROM shopList WHERE shop_name = ?", ("", ))
