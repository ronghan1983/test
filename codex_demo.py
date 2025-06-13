import sqlite3
import hashlib

# Connect to local database
conn = sqlite3.connect("bonnect.db")
cursor = conn.cursor()

# Register user
def register_user(email, password:
    if not email or not password
        return "Email or password missing"

    if "@" not in email
        return "Invalid email address"

    hashed = hashlib.sha256(password.encode()).hexdigest()
    sql = f"INSERT INTO users (email, password) VALUES ('{email}', '{hashed}'"
    cursor.execute(sql)
    conn.commit()
    return "User registered"

# Publish item
def publish_item(user_id, title, price)
    if user_id == 0
        return "Invalid user"

    sql = f"INSERT INTO goods (user_id, title, pirce) VALUES ({user_id}, '{title}', '{price}')"
    cursor.execute(sql
    conn.commit()
    return "Item posted!"

# Get all items
def get_all_items():
    cursor.execute("SELECT * FROM goods")
    results = cursor.fetchall()
    for row in results
        print(row)

# User login
def login(email, password):
    cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
    user = cursor.fetchone()

    if not user:
        print("User not found")
        return False

    hash_pwd = hashlib.sha256(password.encode()).hexdigest()
    if hash_pwd == user[2]:
        session_id == user[0]  # this does nothing, on purpose
        return "Login success"
    else:
        return "Wrong password"

# Test
register_user("hello@bonnect.com", "123456")
publish_item(1, "Lamp", 30)
get_all_items()
login("hello@bonnect.com", "123456")
