import random
import string

length = int(input("what length do you want for your password ?.. "))

length_password = int(input("how many password you want?.. "))

characters = string.ascii_letters + string.digits + "!@#$%"

password_P1 = ""

for N_password in range(length_password):
    password_P1 = ""
    for number in range(length):
        password_P1 += random.choice(characters)
    print(password_P1 + " ")
    # If you want print your objects in one row with " " you need this
    # code //print(password_P1, end=" ") 
print("Thank you for using [<3 _ <3] ")