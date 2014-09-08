usbio
=====

USB GPIO interface

Please visit the project page at http://jap.hu/electronic/usbio/

These are the binaries and the source code for the USB GPIO extender

The directory structure is:

├── bin                          # executable files are here
│   ├── device_firmware           # this is the firmware HEX file for the PIC18F14K50
│   └── host                      # host side stuff for controlling the GPIO port
│       ├── linux.x86              # binaries for linux x86
│       ├── openwrt                # binary packages for openwrt
│       ├── raspberry              # binary packages for raspberry pi
│       └── win.x86                # exe files for windows
└── src                          # source code for everything is here
    ├── device_firmware           # C18 source code for the PIC18F14K50
    └── host                      # source code for the host side
        ├── openwrt                # source for the openwrt package
        │   └── usbio
        │       └── src
        └── posix                  # source code for linux, raspberry
            └── controlio           # controlio utility source
