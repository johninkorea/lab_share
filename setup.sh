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
cp $r_path/* ./.rws
echo "program install done"
echo

echo "shortcut keys seting"
cat $r_path/alias_list
cat $r_path/alias_list >> .bashrc
echo "shortcut keys uodate done"
echo

source ~/.bashrc
echo "install successfully done"
echo "restart terminal. hope you enjoy."
echo "site "
