import sqlite3


def login(username, password):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Insecure SQL query
    query = (
        "SELECT * FROM users WHERE "
        "username='%s' AND password='%s'"
        % (username, password)
    )

    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        print("Login Successful!")
    else:
        print("Invalid Username or Password")

    conn.close()


# Test login
login("admin", "admin123")