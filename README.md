# Raspberry-PI-MCP3208
Read data from MCP3208 on Raspberry Pi. 


# Documentation
This driver (application) communicates with the MCP3208 [1] ADC chip via SPI on the RaspberryPi. 
- [✓] Single-ended configuration only supported
- [x]	Differential configuration not supported


# Requirements:
- [X] Python 3

- [X] spidev 	
  
  
# Instructions:
1. Enable SPI interface on Raspi according to steps outlined in [5]. Remember to reboot Rasp Pi.
2. Wire MCP3208  to Raspi according to the diagram in [4]. MCP3208 pin details are in page 15 of [1].
3. Check that SPI is enabled on Raspi by entering "ls /dev/spi*" in the terminal. This should return "/dev/spidev0.0  /dev/spidev0.1"
  
  
# References
- [1] MCP3204/3208, http://ww1.microchip.com/downloads/en/devicedoc/21298e.pdf
- [2] Y. Kim, Chapter 10: Linux SPI Device Driver, Dep. of Information & Communication Engineering, Yeungnam Univversity, 2017.
- [3] SpiDev Documentation, https://www.sigmdel.ca/michel/ha/rpi/dnld/draft_spidev_doc.pdf
- [4] https://i.stack.imgur.com/DAM3d.png
- [5] Enabling SPI on the Raspberry Pi, https://pimylifeup.com/raspberry-pi-spi/

# Usage: 
python3 example.py
