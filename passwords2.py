from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# def write_salt():
#     salt = os.urandom(16)
#     with open("salt.key", "wb") as key_file:
#         key_file.write(salt)
# write_salt()

def load_salt():
    file = open('salt.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")

salt = load_salt()

# new additional code.
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
fer = Fernet(key)


# reads each password from the files.s
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

# creates a new file to add a password into. Also grab user account to store.
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view or add)? ")
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue
    
print("All right, be on your way.")