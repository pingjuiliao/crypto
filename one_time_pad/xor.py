#!/usr/bin/python
def sxor(s1, s2) :
    if len(s1) != len(s2) :
        print("wrong length for xor-ed strings")
        quit()

    return "".join([ chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(s1, s2)])


def solve_coursera_hw() :
    msg1 = "attack at dawn"
    msg2 = "attack at dusk"
    cipher1 = "6c73d5240a948c86981bc294814d".decode('hex')
    print len(cipher1)
    key = sxor(msg1, cipher1)
    print sxor(msg2, key).encode('hex')

if __name__ == '__main__' :
    solve_coursera_hw()
