#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:00:35 2019

@author: rima
"""
import sympy as sy
from PIL import Image

point_input = (input("Punkt: "))
print point_input


radius =118.25
p1 = [185,95.21]
p2=[185,335.29]
p3=[415.5,97]
p4=[415.5,333.5]
m1 = (195.5,215.25)
m2 = (404.5,215.25)
#(x−m1)2+(y−m2)2=r2

if (point_input[0]<=185.5):
	delete =[]
	#line from the input point to the center of the 1.circle
	m = (195 - point_input[0])/(215.25 - point_input[1])
	b = 195 - m * 215.25
########### testen	
	print m, b
	image = Image.open('map2.png') 
	image1 = image.convert('RGB')
	pixel = image1.load()
############	
 	for i in range(75,186): 
	#	y = 0.0085*(i-215.25)**2+67.25
 		y = sy.Symbol('y')
 		y = sy.solve((i-m1[0])**2+(y-m1[1])**2-120.5**2,y)
		y = list(y)
########### testen		
		#print (i,y) 
 		if len(y)>1:
 			for n in range (len(y)):
				tmp = round(y[n])				 
 				pixel[tmp,i ]= (255,0,0)	
 		else:
 			tmp = round(y[0])				 
			pixel[tmp,i ]= (0,0,255)	
############			
 	# calculate x and y value of the point on the circle 
	x,y = sy.symbols('x, y')
	eq1 = m*x+b-y
	eq2 = (y-m1[0])**2 + (x-m1[1])**2 - 120.5**2
	solution = sy.solve([eq1,eq2],(x,y))
	print solution
	#if there are more points, keep only the one of the given half circle
	for i in range (len(solution)):
 		if solution[i][1]>185:
 			delete.append(solution[i])
 	if len(delete) > 0:
 		for i in range (len(delete)):
 			solution.remove(delete[i])	
####### testen	
	for i in range (215):
 		a = m*i+b
 		pixel[i,a] = (0,0,255)

	#pixel[215,195]=(0,0,255)	
	x1 = int(solution[0][0])
	y1= int(solution[0][1])
	pixel[x1,y1]=(0,255,0)
	image1.save("test.png")		
	point = [y,x]
###########	
	print solution[0]
	
elif (point_input[0]>=415):
	delete =[]
	#line from the input point to the center of the 2.circle	
#==============================================================================
# 	
# 	m = (195 - point_input[0])/(215 - point_input[1])
# 	#m=
# 	b = 195.5 - m * 215.25
# 	print m, b
# 	x = sy.Symbol('x')
# 	# calculate x value of the point on the circle
# 	x = sy.solve( sy.Eq(m*x+b, -0.0085*(x-215.25)**2+533.75) )
# 	#if there are more points, keep only the one of the given half circle
# 	if len(x)>1:
# 		for i in range (len(x)):
# 			if ((x[i]<415.5) or (x[i]>533.75)):
# 				delete.append(x[i])
# 	print x			
# 	if len(delete) > 0:
# 		for i in range (len(delete)):
# 			x.remove(delete[i])
# 	print x
# 	y = m*x[0]+b
# 	point = [y,x]
# 	print point 
#==============================================================================
	
	delete =[]
	#line from the input point to the center of the 1.circle
	m = (405 - point_input[0])/(215.25 - point_input[1])
	b = 405 - m * 215.25
########### testen	
	print m, b
	image = Image.open('map2.png') 
	image1 = image.convert('RGB')
	pixel = image1.load()
############	
 	for i in range(416,526): 
	#	y = 0.0085*(i-215.25)**2+67.25
 		y = sy.Symbol('y')
 		y = sy.solve((i-m2[0])**2+(y-m2[1])**2-120.5**2,y)
		y = list(y)
########### testen		
		print (i,y) 
 		if len(y)>1:
 			for n in range (len(y)):
				print y[n] 
				tmp = round(y[n])				 
 				pixel[tmp,i ]= (255,0,0)	
 		else:
 			tmp = round(y[0])				 
			pixel[tmp,i ]= (0,0,255)	
############			
 	# calculate x and y value of the point on the circle 
	
	x,y = sy.symbols('x, y')
	eq1 = m*x+b-y
	eq2 = (y-m2[0])**2 + (x-m2[1])**2 - 120.5**2
	solution = sy.solve([eq1,eq2],(x,y))
	print solution
	#if there are more points, keep only the one of the given half circle
 	for i in range (len(solution)):
  		if solution[i][1]<415:
  			delete.append(solution[i])
  	if len(delete) > 0:
  		for i in range (len(delete)):
  			solution.remove(delete[i])	
####### testen	
	for i in range (215):
 		a = m*i+b
 		pixel[i,a] = (0,0,255)

	pixel[215,404]=(0,0,255)	
	image1.save("test.png") 
	x1 = int(solution[0][0])
	y1= int(solution[0][1])
	pixel[x1,y1]=(0,255,0)
	image1.save("test.png")		
	point = [y,x]
###########	
	print solution[0]
	
	print "2.circle"