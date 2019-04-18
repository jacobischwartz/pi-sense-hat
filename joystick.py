from sense_hat import SenseHat
import time
sense = SenseHat()
posx = 4
posy = 4
bound = 7
color = 255
color_increment = -15

def pushed_up():
	global posy
	posy = max(0, posy-1)
def pushed_down():
	global posy
	posy = min(bound, posy+1)
def pushed_left():
	global posx
	posx = max(0, posx-1)
def pushed_right():
	global posx
	posx = min(bound, posx+1)
def increment_color():
	global color
        global color_increment
        if(color > 220): 
                color_increment = -20
        if(color < 20): 
                color_increment = 20
        color += color_increment

def pushed_any(event):
	if(event.action != 'pressed'):
                return
	if(event.direction == 'up'):
		pushed_up()
	elif(event.direction == 'down'):
		pushed_down()
	elif(event.direction == 'left'):
		pushed_left()
	elif(event.direction == 'right'):
		pushed_right()
	increment_color()
	sense.set_pixel(posx, posy, 155, color, color)

sense.stick.direction_any = pushed_any

sense.clear(0,0,0)

while True:
	time.sleep(0.1)
