master_pwd = input("What is the master password? ")

def view():
    pass

# creates a new file to add a password into. Also grab user account to store.
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        pass

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