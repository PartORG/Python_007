# imports here
import os
import hashlib as hl

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

KEY_NAME = ".key.txt"


class BaseCipher:

    def __init__(self):
        key = get_random_bytes(16)
        with open(KEY_NAME, "wb") as f:
            f.write(key)

    def decrypt(self, file_name):
        pass

    def encrypt(self, file_name, data):
        pass

    @staticmethod
    def write_cipher_text(file_name, cipher, tag, ciphertext):
        with open(file_name, "at") as f:
            f.write(cipher.nonce)
            f.write(tag)
            f.write(ciphertext)


class AESCipher(BaseCipher):

    def __init__(self):
        super().__init__()

    def decrypt(self, file_name):
        with open(f"{os.getcwd()}/{KEY_NAME}", "rb") as f:
            key_data = f.read()

        with open(file_name, "rb") as f:
            nonce = f.read(16)
            tag = f.read(16)
            ciphered_data = f.read()

        cipher = AES.new(key_data, AES.MODE_EAX, nonce)
        original_text = cipher.decrypt_and_verify(ciphered_data, tag)
        return original_text


    def encrypt(self, file_name, data):
        with open(f"{os.getcwd()}/{KEY_NAME}", "rb") as f:
            key_data = f.read()

        cipher = AES.new(key_data, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        self.write_cipher_text(file_name, cipher, tag, ciphertext)



class RSACipher(BaseCipher):

    def __init__(self):
        super().__init__()

    def decrypt(self):
        pass

    def encrypt(self):
        pass
