#!/bin/bash

## defore run this script.
# git clone https://github.com/johninkorea/lab_share.git
# cd lab_share
# sh setup.sh

r_path=${PWD}
echo "Current path: " $r_path
echo "##############################################"
echo

echo "make .rws folder at your home."
mkdir ~/.rws
mkdir ~/.rws/program
echo "done"
echo
echo "##############################################"
echo

echo "program install"
cp -r $r_path/program/* ~/.rws/program
echo "done"
echo
echo "##############################################"
echo

echo "shortcut keys seting"
mv ~/.rws/program/alias_list  ~/.rws

greet="export rws_path='~/.rws'\nif [ -f ${rws_path}/alias_list ]; then\n. ${rws_path}/alias_list\nfi"

echo $greet >> ~/.bashrc
echo "done"
echo
echo "##############################################"
echo

echo "all successfully done"
echo "you need to restart the terminal."
echo
echo "source ~/.bashrcs"
echo
echo  "hope you enjoy."
echo
echo "[Written by Wonseok Ryu from Sejong Uni]"
