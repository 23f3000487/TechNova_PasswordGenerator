import string 
import random 


characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter password length: "))
if length < 3:
    print("Password length must be at least 3")
    exit()

password = ""
password += random.choice(string.ascii_letters)
password += random.choice(string.digits)
password += random.choice(string.punctuation)


for i in range(length - 3):
    password += random.choice(characters)
print("Generated Password:", password)

with open("passwords.txt", "a") as file:
    file.write(password + "\n")