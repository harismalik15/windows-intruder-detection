from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(path):
    fernet = Fernet(load_key())
    with open(path, "rb") as f:
        encrypted = fernet.encrypt(f.read())

    enc_path = path + ".enc"
    with open(enc_path, "wb") as f:
        f.write(encrypted)

    return enc_path
# once it runs then run this 
#from crypto_utils import generate_key
#generate_key()
