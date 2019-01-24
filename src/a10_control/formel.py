#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sympy as sy
from PIL import Image
import numpy.linalg as numpy
import numpy as np
import math


radius =120.5
p1 = [185,95.21]
p2=[185,335.29]
p3=[415.5,97]
p4=[415.5,333.5]
m1 = (195.5,215.5)
m2 = (404.5,215.5)
lane =0

def find_point(point_input,lane, distance):
	global radius
	
	alpha = 0
	if lane == 1:
			new_radius = radius + 15.5
			
	elif lane == 2:
			new_radius = radius + 32 + 15.5
	if (point_input[0]<=185.5):
		
		
		delete =[]
		#line from the input point to the center of the 1.circle
		m = (195.5 - point_input[0])/(215.5 - point_input[1])
		b = 195.5 - m * 215.5
	
		if(point_input[1]==215.5):
			if lane == 1:
				point = (point_input[0]/100,(95.0+15.5)/100)
			else:	
				point = (point_input[0]/100,(95.0+32)/100)
			
		else:	

		 	# calculate x and y value of the point on the circle 
			x,y = sy.symbols('x, y')
			eq1 = m*x+b-y
			eq2 = (y-m1[0])**2 + (x-m1[1])**2 - new_radius**2
			solution = sy.solve([eq1,eq2],(x,y))
			
			#if there are more points, keep only the one on the given half circle
			for i in range (len(solution)):
		 		if solution[i][1]>185:
		 			delete.append(solution[i])
		 	if len(delete) > 0:
		 		for i in range (len(delete)):
		 			solution.remove(delete[i])	
			
			 
			#point(x,y) - x down, y right        
			point = (solution[0][1]/100,solution[0][0]/100)
			
			
			#angle between point a and b
			alpha =-( distance * 360 / (2* math.pi * new_radius))
			alpha_rad = alpha*math.pi/180
			
			#translation to the coordinate origin; rotation of the point; translation back
			y =  (solution[0][0]-195.5)*math.cos(alpha_rad) + (-(solution[0][1]-215.5))*math.sin(alpha_rad)+195.5
			x = -( -(solution[0][0]-195.5)*math.sin(alpha_rad) + (-(solution[0][1]-215.5))*math.cos(alpha_rad)-215.5)
			point = (x/100.0,y/100.0)

		
	elif (point_input[0]>=415):
		delete =[]
		#line from the input point to the center of the 2.circle	
		
		delete =[]
		#line from the input point to the center of the 1.circle
		m = (404.5 - point_input[0])/(215.5 - point_input[1])
		b = 404.5 - m * 215.5
		
		
		if(point_input[1]==215.5):
			if lane == 1:
				point = (point_input[0]/100,(336.0+15.5)/100)
			else:
				point = (point_input[0]/100, (336.0+32)/100)
			
		else:	
		 	# calculate x and y value of the point on the circle 
			
			x,y = sy.symbols('x, y')
			eq1 = m*x+b-y
			eq2 = (y-m2[0])**2 + (x-m2[1])**2 - new_radius**2
			solution = sy.solve([eq1,eq2],(x,y))
			
			#if there are more points, keep only the one of the given half circle
		 	for i in range (len(solution)):
		  		if solution[i][1]<415:
		  			delete.append(solution[i])
		  	if len(delete) > 0:
		  		for i in range (len(delete)):
		  			solution.remove(delete[i])	

			#nearest point
			point = (solution[0][1]/100, solution[0][0]/100)
			
			alpha =( distance * 360 / (2* math.pi * new_radius))
			alpha_rad = alpha*math.pi/180
		
			#translation to the coordinate origin; rotation of the point; translation back
			x =  (solution[0][0]-195.5)*math.cos(alpha_rad) + (-(solution[0][1]-215.5))*math.sin(alpha_rad)+195.5
			y = -( -(solution[0][0]-195.5)*math.sin(alpha_rad) + (-(solution[0][1]-215.5))*math.cos(alpha_rad)-215.5)

			#(x,y), x down, y right
			point =(x/100.0,y/100.0)
		
		
	elif (point_input[1]<=215):
		#left line
		if lane == 1:
			point = ((point_input[0]+distance)/100,(95.0-15.5)/100)
		else:
			point = ((point_input[0]+distance)/100,(95.0-32-16.5)/100)
			

			
	elif (point_input[1]>215):
		#right line
		if lane ==1:
			point = ((point_input[0]-distance)/100,(336.0+15.5)/100)	
		else:
			point = ((point_input[0]-distance)/100,(336.0+32+16.5)/100)
		
	print point	
		
point_input = (input("Punkt: "))
#point in cm
point_input = (point_input[0]*100,point_input[1]*100)
lane_input = (input("Linie: (1 oder 2) "))
lane = lane_input
dist_input = (input("Distanz in m: "))
#distance in cm
distance = dist_input*100
find_point(point_input, lane, distance)		