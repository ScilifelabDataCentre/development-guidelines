<!-- WIP -->

# Python packages

-- all of them use / recommend the same nonce / IV method -- os.urandom. Except for cobbelstone in cryptography -- OpenSSL rand_bytes, based on NIST SP 800-90A Rev. 1.

## `cryptography`

https://cryptography.io/en/latest/

- DDS uses (for key encryption)
    - AEAD -- AES-GCM 
- Fernet https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption
    - high level functionality
    - easier to use
    - complete message contents must be available in memory -- quote-ish: not suitable for very large files, but good for encrypting data that easily fits in memory https://cryptography.io/en/latest/fernet/#limitations
    - AES CBC with 128 bit key using PKCS7 padding https://cryptography.io/en/latest/fernet/#implementation 
    - "also has support for implementing key rotation via MultiFernet" https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption
- used by (for some features)
    - flask
    - django-allauth
    - celery
- used by
    - pyopenssl (same author)
    - ansible
    - authlib
    - oauthlib
    - google-auth (https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth)
    - jwcrypto


## `Pycryptodome`

https://www.pycryptodome.org/

- "Self-contained Python package of low-level cryptographic primitives"
    - Expects users to have a more solid understanding of cryptography and security engineering than with the others
    - Easier to misuse
    - Requires you to handle some tasks by yourselves
    - nonce is randomly generated if you want it to be, 

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_GCM)         # a random nonce is generated
ciphertext, tag = cipher.encrypt_and_digest(b"attack at dawn")

receiver = AES.new(key, AES.MODE_GCM, nonce=cipher.nonce)
plaintext = receiver.decrypt_and_verify(ciphertext, tag)  # raises ValueError if tampered
```

## `PyNaCl`

https://pynacl.readthedocs.io/en/latest/

- maintained by the same org as cryptography
- doesn't have key-rotation support
- also high-level and low-level, so not as much crypto knowledge needed