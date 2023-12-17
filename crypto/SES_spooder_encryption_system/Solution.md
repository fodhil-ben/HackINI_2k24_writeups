# SES_spooder_encryption_system
## Write up

we were given this file 
```py
#!/bin/python

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

flag = open('flag', 'rb').read()+b'Free Palestine.'

def aes_enc(key, pt):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.encrypt(pt)

pt = pad(flag, AES.block_size)

pt = [pt[i:i + AES.block_size] for i in range(0, len(pt), AES.block_size)]

ct = pt.copy()

for i in range(len(pt)):
    ct[i] = aes_enc(ct[i-1],pt[i])

open('enc','wb').write(b''.join(ct))

```

this program splits the flag into blocks of 16 charecter and encrypt each block using the previous encrypted block
but only the first block gets encrypted with the last block in the plaintext 

so we can recover the plaintext easily because we have the encrypted flag

first we split the encrypted flag to blocks of 16 and decrypting each block with the previous encrypted block
only the first block of the ciphertext get decrypted with the last block of the plaintext wich is the first block we decrypted

> here is the flag : shellmates{N3v3r'b'_stop_t4lK1nG_aB'b'0Ut_P4l3$tinE}

Congrats you made it this far, submit your flag, and never stop praying for your brothers and sisters. Free Palestine.

here is the solve script:
```py
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

```