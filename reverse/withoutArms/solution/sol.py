import base64

class RC4:
    def __init__(self, key):
        self.key = key

    def _key_scheduling(self):
        """Key Scheduling Algorithm (KSA)"""
        S = list(range(256))    
        key_length = len(self.key)

        j = 0
        for i in range(256):
            j = (j + S[i] + self.key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]  

        return S

    def _pseudo_random_generation(self, S):
        """Pseudo-Random Generation Algorithm (PRGA)"""
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  
            K = S[(S[i] + S[j]) % 256]
            yield K

    def encrypt(self, plaintext: bytes) -> str:
        """Encrypt the plaintext and return Base64-encoded ciphertext"""
        S = self._key_scheduling()  
        key_stream = self._pseudo_random_generation(S)
        ciphertext = bytearray()

        for byte in plaintext:
            ciphertext.append(byte ^ next(key_stream))

        
        return base64.b64encode(bytes(ciphertext)).decode('utf-8')

    def decrypt(self, b64_ciphertext: str) -> bytes:
        """Decrypt the Base64-encoded ciphertext"""
        
        ciphertext = base64.b64decode(b64_ciphertext)
        
        return self.encrypt(ciphertext).encode()


# Example Usage
if __name__ == "__main__":
    
    key = b'ImShellm4ateM3mb'  #  key   from assembly code 
    
    ciphertext_b64="eLMtuXBQu+UmHz19Op64mEoObNU="  # from the given ciphertext.txt

    rc4 = RC4(key)

    decrypted_text = rc4.decrypt(ciphertext_b64)

    print(f'Decrypted Text base64: {decrypted_text}')

    text = base64.b64decode(decrypted_text)

    print(f'Decrypted Text : {text}')


