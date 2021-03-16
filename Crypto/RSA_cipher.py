from BaseCipher import BaseCipher
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


class RSACipher(BaseCipher):

    def __init__(self):
        BaseCipher.__init__(self)

    def decrypt_rsa_data(self):
        pass

    def encrypt_rsa_data(self):
        pass