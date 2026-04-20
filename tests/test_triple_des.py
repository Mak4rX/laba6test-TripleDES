import pytest
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def test_triple_des_encrypt_decrypt():
    # Генеруємо коректний 24-байтний ключ для 3DES
    key = DES3.adjust_key_parity(get_random_bytes(24))
    cipher = DES3.new(key, DES3.MODE_CBC)
    
    plaintext = b"Test secret message for TripleDES automation lab!"
    
    # Шифруємо (TripleDES вимагає доповнення/padding до розміру блоку - 8 байт)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
    iv = cipher.iv
    
    # Розшифровуємо
    decrypt_cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = unpad(decrypt_cipher.decrypt(ciphertext), DES3.block_size)
    
    # Перевіряємо, чи розшифрований текст співпадає з оригінальним
    assert decrypted == plaintext
    
def test_invalid_key_length():
    # Перевіряємо, що бібліотека правильно реагує на неправильну довжину ключа
    with pytest.raises(ValueError):
        key = get_random_bytes(10) # Некоректна довжина для 3DES
        DES3.new(key, DES3.MODE_CBC)
