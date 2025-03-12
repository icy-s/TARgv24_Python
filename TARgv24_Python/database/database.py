import select
from sqlite3 import *
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection=connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"'Tekkis viga'{e}'")
    return connection

conn=create_connection("C:/Users/xicey/source/repos/icy-s/TARgv24_Python/TARgv24_Python/database/data.db")

def execute_query(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Taabel on loodud")
    except Error as e:
        print(f"Viga '{e}' tabeli loomisega")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
nationality TEXT
);
"""

create_gender_table = """
CREATE TABLE IF NOT EXISTS gender(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Nimetus TEXT NOT NULL)
"""

insert_gender="""
INSERT INTO
gender(Nimetus)
VALUES
('🐀'),
('🐍');
"""

create_users_table2 = """
CREATE TABLE IF NOT EXISTS users2 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lname TEXT NOT NULL,
age INTEGER NOT NULL,
GenderId INTEGER,
FOREIGN KEY (GenderId) REFERENCES gender (Id)
);
"""

insert_users2="""
INSERT INTO
users2 (Name, Lname, Age, GenderId)
VALUES
('Mati', 'Tamm', 50, 1),
('Kati', 'Kask', 54, 2),
('Margus', 'Tamm', 12, 1),
('Anna', 'Kuusk', 44, 2);
"""

#execute_query(conn,insert_users2)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}'")

create_users = """
INSERT INTO
users (name, age, gender, nationality)
VALUES
('Mati', 25, 'mees', 'USA'),
('Lidia', 32, 'naine', 'France'),
('Brigitte', 35, 'naine', 'England'),
('Mike', 40, 'mees', 'Denmark'),
('Elizabeth', 21, 'naine', 'Eesti');
"""

#execute_query(conn, create_users)

select_users2 = "SELECT * from users2"
user = execute_read_query(conn, select_users2)
print("Kasutajate tabel 1:")
for user in select_users2:
    print(user)

select_users2_gender = "SELECT * from gender"
gender_table = execute_read_query(conn, select_users2_gender)
print("Kasutajate tabel 2:")
for gender_table in select_users2_gender:
    print(gender_table)

#select_users_gender="""
#SELECT
#users2.Name,
#users2.Lname,
#gender.Nimetus
#from users2
#INNER JOIN gender ON users2.GenderId=gender.Id"""

#users = execute_read_query(conn, select_users)
#for user in users:
#    print(user)







def add_users_query(connection,user_data):
    query="INSERT INTO users(name,age,gender,nationality) VALUES("+user_data+")"
    execute_query(connection,query)

#insert_user="'"+input("Nimi: ")+"','"+input("Vanus: ")+"','"+input("Sugu: ")+"','"+input("Riik: ")+"'"
#add_users_query(conn,insert_user)

def add_users_query_2(connection,user_data):
    """Lisame userit, mis on eraldi sisestatud
    """
    query="INSERT INTO users(name,age,gender,nationality) VALUES(?,?,?,?)"
    cursor=connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

#insert_user=(input("Nimi: "),int(input("Vanus: ")),input("Sugu: "),input("Riik: "))
#print(insert_user)
#add_users_query_2(conn,insert_user)

def delete_data_from_tabel(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Andmed on kustutatud")
    except Error as e:
        print(f"Viga '{e}' andmete kustutamisega")

#print("Andmete kustutame tabelist 'users'")
#delete_data_from_users="DELETE FROM users WHERE age<30"
#delete_data_from_tabel(conn,delete_data_from_users)
#print("Tabelis 'users' on jäänud neid, kes vanem kui 30:")
#users = execute_read_query(conn,select_users)

#for user in users:
 #   print(user)