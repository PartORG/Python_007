# imports here
import hashlib as hl


class BaseCipher:

    def __init__(self):
        pass

    def decrypt(self):
        pass

    def encrypt(self):
        pass

    def write_cipher_text(self):
        pass


class AESCipher(BaseCipher):

    def __init__(self):
        BaseCipher.__init__(self)

    def decrypt(self):
        pass

    def encrypt(self):
        pass


class RSACipher(BaseCipher):

    def __init__(self):
        BaseCipher.__init__(self)

    def decrypt(self):
        pass

    def encrypt(self):
        pass
