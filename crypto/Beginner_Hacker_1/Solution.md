# Beginner_Hacker_1

## Write up

we were given this code 
```py
from random import randint as ri

def encrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext

flag = b"shellmates{redacted}"
assert len(flag)%13==0
mykey = bytearray([ri(0, 255) for _ in range(13)])  
enc = encrypt(flag, mykey)
print(enc)

# enc = b'\x1c62\x8f|i\x9a\xadw\xba\x06N\x85\x08+d\xb0C[\xa9\xed|\x8dM\x12\xb4\\\r$\xbct4\x9e\xaaM\x872\x0b\x85.\x12\x00\xa2iW\xa4\xb4W\xfd3 \xa3\x00\x0b\x08\xb1O \x9e\x9ag\xbbN^\xa7'
```

after reading the code we see that it does the XOR operation between the flag and a secret key

since it is doing xor the encryption function is also the decryption function

>plaintext ⊕ key = encrypted_text
>encrypted_text ⊕ plaintext = key
>encrypted_text ⊕ key = plaintext


so to xor we just need to get the key but is that possible ??

since we know that the flag contains the word **shellmates{** we can perform a **KPA (known plaintext attack)** 

we know that the length of the key is 13 and the known plaintext contains 11 so we can just bruteforce the letters number 

12 and 13 in the flag 

here is the script 
```py
def decrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext

enc = b'\x1c62\x8f|i\x9a\xadw\xba\x06N\x85\x08+d\xb0C[\xa9\xed|\x8dM\x12\xb4\\\r$\xbct4\x9e\xaaM\x872\x0b\x85.\x12\x00\xa2iW\xa4\xb4W\xfd3 \xa3\x00\x0b\x08\xb1O \x9e\x9ag\xbbN^\xa7'

for i in range(255):
    for j in range(255):
        key =decrypt(b'shellmates{'+chr(i).encode()+chr(j).encode(), enc[:13])
        try:
            flag = decrypt(enc, key).decode()
            if flag[-1] == '}':
                print(f'{key=}')
                print(f'{flag=}')
                print()
        except:
            pass
```

we got a lot of outputs you can filter the results in the script but i was lazy so i did it manually :)

and we got the flag and the used key

>key=bytearray(b'o^W\xe3\x10\x04\xfb\xd9\x12\xc9}\x7f\xda')
>flag='shellmates{1_gu3SS_R4nD0mn3Ss_d0es_NOt_ALWAyS_mE4N_yoU_R_$eCur3!}'

