

cmd=$(tshark -r illegal.pcapng -Y 'ip.addr == 192.168.1.3 && tcp.flags.syn == 1 && tcp.flags.fin==1 ' -T fields -e tcp.flags.push |sed 's/True/1/g; s/False/0/g' | tr -d '\n')

res=""
for (( i=1; i<${#cmd}; i+=2 )); do
    res+="${cmd:$i:1}"
done

echo -n  $res | perl -lpe '$_=pack("B*",$_)' 

