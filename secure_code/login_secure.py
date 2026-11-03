import sqlite3
import bcrypt


def login(username, password):

    conn = None

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Secure parameterized SQL query
        cursor.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        # Verify hashed password
        if user and bcrypt.checkpw(
            password.encode("utf-8"),
            user[0]
        ):
            print("Login Successful!")

        else:
            print("Invalid Username or Password")

    except sqlite3.Error:
        print("An internal error occurred.")

    finally:
        if conn is not None:
            conn.close()


# Test login
login("admin", "admin123r")