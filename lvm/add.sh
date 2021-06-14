#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo 'please tell me the device to resize as the first parameter, like /dev/sda'
    exit 1
fi
disk=$1
mkfs.xfs -f $disk
pvcreate $disk -y
vgdata=`df -h|grep mapper|awk '{print $1}'| uniq`
vgname=`vgdisplay|grep 'VG Name'|awk '{print $3}'`
vgextend $vgname $disk
lvextend -r $vgdata -l '+100%FREE'
resize2fs $vgdata