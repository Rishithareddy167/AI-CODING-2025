import logging
import re
import sys

# Configure logging for the web application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def log_user_action(user_id, action, details=None):
    """
    Log user actions in the application.
    DO NOT log sensitive information such as passwords, emails, or personal identifiers.
    Only log non-sensitive, necessary details for debugging or auditing.
    """
    # Remove or mask any sensitive fields from details before logging
    if details and isinstance(details, dict):
        # Example: Remove sensitive keys if present
        sensitive_keys = {"password", "email", "ssn", "token"}
        sanitized_details = {k: ("***" if k in sensitive_keys else v) for k, v in details.items()}
    else:
        sanitized_details = details

    # Log the action with sanitized details
    logging.info(f"UserAction | user_id={user_id} | action={action} | details={sanitized_details}")

# Example usage in a web route handler (pseudo-code)
def login_route(request):
    # ... authentication logic ...
    # DO NOT log the password or email
    log_user_action(
        user_id="anonymous",  # Use a pseudonym or session id, not real user identifiers
        action="login_attempt",
        details={"ip": request.remote_addr}
    )
    # ... rest of the handler ...

# Ethical Logging Practices:
# - Never log sensitive user data (passwords, emails, tokens, personal identifiers).
# - Regularly review log files for accidental leaks of sensitive information.
# - Use pseudonyms or session IDs instead of real user IDs where possible.
# - Secure log files and restrict access to authorized personnel only.
# - Comply with privacy laws and organizational policies regarding data retention and logging.


def is_valid_email(email: str) -> bool:
    """
    Basic email format validation.
    """
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(email_pattern, email) is not None


def prompt_email_or_password() -> None:
    """
    Ask the user whether they want to enter an email or a password, then prompt accordingly.
    Sensitive inputs are not logged; only non-sensitive metadata is recorded.
    """
    try:
        while True:
            choice = input("Do you want to enter 'email' or 'password'? ").strip().lower()
            if choice in {"email", "mail"}:
                email = input("Enter email: ").strip()
                is_valid = is_valid_email(email)
                print("Email format looks valid." if is_valid else "Invalid email format.")
                # Log only non-sensitive metadata
                log_user_action(
                    user_id="anonymous",
                    action="email_input",
                    details={"input_type": "email", "valid": is_valid}
                )
                break
            elif choice in {"password", "pass", "pwd"}:
                # Use getpass to avoid echoing the password
                try:
                    import getpass
                    password = getpass.getpass("Enter password: ")
                except Exception:
                    # Fallback if getpass fails (rare on some terminals)
                    password = input("Enter password: ")

                is_strong_enough = len(password) >= 8
                print("Password received." + (" Consider using at least 8 characters." if not is_strong_enough else ""))
                # Log only non-sensitive metadata
                log_user_action(
                    user_id="anonymous",
                    action="password_input",
                    details={"input_type": "password", "strong_len": is_strong_enough}
                )
                break
            else:
                print("Please type 'email' or 'password'.")
    except KeyboardInterrupt:
        print("\nCancelled by user.")


if __name__ == "__main__":
    # If launched with an argument, allow quick non-interactive selection
    #   e.g., python task1.4.py email
    #         python task1.4.py password
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip().lower()
        if arg in {"email", "mail"}:
            # Simulate the same flow directly
            email = input("Enter email: ").strip()
            is_valid = is_valid_email(email)
            print("Email format looks valid." if is_valid else "Invalid email format.")
            log_user_action(
                user_id="anonymous",
                action="email_input",
                details={"input_type": "email", "valid": is_valid}
            )
        elif arg in {"password", "pass", "pwd"}:
            try:
                import getpass
                password = getpass.getpass("Enter password: ")
            except Exception:
                password = input("Enter password: ")
            is_strong_enough = len(password) >= 8
            print("Password received." + (" Consider using at least 8 characters." if not is_strong_enough else ""))
            log_user_action(
                user_id="anonymous",
                action="password_input",
                details={"input_type": "password", "strong_len": is_strong_enough}
            )
        else:
            print("Unknown argument. Starting interactive mode...\n")
            prompt_email_or_password()
    else:
        prompt_email_or_password()
