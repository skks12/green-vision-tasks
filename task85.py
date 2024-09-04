def register(users):
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists!")
    else:
        password = input("Enter a password: ")
        users[username] = password
        print("Registration successful!")

def login(users):
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

def menu():
    users = {}
    while True:
        print("\nMenu:\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register(users)
        elif choice == '2':
            login(users)
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")

menu()
