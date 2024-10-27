# Challenge: Mind-your-own-keys

## Write-up

The challenge revolves around a Flask-based web service that encrypts a secret flag using DES (Data Encryption Standard) in ECB mode. You can provide an 8-byte key, which is used to encrypt the flag and return the result as a hexadecimal string. The task seems straightforward, but the true solution lies in exploiting a weak key property in DES.

### Weak Keys in DES
DES has several well-known weak keys, and these keys exhibit the peculiar property where encryption and decryption are identical. In other words, for these weak keys, performing the encryption process twice results in the original plaintext being recovered.

### Solution Steps:
1. Encryption Using the Weak Key When we provide the weak key 0xE1E1E1E1F0F0F0F0, the web service encrypts the secret flag using DES in ECB mode. Normally, the encrypted output would be difficult to reverse without the key, but due to the nature of this weak key, something special happens when we apply the encryption again.

2. Encrypting the Encrypted Flag After receiving the encrypted flag, we can re-encrypt this encrypted flag using the same weak key. Since DES weak keys make encryption and decryption identical, applying DES encryption again with the same key actually performs the decryption of the ciphertext. Thus, this second encryption step effectively reveals the original flag.

### Understanding Why It Works

The reason this approach works is because of the weak key property. Normally, encryption and decryption are inverse operations, but weak DES keys exhibit the behavior where encrypting a second time with the same key "undoes" the first encryption. In essence, DES_encrypt(DES_encrypt(plaintext, weak_key), weak_key) is equivalent to plaintext.


## Flag

`shellmates{w3aK_keY$_aRe_a_PR0Bl3m}`