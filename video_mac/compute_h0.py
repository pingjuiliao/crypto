#!/usr/bin/python
from Crypto.Hash import SHA256
import sys
import os
BLOCKSIZE = 1024

def do_it(msg) :

    msg, last_block = msg[:- (len(msg) % BLOCKSIZE)], msg[-(len(msg) % BLOCKSIZE):]

    block = last_block
    tag   = ""
    while len(block) :
        hash = SHA256.new()
        hash.update( block + tag )
        tag = hash.digest()
        msg, block = msg[:-BLOCKSIZE], msg[-BLOCKSIZE:]

    print tag.encode("hex")


if __name__ == '__main__' :
    if len(sys.argv) < 2 :
        print "Usage: %s <msg_filename>" % sys.argv[0]
        quit()
    if not os.path.exists(sys.argv[1]) :
        print "Error: filename %s cannot be found " % sys.argv[1]
        quit()

    with open(sys.argv[1], "r") as f :
        m = f.read()
        f.close()

    do_it(m)
