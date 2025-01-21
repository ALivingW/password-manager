import json
from encryption import encryption
def add_password(name):

    password_identifier = input("""OK! Enter the account that the password is for
eg. Gmail, Twitter, Reddit etc. """)
    enc_identifier = encryption(password_identifier)

    password = input(f"Now Enter the Password for your {password_identifier} account: ")
    enc_password = encryption(password)

    file = open(f"{name}_passwords.txt", "r")
    file_contents = json.load(file)  # returns- {'passwords':[{'name':'password'}]}
    file.close()
    # (file_contents['passwords'][0][f'{name}']] returns the 'password'
    file_contents["passwords"][len(["passwords"]) - 1][f"{enc_identifier}"] = f"{enc_password}"
    print("Adding new password. Do not close ")
    file = open(f"{name}_passwords.txt", "w")
    json.dump(file_contents, file)
    file.close()
    print("Password Successfully Added.")
