import os
from cryptography.fernet import Fernet
from getpass import getpass

def generate_key():
    """Generate a new key for encryption."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'.")

def load_key():
    """Load the previously generated key."""
    return open("secret.key", "rb").read()

def encrypt_file(file_name):
    """Encrypt a file."""
    key = load_key()
    f = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)

    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    
    print(f"{file_name} has been encrypted and saved as {file_name}.encrypted.")

def decrypt_file(file_name):
    """Decrypt a file."""
    key = load_key()
    f = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)

    with open(file_name.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)
    
    print(f"{file_name} has been decrypted.")

def main():
    print("Welcome to the Advanced Encryption Tool")
    while True:
        print("\nOptions:")
        print("1. Generate a new encryption key")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            file_name = input("Enter the name of the file to encrypt: ")
            if os.path.exists(file_name):
                encrypt_file(file_name)
            else:
                print("File does not exist.")
        elif choice == '3':
            file_name = input("Enter the name of the file to decrypt: ")
            if os.path.exists(file_name):
                decrypt_file(file_name)
            else:
                print("File does not exist.")
        elif choice == '4':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()