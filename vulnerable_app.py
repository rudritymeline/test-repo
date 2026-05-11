# import sqlite3
# import hashlib
# import os

# # 1. SECURITY HOTSPOT: Hardcoded secret
# # This will show up in the "Hotspots" tab.
# DB_PASSWORD = "admin_password_123"

# def get_user_details(event_params):
#     """
#     This function simulates taking data from a web request (event_params)
#     and passing it directly to a database.
#     """
#     db = sqlite3.connect("users.db")
#     cursor = db.cursor()

#     # 2. CRITICAL VULNERABILITY: SQL Injection
#     # By using string concatenation with a variable that looks like 'user input',
#     # SonarQube's Taint Analysis will trigger a 'Critical' issue.
#     username = event_params.get("username")
#     query = "SELECT * FROM users WHERE username = '" + username + "';"
    
#     # The 'Issue' will be flagged here:
#     cursor.execute(query)
#     return cursor.fetchone()

# def create_password_hash(password):
#     # 3. SECURITY HOTSPOT: Weak Hashing
#     # MD5 is deprecated for security-sensitive data.
#     return hashlib.md5(password.encode()).hexdigest()

# def execute_system_command(user_input):
#     # 4. CRITICAL VULNERABILITY: OS Command Injection
#     # If an attacker passes '; rm -rf /', this would be disastrous.
#     # SonarQube will flag this as a critical vulnerability.
#     os.system("echo " + user_input)

# if __name__ == "__main__":
#     # Simulated untrusted input
#     mock_request = {"username": "admin' OR '1'='1"}
    
#     print("Fetching user...")
#     user = get_user_details(mock_request)
    
#     print("Hashing admin password...")
#     print(create_password_hash(DB_PASSWORD))


import os
import subprocess
import crypt
import flask

app = flask.Flask(__name__)

# 1. CRITICAL ISSUE: Hardcoded Password
# SonarQube will flag this as a 'Critical' security hotspot/issue.
DATABASE_PASSWORD = "Password123!" 

@app.route('/run-command')
def run_command():
    # 2. MAJOR ISSUE: Use of unsafe 'os.system'
    # The free tier identifies this as a 'Code Smell' or 'Security Hotspot' 
    # because it is an inherently dangerous function.
    user_cmd = flask.request.args.get("cmd")
    os.system(f"echo {user_cmd}") 

    # 3. MAJOR ISSUE: Use of 'subprocess' with shell=True
    # This is a classic "Security Blocker" for Python applications.
    subprocess.call(f"ls {user_cmd}", shell=True)

    return "Command executed"

def insecure_crypto():
    # 4. MAJOR ISSUE: Using DES (Weak Cryptography)
    # The free tier catches this because the 'crypt' module usage 
    # with certain salts is a known vulnerability.
    weak_hash = crypt.crypt("mypassword", "aa")
    return weak_hash

# 5. CODE SMELL: Debug mode enabled
# This is a high-confidence security risk for web apps.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")