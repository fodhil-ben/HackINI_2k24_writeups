# diffie_3ilman
## Write up

we were given this code 
```py
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
from random import randint
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


with open("flag.txt", "rb") as f:
    flag = f.read().strip()

def main():
    print("I know that diffie hellman is robust so I let you play with parameters")

    g, p = 2, getPrime(1024)
    a = randint(2, p - 1)
    A = pow(g, a, p)
    print("Public key:")
    print(f"{g = }")
    print(f"{p = }")
    print(f"{A = }")

    try:
        k = int(input("Choose k = "))
    except:
        print("please enter a number...")
        return
    if k == 1 or k == p - 1 or k <= 0 or k >= p:
        print("Noooo not like that...")
        return

    Ak = pow(A, k, p)
    b = randint(2, p - 1)
    B = pow(g, b, p)
    Bk = pow(B, k, p)
    shared = pow(Bk, a, p)

    key = hashlib.md5(long_to_bytes(shared)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    c = bytes_to_long(cipher.encrypt(pad(flag, 16)))

    print("chipherText: ")
    print(f"    {c = }")
    return

if __name__ == "__main__":
    main()
```

from the challenge description we see that the challenge talks about diffie hellman key-exchange

after checking the code we see that the program ask for a number k
so that it generates a new value **Bk** with the parameter **b** and it uses that to calculate the shared secret to encrypt the flag

so the to solve the challenge we need to proveide a value of k so that we can find the value of the shared and decrypt the flag

we can see here it checks if the **k** is one of these values so it exit

```py
    if k == 1 or k == p - 1 or k <= 0 or k >= p:
        print("Noooo not like that...")
        return
```

but why ??

```
we know that 
bk = B ** k % p
shared = bk ** a % p
```

if there was no checks the easiest solution was to submit k = 0

so that 

```
bk = b ** 0 % p == 1
shared = 1 ** a % p == 1
```

and we easily get the flag but sadly the we cant provide the 0 and other values after some researching i found that if we send the value 
**k = (p-1) //2**
we can calculate the shared secret easily and get the flag 

```
if we give it 
k = (p-1) // 2
we can get the shared like this 
shared = pow(g, 2*(p-1)//2, p)
```

well how is that possible ??

here it comes to math and im not the best person to talks about math 
i found a similair challenge so you can read more about it here

https://github.com/ctfguy/My_CTF_Writeups/blob/main/UIUCTF%202023/Crypto/Group%20Project%20and%20Projection/solution.md

**my solve script**

```py
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
```



> flag : shellmates{D0_n0t_L3t_Str4ngers_Pl4y_w1th_D1ffie_H3llman_p4ram$}
