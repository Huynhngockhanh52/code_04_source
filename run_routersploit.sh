#!bin/bash/sh

# chương trình cho mục kiểm thử thứ 02:
file2="check02.py"
ip="target `hostname -I`"
threads="threads 10"
module_non=scanners/autopwn
echo $ip
sudo routersploit -m $module_non  -s $ip -s $threads > test.txt
python3 $file2

