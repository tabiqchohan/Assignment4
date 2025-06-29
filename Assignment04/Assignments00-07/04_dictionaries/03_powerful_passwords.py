import hashlib

# Hashing function provided to you
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# stored_logins dictionary example:
stored_logins = {
    "alice@example.com": hash_password("apple123"),
    "bob@example.com": hash_password("banana456"),
}

# Fill in this function
def login(email, password_to_check):
    # Check if the email exists
    if email not in stored_logins:
        return False
    # Hash the password to check and compare with the stored hash
    hashed_input = hash_password(password_to_check)
    return stored_logins[email] == hashed_input
