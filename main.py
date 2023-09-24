from cryptography.fernet import Fernet
import hashlib


def generate_key():
    return Fernet.generate_key()


def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def hash_password(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    password_hash = "fe16" + hash_object.hexdigest() + "fas34R"
    return password_hash


encryption_key = generate_key()


password = input("Enter your password: ")


password_hash = hash_password(password)


encrypted_password = encrypt_password(password, encryption_key)

print("Encrypted Password:", encrypted_password)
print("Password hash:", password_hash)


decrypted_password = decrypt_password(encrypted_password, encryption_key)
print("Decrypted Password:", decrypted_password)
