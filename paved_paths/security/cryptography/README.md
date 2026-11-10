<!-- WIP -->

# Python packages

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
    - Expects users to have a solid understanding of cryptography and security engineering
    - Easier to misuse
    - Requires you to handle some tasks by yourselves (e.g. nonce generation and algorithm choice)

## `PyNaCl`

https://pynacl.readthedocs.io/en/latest/

- maintained by the same org as cryptography
- doesn't have key-rotation support
- also high-level and low-level, so not as much crypto knowledge needed