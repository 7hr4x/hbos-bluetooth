# Glossary

## Definitions
### dbus
A message bus system providing a simple way for applications to talk to one another.
[BlueZ](./Glossary.md#BlueZ) provides dbus hooks,
allowing applications to establish
and manage bluetooth hardware and devices.

### PHY
Short for *physical layer*.
It is used to connect a device to the physical medium e.g.,
the USB controller has a PHY to provide functions such as
serialization, de-serialization, encoding, decoting
and is responsible for obtaining the required data transmission rate.

### BlueZ
*BlueZ* provides support for the core Bluetooth layers and protocols.
Its flexible, efficient and uses a modular implementation.
Currently BlueZ consists of many seperate modules:
- Bluetooth kernel subsystem core
- L2CAP and SCO audio kernel layers
- RFCOMM, BNEP, CMTP and HIDP kernel implementations
- [HCI](./Glossary.md#HCI) UART, USB, PCMCIA and virtual device drivers
- General Bluetooth and SDP libraries and daemons
- Configuration and testing utilities
- Protocol decoding and analysis tools

### HFP
Short for *Hands-free profile*.
The service profile used by devices that support a
hands-free mode of operation, such as,
a mobile phone connected to a car.

### HSP
Short for *Headset profile*.
The service profile used by bluetooth headphones or earpieces.

### Source
An entity capable of generating media content for streaming.
For example, a music player

### Sink
An entity capable of receiving media content for rendering.
For example, a headset or speaker.

### HCI
Short for *Host controller interface*.
This is typically a serial link between the bluetooth stack
and the bluetooth adapter and provides a standard interface
such that different stack implementations can be easily plugged-in.
It provides low-level commands for device setup, flow control, device discover,
quality of service, physical links, authentication and encryption.


## Sources
- [dbus](https://pythonhosted.org/BT-Manager/glossary.html#term-dbus)
- [PHY](https://www.kernel.org/doc/html/latest/driver-api/phy/phy.html)
- [BlueZ](https://www.bluez.org/about/)
- [HFP](https://pythonhosted.org/BT-Manager/glossary.html#term-hfp)
- [HSP](https://pythonhosted.org/BT-Manager/glossary.html#term-hsp)
- [source](https://pythonhosted.org/BT-Manager/glossary.html#term-source)
- [sink](https://pythonhosted.org/BT-Manager/glossary.html#term-sink)
- [HCI](https://pythonhosted.org/BT-Manager/glossary.html#term-hci)
