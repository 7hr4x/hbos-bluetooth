# hbos bluetooth
## Setup

**1. Install [hbos](https://github.com/hifiberry/hifiberry-os/tree/hbosng)**
Follow the steps given in the repository

**2. Edit bluetooth configuration**
Open the file with your editor of choice, in this example vi:
```bash
sudo vi /etc/bluetooth/main.conf
```

This should show a file with contents.

Search the following lines and
change them so they match the configuration below:
```bash
[General]
Class = 0x200414
DiscoverableTimeout = 0
PairableTimeout = 0
```

Save the file and restart bluetooth:
```bash
sudo systemctl restart bluetooth
```

2. `sudo rfkill unblock all` in bash
3. `bluetoothctl` in bash
4. `pairable on` in bluetoothctl
5. `discoverable on` in bluetoothctl
