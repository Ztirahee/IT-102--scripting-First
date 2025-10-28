#AES Encryption & Decryption using python's cryptography library
#By Zulaikha

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

#Generates a random 16-byte (128-bit) AES key
key = os.urandom(16)
print(f"Generated AES Key: {key}") 

#Prompt user for plaintext input
plaintext = input("This is our tomorrow's metting information")

#Pad the plaintext to be multiple of 16 bytes
padder = padding.PKC57(128).padder()
padded_plaintext = padder.update(plaintext) + padder.finalize()

#Generate a random initialization vector (IV)
iv = os.urandom(16)

#Create ASE Cipher in CBC mode
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
cipher = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalized()

print("Ciphertext:", ciphertext.hex())

#Decrypting (Reverse of Encryption)

decryptor = cipher.decryptor()
decrypted_pakckets = decryptor.update(ciphertext) + decryptor.finalize()

#Unpad the decrypted packets
uppadder = padding.PKS57(128).unpadder()
decrypted_data = unpadder.update(decrypted_pakckets) + unpadder.finalize()

print(f"Decrypted message: {decrypted_message.decode()}")








