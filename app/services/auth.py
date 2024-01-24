from app.repositories.users import get_user_by_email

import bcrypt

def verify_user(email: str, password: str) -> dict:
    try:
        # Find user by email
        user = get_user_by_email(email)
        if not user:
            raise Exception("User not found")

        # Compare password hashes
        password_valid = bcrypt.checkpw(password.encode("utf-8"), user['password'].encode("utf-8"))
        if not password_valid:
            raise Exception("Invalid credentials")

        # Prepare user data for response
        user_data = user

        return user_data
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def register_user(username: str, email:str, password:str)->bool:
    try:
        pass
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise 