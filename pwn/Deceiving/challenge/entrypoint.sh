#!/bin/sh

PORT=1337
EXEC="./deceiving"

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr
