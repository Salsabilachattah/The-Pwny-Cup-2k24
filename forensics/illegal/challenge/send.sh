for char in $(echo -n "1ll3g4l_fl4gs_ex1st!" | od -An -tuC); do
  binary=$(echo "obase=2; $char" | bc | awk '{printf "%08d", $0}')
  
  for bit in $(echo "$binary" | grep -o .); do
    if [ "$bit" -eq "1" ]; then
      nmap -T5  -p 80 --scanflags SYNFINPSH  93.184.215.14
    else
      nmap -T5  -p 80 --scanflags SYNFIN  93.184.215.14
    fi
    
  done
done    