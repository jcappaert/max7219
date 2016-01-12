import max7219.led as led
from time import *

MAX_NUM_DIGITS_D2 = 8
MAX_NUM_DIGITS_D1 = 8

device = led.sevensegment()

def write_large_number(largenumber, spidevice):
	# split number over the displays
	device = led.sevensegment(cascaded=2, spi_device=spidevice)
	num_str = str(largenumber)
	num_len = len(str(largenumber))
	device.clear(deviceId=0)
	device.clear(deviceId=1)
	print i
	if (num_len > MAX_NUM_DIGITS_D1):
		str_d1 = num_str[-MAX_NUM_DIGITS_D1:]
		print str_d1
		num_d1 = int(str_d1)
		print num_d1
		str_d2 = num_str[0:len(num_str)-MAX_NUM_DIGITS_D1]
		print str_d2
		num_d2 = int(str_d2)
		print num_d2
		device.write_number(deviceId=1, zeroPad=True, value=num_d1)
		device.write_number(deviceId=0, value=num_d2)
	elif num_len > (MAX_NUM_DIGITS_D1 + MAX_NUM_DIGITS_D2):
		print "Number too large for display"
	else:
		device.write_number(deviceId=1, value=largenumber)


# example
i = 9950
while 1:

	write_large_number(i, 0)
	write_large_number(i**2, 1)
	i += 111
	sleep(0.05)

