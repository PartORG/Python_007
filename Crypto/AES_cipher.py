from BaseCipher import BaseCipher
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AESCipher(BaseCipher):

    def __init__(self):
        BaseCipher.__init__(self)

    def decrypt_aes_data(self):
        pass

    def encrypt_aes_data(self):
        pass
