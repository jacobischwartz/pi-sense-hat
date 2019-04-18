from sense_hat import SenseHat
import time
sense = SenseHat()
sense.set_rotation(270)
for i in range(8):
	color = i*31
	for y in range(i+1):
		sense.set_pixel(i,y,255,255-color,0)
	for z in range(i+1):
		sense.set_pixel(z,i,255,255-color,0)
	time.sleep(1)
