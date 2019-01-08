#!/usr/bin/python
from PIL import Image
import random
import numpy.linalg as numpy
import numpy as np
import cv2
import os.path
 

def picture(array,array2):
	image = Image.open('bild.png') 
	image1 = image.convert('RGB')
	 
	width ,height = image.size

	for y in range(1, height,10): 
	    for x in range(100, width-1):
	 
		rgb = image1.getpixel((x,y))
		left = x-1
		high = y-1
		right = x+1
		black_right = image1.getpixel((right,y))
		black_left = image1.getpixel((left,y))
		black_high = image1.getpixel((x,high))

		if(x >= 300): 
			  if (rgb == (255,255,255) and black_right == (0,0,0) and black_high == (0,0,0)):  
					array2.append((x,y))
		else:
	       		 if (rgb == (255,255,255) and black_left == (0,0,0) and black_high == (0,0,0)):   
			    		array.append((x,y))
	
	return


def ransac(array2):
	s = 2
	n = 100
	d = 1
	t1 = len(array2)-7
	set_final=[]
	set_tmp=[]
	a_final=(0,0)
	b_final=(0,0)
	while(n>0):
		set_tmp = []
		a=random.choice(array2)
		b=random.choice(array2)
		while(b==a):
			b=random.choice(array2)
		for i in range(0,len(array2)):
			a_np = np.asarray(a)
			b_np = np.asarray(b)
			c = np.asarray(array2[i])
			d1 = numpy.norm(np.cross(b_np-a_np, a_np-c))/numpy.norm(b_np-a_np)
			if(d1<d):
				set_tmp.append(array2[i])
		if(len(set_tmp)>=t1 and len(set_tmp)>len(set_final)):
			a_final = a
			b_final = b
			set_final = set_tmp
		n-=1
		
	print a_final
	print b_final
	print len(set_final)
	if not os.path.isfile('img_lines.png'):
		image = Image.open('bild.png') 
		image = image.convert('RGB')
		image = np.array(image)
	else:
		image = Image.open('img_lines.png') 
		image = image.convert('RGB')
		image = np.array(image)	
	
	cv2.line(image,a_final,b_final,(255,0,0),3)
	cv2.imwrite('img_lines.png',image)

	m1 = (b_final[1]-a_final[1])/float(b_final[0]-a_final[0])
	b1 = a_final[1]-m1*a_final[0]
	print "\n"	
	print "m: "
	print m1
	print "b: "
	print b1
	print "\n"
	return


array=[]
array2=[]
picture(array,array2)
print array
print len(array)
print array2
print len(array2)

ransac(array)
ransac(array2)

