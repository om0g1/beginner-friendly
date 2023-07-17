import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"

def generate_password(length):
    password = " ".join([random.choice(characters) for i in range(length)])
    print(password)

generate_password(36)