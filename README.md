# hbos bluetooth
## Setup

1. **Install Raspberry Pi OS**
Install *Raspberry Pi OS* using your flashing application of choice.
For convenience I would recommend [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

Flash a 64-bit version of the Raspberry Pi OS.
Since I don't need a desktop environment,
I'll go with Raspberry Pi OS Lite.

2. **Update Repositories and Packages**
Open a terminal on the Raspberry Pi
and enter the following commands:

```bash
sudo apt update
sudo apt upgrade
```

`sudo apt update` refreshes the available software packages
and `sudo apt upgrade` updates any outdated packages on your system.

3. **Setup HifiBerry OS**
Since *HifiBerry OS* is built on *Raspberry Pi OS*,
you just need to install some extra packages.

For the latest guide, 
please read the installation section on the 
[project's README](https://github.com/hifiberry/hifiberry-os/tree/hbosng?tab=readme-ov-file#installation).

4. **Remove softblock from bluetooth**
Sometimes the Raspberry Pi has a soft-block applied for bluetooth.
You can see if this occured on your device by running:
```bash
rfkill list
```

If your output looks like this, your bluetooth interface is soft-blocked:
```bash
username@raspi:~ $ rfkill list
0: hci0: Bluetooth
        Soft blocked: yes
        Hard blocked: no
1: phy0: Wireless LAN
        Soft blocked: no
        Hard blocked: no
```

You can remove the soft-block by running the following command in your terminal:
```bash
sudo rfkill unblock all
```

When running `rfkill list` again, the soft-block should now be gone.

4. **Connect bluetooth device**
Since [BlueZ](./docs/Glossary.md#BlueZ) doesn't need any additional setup,
you should be able to just connect to the pi via bluetooth.
Your phone/tablet/computer should automatically detect it as an output source.


To make the Pi visible over bluetooth, you need to enter the `bluetoothctl` cli:
```bash
bluetoothctl
```

After that, enter the following commands:
```bash
power on
agent on
default-agent
pairable on
discoverable on
```
