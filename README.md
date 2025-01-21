PASSWORD-MANAGER-PROJECT
In my Password Manager app, I first introduce the user to the app, and request them to make an account if they don't already have one. The user can then add any passwords for any accounts that they'd like. 

After adding the passwords for their accounts, the passwords and accounts are encrypted and put into a dictionary (within a text file), the account being the key and the password being the value.

If the user would like to see their account passwords, the dictionary keys and values are decrypted and displayed to the user.

NOTES-
For encryption, I avoided using the cryptography library to give me more of a challenge.
When storing the passwords, there were a lot of different ways to do it, such as using an sqlite3 database, however, I felt that I needed to practise file handling.
I have gained valuable back-end development experience from this project, and am producing a GUI using Kivy to gain front-end experience aswell. I will soon add the password manager with GUI once completed.
