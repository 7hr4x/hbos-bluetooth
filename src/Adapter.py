import dbus
class Adapter:
    BUS_NAME = "org.bluez"
    ADAPTER_ROOT = "/org/bluez/hci"
    ADAPTER_IFACE = "org.bluez.Adapter1"
    def __init__(self, idx=0):
        bus = dbus.SystemBus()
        self.path = f'{self.ADAPTER_ROOT}{idx}'
        self.adapter_object = bus.get_object(self.BUS_NAME, self.path)
        self.adapter_props = dbus.Interface(self.adapter_object,
                                            dbus.PROPERTIES_IFACE)
        self.adapter_props.Set(self.ADAPTER_IFACE, 'DiscoverableTimeout', dbus.UInt32(0))
        self.adapter_props.Set(self.ADAPTER_IFACE, 'Discoverable', True)
        self.adapter_props.Set(self.ADAPTER_IFACE, 'PairableTimeout', dbus.UInt32(0))
        self.adapter_props.Set(self.ADAPTER_IFACE, 'Pairable', True)
