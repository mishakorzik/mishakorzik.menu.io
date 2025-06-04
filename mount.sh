#!/bin/bash
lsblk
read -p "Select drive (ex. sdb1): " device_name

device_path="/dev/$device_name"
mount_point="/mnt/usb"

# Create mount point if it doesn't exist
if [ ! -d "$mount_point" ]; then
    echo "creating mounting point $mount_point..."
    sudo mkdir -p "$mount_point"
fi

# Mount drive (Fat32)
echo "mounting $device_path to $mount_point..."
sudo mount -t vfat "$device_path" "$mount_point"

# Result
if [ $? -eq 0 ]; then
    echo "Drive mounted on $mount_point"
else
    echo "Failed to mount"
fi
