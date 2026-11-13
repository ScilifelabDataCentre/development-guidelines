# Cryptography in Python

This file provides the reasoning behind the chosen paved path stated in the [README.md](./README.md). Four different Python packages with cryptographic functionalities were compared:

- [`cryptography`](https://cryptography.io/en/latest/)
- [`PyCryptodome`](https://www.pycryptodome.org/)
- [`PyNaCl`](https://pynacl.readthedocs.io/en/latest/)
- [`Tink`](https://developers.google.com/tink)

<!-- -- all of them use / recommend the same nonce / IV method -- os.urandom. Except for cobbelstone in cryptography -- OpenSSL rand_bytes, based on NIST SP 800-90A Rev. 1. -->

## Comparison

**Legend:** ✅ yes, functionality provided / covered · ❌ no, functionality not covered

| Criterion | `cryptography` | PyCryptodome | PyNaCl | Tink |
| --- | --- | --- | --- | --- |
| First on PyPI | 2014-01-08 [^1][^2] | 2014-06-14 [^3][^4] | 2013-04-14 [^5] | 2020-07-14 [^6][^7] |
| High-level, hard-to-misuse API | ✅ "Recipes" layer: Fernet and Cobblestone [^8] | ❌ [^12] | ✅ `SecretBox` and `Aead` [^9] | ✅ Primitives used through keysets [^10] |
| Low-level primitives | ✅ "Hazmat" layer [^11] | ✅ [^12] | ✅ [^13] | ❌ [^10] |
| Nonce generated for you | ✅ High-level </br> ❌ Low-level | ✅ [^14] | ✅ | ✅ |
| Streaming functionality provided | ✅ [^15] | ❌ | ❌ | ✅ |
| Key rotation | ✅ [^16] | ❌ | ❌ | ✅ |
| Maintainer | PyCA [^17] | Legrandin [^18] | PyCA [^17] | Google [^19] |
| License | Apache-2.0 </br> OR </br> BSD-3-Clause [^20] | BSD-2-Clause </br> + </br> public domain [^20] | Apache-2.0 [^20] | Apache-2.0 [^20] |

[^1]: [Docs](https://cryptography.io/en/latest/changelog/#v0-1)
[^2]: [PyPI](https://pypi.org/project/cryptography/#history)
[^3]: [PyPI](https://pypi.org/project/pycryptodome/#history)
[^4]: Fork of PyCrypto
[^5]: [PyPI](https://pypi.org/project/PyNaCl/#history)
[^6]: [Project public since 2018](https://security.googleblog.com/2018/08/introducing-tink-cryptographic-software.html?m=1)
[^7]: [PyPI](https://pypi.org/project/tink/#history)
[^8]: [Docs: Layout](https://cryptography.io/en/latest/#layout)
[^9]: [Docs](https://pynacl.readthedocs.io/en/latest/secret/)
[^10]: Not raw primitives; mainly through keysets. Requires you to choose algorithm, from vetted list, with a recommended default.[Understand Key Concepts in Tink](https://developers.google.com/tink/get-started).
[^11]: [The hazardous materials layer](https://cryptography.io/en/latest/hazmat/primitives/)
[^12]: ["Self-contained Python package of low-level cryptographic primitives"](https://www.pycryptodome.org/#pycryptodome). No high-level, hard-to-misuse API.
[^13]: Small hand-picked set only. Undocumented, but available via `nacl.bindings`.
[^14]: [You can choose whether or not you want to generate and provide it yourself, or let PyCryptodome handle it](https://www.pycryptodome.org/src/cipher/aes#Crypto.Cipher.AES.new)
[^15]: [Encrypting large files through streaming possible via Cobblestone](https://cryptography.io/en/latest/cobblestone/), but [not Fernet](https://cryptography.io/en/latest/fernet/#limitations).
[^16]: Key rotation functionality via [`MultiFernet`](https://cryptography.io/en/latest/fernet/#cryptography.fernet.MultiFernet). No key rotation functionality documented for Cobblestone or hazmat-layer.
[^17]: [Python Cryptographic Authority](https://github.com/pyca), a community project.
[^18]: [Legrandin](https://github.com/Legrandin), GitHub user.
[^19]: [Google maintains and designs, but there are external contributors as well.](https://github.com/tink-crypto/tink-py)
[^20]: Permissive licenses. [Free to use](https://choosealicense.com/licenses/); include the license text only when redistributing the code (e.g. in a container image).

## `cryptography`

https://cryptography.io/en/latest/
https://cryptography.io/en/latest/faq/#why-use-cryptography

- DDS uses (for key encryption)
    - AEAD -- AES-GCM 
- Has 2 levels: https://cryptography.io/en/latest/#layout
    - Recipes: "One with safe cryptographic recipes that require little to no configuration choices. These are safe and easy to use and don’t require developers to make many decisions." 
    - "Hazmat": 
        - "The other level is low-level cryptographic primitives. These are often dangerous and can be used incorrectly. They require making decisions and having an in-depth knowledge of the cryptographic concepts at work."
        - "We recommend using the recipes layer whenever possible, and falling back to the hazmat layer only when necessary."
- In recipes layer
    - Fernet https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption
        - high level functionality
        - easier to use
        - complete message contents must be available in memory
            - "Fernet is ideal for encrypting data that easily fits in memory. As a design feature it does not expose unauthenticated bytes. This means that the complete message contents must be available in memory, making Fernet generally unsuitable for very large files at this time." https://cryptography.io/en/latest/fernet/#limitations
        - AES CBC with 128 bit key using PKCS7 padding https://cryptography.io/en/latest/fernet/#implementation 
        - "also has support for implementing key rotation via MultiFernet" https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption
    - Cobbelstone now also avaialble
        - applicable for e.g. file encryption
        - possible to stream authenticated encryption
        - up to 4 PiB -- not in memory
        - AES-128-GCM or AES-256-GCM -- advanced encrption standard with galois counter mode
            - AES is approved in FIPS 197 https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf
            - GCM is a NIST-recommended mode https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf
            - it's a standard default choice https://www.rfc-editor.org/info/rfc5116/
        - no rotation helper for cobbelstone is documented 
- In hazmat layer: A range of different algorithms https://cryptography.io/en/latest/hazmat/primitives/#primitives
- used by 
    - (for some features)
        - flask
        - django-allauth
        - celery
    - (required)
        - pyopenssl (same author)
        - ansible
        - authlib
        - oauthlib
        - google-auth (https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth)
        - jwcrypto
- The project states it has not had an external audit of its code or documentation. https://cryptography.io/en/latest/

```python
# Example with fernet -- high level recipe 
>>> from cryptography.fernet import Fernet
>>> key = Fernet.generate_key()
>>> f = Fernet(key)
>>> token = f.encrypt(b"my deep dark secret")
>>> token
b'...'
>>> f.decrypt(token)
b'my deep dark secret'

# Example with hazmat
>>> import os
>>> from cryptography.hazmat.primitives.ciphers.aead import AESGCM
>>> data = b"a secret message"
>>> aad = b"authenticated but unencrypted data"
>>> key = AESGCM.generate_key(bit_length=128)
>>> aesgcm = AESGCM(key)
>>> nonce = os.urandom(12)
>>> ct = aesgcm.encrypt(nonce, data, aad)
>>> aesgcm.decrypt(nonce, ct, aad)
b'a secret message'
```

## `Pycryptodome`

https://www.pycryptodome.org/
https://github.com/Legrandin/pycryptodome#why-pycryptodome

- "Self-contained Python package of low-level cryptographic primitives"
    - Expects users to have a more solid understanding of cryptography and security engineering than with the others
    - Easier to misuse
    - Requires you to handle some tasks by yourselves
    - nonce is randomly generated if you want it to be, 
- very broad algorithm set 
- no "high level" recipe
- decrypt() returns plaintext before the tag is checked -- must verify() before using output  https://www.pycryptodome.org/src/guides/symmetric#encrypt-a-large-file
- no rotation helper 

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

- python binding to libsodium https://github.com/jedisct1/libsodium
- maintained by the same org as cryptography
- cryptography FAQ recommends it if you prefer this design
- doesn't have key-rotation support
- also high-level and low-level, so not as much crypto knowledge needed
    - nonces are handled for you -- risk of random nonce reuse is negligable
- Secret box available https://pynacl.readthedocs.io/en/latest/secret/#secret-key-encryption
- few choices to get wrong 
- only a few algorithms -- usability, security and speed
- no streaming or key rotation -- would have to build this yourself

```python
import nacl.secret
import nacl.utils

# This must be kept secret, this is the combination to your safe
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# This is your safe, you can use it to encrypt or decrypt messages
box = nacl.secret.SecretBox(key)

# This is our message to send, it must be a bytestring as SecretBox will
#   treat it as just a binary blob of data.
message = b"The president will be exiting through the lower levels"

# Encrypt our message, it will be exactly 40 bytes longer than the
#   original message as it stores authentication information and the
#   nonce alongside it.
encrypted = box.encrypt(message)

assert len(encrypted) == len(message) + box.NONCE_SIZE + box.MACBYTES

# This is a nonce, it *MUST* only be used once, but it is not considered
#   secret and can be transmitted or stored alongside the ciphertext. A
#   good source of nonces are just sequences of 24 random bytes.
nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)

encrypted = box.encrypt(message, nonce)
```