from pwn import *
from Crypto.Util.number import long_to_bytes
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import gmpy2

conn = remote('diffie-3ilman.hackini24.shellmates.club', 443, ssl=True)

print(conn.recvuntil("I know that diffie hellman is robust so I let you play with parameters"))

response = conn.recvuntil("Choose k =").decode()
g = int(response.split("g = ")[1].split("\n")[0])
p = int(response.split("p = ")[1].split("\n")[0])
A = int(response.split("A = ")[1].split("\n")[0])




print(f'{g=}')
print(f'{p=}')
print(f'{A=}')

k = (p-1) // 2

conn.sendline(str(k))
conn.recvuntil("\n")
response = conn.recvuntil("\n")
ciphertext=response.decode().split("c = ")[1].split("\n")[0]
c=int(ciphertext)

shared = pow(g, 2*(p-1)//2, p)

key = hashlib.md5(long_to_bytes(shared)).digest()
cipher = AES.new(key, AES.MODE_ECB)
c_bytes = long_to_bytes(c)

flag = unpad(cipher.decrypt(c_bytes), 16)
print(flag)

"""
shellmates{D0_n0t_L3t_Str4ngers_Pl4y_w1th_D1ffie_H3llman_p4ram$}
"""