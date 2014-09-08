#!/usr/bin/python
#
# This code needs pyusb from http://walac.github.io/pyusb/
#

import usb.core
import usb.util

SETPORT = 0x54
GETPORT = 0x53
SETDIR = 0x55
SETBIT = 0x56
CLEARBIT = 0x57

# find our device
dev = usb.core.find(idVendor=0x04d8, idProduct=0xf7c0)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# claim device
usb.util.claim_interface(dev, 0)

# send a setport request
bmRequestType = usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE | usb.util.CTRL_OUT
bmRequest = SETPORT
wValue = 0xa0bb
wIndex = 0
ret = dev.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, None)

# send a getport request, print result
bmRequestType = usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE | usb.util.CTRL_IN
bmRequest = GETPORT
ret = dev.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, 8)
print hex(ret[1] * 256 + ret[0])
