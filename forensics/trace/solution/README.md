# trace

## Write-up

- The given file is a simple process coredump of `pwncat` (coredump is a process memory dump on linux).
- The challenge can be solved in different ways. The flag has different parts: 
- PID: you can just get it from the file name as it is the convention used to name coredumps files.
- AttackerIP:PORT : You can download pwncat and run it with its memory dump with `gdb $(which pwncat) core.170530` and execute `telescope 300 $sp` to view the stack memory, you'll find there the ip:port there. 
- For the other part you can keep digging in the process memory using gdb, but using strings is just easier :p ( that's why the challenge is marked as easy lol xD). 


## Flag

`shellmates{170530_192.168.1.3:9164_192.168.1.14:59936_Rxxxf$!$1337}`
