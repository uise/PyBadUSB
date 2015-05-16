
##Module
The Python module is split up into three files:
* [badusb](lib/pybadusb/badusb.py)
  - Used to embed firmware and burn firmware to a device.
* [phison](lib/pybadusb/phison.py)
  - Used to create SCSI commands for the device to get info, burn firmware, etc.
* [scsi](lib/scsi.cpp)
  - Used to send SCSI commands to the device
  - Written in C++ as a Python extension module

