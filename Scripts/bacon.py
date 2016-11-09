from PIL.Image import *

def readImage(i):
	(l, h) = i.size
	result = ""
	for x in range(l):
        	for y in range(h):
            		c = Image.getpixel(i, (x, y))
			if c == (0,0,0):
				result += "A"
			else:
				result += "B"
	print result

i=open("baconian.bmp")
readImage(i)
