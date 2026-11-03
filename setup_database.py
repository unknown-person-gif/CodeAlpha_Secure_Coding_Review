import sqlite3
import bcrypt

# Connect to SQLite database
conn = sqlite3.connect("users.db")

cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash BLOB NOT NULL
)
""")

# Create test password
password = "admin123".encode("utf-8")

# Generate secure password hash
hashed_password = bcrypt.hashpw(
    password,
    bcrypt.gensalt()
)

# Insert test user into database
cursor.execute(
    """
    INSERT OR IGNORE INTO users (username, password_hash)
    VALUES (?, ?)
    """,
    ("admin", hashed_password)
)

# Save changes
conn.commit()

# Close database connection
conn.close()

print("Test database created successfully!")
print("Test user added successfully!")