import mysql.connector


def signup(cursor):
    username = input("User Name: ")
    # print(username)
    
    cursor.execute(f"""SELECT username from usercred where username='{username}'""")
    user = cursor.fetchone()
    print(user)
    if user == None:
        password = input("Password: ")
        # print(password)
        # print(f"INSERT INTO usercred (username,password) VALUES ('{username}','{password}')")
        cursor.execute(f"""INSERT INTO usercred (username,password) VALUES ('{username}','{password}')""")
        # cursor.commit()
        signin(cursor)
    else:
        print('username already exists, enter different username')
        signup(cursor)


def signin(cursor):
    username = input("User Name: ")
    # credential = {'username':username, 'password':password}
    cursor.execute(f"SELECT username from usercred where username='{username}'")
    user = cursor.fetchone()
    if user == None:
        print("User does not exists. Enter correct details")
        signin(cursor)
    else:
        password = input("Password: ")
        cursor.execute(f"SELECT password from usercred where username='{username}'")
        pwd_in_db = cursor.fetchone()
        if pwd_in_db[0] == password:
            print("Login Success")
        else:
            print('Login Failed. Enter correct details')





conn=mysql.connector.connect(host="localhost", user="root", password="admin", database = "softmania")
conn.autocommit = True
print(conn)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usercred(username VARCHAR(64) PRIMARY KEY, password VARCHAR(64))")
login_method = input("Enter Login method(Sign in or Sign up: )")

if login_method.lower() == "sign up":
    signup(cursor)

if login_method.lower() == "sign in":
    signin(cursor)