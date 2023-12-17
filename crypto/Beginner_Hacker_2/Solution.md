# Beginner_Hacker_2
## Write up

we were given this file
```py
from random import shuffle, seed, randint as ri
from Crypto.Util.number import bytes_to_long

def encrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext

flag = "shellmates{redacted}"
assert len(flag)%12==0
mykey = bytearray([ri(0, 255) for _ in range(12)])
print(mykey)
pt = flag[11:-1]
print(pt)
l_pt = list(pt)
seed(bytes_to_long(mykey))
shuffle(l_pt)
shuffled_flag = "shellmates{" + "".join(l_pt) + "}"
enc = encrypt(shuffled_flag.encode(), mykey)
print(enc)

# enc = b'S64\xd1\xeeG\x95\xcf\rl\xe3n\x7f\x013\xd3\xf4M\x80\xff<@\xcd\x18h\te\xe2\xa3d\xad\x9f\r/\xf6X\x7f\x0cb\xcf\xe3O\x8d\xd2\x00J\xd9\x18W\x15b\xe2\xc0d\xbd\xde7V\xebn\x7f\x1d\x1f\xe2\xc6G\xc4\xe4-s\xc7V'
```

the program generate a random key of length 12

and shuffle the flag letters using the random.shuffle

and the perform the xor operation with the generated key

## solution

we notice this line of code 
```py
seed(bytes_to_long(mykey))
```

it is setting the seed to the value of the key so we can get the key we can easily reverse the shuflle operation

so first step is how to get the key 
like the first challenge we can perform **KPA(known plaintext attack)**
we xor the first 11 charecter of the encrypted with **shellmates{**
and the last charecter of the encrypted with **}**

since the flag starts with shellmates and ends with }

so after getting the key we can give its value as a seed to the random

and genereates the same random shuflling sequence and map it to the decrypted flag

and we got the flag 

>flag: shellmates{ev3n_D0Uble_EnCRYti0N_Is_B4D_WHeN_wE_ar3_UsINg_ThE_$Am3_K3y!}

here is the solve script :
```py
from random import shuffle, seed, randint as ri
from Crypto.Util.number import bytes_to_long

def decrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext

def unshuffle(shuffled_string, seed_value):
    shuffled_list = list(shuffled_string)

    seed(seed_value)
    indices = list(range(len(shuffled_list)))
    shuffle(indices)


    unshuffled_list = [None] * len(shuffled_list)
    for i, j in zip(indices, range(len(shuffled_list))):
        unshuffled_list[i] = chr(shuffled_list[j])
    unshuffled_string = ''.join(unshuffled_list)
    
    return unshuffled_string

flag_enc = b'S64\xd1\xeeG\x95\xcf\rl\xe3n\x7f\x013\xd3\xf4M\x80\xff<@\xcd\x18h\te\xe2\xa3d\xad\x9f\r/\xf6X\x7f\x0cb\xcf\xe3O\x8d\xd2\x00J\xd9\x18W\x15b\xe2\xc0d\xbd\xde7V\xebn\x7f\x1d\x1f\xe2\xc6G\xc4\xe4-s\xc7V'

know_key = decrypt(flag_enc[:11], b'shellmates{')

last_byte = decrypt(b'}', flag_enc[-1:])

know_key = know_key + last_byte

flag = decrypt(flag_enc, (know_key))

flag = 'shellmates{'+unshuffle(flag[11:-1], bytes_to_long(know_key)) + '}'

print(flag)

```