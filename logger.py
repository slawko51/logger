import os

print("Logger")
email = input("Your email: ")
password = input("Your password: ")

filename = "log.txt"
if not os.path.isfile(filename):
    f = open(filename, "w")
f.write(str(email) + "/" + str(password))  
