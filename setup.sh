#!/bin/bash

# git clone https://github.com/johninkorea/lab_share.git
# cd lab_share

echo "Determine where the repository is cloned."
r_path=${PWD}
echo "path: " $r_path
echo


echo "making .rws dir at your home."
cd ~
mkdir .rws
echo "done"
echo

echo "program install"
cp $r_path/program/* ./.rws
echo "done"
echo

echo "shortcut keys seting"
cat $r_path/alias_list
cat $r_path/alias_list >> .bashrc
echo "done"
echo

source ~/.bashrc

echo "all successfully done"
echo "please restart terminal. hope you enjoy."
echo "-johninkorea-"
