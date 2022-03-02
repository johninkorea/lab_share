#!/bin/bash

echo "enter the file path: "
read path
echo "path: $path"

scp id@ip_adress:/$path .
