#!/bin/bash

PATH=`pwd -P`
cd ~

mkdir .rws
# cp ./lab_share/program/* ./.rws
cp $PATH/program/* ~/.rws
echo "program install done"

#cat ./lab_share/alias_list
#cat ./lab_share/alias_list >> .bashrc

cat $PATH/alias_list
cat $PATH/alias_list >> .bashrc



echo "shortcut keys uodate done"

source ~/.bashrc
echo "install successfully done"
