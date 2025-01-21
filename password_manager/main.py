import json
from adding_passwords import add_password
from encryption import encryption
from decrypt import decryption

print("Welcome to the password manager!")

choice1 = input("""
Login            (a)
Make New Account (b)
""")

if choice1 == "a":
    name = input("Enter Your Name: ").strip()
    master_password = input("Enter the Master Password: ").strip()
    file = open(f"{name}_passwords.txt", "r")
    file_contents = json.load(file)  # this is where the error is coming from
    file.close()
    supposed_password = file_contents["passwords"][0][encryption("master_password")]
    if supposed_password == encryption(master_password):
        print("Access Granted")
        choice1 = input("""
Would you like to see your passwords    (a)
Add a new password                      (b)
""")
        if choice1 == "a":  # choice for logged-in user
            passwords = file_contents["passwords"][0]
            for key, value in passwords.items():
                key = decryption(key)
                value = decryption(value)
                print(f"{key} : {value}")
        elif choice1 == "b":
            add_password(name)
        else:
            print('Please Enter One Of The Given Choices.')
    else:
        print("Wrong Name Or Password")


elif choice1 == "b":
    name = input("Enter Your Name: ")
    master_password = input("Enter the Master Password, Ensure It Is Secure: ")

    enc_master_password_name = encryption("master_password")
    enc_master_password = encryption(master_password)

    creation = {
        "passwords": [
            {
                f"{enc_master_password_name}": f"{enc_master_password}"
            },
        ]
    }

    file = open(f"{name}_passwords.txt", "w")
    json.dump(creation, file)
    file.close()
    choice = input("Would You Like To Add a New Password? ").lower()
    if choice == "yes":
        add_password(name)
else:
    print('Please Enter One Of The Given Choices.')