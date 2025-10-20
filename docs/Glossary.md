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
*HFP* builds on top of [HSP](./Glossary.md#HSP).

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

### PulseAudio
*PulseAudio* is a general purpose sound server,
intended to run as a middleware between your applications
and your hardware devices, either using ALSA or OSS.
While its main purpose is to ease audio configuration,
its modular design allows more advanced users
to configure the daemon percisely to best suit their needs.

### PipeWire
*PipeWire* is a new low-level multimedia framework.
It aims to offer capture and playback
for both audio and video with minimal latency
and support for [PulseAudio](./Glossary.md#PulseAudio),
JACK, ALSA and GStreamer-based applications.

*PipeWire* uses systemd/User for management of the server and automatic socket activation.

### WirePlumber
*WirePlumber* is a powerful session and policy manager for [PipeWire](./Glossary.md#PipeWire).
Based on a modular design, with Lua plugins,
that implement the actual management functionality,
it is highly configurabe and extendable.

*WirePlumber* uses SPA-JSON, a superset of JSON,
to change its behavior.

The configuration files are read from
`~/.config/wireplumber/` (user configuration),
`/etc/wireplumber` (global configuration) 
and then `/usr/share/wireplumber/`(stock configuration).

To configure *WirePlumber* its recommended
to add the directory `wireplumber.conf.d/` within
`/etc/wireplumber/` or `~/.config/wireplumber/`.

User configuration files have a higher priority than system files.
Configuration files with the same name but
in a lower priority location will be ignored.
Within each configuration directory,
the individual files are opened in alphanumerical order.

### GStreamer
*GStreamer* is a pipeline-based multimedia framework,
that links together a wide variety of
media processing systems to complete complex workflows.
For instance, 
GStreamer can be used to build a system that reads files in one format,
processes them, and exports them in another.
The formats and processes can be changed in a plug and play fashion.

## Sources
- [dbus](https://pythonhosted.org/BT-Manager/glossary.html#term-dbus)
- [PHY](https://www.kernel.org/doc/html/latest/driver-api/phy/phy.html)
- [BlueZ](https://www.bluez.org/about/)
- [HFP](https://pythonhosted.org/BT-Manager/glossary.html#term-hfp)
- [HFP](https://wiki.archlinux.org/title/Bluetooth_headset)
- [HSP](https://pythonhosted.org/BT-Manager/glossary.html#term-hsp)
- [source](https://pythonhosted.org/BT-Manager/glossary.html#term-source)
- [sink](https://pythonhosted.org/BT-Manager/glossary.html#term-sink)
- [HCI](https://pythonhosted.org/BT-Manager/glossary.html#term-hci)
- [PulseAudio](https://wiki.archlinux.org/title/PulseAudio)
- [PipeWire](https://wiki.archlinux.org/title/PipeWire)
- [WirePlumber](https://wiki.archlinux.org/title/WirePlumber)
- [WirePlumber](https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/conf_file.html#the-spa-json-format)
- [GStreamer](https://en.wikipedia.org/wiki/GStreamer)
