import random
import string


def generate_passsword(length):

    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(characters) for _ in range(length))
    return password

try:
    pass_len = int(input("Enter length for password: "))
    if pass_len <=0:
        print("Password length must be positive integer")
    else:
        generated_password =  generate_passsword(pass_len)
        print(f"your password {generated_password}")

except ValueError:
    print("Invalid input. Please enter a valid positive number for the password length")
