# create_admin.py

import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

try:
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("admin", "admin123", "admin")
    )
    conn.commit()
    print("Admin created ✅")
except:
    print("Admin already exists")

conn.close()