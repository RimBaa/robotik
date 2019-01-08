#!/usr/bin/python
from PIL import Image
import random
import numpy.linalg as numpy
import numpy as np
import cv2
import os.path
import pylab as pl
 

def picture(array):
	help_array = []
	image = Image.open('img_lines2.png') 
	image1 = image.convert('RGB')
	 
	width ,height = image.size
	
	for y in range(100, height-1): 
		for x in range(100, width-1):
	 
			rgb = image1.getpixel((x,y))
		
			if (rgb >= (200,200,200)):
			  
				help_array.append((x,y))
		#mittleren Punkt der weissen Linie nehmen		
		if (help_array != []):		
			array.append(help_array[(len(help_array)/2)-1])
		#print help_array, len(help_array), "hhhh " , array
		help_array = []			
			
	#werte der weissen linie bestimmen
#==============================================================================
# 	pixel = image1.load()
# 	for i in range(1,400):
# 		
# 		if(image1.getpixel((i,363))>=(200,200,200)):
# 			print image1.getpixel((i,363))
# 			pixel[i,363] = (255,0,0)
# 			
# 		else:
# 			pixel[i,363] = (0,0,0)
# 	image1.save("test.png")
#==============================================================================
	return


def ransac(array2):
	n = 20
	d = 4
	t1 = len(array2)/4
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
	if not os.path.isfile('img_lines3.png'):
		image = Image.open('img_lines2.png') 
		image = image.convert('RGB')
		image = np.array(image)
	else:
		image = Image.open('img_lines3.png') 
		image = image.convert('RGB')
		image = np.array(image)	
	
	cv2.line(image,a_final,b_final,(255,0,0),3)
	cv2.imwrite('img_lines3.png',image)

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
picture(array)
print array
print len(array)

ransac(array)
x =[]
y = []
for i in range (len(array)-1):
	x.append(array[i][0])
	y.append(array[i][1])
	
x = [1545148331, 1545148338, 1545148347, 1545148353, 1545148357, 1545148362, 1545148367, 1545148373, 1545148379] 
y = [75.0, 95.0, 89.0, 75.0, 75.0, 89.0, 95.0, 95.0, 95.0]	
pl.plot(x,y )
pl.show()