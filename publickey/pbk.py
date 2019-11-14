#!/usr/bin/env python3

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256

random_generator = Random.new().read

pj_key = RSA.generate(1024, random_generator) #generate public and private keys

pj_pub_key = pj_key.publickey()

yj_key = RSA.generate(1024, random_generator) #generate public and private keys
yj_pub_key = yj_key.publickey()


print(pj_key.n)
print(pj_pub_key)

print(yj_key.n)
print(yj_pub_key)


secret = Random.new().read(32)
print("secret %s" % repr(secret))

encrypted_secret = pj_pub_key.encrypt(secret, 32)
print("es: %s" % repr(encrypted_secret))

K = None
h = SHA256.new()
h.update(encrypted_secret[0])
secret_digest = h.digest()
print("sd %s" % repr(secret_digest))

signature = yj_key.sign(secret_digest, K)
print("sign %s" % repr(signature))


h = SHA256.new()
h.update(encrypted_secret[0])
secret_digest_by_pj = h.digest()

verify = yj_pub_key.verify(secret_digest_by_pj, signature)
print("verify %s" % repr(verify))
decrypted_secret = pj_key.decrypt(encrypted_secret)
print(hash(secret))
print(hash(decrypted_secret))




"""
publickey = key.publickey # pub key export for exchange

encrypted = publickey.encrypt('encrypt this message', 32)
#message to encrypt is in the above line 'encrypt this message'

print 'encrypted message:', encrypted #ciphertext

f = open ('encryption.txt', 'w'w)
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open ('encryption.txt', 'r')
message = f.read()

decrypted = key.decrypt(message)

print 'decrypted', decrypted

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()
"""
