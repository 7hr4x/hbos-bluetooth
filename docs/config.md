# Config

## Syntax
**hbos-bluetooth** uses the [toml](https://toml.io/en/) format.

## Location
**hbos-bluetooth** creates the config file for you.
The file can be found under `~/.config/hifiberry/bluetooth.conf`.

## Example config
An example config will be created if you delete the existing file.
Alternatively, you can look at the example below.

```toml
[Bluetooth]
capability=NoInputNoOutput
```

## Bluetooth
In this section of the file, the bluetooth settings are defined.

### Capability
This is how you connect to the device.

If you, for example, want to automatically connect the device
without any confirmation

Possible options are:

#### `DisplayOnly`, `DisplayYesNo` and `KeyboardDisplay`

The user gets displayed a code from the RPi
and needs to type the code into
the device that wants to connect to the RPi (for example a phone).

**for developers:**
Both use the `RequestConfirmation()` function in [Agent.py](../src/Agent.py).


#### `KeyboardOnly`
The user gets displayed a code on
the device that wants to connect to the RPi (for example a phone).
He then needs to type in that code into the RPi.

**for developers:**
This uses the function `RequestPasskey()` function in [Agent.py](../src/Agent.py).

#### `NoInputNoOutput`
The user doesn't need to confirm anything.
If he wants to connect to the RPi, the device (for example a phone)
will automatically do that for him.
