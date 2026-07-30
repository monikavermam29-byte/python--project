import random
import string

password =  {}

# load Exiting  password file
try:
    with open("passwords.txt" ,"r") as file:
           for line in file :
               website, psd = line.strip().split(":")
               password[website] = psd
except:
      pass
def generate_password():
      chars = string.ascii_letters + string.digits + "!@#$%^&"
      password = "".join(random.choice (chars) for _ in range(8))
      return  password

while True:
     print("\n----- PERSONAL PASSWORD MANAGER-----")
     print("1. save password ")
     print("2. View password ")
     print("3. Generate password")
     print("4. Exit  ")

     choice = input("Enter your choice:")

     if choice == "1" :
         site = input("Enter website:")

         psd  = input("Enter password:")
         password[site] = psd

         with open("password.txt","a") as file:
             file.write(f"{site}:{psd}\n")


         print("password saved!")



     elif choice == "2":
      if not password:
               print("No data")
      else:
        for site , password in password.items():
            print(f"{site} : {password}")


     elif choice == "3":
         print("Generate password" , generate_password())


     elif choice == "4":
          print("ok by..")
          break

     else:
         print("In-valid input")

