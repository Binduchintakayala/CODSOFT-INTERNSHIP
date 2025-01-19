import random
import string
def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password
def main():
    length = int(input("Enter the desired length for the password: "))
    password = generate_password(length)
    print("Your generated password is:", password)
main()
