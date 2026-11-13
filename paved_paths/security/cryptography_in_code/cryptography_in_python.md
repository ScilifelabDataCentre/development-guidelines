# Cryptography in Python

This file provides the reasoning behind the chosen paved path stated in the [README.md](./README.md). Four different Python packages with cryptographic functionalities were compared:

- [`cryptography`](https://cryptography.io/en/latest/)
- [`PyCryptodome`](https://www.pycryptodome.org/)
- [`PyNaCl`](https://pynacl.readthedocs.io/en/latest/)
- [`Tink`](https://developers.google.com/tink)

## Comparison

**Legend:** ✅ yes, functionality provided / covered · ❌ no, functionality not covered

| Criterion                        | `cryptography`                                  | PyCryptodome                                   | PyNaCl                         | Tink                                     |
| -------------------------------- | ----------------------------------------------- | ---------------------------------------------- | ------------------------------ | ---------------------------------------- |
| First on PyPI                    | 2014-01-08 [^1][^2]                             | 2014-06-14 [^3][^4]                            | 2013-04-14 [^5]                | 2020-07-14 [^6][^7]                      |
| High-level, hard-to-misuse API   | ✅ "Recipes" layer: Fernet and Cobblestone [^8] | ❌ [^12]                                       | ✅ `SecretBox` and `Aead` [^9] | ✅ Primitives used through keysets [^10] |
| Low-level primitives             | ✅ "Hazmat" layer [^11]                         | ✅ [^12]                                       | ✅ [^13]                       | ❌ [^10]                                 |
| Nonce generated for you          | ✅ High-level </br> ❌ Low-level                | ✅ [^14]                                       | ✅                             | ✅                                       |
| Streaming functionality provided | ✅ [^15]                                        | ❌                                             | ❌                             | ✅                                       |
| Key rotation                     | ✅ [^16]                                        | ❌                                             | ❌                             | ✅                                       |
| Maintainer                       | PyCA [^17]                                      | Legrandin [^18]                                | PyCA [^17]                     | Google [^19]                             |
| License                          | Apache-2.0 </br> OR </br> BSD-3-Clause [^20]    | BSD-2-Clause </br> + </br> public domain [^20] | Apache-2.0 [^20]               | Apache-2.0 [^20]                         |

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

[![Docs](https://img.shields.io/badge/Docs-blue)](https://cryptography.io/en/latest/) ·
[![Source](https://img.shields.io/badge/Source-black)](https://github.com/pyca/cryptography) ·
[![PyPI](https://img.shields.io/badge/PyPI-orange)](https://pypi.org/project/cryptography/) ·
[![Why `cryptography`](https://img.shields.io/badge/Why_cryptography-green)](https://cryptography.io/en/latest/faq/#why-use-cryptography)

### Activity

The `cryptography` package is actively maintained and [widely used](https://github.com/pyca/cryptography/network/dependents), e.g. by Ansible, Authlib, Oauthlib, Google-auth, jwcrypto, Flask, Django-allauth, Celery.

### Ease of use

`cryptography` [has two levels](https://cryptography.io/en/latest/#layout) with different requirements on cryptographic knowledge and configuration choices:

- The high-level "Recipes" layer contains two methods of implementing symmetric encryption. They "require little to no configuration choices" and "are safe and easy to use and don't require developers to make many decisions" [^28].
- The low-level "Hazmat" layer provides a range of different algorithms via low-level primitives [^27]. It requires "making decisions and having an in-depth knowledge of the cryptographic concepts at work" and "can be used incorrectly" [^28].

[^27]: [Low-level primitives in `cryptography`](https://cryptography.io/en/latest/hazmat/primitives/#primitives)

[^28]: [`cryptography` docs: Layout](https://cryptography.io/en/latest/#layout)

|                            | [Fernet](https://cryptography.io/en/latest/fernet/)                                               | [Cobblestone](https://cryptography.io/en/latest/cobblestone/) | Primitives             |
| -------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------- |
| Layer                      | High-level Recipes                                                                                | High-level Recipes                                            | Low-level Hazmat       |
| Algorithm [^23]            | AES-128-CBC [^24] + HMAC-SHA256 [^22]                                                             | AES-128-GCM **or** AES-256-GCM [^25][^26]                     | You choose             |
| Whole message in memory    | Yes                                                                                               | No (streaming, up to 4 PiB)                                   | You configure          |
| Suitable for encryption of | Small amounts of data [^21]                                                                       | Any data, incl large files                                    | Any, but you configure |
| Nonce generated for you    | Yes                                                                                               | Yes                                                           | No                     |
| Key rotation               | Yes, via [MultiFernet](https://cryptography.io/en/latest/fernet/#cryptography.fernet.MultiFernet) | No                                                            | No                     |

[^21]: [Fernet limitations](https://cryptography.io/en/latest/fernet/#limitations)

[^22]: [Fernet implementation](https://cryptography.io/en/latest/fernet/#implementation)

[^23]: AES: Advanced Encrption Standard. Approved in [FIPS 197](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf).

[^24]: CBC: Cipher Block Chaining.

[^25]: GCM: Galois Counter mode. [NIST-recommended: SP 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)

[^26]: AES-256-GCM is a standard default choice. [RFC 5116](https://www.rfc-editor.org/info/rfc5116/).

### Additional information

`cryptography`'s own documentation states that is has not had an external audit of its code or documentation.

## `Pycryptodome`

[![Docs](https://img.shields.io/badge/Docs-blue)](https://www.pycryptodome.org/) ·
[![Source](https://img.shields.io/badge/Source-black)](https://github.com/Legrandin/pycryptodome) ·
[![PyPI](https://img.shields.io/badge/PyPI-orange)](https://pypi.org/project/pycryptodome/) ·
[![Why PyCryptodome](https://img.shields.io/badge/Why_PyCryptodome-green)](https://github.com/Legrandin/pycryptodome#why-pycryptodome)

- "Self-contained Python package of low-level cryptographic primitives"
  - Expects users to have a more solid understanding of cryptography and security engineering than with the others
  - Easier to misuse
  - Requires you to handle some tasks by yourselves
  - nonce is randomly generated if you want it to be,
- very broad algorithm set
- no "high level" recipe
- decrypt() returns plaintext before the tag is checked -- must verify() before using output https://www.pycryptodome.org/src/guides/symmetric#encrypt-a-large-file
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

[![Docs](https://img.shields.io/badge/Docs-blue)](hhttps://pynacl.readthedocs.io/en/latest/) ·
[![Source](https://img.shields.io/badge/Source-black)](https://github.com/pyca/pynacl) ·
[![PyPI](https://img.shields.io/badge/PyPI-orange)](https://pypi.org/project/PyNaCl/)

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

## Tink

[![Docs](https://img.shields.io/badge/Docs-blue)](https://developers.google.com/tink) ·
[![Source](https://img.shields.io/badge/Source-black)](https://github.com/tink-crypto/tink-py) ·
[![PyPI](https://img.shields.io/badge/PyPI-orange)](https://pypi.org/project/tink/)
