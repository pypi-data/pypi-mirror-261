# passwordcrypto

This Python module provides a simple password manager for securely storing and retrieving encrypted password entries. The passwords are encrypted using the Fernet symmetric encryption scheme. The module includes functionality to derive a Fernet key from a password, initialize a password manager instance, retrieve encrypted passwords, decrypt and read stored passwords, encrypt text, and write new password entries to a file.

## Usage

### Installation

Execute the following command: `pip install passwordcrypto`

For windows users it's recommended to execute `pythonX.YY -m pip install passwordcrypto`

Change X.YY to the python version you use

### Initialization

```python
import passwordcrypto

# Example usage
password = bytes(input("Write your password: "))
filename = 'passwords.txt'

# Initialize a Passwd instance
password_manager = passwordcrypto.Passwd(filename, password)
```

### Reading Passwords

```python
password_entries = password_manager.read()
""" Outputs a list of passwords which themselves are a list of [App, Email, Password]
Example: [
    ['testApp', 'testEmail', 'testPassword'],
    ['testApp2','testEmail2','testPassword2'],
    ]
"""
```

### Writing Passwords

```python
# Write a new password entry to the file
app_name = 'MyApp'
email_address = 'user@example.com'
user_password = 'SecurePassword123'

password_manager.write(app_name, email_address, user_password)
```

### Example
```python
import passwordcrypto

inputKey = bytes(input("Insert your password: ").encode())
passwodManager = passwordcrypto.Passwd("example.txt", inputKey)

while True:
    option = input("\nWhat do you want to do? (1: Read 2: Write): ")

    match option:
        case "1":
            print("\nAPP, EMAIL, PASSWORD")
            passwordList = passwodManager.read()
            for line in passwordList:
                print(", ".join(line))

        case "2":
            app = input("Insert app name: ")
            email = input("Insert email/username: ")
            password = input("Insert password: ")
            passwodManager.write(app,email,password)

        case _:
            exit()
```

## API Reference

### `generate_key_from_password(password: bytes) -> Fernet`

Generates a Fernet key derived from the provided password.

### `class Passwd(filename: str, key: bytes) -> None`

Initialize a Passwd instance.

- `filename (str)`: The name of the file to store encrypted passwords.
- `key (bytes)`: The Fernet key used for encryption and decryption.

### `getEncryptedPasswds() -> list[bytes]`

Retrieve encrypted passwords from the file.

### `read() -> list[list[str]]`

Decrypt and read stored passwords from the file. Returns a list of decrypted password entries, where each entry is a list with the format `[App, Email, Password]`.

### `encrypt(text: str) -> bytes`

Encrypt the given text using the Fernet key.

- `text (str)`: The text to be encrypted.

### `write(app: str, email: str, password: str) -> None`

Encrypt and write a new password entry to the file.

- `app (str)`: The application or service name.
- `email (str)`: The associated email address.
- `password (str)`: The password for the application or service.

## Security Note

The password used to create the instances of Passwd should not be stored anywhere, instead inputted by the user.

Adjust the number of iterations in the key derivation process (`iterations` parameter in `generate_key_from_password`) based on your security requirements. Higher iterations increase security but also result in longer key derivation times.