import binascii
from Crypto.Cipher import DES3, DES
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class TripleDESService:

    @staticmethod
    def encrypt_pycryptodome(key_hex: str, iv_hex: str, plaintext_hex: str) -> str:
        key = binascii.unhexlify(key_hex)
        iv = binascii.unhexlify(iv_hex)
        plaintext = binascii.unhexlify(plaintext_hex)
        
        try:
            cipher = DES3.new(key, DES3.MODE_CBC, iv)
        except ValueError as e:
            if "degenerates to single des" in str(e).lower():
               
                cipher = DES.new(key[:8], DES.MODE_CBC, iv)
            else:
                raise
                
        ciphertext = cipher.encrypt(plaintext)
        
        return binascii.hexlify(ciphertext).decode('utf-8').upper()

    @staticmethod
    def encrypt_cryptography(key_hex: str, iv_hex: str, plaintext_hex: str) -> str:
        key = binascii.unhexlify(key_hex)
        iv = binascii.unhexlify(iv_hex)
        plaintext = binascii.unhexlify(plaintext_hex)
        
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        
        return binascii.hexlify(ciphertext).decode('utf-8').upper()
