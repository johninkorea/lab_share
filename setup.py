from ipaddress import ip_address
import os

os.system('sh setup.sh')


id=input("please enter slurm id: ")
ipaddress=input("please enter slurm ip_address: ")

st=f'''#!/bin/bash

echo "enter the file path: "
read path
echo "path: $path"

scp {id}@[{ipaddress}]:/$path .'''

file=open('~/.rws/mscp.sh')

file.write(st)
file.close()