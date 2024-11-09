# illegal

## Write-up

- Each bit of the flag is exfiltrated twice through packets that have tcp flags **SYN** and **FIN** at the same time (which is a common illegal tcp flag combination)  
- Challenge can be solved using `solve.sh`


## Flag

`shellmates{1ll3g4l_fl4gs_ex1st!}`
