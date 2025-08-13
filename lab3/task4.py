user_db = {}

def register_user(username, password):
    if username in user_db:
        return "Username already exists."
    user_db[username] = password
    return "User registered successfully."

def login_user(username, password):
    if username not in user_db:
        return "User not found."
    if user_db[username] == password:
        return "Login successful."
    return "Invalid password."

# Example usage
print(register_user("alice", "password123"))  # User registered successfully.
print(register_user("alice", "newpass"))      # Username already exists.
print(login_user("alice", "password123"))     # Login successful.
print(login_user("alice", "wrongpass"))       # Invalid password.
print(login_user("bob", "12345"))             # User not found.
