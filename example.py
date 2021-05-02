"""
	Author: Rockson Agyeman
	Date: 	Friday 30th March, 2021 (first authoring date)
	Version:1.0.0 
	
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
  	
  	
  	usage: python3 example.py
  	
"""
# import MCP3208 module / class
from MCP3208 import MCP3208

# instantiate the class
mcp3208 = MCP3208()


while(1):
    # read channel 1 (CH0) of MCP3208
	adc_val = mcp3208.read_ADC(1)
	print(adc_val)
