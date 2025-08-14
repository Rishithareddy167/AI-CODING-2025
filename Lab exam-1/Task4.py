def generate_email_ids(names):
    emails = []
    for name in names:
        parts = name.strip().split()
        if len(parts) < 2:
            continue  # Skip if not enough parts
        first_letter = parts[0][0].lower()
        last_name = parts[-1].lower()
        email = f"{first_letter}{last_name}@sru.edu.in"
        emails.append(email)
    return emails

# Example usage:
student_names = ["Anita Sharma", "Rahul Verma", "Priya Singh"]
email_ids = generate_email_ids(student_names)
for email in email_ids:
    print(email)