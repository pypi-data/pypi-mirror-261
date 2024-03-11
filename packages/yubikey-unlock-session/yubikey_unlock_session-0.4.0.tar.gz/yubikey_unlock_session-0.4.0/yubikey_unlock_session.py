"""
Unlock Gnome Session using a yubikey, disable screensaver while plugged in.
"""
import logging
import os.path
import pyotp
import dbus
import usb_plug_notification
import yubikey_manager_lib
import gi.repository.Gio

logging.disable(logging.NOTSET)


def main():
    """
    Main function
    """
    gsettings = gi.repository.Gio.Settings.new("org.gnome.desktop.session")
    with open(
        os.path.expanduser("~/.config/yubikey-unlock-session/credentials"),
        encoding="utf8"
    ) as credentials:
        secret, slot, vendor, product = credentials.read().strip().split(":")
    u = usb_plug_notification.USBPlugNotification(int(vendor, 16), int(product, 16))
    ykman = yubikey_manager_lib.YKMan()
    while 1:
        notification = u.get_notification()
        if notification == "plug" and verify(ykman, secret, slot):
            unlock()
            gsettings.set_uint("idle-delay", 0)
        elif notification == "unplug":
            gsettings.set_uint("idle-delay", 60)


def verify(ykman, secret, slot):
    """
    Verify attached Yubikey
    """
    totp = pyotp.TOTP(secret)

    stdout = ykman.run("oath", "accounts", "code", "-s", slot)["stdout"]
    print(stdout, flush=True)
    return totp.verify(stdout[0])


def unlock():
    """
    Unlock all sessions
    """
    system_bus = dbus.SystemBus()
    login1 = system_bus.get_object("org.freedesktop.login1", "/org/freedesktop/login1")
    login1_manager = dbus.Interface(
        login1, dbus_interface="org.freedesktop.login1.Manager"
    )
    seat = None
    for i in login1_manager.ListSessions():
        print(i, flush=True)
        session, _uid, _user, seat, _objectpath = i
        if seat:
            login1_manager.UnlockSession(session)

    if not seat:
        print("no seats found", flush=True)
