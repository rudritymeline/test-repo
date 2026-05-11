import sqlite3
import hashlib
import os

# 1. SECURITY HOTSPOT: Hardcoded secret
# This will show up in the "Hotspots" tab.
DB_PASSWORD = "admin_password_123"

def get_user_details(event_params):
    """
    This function simulates taking data from a web request (event_params)
    and passing it directly to a database.
    """
    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    # 2. CRITICAL VULNERABILITY: SQL Injection
    # By using string concatenation with a variable that looks like 'user input',
    # SonarQube's Taint Analysis will trigger a 'Critical' issue.
    username = event_params.get("username")
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    
    # The 'Issue' will be flagged here:
    cursor.execute(query)
    return cursor.fetchone()

def create_password_hash(password):
    # 3. SECURITY HOTSPOT: Weak Hashing
    # MD5 is deprecated for security-sensitive data.
    return hashlib.md5(password.encode()).hexdigest()

def execute_system_command(user_input):
    # 4. CRITICAL VULNERABILITY: OS Command Injection
    # If an attacker passes '; rm -rf /', this would be disastrous.
    # SonarQube will flag this as a critical vulnerability.
    os.system("echo " + user_input)

if __name__ == "__main__":
    # Simulated untrusted input
    mock_request = {"username": "admin' OR '1'='1"}
    
    print("Fetching user...")
    user = get_user_details(mock_request)
    
    print("Hashing admin password...")
    print(create_password_hash(DB_PASSWORD))