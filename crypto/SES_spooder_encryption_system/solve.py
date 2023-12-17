#!/bin/python

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

flag = open('flag', 'rb').read()+b'Free Palestine.'

def aes_dec(key, ct):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.decrypt(ct)

with open('enc', 'rb') as f1:
    enc = f1.read()

ct = [enc[i:i + AES.block_size] for i in range(0, len(enc), AES.block_size)]

pt = []

for i in range(len(ct)-1):
    print(len(ct)-i-2)
    tmp = (aes_dec(ct[len(ct)-i-2], ct[len(ct)-i-1]))
    pt = [tmp] + pt

pt = [(aes_dec(pt[-1], ct[0]))] + pt

print(''.join([(p).decode() for p in pt]))
