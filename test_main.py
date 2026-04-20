import time
from triple_des_logic import TripleDESService


VECTOR_1 = {
    "KEY": "010101010101010101010101010101010101010101010101", 
    "IV": "0000000000000000",
    "PLAIN": "8000000000000000",
    "CIPHER": "95F8A5E5DD31D900"
}

VECTOR_2 = {
    "KEY": "010101010101010101010101010101010101010101010101", 
    "IV": "0000000000000000", 
    "PLAIN": "4000000000000000",
    "CIPHER": "DD7F121CA5015619" 
}

VECTOR_3 = {
    "KEY": "010101010101010101010101010101010101010101010101", 
    "IV": "0000000000000000", 
    "PLAIN": "2000000000000000", 
    "CIPHER": "2E8653104F3834EA" 
}

VECTORS = [VECTOR_1, VECTOR_2, VECTOR_3]

def test_correctness_pycryptodome():
    for v in VECTORS:
        res = TripleDESService.encrypt_pycryptodome(v["KEY"], v["IV"], v["PLAIN"])
        assert res == v["CIPHER"], f"Failed PyCryptodome for plain {v['PLAIN']}"

def test_correctness_cryptography():
    for v in VECTORS:
        res = TripleDESService.encrypt_cryptography(v["KEY"], v["IV"], v["PLAIN"])
        assert res == v["CIPHER"], f"Failed Cryptography for plain {v['PLAIN']}"

def test_both_libraries_match():
    for v in VECTORS:
        res1 = TripleDESService.encrypt_pycryptodome(v["KEY"], v["IV"], v["PLAIN"])
        res2 = TripleDESService.encrypt_cryptography(v["KEY"], v["IV"], v["PLAIN"])
        assert res1 == res2, f"Mismatch for plain {v['PLAIN']}"

def test_performance(capsys):
    iterations = 1000
    
   
    start_time = time.time()
    for _ in range(iterations):
        TripleDESService.encrypt_pycryptodome(VECTOR_1["KEY"], VECTOR_1["IV"], VECTOR_1["PLAIN"])
    pycrypto_time = time.time() - start_time
    
    
    start_time = time.time()
    for _ in range(iterations):
        TripleDESService.encrypt_cryptography(VECTOR_1["KEY"], VECTOR_1["IV"], VECTOR_1["PLAIN"])
    crypto_time = time.time() - start_time
    
    with capsys.disabled():
        print(f"\nPyCryptodome: {pycrypto_time:.4f}s | Cryptography: {crypto_time:.4f}s")
