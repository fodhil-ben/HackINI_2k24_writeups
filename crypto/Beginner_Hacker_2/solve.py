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
