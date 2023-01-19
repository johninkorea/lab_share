#!/bin/bash

# git clone https://github.com/johninkorea/lab_share.git
# cd lab_share

r_path=${PWD}
echo "path: " $r_path
echo

echo "make .rws dir in your home."
mkdir ~/.rws
echo "done"
echo

echo "program install"
cp -r $r_path/program/* ~/.rws
echo "done"
echo

echo "shortcut keys seting"
cat $r_path/program/alias_list_1
cat $r_path/program/alias_list_1 >> .bashrc
echo "done"
echo

echo "all successfully done"
echo "restart terminal."
echo  "hope you enjoy."

echo
echo "github id : johninkorea"
