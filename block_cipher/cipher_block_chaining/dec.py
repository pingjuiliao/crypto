#!/usr/bin/python
import sys
from Crypto.Cipher import AES
from Crypto import Random

def counter_mode_dec(k, c) :
    """
    Decoder
    """
    block_len = AES.block_size
    iv = c[:block_len]
    c  = c[block_len:]

    ## decode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    m = cipher.decrypt(c)
    return m



if __name__ == '__main__' :

    if len(sys.argv) < 3 :
        print "Usage: %s <key> <ciphertext>" % sys.argv[0]
        quit()
    with open(sys.argv[1], "r") as key_file :
        key = key_file.read().decode('hex')
        key_file.close()
    with open(sys.argv[2], "r") as cipher_file:
        ciphertext = cipher_file.read().decode('hex')
        cipher_file.close()

    print "length of key : %d" % len(key)
    print "length of cipher : %d " % len(ciphertext)


    msg = counter_mode_dec(key, ciphertext)
    print msg


