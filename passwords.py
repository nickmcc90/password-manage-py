from cryptography.fernet import Fernet

# Generate a unique encryption key
key = Fernet.generate_key()

master_pwd = input("What is the master password? ")
print(key)

# reads each password from the files.s
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)

# creates a new file to add a password into. Also grab user account to store.
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

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