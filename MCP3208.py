"""
	Author: 	Rockson Agyeman
	Date: 	Friday 30th March, 2021 (first authoring date)
	Version:	1.0.0 
	
	Doc:
		This driver (application) communicates with the MCP3208 [1] ADC chip via SPI on the RaspberryPi. 
		
		requirements: 	Python3
							spidev 	
  	
  	
  	Instructions:
  		1. Enable SPI interface on Raspi according to steps outlined in [5]. Remember to reboot Rasp Pi.
  		2. Wire MCP3208  to Raspi according to the diagram in [4]. MCP3208 pin details are in page 15 of [1].
  		3. Check that SPI is enabled by on Rasp Pi entering "ls /dev/spi*" on the terminal. 
  		 	This should return "/dev/spidev0.0  /dev/spidev0.1"
  		 	
  	
  	REFERENCES
  	---------------------------------------------------------------------------------------------------------------------------------
  	[1] MCP3204/3208, http://ww1.microchip.com/downloads/en/devicedoc/21298e.pdf
  	[2] Y. Kim, Chapter 10: Linux SPI Device Driver, Department of Information & Communication Engineering, Yeungnam Univversity, 2017.
  	[3] SpiDev Documentation, https://www.sigmdel.ca/michel/ha/rpi/dnld/draft_spidev_doc.pdf
  	[4] https://i.stack.imgur.com/DAM3d.png
  	[5] Enabling SPI on the Raspberry Pi, https://pimylifeup.com/raspberry-pi-spi/
  	
"""

import spidev
import sys

class MCP3208:
	"""
		Typical SPI path: /dev/spidev<bus>.<device>
		
		eg. /dev/spidev0.0
			bus: 0
			device: 0
			
		Details of Serial Communication (configuration) parameters are in page 19~22 of [1]
	"""
	def __init__(self,bus:int=0,device:int=0,mode:int=0,bits_per_word:int=8,max_speed_hz:int=500000):

		# Raspi SPI configuration parameters		
		self.bus = bus
		self.device = device
		self.mode = mode
		self.bits_per_word = bits_per_word
		self.max_speed_hz = max_speed_hz
		
		# chip setting parameters
		self.MCP_CH_NUM = 8		# Max. number of supported ADC channels 
		self.MCP_SPI_SB = 2     # Start bit
		self.MCP_SPI_SD = 1     # Single-ended & Differential input mode
		self.MCP_SPI_D2 = 0     # Input channel configuration
		self.MCP_SPI_D1 = 7     # Input channel configuration
		self.MCP_SPI_D0 = 6     # Input channel configuration
		
		# open and configure SPI device
		# Details of spidev are in [3]
		self.spi = spidev.SpiDev()
		self.spi.open(self.bus,self.device)
		self.spi.mode = self.mode
		self.spi.bits_per_word = self.bits_per_word
		self.spi.max_speed_hz = self.max_speed_hz
		# -- add more configuration as desired
		
	
	"""
		Method: read ADC value and return in decimal
				Input: 	MCP3208 channel number [1 - 8]
				Output:	ADC value [0 - 4096]
	"""
	def read_ADC(self,channel_mumber:int=None)->int:
		
		# system check
		if channel_mumber is None:
			sys.exit("Please specify the channel number!")
			
		elif (channel_mumber < 1) or (channel_mumber > 8):
			sys.exit("Invalid channel number. Range is from 1~8")
			
			
		# initialize / reset
		adc_value = 0
		data = [0x0,0x0,0x0,]
		
		# prepare the commands to sent be sent to MCP3208
		cmd1  =  (1 << self.MCP_SPI_SB) | (1 << self.MCP_SPI_SD) | ((channel_mumber & 0x04) >> 2);
		cmd2  =  (((channel_mumber & 0x02) >> 1) << self.MCP_SPI_D1) | ((channel_mumber & 0x01) << self.MCP_SPI_D0);
		cmd3  =  0x0;
		
		# transfer command and get the returned value
		data = self.spi.xfer([cmd1,cmd2,cmd3])
		data[1] = data[1] & 0x0F;
		adc_value = (data[1] << 8) | data[2];
		
		# return value in decimal
		return adc_value
		
	