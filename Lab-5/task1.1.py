# Python script to collect user data

def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    user_data = {
        "name": name,
        "age": age,
        "email": email
    }
    return user_data

def anonymize_user_data(user_data):
    # To anonymize user data:
    # - Do not store the real name; use a pseudonym or hash if needed
    # - Age can be stored as a range instead of exact value
    # - Email addresses should be hashed before storage to protect privacy

    import hashlib

    # Hash the email using SHA-256
    email_hash = hashlib.sha256(user_data["email"].encode()).hexdigest()

    # Replace name with a pseudonym (e.g., "User1")
    pseudonym = "User1"

    # Convert age to a range (e.g., 20-29, 30-39, etc.)
    try:
        age_int = int(user_data["age"])
        if age_int < 20:
            age_range = "<20"
        elif age_int < 30:
            age_range = "20-29"
        elif age_int < 40:
            age_range = "30-39"
        elif age_int < 50:
            age_range = "40-49"
        else:
            age_range = "50+"
    except ValueError:
        age_range = "Unknown"

    anonymized_data = {
        "name": pseudonym,
        "age_range": age_range,
        "email_hash": email_hash
    }
    return anonymized_data

if __name__ == "__main__":
    # Collect user data
    user_data = collect_user_data()
    print("Collected user data:", user_data)

    # Anonymize user data before storing or processing further
    anonymized = anonymize_user_data(user_data)
    print("Anonymized user data:", anonymized)

    # Note:
    # - Never store sensitive user data (like real names or emails) in plain text.
    # - Always use secure storage and consider encryption for any data at rest.
    # - Hashing emails helps protect user privacy in case of data breaches.
    # - Avoid collecting unnecessary personal information.
