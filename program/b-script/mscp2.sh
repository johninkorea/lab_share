#!/bin/bash

path_L=$(pwd)

echo "enter the fil name you want pass: "
read name

echo "*****************************"
echo "enter the path you want pass: "
read path

scp -r $path_L/$name rws@223.195.71.123:/$path
