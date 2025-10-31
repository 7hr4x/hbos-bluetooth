import dbus
import dbus.mainloop.glib
from gi.repository import GLib

from Agent import Agent
from Adapter import Adapter

BUS_NAME = "org.bluez"
AGNT_MNGR_IFACE = "org.bluez.AgentManager1"
AGENT_PATH = "/com/hifiberry/btagent"
AGNT_MNGR_PATH = "/org/bluez"
CAPABILITY = "NoInputNoOutput"
DEVICE_IFACE = "org.bluez.Device1"

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

def set_trusted(path):
    props = dbus.Interface(bus.get_object(BUS_NAME, path), dbus.PROPERTIES_IFACE)
    props.Set(DEVICE_IFACE, "Trusted", True)



if __name__ == '__main__':
    agent = Agent(bus, AGENT_PATH)
    agnt_mngr = dbus.Interface(bus.get_object(BUS_NAME, AGNT_MNGR_PATH),
                               AGNT_MNGR_IFACE)
    agnt_mngr.RegisterAgent(AGENT_PATH, CAPABILITY)
    agnt_mngr.RequestDefaultAgent(AGENT_PATH)

    adapter = Adapter()
    mainloop = GLib.MainLoop()
    try:
        mainloop.run()
    except KeyboardInterrupt:
        agnt_mngr.UnregisterAgent(AGENT_PATH)
        mainloop.quit()

