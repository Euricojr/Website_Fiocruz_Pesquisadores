"""
create_admin.py - Interactive script to create the first admin user.
"""
import getpass
import sys
import os

# Add the current directory to path to ensure modules can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_db, create_user, get_user_by_email

def main():
    print("=== Setup Admin User ===")
    init_db()
    
    email = input("Email: ").strip()
    if not email:
        print("Email cannot be empty.")
        return

    if get_user_by_email(email):
        print("User with this email already exists.")
        return

    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
        
    password = getpass.getpass("Password: ")
    if not password:
        print("Password cannot be empty.")
        return
        
    confirm_password = getpass.getpass("Confirm Password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return
        
    user_id = create_user(email, name, password)
    if user_id:
        print(f"Admin user '{name}' ({email}) created successfully!")
    else:
        print("Failed to create user. Ensure the email is unique.")

if __name__ == "__main__":
    main()
