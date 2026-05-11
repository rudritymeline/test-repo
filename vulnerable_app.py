import sqlite3
import hashlib

# SECURITY HOTSPOT: Hardcoded secret/key
SECRET_KEY = "super-secret-key-12345"

def get_user_data(username):
    # VULNERABILITY: SQL Injection (Direct string formatting) so SonarQube should flag this as a critical vulnerability
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'" 
    cursor.execute(query)
    return cursor.fetchone()

def hash_password(password):
    # CODE SMELL: Using an insecure/deprecated hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    user = get_user_data("admin")
    print(f"User found: {user}")