#!/bin/bash

PATH=`pwd -P`
cd ~

mkdir .rws
cp ./lab_share/program/* ./.rws
echo "program install done"

cat ./lab_share/alias_list
cat ./lab_share/alias_list >> .bashrc
echo "shortcut keys uodate done"

source ~/.bashrc
echo "install successfully done"
