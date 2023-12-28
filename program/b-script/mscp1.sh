#!/bin/bash

echo "enter the file path: "
read path
echo "path: $path"

scp -r rws@223.195.71.123:/$path .
