import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P6)

##### Initialize Parameters #######
kvalue                 = 0.996
#kvalueLow              = 1.0
#kvalueHigh             = 1.0
temperature            = 25.000
v_level = 5
##################################

while True:
	##### Calculations ###############
	voltage = ((chan.value)/(2**16)*1000*v_level)
	rawEC = 1000.000*voltage/(820.000*200.000)
	valueTemp = rawEC * kvalue
	value = rawEC * kvalue
	value = value / (1.0+0.0185*(temperature-25.0))
	round(value, 3)

	#print('EC Value = ', value, "mS/cm")
	if (value == 0):
		print("Probe not dipped in water.")
		print("_______________________________________________________")
	elif value < 1:
		print('EC Value = ', 1000*value, "uS/cm")
		print("Estimated Total Dissolved Solids = ", 500*value, "mg/L")
		print("Water is safe to drink")
		print("_______________________________________________________")
	else:
		print('EC Value = ', value, "mS/cm")
		print("Estimated Total Dissolved Solids = ", 500*value, "mg/L")
		print("Water is unfit for human consumption.")
		print("_______________________________________________________")
	#print(valueTemp)
	#print(chan.value)
	time.sleep(2)
