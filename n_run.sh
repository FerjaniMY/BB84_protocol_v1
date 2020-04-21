#!/bin/bash
n=10 
for ((i=1;i<=n;i++));
do
  python3 Alice.py  &
  python3 Bob.py t &
  sleep 7
done
